import maya.cmds as cmds
import maya.mel as mm

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
            rigScale = 1.0,
            createCircleFkControl = True,
            surroundingMeshes = []
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

                curFKControl = None
                if createCircleFkControl:
                    curFKControl = SERigControl.RigCircleControl(
                                            rigSide = self.RigSide,
                                            rigType = curRigType,
                                            rigControlIndex = curRigControlIndex,
                                            prefix = SERigNaming.sFKPrefix + fkJoints[i], 
                                            translateTo = curFKJnt,
                                            rotateTo = curFKJnt,
                                            scale = rigScale,
                                            parent = preParent,
                                            lockChannels = ['t', 's', 'v'],
                                            overrideControlColor = True, 
                                            controlColor = (0.4, 0.9, 0.9),
                                            fitToSurroundingMeshes = True,
                                            surroundingMeshes = surroundingMeshes,
                                            postFitScale = 1.6,
                                            overrideFitRayDirection = True, 
                                            fitRayDirection = (0, 0, 1)
                                            )
                else:
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
                                            transparency = 0.75,
                                            overrideControlColor = True, 
                                            controlColor = (0.4, 0.9, 0.9),
                                            fitToSurroundingMeshes = True,
                                            surroundingMeshes = surroundingMeshes,
                                            postFitScale = 1.3,
                                            overrideFitRayDirection = True, 
                                            fitRayDirection = (0, 0, 1)
                                            )
            else:
                # Head FK.
                distance *= 3
                curScaleYZ = 18
                curRigType = SERigEnum.eRigType.RT_HeadFK
                curRigControlIndex = 0

                curFKControl = None
                if createCircleFkControl:
                    curFKControl = SERigControl.RigCircleControl(
                                            rigSide = self.RigSide,
                                            rigType = curRigType,
                                            rigControlIndex = curRigControlIndex,
                                            prefix = SERigNaming.sFKPrefix + fkJoints[i], 
                                            translateTo = curFKJnt,
                                            rotateTo = curFKJnt,
                                            scale = rigScale,
                                            parent = preParent,
                                            lockChannels = ['t', 's', 'v'],
                                            overrideControlColor = True, 
                                            controlColor = (0.4, 0.9, 0.9),
                                            fitToSurroundingMeshes = True,
                                            surroundingMeshes = surroundingMeshes,
                                            postFitScale = 1.6,
                                            overrideFitRayDirection = True, 
                                            fitRayDirection = (0, 0, -1)
                                            )

                    curFKControl.offsetCVsLocal(offset = (20.0, 0, 0))

                else:
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
                                            transparency = 0.75,
                                            overrideControlColor = True, 
                                            controlColor = (0.4, 0.9, 0.9),
                                            fitToSurroundingMeshes = True,
                                            surroundingMeshes = surroundingMeshes,
                                            postFitScale = 1.25,
                                            overrideFitRayDirection = True, 
                                            fitRayDirection = (0, 0, -1)
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
        tempExpressionTail = mainControl + '.' + SERigNaming.sBodyControlsVisibilityAttr + ';'
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
        self.NeckKeepOutSystemGroup = None
        self.KeepOutJointCount = 0

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
            createMuscleSpline = False,
            keepOutJointCount = 5,
            spineReferenceLength = 45.0,
            createCircleFkControl = True,
            surroundingMeshes = []
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
                if createCircleFkControl:
                    curFKControl = SERigControl.RigCircleControl(
                                            rigSide = self.RigSide,
                                            rigType = curRigType,
                                            rigControlIndex = curRigControlIndex,
                                            prefix = SERigNaming.sFKPrefix + fkJoints[i], 
                                            translateTo = curFKJnt,
                                            rotateTo = curFKJnt,
                                            scale = rigScale,
                                            parent = preParent,
                                            lockChannels = ['t', 's', 'v'],
                                            overrideControlColor = True, 
                                            controlColor = (0.4, 0.9, 0.9),
                                            fitToSurroundingMeshes = True,
                                            surroundingMeshes = surroundingMeshes,
                                            postFitScale = 1.6,
                                            overrideFitRayDirection = True, 
                                            fitRayDirection = (0, 0, 1)
                                            )
                else:
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
                                            transparency = 0.75,
                                            overrideControlColor = True, 
                                            controlColor = (0.4, 0.9, 0.9),
                                            fitToSurroundingMeshes = True,
                                            surroundingMeshes = surroundingMeshes,
                                            postFitScale = 1.3,
                                            overrideFitRayDirection = True, 
                                            fitRayDirection = (0, 0, 1)
                                            )
            else:
                # Head FK.
                if createCircleFkControl:
                    curFKControl = SERigControl.RigCircleControl(
                                            rigSide = self.RigSide,
                                            rigType = curRigType,
                                            rigControlIndex = curRigControlIndex,
                                            prefix = SERigNaming.sFKPrefix + fkJoints[i], 
                                            translateTo = curFKJnt,
                                            rotateTo = curFKJnt,
                                            scale = rigScale,
                                            parent = fkNeckControlGroup,
                                            lockChannels = ['t', 's', 'v'],
                                            overrideControlColor = True, 
                                            controlColor = (0.4, 0.9, 0.9),
                                            fitToSurroundingMeshes = True,
                                            surroundingMeshes = surroundingMeshes,
                                            postFitScale = 1.6,
                                            overrideFitRayDirection = True, 
                                            fitRayDirection = (0, 0, -1)
                                            )

                    curFKControl.offsetCVsLocal(offset = (20.0, 0, 0))

                else:
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
                                            transparency = 0.75,
                                            overrideControlColor = True, 
                                            controlColor = (0.4, 0.9, 0.9),
                                            fitToSurroundingMeshes = True,
                                            surroundingMeshes = surroundingMeshes,
                                            postFitScale = 1.25,
                                            overrideFitRayDirection = True, 
                                            fitRayDirection = (0, 0, -1)
                                            )

                # Head local to world rotation driver group.
                fkHeadDrvGrpName = curFKControl.Prefix + SERigNaming.sDriverGroup
                headLocalToWorldDrvGroup = curFKControl.InsertNewGroup(fkHeadDrvGrpName)

                locatorHeadLocalToWorldRot = cmds.spaceLocator(n = 'locator_' + self.Prefix + '_LocalToWorldRot')[0]
                cmds.delete(cmds.parentConstraint(headLocalToWorldDrvGroup, locatorHeadLocalToWorldRot, mo = 0))
                cmds.parent(locatorHeadLocalToWorldRot, self.RigPartsGrp)
                cmds.parentConstraint(self.BaseRig.Global02Control.ControlObject, locatorHeadLocalToWorldRot, mo = 1)
                oc = cmds.orientConstraint(locatorHeadLocalToWorldRot, headLocalToWorldDrvGroup, mo = 1)[0]
                cmds.hide(locatorHeadLocalToWorldRot)

                # Add Head follow world rotation switch.
                cmds.addAttr(curFKControl.ControlObject, ln = SERigNaming.sHeadFkFollowWorldSwitch, at = 'float', k = 1, dv = 0.0, hasMinValue = True, min = 0.0, hasMaxValue = True, max = 1.0)
                cmds.setAttr(curFKControl.ControlObject + '.' + SERigNaming.sHeadFkFollowWorldSwitch, cb = 1)
                cmds.connectAttr(curFKControl.ControlObject + '.' + SERigNaming.sHeadFkFollowWorldSwitch, oc + '.' + locatorHeadLocalToWorldRot + 'W0')
                
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
        cmds.setAttr(headAimJnt1 + '.translateX', spineReferenceLength * 1.5)
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
        tempExpressionTail = mainControl + '.' + SERigNaming.sBodyControlsVisibilityAttr + ';'
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
                                                      headJoint, neckAttachPoint, keepOutJointCount = keepOutJointCount)
            else:
                cmds.warning('Failed creating muscle spline keep out system. Please create chest head begin and end locators in the builder file.')


    def getLeftNeckKeepOutDrivenJoints(self):
        res = []
        for i in range(self.KeepOutJointCount):
            res.append('driven_L_ChestHead' + str(i + 1))

        return res


    def getRightNeckKeepOutDrivenJoints(self):
        res = []
        for i in range(self.KeepOutJointCount):
            res.append('driven_R_ChestHead' + str(i + 1))

        return res


    def getLeftNeckKeepOutDriverJoints(self):
        res = [SERigNaming.sIKPrefix + 'L_ChestHeadBegin', SERigNaming.sIKPrefix + 'L_ChestHeadEnd']
        return res


    def getRightNeckKeepOutDriverJoints(self):
        res = [SERigNaming.sIKPrefix + 'R_ChestHeadBegin', SERigNaming.sIKPrefix + 'R_ChestHeadEnd']
        return res


    def _createMuscleSplineKeepOutSystem(self, leftChestHeadBegin, leftChestHeadEnd, rightChestHeadBegin, rightChestHeadEnd, headJoint, 
                                         neckAttachPoint, keepOutJointCount):
        print('Creating neck muscle spline keep out system.')

        self.KeepOutJointCount = keepOutJointCount
        
        neckKeepOutSystemGrp = cmds.group(n = self.Prefix + 'NeckKeepOutSystem', em = 1, p = self.RigPartsGrp)
        self.NeckKeepOutSystemGroup = neckKeepOutSystemGrp
        cmds.parent(leftChestHeadBegin, leftChestHeadEnd, rightChestHeadBegin, rightChestHeadEnd, neckKeepOutSystemGrp)
        cmds.parentConstraint(headJoint, leftChestHeadEnd, mo = 1)
        cmds.parentConstraint(headJoint, rightChestHeadEnd, mo = 1)
        cmds.hide(leftChestHeadBegin, leftChestHeadEnd, rightChestHeadBegin, rightChestHeadEnd)

        # Create IK joints.
        cmds.select(cl = True)
        leftChestHeadBeginJnt = cmds.joint(n = SERigNaming.sIKPrefix + 'L_ChestHeadBegin')
        cmds.delete(cmds.pointConstraint(leftChestHeadBegin, leftChestHeadBeginJnt, mo = 0))
        cmds.select(cl = True)
        leftChestHeadEndJnt = cmds.joint(n = SERigNaming.sIKPrefix + 'L_ChestHeadEnd')
        cmds.delete(cmds.pointConstraint(leftChestHeadEnd, leftChestHeadEndJnt, mo = 0))
        cmds.hide(leftChestHeadBeginJnt)

        cmds.select(cl = True)
        rightChestHeadBeginJnt = cmds.joint(n = SERigNaming.sIKPrefix + 'R_ChestHeadBegin')
        cmds.delete(cmds.pointConstraint(rightChestHeadBegin, rightChestHeadBeginJnt, mo = 0))
        cmds.select(cl = True)
        rightChestHeadEndJnt = cmds.joint(n = SERigNaming.sIKPrefix + 'R_ChestHeadEnd')
        cmds.delete(cmds.pointConstraint(rightChestHeadEnd, rightChestHeadEndJnt, mo = 0))
        cmds.hide(rightChestHeadBeginJnt)

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

        # Create IK handles.
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

        # Create chest-head locators' distance nodes.
        leftDisNode = self._createDistanceBetweenNode(leftChestHeadBegin, leftChestHeadEnd)
        leftInitDis = cmds.getAttr(leftDisNode + '.distance')
        rightDisNode = self._createDistanceBetweenNode(rightChestHeadBegin, rightChestHeadEnd)
        rightInitDis = cmds.getAttr(rightDisNode + '.distance')

        divNode = cmds.createNode('multiplyDivide')
        cmds.setAttr(divNode + '.operation', 2)
        cmds.setAttr(divNode + '.input2X', leftInitDis)
        cmds.connectAttr(leftDisNode + '.distance', divNode + '.input1X', f = 1)
        cmds.setAttr(divNode + '.input2Y', rightInitDis)
        cmds.connectAttr(rightDisNode + '.distance', divNode + '.input1Y', f = 1)
        
        # Scale IK start joints.
        cmds.connectAttr(divNode + '.outputX', leftChestHeadBeginJnt + '.scaleX', f = 1)
        cmds.connectAttr(divNode + '.outputY', rightChestHeadBeginJnt + '.scaleX', f = 1)

        # Create muscle spline systems for the neck.
        leftPrefix = '_L_ChestHead'
        rightPrefix = '_R_ChestHead'
        leftMuscleSplineGrp = self._createMuscleSpline(keepOutJointCount, leftPrefix)
        rightMuscleSplineGrp = self._createMuscleSpline(keepOutJointCount, rightPrefix)
        cmds.parent(leftMuscleSplineGrp, self.NeckKeepOutSystemGroup)
        cmds.parent(rightMuscleSplineGrp, self.NeckKeepOutSystemGroup)

        leftMuscleSplineControlBegin = 'iControl' + leftPrefix + '1'
        cmds.pointConstraint(leftChestHeadBeginJnt, leftMuscleSplineControlBegin)
        leftMuscleSplineControlEnd = 'iControl' + leftPrefix + str(keepOutJointCount)
        cmds.pointConstraint(leftChestHeadEndJnt, leftMuscleSplineControlEnd)

        rightMuscleSplineControlBegin = 'iControl' + rightPrefix + '1'
        cmds.pointConstraint(rightChestHeadBeginJnt, rightMuscleSplineControlBegin)
        rightMuscleSplineControlEnd = 'iControl' + rightPrefix + str(keepOutJointCount)
        cmds.pointConstraint(rightChestHeadEndJnt, rightMuscleSplineControlEnd)

        for i in range(1, keepOutJointCount + 1):
            curLeftMuscleSplineControl = 'iControl' + leftPrefix + str(i)
            cmds.setAttr(curLeftMuscleSplineControl + '.tangentLength', 0)
            curRightMuscleSplineControl = 'iControl' + rightPrefix + str(i)
            cmds.setAttr(curRightMuscleSplineControl + '.tangentLength', 0)

        cmds.hide(self.NeckKeepOutSystemGroup)


    def _createDistanceBetweenNode(self, locatorStart, locatorEnd):
        disNode = cmds.createNode('distanceBetween')
        locatorStartShape = cmds.listRelatives(locatorStart, s = 1)[0]
        locatorEndShape = cmds.listRelatives(locatorEnd, s = 1)[0]
        cmds.connectAttr(locatorStartShape + '.worldPosition', disNode + '.point1')
        cmds.connectAttr(locatorEndShape + '.worldPosition', disNode + '.point2')

        return disNode

    def _createMuscleSpline(self, jointCount = 5, namePrefix = ''):
        commandStr = '{string $ctrls[];'
        commandStr += 'string $reads[];'
        commandStr += 'string $baseName = '
        commandStr += '"' + namePrefix + '";'
        commandStr += 'int $nControls = '
        commandStr += str(jointCount) + ';'
        commandStr += 'string $controlType = "cube";'
        commandStr += 'int $detail = 8;'
        commandStr += 'int $nRead = '
        commandStr +=  str(jointCount) + ';'
        commandStr += 'string $readType = "joint";'
        commandStr += 'int $bConstrainMid = 1;'
        commandStr += 'string $spline = cMS_makeSpline($baseName, $nControls, $controlType, $detail, $nRead, $readType, $ctrls, $reads, $bConstrainMid);}'
        mm.eval(commandStr)
    
        res = 'grp' + namePrefix + 'RIG'
        return res
