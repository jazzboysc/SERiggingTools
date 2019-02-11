import maya.cmds as cmds
from ..Base.SERigComponent import RigComponent
from ..Base import SERigControl
from ..Base import SERigEnum
from ..Base import SERigNaming
from ..Utils import SEStringHelper
from ..Utils import SEMathHelper
from ..Utils import SEJointHelper
from ..Utils import SERigObjectTypeHelper

#-----------------------------------------------------------------------------
# Rig Simple Human Neck Class
# Sun Che
#-----------------------------------------------------------------------------
class RigSimpleHumanNeck(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Center,
                 rigType = SERigEnum.eRigType.RT_NeckComponent
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.FKNeckControls = []

    def build(
            self,
            neckJoints = [],  # ['C_Neck_0', 'C_Neck_1', 'C_Head', 'C_FacialRoot']
            rootJoint = '',
            neckAttachPoint = '',
            rigScale = 1.0
            ):
        
        fkNeckControlGroup = cmds.group(n = self.Prefix + SERigNaming.s_FKPrefix + 'Neck' + SERigNaming.sControlGroup, em = 1, 
                                        p = self.FKControlGroup)

        # Attach fk neck to the spine.
        if cmds.objExists(neckAttachPoint):
            cmds.parentConstraint(neckAttachPoint, fkNeckControlGroup)

        # Create FK neck and head controls.
        preParent = fkNeckControlGroup
        curFKJnt = None
        nextFKJnt = None
        fkJoints = neckJoints
        for i in range(len(fkJoints) - 1):
            curFKJnt = fkJoints[i]
            nextFKJnt = fkJoints[i + 1]
            curFKJntLoc = SEMathHelper.getWorldPosition(curFKJnt)
            nextFKJntLoc = SEMathHelper.getWorldPosition(nextFKJnt)
            distance = SEMathHelper.getDistance3(curFKJntLoc, nextFKJntLoc)
            curRigType = 0
            curRigControlIndex = 0
            if i != (len(fkJoints) - 2):
                # Neck FK.
                distance *= 0.618
                curScaleYZ = 14
                curRigType = SERigEnum.eRigType.RT_NeckFK
                curRigControlIndex = i
            else:
                # Head FK.
                distance *= 3
                curScaleYZ = 18
                curRigType = SERigEnum.eRigType.RT_HeadFK
                curRigControlIndex = 0

            curFKControl = SERigControl.RigCubeControl(
                                    rigSide = self.RigSide,
                                    rigType = curRigType,
                                    rigControlIndex = curRigControlIndex,
                                    prefix = SERigNaming.sFKPrefix + fkJoints[i], 
                                    translateTo = curFKJnt,
                                    rotateTo = curFKJnt,
                                    scale = rigScale,
                                    parent = preParent,
                                    lockChannels = ['t', 's', 'v'],
                                    cubeScaleX = distance,
                                    cubeScaleY = curScaleYZ,
                                    cubeScaleZ = curScaleYZ,
                                    transparency = 0.75
                                    )
            self.FKNeckControls.append(curFKControl)
            SERigObjectTypeHelper.linkRigObjects(self.TopGrp, curFKControl.ControlGroup, 'FKControl' + str(i), 'ControlOwner')

            cmds.orientConstraint(curFKControl.ControlObject, curFKJnt)
            cmds.pointConstraint(curFKControl.ControlObject, curFKJnt)

            preParent = curFKControl.ControlObject

        # Create controls visibility expression.
        mainControl = SERigNaming.sMainControlPrefix + SERigNaming.sControl
        controlsVisEN = SERigNaming.sExpressionPrefix + self.Prefix + 'ControlsVis'
        fkControlsCount = len(self.FKNeckControls)
        tempExpressionTail = mainControl + '.' + SERigNaming.sControlsVisibilityAttr + ';'
        if fkControlsCount > 0:
            controlsVisES = self.FKNeckControls[0].ControlGroup + '.visibility = ' + tempExpressionTail
            for i in range(1, fkControlsCount):
                controlsVisES += '\n'
                controlsVisES += self.FKNeckControls[i].ControlGroup + '.visibility = ' + tempExpressionTail

        cmds.expression(n = controlsVisEN, s = controlsVisES, ae = 1)


#-----------------------------------------------------------------------------
# Rig Muscle Spline Human Neck Class
# Sun Che
#-----------------------------------------------------------------------------
class RigMuscleSplineHumanNeck(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Center,
                 rigType = SERigEnum.eRigType.RT_NeckComponent
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.FKNeckControls = []
        self.HeadAimIKControl = None
        self.IKJointsGroup = None

    def build(
            self,
            neckJoints = [],  # ['C_Neck_0', 'C_Neck_1', 'C_Head', 'C_FacialRoot']
            rootJoint = '',
            neckAttachPoint = '',
            rigScale = 1.0,
            leftChestHeadBegin = '',
            leftChestHeadEnd = '',
            rightChestHeadBegin = '',
            rightChestHeadEnd = '',
            createMuscleSpline = False
            ):
        if not cmds.objExists(neckAttachPoint):
            return

        fkNeckControlGroup = cmds.group(n = self.Prefix + SERigNaming.s_FKPrefix + 'Neck' + SERigNaming.sControlGroup, em = 1, 
                                        p = self.FKControlGroup)

        ikJointsGroup = cmds.group(n = self.Prefix + '_IK_JointsGrp', em = 1, p = self.JointsGrp)
        self.IKJointsGroup = ikJointsGroup

        # Attach neck to the spine.
        if cmds.objExists(neckAttachPoint):
            cmds.parentConstraint(neckAttachPoint, self.FKControlGroup, mo = 1)
            cmds.parentConstraint(neckAttachPoint, self.IKControlGroup, mo = 1)
            cmds.parentConstraint(neckAttachPoint, ikJointsGroup, mo = 1)
            cmds.parentConstraint(neckAttachPoint, self.RigPartsGrp, mo = 1)

        # Create FK neck and head controls.
        fkControlDrvGrpNames = []
        headDrvGrp0 = None
        headDrvGrp1 = None
        preParent = fkNeckControlGroup
        curFKJnt = None
        nextFKJnt = None
        fkJoints = neckJoints
        for i in range(len(fkJoints) - 1):
            curFKJnt = fkJoints[i]
            nextFKJnt = fkJoints[i + 1]
            curFKJntLoc = SEMathHelper.getWorldPosition(curFKJnt)
            nextFKJntLoc = SEMathHelper.getWorldPosition(nextFKJnt)
            distance = SEMathHelper.getDistance3(curFKJntLoc, nextFKJntLoc)
            curRigType = 0
            curRigControlIndex = 0
            if i != (len(fkJoints) - 2):
                # Neck FK.
                distance *= 0.618
                curScaleYZ = 14
                curRigType = SERigEnum.eRigType.RT_NeckFK
                curRigControlIndex = i
            else:
                # Head FK.
                distance *= 3
                curScaleYZ = 18
                curRigType = SERigEnum.eRigType.RT_HeadFK
                curRigControlIndex = 0

            if i != (len(fkJoints) - 2):
                # Neck FK.
                curFKControl = SERigControl.RigCubeControl(
                                        rigSide = self.RigSide,
                                        rigType = curRigType,
                                        rigControlIndex = curRigControlIndex,
                                        prefix = SERigNaming.sFKPrefix + fkJoints[i], 
                                        translateTo = curFKJnt,
                                        rotateTo = curFKJnt,
                                        scale = rigScale,
                                        parent = preParent,
                                        lockChannels = ['t', 's', 'v'],
                                        cubeScaleX = distance,
                                        cubeScaleY = curScaleYZ,
                                        cubeScaleZ = curScaleYZ,
                                        transparency = 0.75
                                        )
            else:
                # Head FK.
                curFKControl = SERigControl.RigCubeControl(
                                        rigSide = self.RigSide,
                                        rigType = curRigType,
                                        rigControlIndex = curRigControlIndex,
                                        prefix = SERigNaming.sFKPrefix + fkJoints[i], 
                                        translateTo = curFKJnt,
                                        rotateTo = curFKJnt,
                                        scale = rigScale,
                                        parent = fkNeckControlGroup,
                                        lockChannels = ['t', 's', 'v'],
                                        cubeScaleX = distance,
                                        cubeScaleY = curScaleYZ,
                                        cubeScaleZ = curScaleYZ,
                                        transparency = 0.75
                                        )
                
                # head driver group 0 drives the rotation of the head joint. It will be drived by head aim IK joint.
                headDrvGrp0 = cmds.group(n = 'C_Head_DrvGrp_0', em = 1)
                cmds.delete(cmds.parentConstraint(curFKControl.ControlObject, headDrvGrp0, mo = 0))
                cmds.parent(headDrvGrp0, curFKControl.ControlObject)
                cmds.orientConstraint(headDrvGrp0, curFKJnt)

                headDrvGrp1 = cmds.group(n = 'C_Head_DrvGrp_1', em = 1)
                cmds.parentConstraint(curFKJnt, headDrvGrp1, mo = 0)
                cmds.parent(headDrvGrp1, headDrvGrp0)

            self.FKNeckControls.append(curFKControl)
            SERigObjectTypeHelper.linkRigObjects(self.TopGrp, curFKControl.ControlGroup, 'FKControl' + str(i), 'ControlOwner')

            if i != (len(fkJoints) - 2):
                # Neck FK.
                cmds.orientConstraint(curFKControl.ControlObject, curFKJnt)
                cmds.pointConstraint(curFKControl.ControlObject, curFKJnt)

                # Create additional driver group for FK neck controls.
                drvGrpName = curFKControl.Prefix + SERigNaming.sDriverGroup
                curFKControl.InsertNewGroup(drvGrpName)
                fkControlDrvGrpNames.append(drvGrpName)

            preParent = curFKControl.ControlObject

        # Create IK aim joints.
        headJoint = neckJoints[2]
        cmds.select(cl = True)
        headAimJnt0 = cmds.joint(n = SERigNaming.sIKPrefix + 'C_HeadAim_0')
        cmds.delete(cmds.pointConstraint(headJoint, headAimJnt0, mo = 0))
        cmds.parent(headAimJnt0, ikJointsGroup)
        cmds.setAttr(headAimJnt0 + '.jointOrientX', -90)
        cmds.setAttr(headAimJnt0 + '.jointOrientY', -90)
        cmds.hide(headAimJnt0)

        if headDrvGrp0:
            cmds.orientConstraint(headAimJnt0, headDrvGrp0, mo = 1)

        cmds.select(cl = True)
        headAimJnt1 = cmds.joint(n = SERigNaming.sIKPrefix + 'C_HeadAim_1')
        cmds.delete(cmds.pointConstraint(headJoint, headAimJnt1, mo = 0))
        cmds.parent(headAimJnt1, headAimJnt0)
        cmds.setAttr(headAimJnt1 + '.translateX', 75)
        cmds.setAttr(headAimJnt1 + '.jointOrientY', 90)
        cmds.hide(headAimJnt1)

        # Create head aim IK control.
        self.HeadAimIKControl = SERigControl.RigFlatHexagonControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_HeadAimIK,
                                rigFacing = SERigEnum.eRigFacing.RF_Z,
                                prefix = self.Prefix + '_IK_HeadAim', 
                                scale = rigScale * 2, 
                                translateTo = headAimJnt1,
                                rotateTo = headAimJnt1, 
                                parent = self.IKControlGroup, 
                                lockChannels = ['s', 'r', 'tz', 'v'],
                                preRotateY = 90
                                )
        self.HeadAimIKControl.adjustControlGroupOffset(offsetY = 5)
        headAimPC = cmds.parentConstraint(self.FKNeckControls[-1].ControlObject, self.BaseRig.Global02Control.ControlObject, 
                                          self.HeadAimIKControl.ControlGroup, mo = 1)[0]
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.HeadAimIKControl.ControlGroup, 'HeadAimIKControl', 'ControlOwner')

        # Create neck rotation base locator.
        locatorNeckRotationBase = cmds.spaceLocator(n = 'locator_' + self.Prefix + '_RotationBase')[0]
        cmds.delete(cmds.pointConstraint(neckAttachPoint, locatorNeckRotationBase, mo = 0))
        cmds.delete(cmds.orientConstraint(headAimJnt1, locatorNeckRotationBase))
        cmds.parent(locatorNeckRotationBase, self.RigPartsGrp)
        cmds.hide(locatorNeckRotationBase)

        # Create head aim IK PV locator.
        locatorHeadAimPV = cmds.spaceLocator(n = 'locator_' + self.Prefix + '_HeadAimPV')[0]
        cmds.delete(cmds.pointConstraint(headAimJnt1, locatorHeadAimPV))
        curY = cmds.getAttr(locatorHeadAimPV + '.translateY')
        cmds.setAttr(locatorHeadAimPV + '.translateY', curY + 40)
        cmds.parent(locatorHeadAimPV, self.HeadAimIKControl.ControlObject)
        cmds.hide(locatorHeadAimPV)

        # Create head aim IK handle.
        headAimIK = cmds.ikHandle(n = self.Prefix + 'headAim' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', sj = headAimJnt0, ee = headAimJnt1)[0]
        cmds.hide(headAimIK)
        cmds.parent(headAimIK, self.RigPartsGrp)
        cmds.pointConstraint(self.HeadAimIKControl.ControlObject, headAimIK, mo = 1)
        cmds.poleVectorConstraint(locatorHeadAimPV, headAimIK)
        SEJointHelper.adjustIKTwist(headAimIK, headAimJnt0, startTwistValue = 0, endTwistValue = 360, twistValueStep = 90)

        # Create fk neck control driver based on IK head aim end joint.
        neckFollowHeadOC = cmds.orientConstraint(locatorNeckRotationBase, headAimJnt1, fkControlDrvGrpNames[0], mo = 1)[0]

        # Create controls visibility expression.
        mainControl = SERigNaming.sMainControlPrefix + SERigNaming.sControl
        controlsVisEN = SERigNaming.sExpressionPrefix + self.Prefix + 'ControlsVis'
        fkControlsCount = len(self.FKNeckControls)
        tempExpressionTail = mainControl + '.' + SERigNaming.sControlsVisibilityAttr + ';'
        if fkControlsCount > 0:
            controlsVisES = self.FKNeckControls[0].ControlGroup + '.visibility = ' + tempExpressionTail
            for i in range(1, fkControlsCount):
                controlsVisES += '\n'
                controlsVisES += self.FKNeckControls[i].ControlGroup + '.visibility = ' + tempExpressionTail

        if self.HeadAimIKControl:
            controlsVisES += '\n'
            controlsVisES += self.HeadAimIKControl.ControlGroup + '.visibility = ' + tempExpressionTail

        cmds.expression(n = controlsVisEN, s = controlsVisES, ae = 1)

        # Create FK neck follow IK head expression.
        neckFollowHeadEN = SERigNaming.sExpressionPrefix + self.Prefix + 'HeadAim'
        tempExpressionTail = mainControl + '.' + SERigNaming.sFKNeckJoint0FollowHeadAttr + ';'
        tempExpressionTail2 = mainControl + '.' + SERigNaming.sIKHeadAimLocalToWorldAttr + ';'
        neckFollowHeadES = neckFollowHeadOC + '.' + headAimJnt1 + 'W1 = ' + tempExpressionTail
        neckFollowHeadES += '\n'
        neckFollowHeadES += neckFollowHeadOC + '.' + locatorNeckRotationBase + 'W0 = 1.0 - ' + tempExpressionTail
        neckFollowHeadES += '\n'
        neckFollowHeadES += headAimPC + '.' + self.FKNeckControls[-1].ControlObject + 'W0 = 1.0 - ' + tempExpressionTail2
        neckFollowHeadES += '\n'
        neckFollowHeadES += headAimPC + '.' + self.BaseRig.Global02Control.ControlObject + 'W1 = ' + tempExpressionTail2

        cmds.expression(n = neckFollowHeadEN, s = neckFollowHeadES, ae = 1)

        # Create muscle spline keep out system.
        if createMuscleSpline:
            if cmds.objExists(leftChestHeadBegin) and cmds.objExists(leftChestHeadEnd) and cmds.objExists(rightChestHeadBegin) and cmds.objExists(rightChestHeadEnd):
                self._createMuscleSplineKeepOutSystem(leftChestHeadBegin, leftChestHeadEnd, rightChestHeadBegin, rightChestHeadEnd, 
                                                      headJoint, neckAttachPoint)
            else:
                cmds.warning('Failed creating muscle spline keep out system. Please create chest head begin and end locators in the builder file.')


    def _createMuscleSplineKeepOutSystem(self, leftChestHeadBegin, leftChestHeadEnd, rightChestHeadBegin, rightChestHeadEnd, headJoint, neckAttachPoint):
        print('Creating neck muscle spline keep out system.')

        neckKeepOutSystemGrp = cmds.group(n = self.Prefix + 'NeckKeepOutSystem', em = 1, p = self.RigPartsGrp)
        cmds.parent(leftChestHeadBegin, leftChestHeadEnd, rightChestHeadBegin, rightChestHeadEnd, neckKeepOutSystemGrp)
        cmds.parentConstraint(headJoint, leftChestHeadEnd, mo = 1)
        cmds.parentConstraint(headJoint, rightChestHeadEnd, mo = 1)

        cmds.select(cl = True)
        leftChestHeadBeginJnt = cmds.joint(n = 'IK_L_ChestHeadBegin')
        cmds.delete(cmds.pointConstraint(leftChestHeadBegin, leftChestHeadBeginJnt, mo = 0))
        cmds.select(cl = True)
        leftChestHeadEndJnt = cmds.joint(n = 'IK_L_ChestHeadEnd')
        cmds.delete(cmds.pointConstraint(leftChestHeadEnd, leftChestHeadEndJnt, mo = 0))

        cmds.select(cl = True)
        rightChestHeadBeginJnt = cmds.joint(n = 'IK_R_ChestHeadBegin')
        cmds.delete(cmds.pointConstraint(rightChestHeadBegin, rightChestHeadBeginJnt, mo = 0))
        cmds.select(cl = True)
        rightChestHeadEndJnt = cmds.joint(n = 'IK_R_ChestHeadEnd')
        cmds.delete(cmds.pointConstraint(rightChestHeadEnd, rightChestHeadEndJnt, mo = 0))

        cmds.delete(cmds.aimConstraint(leftChestHeadEndJnt, leftChestHeadBeginJnt, offset = [0, 0, 0], w = 1, aim = [1, 0, 0], u = [0, 0, -1], 
                           worldUpType = 'object', worldUpObject = rightChestHeadBegin))
        cmds.delete(cmds.aimConstraint(rightChestHeadEndJnt, rightChestHeadBeginJnt, offset = [0, 0, 0], w = 1, aim = [1, 0, 0], u = [0, 0, -1], 
                           worldUpType = 'object', worldUpObject = leftChestHeadBegin))
        cmds.delete(cmds.orientConstraint(leftChestHeadBeginJnt, leftChestHeadEndJnt, mo = 0))
        cmds.delete(cmds.orientConstraint(rightChestHeadBeginJnt, rightChestHeadEndJnt, mo = 0))
        cmds.parent(leftChestHeadEndJnt, leftChestHeadBeginJnt)
        cmds.parent(rightChestHeadEndJnt, rightChestHeadBeginJnt)

        cmds.parent(leftChestHeadBeginJnt, self.IKJointsGroup)
        cmds.parent(rightChestHeadBeginJnt, self.IKJointsGroup)
        cmds.makeIdentity(leftChestHeadBeginJnt, apply = True)
        cmds.makeIdentity(rightChestHeadBeginJnt, apply = True)

        leftChestHeadIK = cmds.ikHandle(n = self.Prefix + '_L_ChestHead' + SERigNaming.s_IKHandle, sol = 'ikSCsolver', 
                                        sj = leftChestHeadBeginJnt, ee = leftChestHeadEndJnt)[0]
        cmds.hide(leftChestHeadIK)
        rightChestHeadIK = cmds.ikHandle(n = self.Prefix + '_R_ChestHead' + SERigNaming.s_IKHandle, sol = 'ikSCsolver', 
                                        sj = rightChestHeadBeginJnt, ee = rightChestHeadEndJnt)[0]
        cmds.hide(rightChestHeadIK)
        cmds.parent(leftChestHeadIK, self.RigPartsGrp)
        cmds.parent(rightChestHeadIK, self.RigPartsGrp)

        cmds.parentConstraint(headJoint, leftChestHeadIK, mo = 1)
        cmds.parentConstraint(headJoint, rightChestHeadIK, mo = 1)

    def _createDistanceBetweenNode(locatorStart, locatorEnd):
        pass
