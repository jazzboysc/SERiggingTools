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

    def build(
            self,
            neckJoints = [],  # ['C_Neck_0', 'C_Neck_1', 'C_Head', 'C_FacialRoot']
            rootJoint = '',
            neckAttachPoint = '',
            rigScale = 1.0
            ):
        if not cmds.objExists(neckAttachPoint):
            return

        fkNeckControlGroup = cmds.group(n = self.Prefix + SERigNaming.s_FKPrefix + 'Neck' + SERigNaming.sControlGroup, em = 1, 
                                        p = self.FKControlGroup)

        ikJointsGroup = cmds.group(n = self.Prefix + '_IK_JointsGrp', em = 1, p = self.JointsGrp)

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
        cmds.setAttr(headAimJnt1 + '.translateX', 40)
        cmds.setAttr(headAimJnt1 + '.jointOrientY', 90)
        cmds.hide(headAimJnt1)

        # Create head aim IK control.
        self.HeadAimIKControl = SERigControl.RigCircleControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_HeadAimIK,
                                rigFacing = SERigEnum.eRigFacing.RF_Z,
                                prefix = self.Prefix + '_IK_HeadAim', 
                                scale = rigScale * 8, 
                                translateTo = headAimJnt1,
                                rotateTo = headAimJnt1, 
                                parent = self.IKControlGroup, 
                                lockChannels = ['s', 'r', 'v']
                                )
        self.HeadAimIKControl.adjustControlGroupOffset(offsetY = 5)
        cmds.parentConstraint(self.FKNeckControls[-1].ControlObject, self.HeadAimIKControl.ControlGroup, mo = 1)
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
        cmds.orientConstraint(locatorNeckRotationBase, headAimJnt1, fkControlDrvGrpNames[0], mo = 1)