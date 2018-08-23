import maya.cmds as cmds
from ..Base.SERigComponent import RigComponent
from ..Base import SERigControl
from ..Base import SERigEnum
from ..Base import SERigNaming
from ..Utils import SEStringHelper
from ..Utils import SEMathHelper
from ..Utils import SEJointHelper

#-----------------------------------------------------------------------------
# Rig Human Leg Class
# Sun Che
#-----------------------------------------------------------------------------
class RigHumanLeg(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.FootHelperJointsGroup = cmds.group(n = prefix + '_FootHelperJointsGrp', p = self.JointsGrp, em = 1)
        self.FootHelperJoints = None
        self.FootIKMainControl = None
        self.FootBaseSwiveControl = None
        self.FootToeSwiveControl = None
        self.FootRotationControl = None
        self.FKLegControls = []
        self.LegPVControl = None

    def build(
            self,
            legJoints = [],  # 0: hip, -1: toe, -2: ball, -3: ankle
            footHelperJoints = {},
            legPVLocator = '',
            rootJoint = '',
            rigScale = 1.0
            ):

        self.FootHelperJoints = self.attachFootHelperJoints(footHelperJoints)

        # Measure foot size.
        footBaseLocation = SEMathHelper.getWorldPosition(self.FootHelperJoints[SERigNaming.sFootBaseJnt])
        footToeLocation = SEMathHelper.getWorldPosition(self.FootHelperJoints[SERigNaming.sFootToeProxy])
        footSize = SEMathHelper.getDistance3(footBaseLocation, footToeLocation)
        footSize *= 1.2

        # Create foot IK main control based on foot size.
        flipScaleXYZ = False
        if self.RigSide == SERigEnum.eRigSide.RS_Right:
            flipScaleXYZ = True
        footIKMainControl = SERigControl.RigFootControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_Foot,
                                prefix = self.Prefix + '_IK_Main', 
                                scale = rigScale * 55, 
                                matchBoundingBoxScale = True,
                                scaleX = footSize,
                                scaleZ = footSize,
                                translateTo = self.FootHelperJoints[SERigNaming.sFootBaseJnt],
                                rotateTo = self.FootHelperJoints[SERigNaming.sFootBaseJnt],
                                parent = self.IKControlGroup, 
                                lockChannels = ['s', 'v'],
                                flipScaleX = flipScaleXYZ,
                                flipScaleY = flipScaleXYZ,
                                flipScaleZ = flipScaleXYZ
                                )
        self.FootIKMainControl = footIKMainControl

        if self.RigSide == SERigEnum.eRigSide.RS_Right:
            ikMainControlOffsetX = -0.5
        else:
            ikMainControlOffsetX = 0.5
        footIKMainControl.adjustControlGroupOffset(ikMainControlOffsetX, 0, -5)

        # Adjust main IK control's pivot to ankle's position.
        SEMathHelper.movePivotTo(footIKMainControl.ControlObject, legJoints[-3])

        # Create foot base swive control.
        flipScaleX = False
        if self.RigSide == SERigEnum.eRigSide.RS_Right:
            flipScaleX = True

        footBaseSwiveControl = SERigControl.RigCircleControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_Foot,
                                rigFacing = SERigEnum.eRigFacing.RF_Y,
                                prefix = self.Prefix + '_FootBaseSwive', 
                                scale = rigScale * 3.5, 
                                translateTo = self.FootHelperJoints[SERigNaming.sFootBaseSwiveJnt],
                                parent = footIKMainControl.ControlObject, 
                                lockChannels = ['s', 't', 'rx', 'rz', 'v'],
                                flipScaleX = flipScaleX
                                )
        self.FootBaseSwiveControl = footBaseSwiveControl

        # Create foot toe swive control.
        footToeSwiveControl = SERigControl.RigCircleControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_Foot,
                                rigFacing = SERigEnum.eRigFacing.RF_Y,
                                prefix = self.Prefix + '_ToeSwive', 
                                scale = rigScale * 6, 
                                translateTo = self.FootHelperJoints[SERigNaming.sFootToeSwiveJnt],
                                parent = footIKMainControl.ControlObject, 
                                lockChannels = ['s', 't', 'rx', 'rz', 'v'],
                                flipScaleX = flipScaleX
                                )
        self.FootToeSwiveControl = footToeSwiveControl

        # Create foot rotation control.
        footRotationControl = SERigControl.RigRotationControl(
                                 rigSide = self.RigSide,
                                 rigType = SERigEnum.eRigType.RT_Foot,
                                 rigFacing = SERigEnum.eRigFacing.RF_Z,
                                 prefix = self.Prefix + '_Rotation', 
                                 scale = rigScale * 6, 
                                 translateTo = self.FootHelperJoints[SERigNaming.sFootBaseJnt],
                                 parent = footIKMainControl.ControlObject, 
                                 lockChannels = ['s', 't', 'v'],
                                 flipScaleX = flipScaleX
                                 )
        self.FootRotationControl = footRotationControl

        footRotationControl.adjustControlGroupOffset(0, 8, -15)

        # Create leg PV control.
        legPVControl = SERigControl.RigDiamondControl(
                                 rigSide = self.RigSide,
                                 rigType = SERigEnum.eRigType.RT_LegPV,
                                 rigFacing = SERigEnum.eRigFacing.RF_Y,
                                 prefix = self.Prefix + '_PV', 
                                 scale = rigScale * 15, 
                                 translateTo = legPVLocator,
                                 parent = self.ControlsGrp, 
                                 lockChannels = ['s', 'r', 'v'],
                                 flipScaleX = flipScaleX
                                 )
        self.LegPVControl = legPVControl
        
        # Move leg PV locator from builder scene to this component.
        cmds.parent(legPVLocator, self.RigPartsGrp)
        cmds.pointConstraint(legPVControl.ControlObject, legPVLocator)
        cmds.hide(legPVLocator)

        # Attach foot helper joints to the foot IK main control.
        cmds.parentConstraint(footIKMainControl.ControlObject, self.FootHelperJointsGroup, mo = 1)

        # Create IK leg joints.
        ikJoints = SEJointHelper.duplicateHierarchy(legJoints[0], SERigNaming.sIKPrefix)

        # Create IK handles.
        ankleIK = cmds.ikHandle(n = self.Prefix + 'Ankle' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', sj = ikJoints[0], ee = ikJoints[2])[0]
        cmds.hide(ankleIK)
        cmds.parent(ankleIK, self.RigPartsGrp)
        cmds.pointConstraint(self.FootHelperJoints[SERigNaming.sFootAnkleProxy], ankleIK, mo = 0)
        cmds.poleVectorConstraint(legPVLocator, ankleIK)

        ballIK = cmds.ikHandle(n = self.Prefix + 'Ball' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', sj = ikJoints[2], ee = ikJoints[3])[0]
        cmds.hide(ballIK)
        cmds.parent(ballIK, self.RigPartsGrp)
        cmds.pointConstraint(self.FootHelperJoints[SERigNaming.sFootBallProxy], ballIK, mo = 0)
        cmds.poleVectorConstraint(self.FootHelperJoints[SERigNaming.sBallProxyPVlocator], ballIK)
        if self.RigSide == SERigEnum.eRigSide.RS_Left:
            cmds.setAttr(ballIK + '.twist', 90)
        else:
            cmds.setAttr(ballIK + '.twist', 270)

        toeIK = cmds.ikHandle(n = self.Prefix + 'Toe' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', sj = ikJoints[3], ee = ikJoints[4])[0]
        cmds.hide(toeIK)
        cmds.parent(toeIK, self.RigPartsGrp)
        cmds.pointConstraint(self.FootHelperJoints[SERigNaming.sFootToeProxy], toeIK, mo = 0)
        cmds.poleVectorConstraint(self.FootHelperJoints[SERigNaming.sToeProxyPVlocator], toeIK)
        if self.RigSide == SERigEnum.eRigSide.RS_Left:
            cmds.setAttr(toeIK + '.twist', 90)
        else:
            cmds.setAttr(toeIK + '.twist', 0)

        # Attach ik joints to current rig component.
        ikJointsGroup = cmds.group(n = self.Prefix + '_IK_JointsGrp', em = 1, p = self.JointsGrp)
        cmds.parent(ikJoints[0], ikJointsGroup)
        ikJointsParent = SEJointHelper.getFirstParentJoint(legJoints[0])
        cmds.parentConstraint(ikJointsParent, ikJointsGroup, mo = 1)

        # Create FK leg joints.
        fkJoints = SEJointHelper.duplicateHierarchy(legJoints[0], SERigNaming.sFKPrefix)

        # Create FK leg controls.
        preParent = self.FKControlGroup
        curScaleYZ = 19
        for i in range(len(fkJoints) - 1):
            curFKJnt = fkJoints[i]
            nextFKJnt = fkJoints[i + 1]
            curFKJntLoc = SEMathHelper.getWorldPosition(curFKJnt)
            nextFKJntLoc = SEMathHelper.getWorldPosition(nextFKJnt)
            distance = SEMathHelper.getDistance3(curFKJntLoc, nextFKJntLoc)

            curFKControl = SERigControl.RigCubeControl(
                                    rigSide = self.RigSide,
                                    rigType = SERigEnum.eRigType.RT_Foot,
                                    prefix = SERigNaming.sFKPrefix + self.Prefix + str(i), 
                                    translateTo = curFKJnt,
                                    rotateTo = curFKJnt,
                                    scale = rigScale*20,
                                    parent = preParent,
                                    lockChannels = ['t', 's', 'v'],
                                    cubeScaleX = distance,
                                    cubeScaleY = curScaleYZ,
                                    cubeScaleZ = curScaleYZ,
                                    transparency = 0.85
                                    )
            self.FKLegControls.append(curFKControl)

            cmds.orientConstraint(curFKControl.ControlObject, curFKJnt)
            cmds.pointConstraint(curFKControl.ControlObject, curFKJnt)

            preParent = curFKControl.ControlObject
            curScaleYZ *= 0.75

        # Attach fk joints to current rig component.
        fkJointsGroup = cmds.group(n = self.Prefix + '_FK_JointsGrp', em = 1, p = self.JointsGrp)
        cmds.parent(fkJoints[0], fkJointsGroup)
        fkJointsParent = SEJointHelper.getFirstParentJoint(legJoints[0])
        cmds.parentConstraint(fkJointsParent, fkJointsGroup, mo = 1)

        # Create FK IK blenders.
        if self.BaseRig:
            for i in range(len(legJoints)):
                blender = cmds.createNode("blendColors")
                cmds.connectAttr(ikJoints[i] + '.r', blender + '.color1', f = 1)
                cmds.connectAttr(fkJoints[i] + '.r', blender + '.color2', f = 1)
                cmds.connectAttr(blender + '.output', legJoints[i] + '.r', f = 1)

                blenderControlAttr = self.BaseRig.getLegIKFKSwitch(self.RigSide)
                cmds.connectAttr(blenderControlAttr, blender + '.blender')

            fkAttachPoint = SEJointHelper.getFirstParentJoint(legJoints[0])
            if fkAttachPoint:
                cmds.parentConstraint(fkAttachPoint, self.FKControlGroup, mo = 1)

        # Create foot swive control expressions.
        footBaseSwiveEN = SERigNaming.sExpressionPrefix + self.Prefix + 'FootBaseSwive'
        footBaseSwiveES = self.FootHelperJoints[SERigNaming.sFootBaseSwiveJnt] + '.rotateY = ' + footBaseSwiveControl.ControlObject + '.rotateY;'
        cmds.expression(n = footBaseSwiveEN, s = footBaseSwiveES, ae = 1)

        footToeSwiveEN = SERigNaming.sExpressionPrefix + self.Prefix + 'FootToeSwive'
        footToeSwiveES = self.FootHelperJoints[SERigNaming.sFootToeSwiveJnt] + '.rotateY = ' + footToeSwiveControl.ControlObject + '.rotateY;'
        cmds.expression(n = footToeSwiveEN, s = footToeSwiveES, ae = 1)

        # Create foot rotation control expressions.
        # TODO: hard coded rotation angel for now.
        footRotationEN = SERigNaming.sExpressionPrefix + self.Prefix + 'FootRotation'
        footRotationES = self.FootHelperJoints[SERigNaming.sFootBaseJnt] + '.rotateX = clamp(-60, 0, ' + footRotationControl.ControlObject + '.rotateX);'
        footRotationES += '\n'
        footRotationES += self.FootHelperJoints[SERigNaming.sFootBallProxy] + '.rotateZ = clamp(0, 15, ' + footRotationControl.ControlObject + '.rotateX);'
        footRotationES += '\n'
        footRotationES += self.FootHelperJoints[SERigNaming.sFootToeProxy] + '.rotateZ = clamp(15, 45, ' + footRotationControl.ControlObject + '.rotateX) - 15;'
        footRotationES += '\n'
        footRotationES += self.FootHelperJoints[SERigNaming.sFootExtJnt] + '.rotateZ = clamp(-25, 0, ' + footRotationControl.ControlObject + '.rotateZ);'
        footRotationES += '\n'
        footRotationES += self.FootHelperJoints[SERigNaming.sFootIntJnt] + '.rotateZ = clamp(0, 25, ' + footRotationControl.ControlObject + '.rotateZ);'

        cmds.expression(n = footRotationEN, s = footRotationES, ae = 1)

    def attachFootHelperJoints(
            self,
            footHelperJointsMap
            ):

        # Fetch joints from map.
        footExtJnt = footHelperJointsMap[SERigNaming.sFootExtJnt]
        footToeProxy = footHelperJointsMap[SERigNaming.sFootToeProxy]
        footBallProxy = footHelperJointsMap[SERigNaming.sFootBallProxy]
        footAnkleProxy = footHelperJointsMap[SERigNaming.sFootAnkleProxy]

        # Attach foot helper joints to component's FootHelperJointsGroup.
        cmds.parent(footExtJnt, self.FootHelperJointsGroup)
        cmds.makeIdentity(footExtJnt, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)
        cmds.hide(footExtJnt)

        # Create foot PVs for foot IK handles.

        offsetZ = 5
        if self.RigSide == SERigEnum.eRigSide.RS_Right:
            offsetZ *= -1

        toeProxyPVlocator = cmds.spaceLocator(n = footToeProxy + SERigNaming.s_PoleVector)
        #cmds.delete(cmds.parentConstraint(footToeProxy, toeProxyPVlocator))  # This is WRONG!
        cmds.delete(cmds.parentConstraint(footBallProxy, toeProxyPVlocator))
        cmds.delete(cmds.pointConstraint(footToeProxy, toeProxyPVlocator))
        cmds.move(0, 0, offsetZ, toeProxyPVlocator, r = 1, os = 1)
        cmds.parent(toeProxyPVlocator, footToeProxy)
        cmds.makeIdentity(toeProxyPVlocator, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        ballProxyPVlocator = cmds.spaceLocator(n = footBallProxy + SERigNaming.s_PoleVector)
        #cmds.delete(cmds.parentConstraint(footBallProxy, ballProxyPVlocator))  # This is WRONG!
        cmds.delete(cmds.parentConstraint(footAnkleProxy, ballProxyPVlocator))
        cmds.delete(cmds.pointConstraint(footBallProxy, ballProxyPVlocator))
        cmds.move(0, 0, offsetZ, ballProxyPVlocator, r = 1, os = 1)
        cmds.parent(ballProxyPVlocator, footBallProxy)
        cmds.makeIdentity(ballProxyPVlocator, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        # Insert foot helper PVs into the map
        footHelperJointsMap[SERigNaming.sToeProxyPVlocator] = toeProxyPVlocator
        footHelperJointsMap[SERigNaming.sBallProxyPVlocator] = ballProxyPVlocator

        return footHelperJointsMap

    @staticmethod
    def mirrorFootHelperJointsMapForRightSide(leftFootHelperJoints = {}):

        leftFootExtJnt = leftFootHelperJoints[SERigNaming.sFootExtJnt]
        mirroredJoints = cmds.mirrorJoint(leftFootExtJnt, mb = True, myz = True, sr = ('L_', 'R_'))

        return {
                SERigNaming.sFootExtJnt:mirroredJoints[0],
                SERigNaming.sFootIntJnt:mirroredJoints[1],
                SERigNaming.sFootBaseJnt:mirroredJoints[2],
                SERigNaming.sFootBaseSwiveJnt:mirroredJoints[3],
                SERigNaming.sFootToeSwiveJnt:mirroredJoints[4],
                SERigNaming.sFootToeProxy:mirroredJoints[5],
                SERigNaming.sFootBallProxy:mirroredJoints[6],
                SERigNaming.sFootAnkleProxy:mirroredJoints[7]
                }


    @staticmethod
    def buildFootHelperJointsMapForLeftSide(
            legJoints = [],  # 0: hip, -1: toe, -2: ball, -3: ankle
            footExtLocator = '',
            footIntLocator = '',
            footBaseLocator = '',
            footBaseSwiveLocator = '',
            footToeSwiveLocator = ''
            ):

        nameNoPrefix = SEStringHelper.SE_RemovePrefix(footExtLocator)
        cmds.select(cl=1)
        footExtJnt = cmds.joint(n = nameNoPrefix + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(footExtLocator, footExtJnt))

        nameNoPrefix = SEStringHelper.SE_RemovePrefix(footIntLocator)
        cmds.select(cl=1)
        footIntJnt = cmds.joint(n = nameNoPrefix + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(footIntLocator, footIntJnt))

        nameNoPrefix = SEStringHelper.SE_RemovePrefix(footBaseLocator)
        cmds.select(cl=1)
        footBaseJnt = cmds.joint(n = nameNoPrefix + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(footBaseLocator, footBaseJnt))

        nameNoPrefix = SEStringHelper.SE_RemovePrefix(footBaseSwiveLocator)
        cmds.select(cl=1)
        footBaseSwiveJnt = cmds.joint(n = nameNoPrefix + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(footBaseSwiveLocator, footBaseSwiveJnt))

        nameNoPrefix = SEStringHelper.SE_RemovePrefix(footToeSwiveLocator)
        cmds.select(cl=1)
        footToeSwiveJnt = cmds.joint(n = nameNoPrefix + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(footToeSwiveLocator, footToeSwiveJnt))

        cmds.select(cl=1)
        footToeProxy = cmds.joint(n = legJoints[-1] + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(legJoints[-1], footToeProxy))

        cmds.select(cl=1)
        footBallProxy = cmds.joint(n = legJoints[-2] + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(legJoints[-2], footBallProxy))

        cmds.select(cl=1)
        footAnkleProxy = cmds.joint(n = legJoints[-3] + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(legJoints[-3], footAnkleProxy))

        cmds.parent(footAnkleProxy, footBallProxy)
        cmds.parent(footBallProxy, footToeProxy)
        cmds.parent(footToeProxy, footToeSwiveJnt)
        cmds.parent(footToeSwiveJnt, footBaseSwiveJnt)
        cmds.parent(footBaseSwiveJnt, footBaseJnt)
        cmds.parent(footBaseJnt, footIntJnt)
        cmds.parent(footIntJnt, footExtJnt)

        return {
                SERigNaming.sFootExtJnt:footExtJnt,
                SERigNaming.sFootIntJnt:footIntJnt,
                SERigNaming.sFootBaseJnt:footBaseJnt,
                SERigNaming.sFootBaseSwiveJnt:footBaseSwiveJnt,
                SERigNaming.sFootToeSwiveJnt:footToeSwiveJnt,
                SERigNaming.sFootToeProxy:footToeProxy,
                SERigNaming.sFootBallProxy:footBallProxy,
                SERigNaming.sFootAnkleProxy:footAnkleProxy
                }

#-----------------------------------------------------------------------------
# Rig Human Arm Class
# Sun Che
#-----------------------------------------------------------------------------
class RigHumanArm(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.FKArmControls = []
        self.ClavRotationControl = None
        self.ArmIKMainControl = None
        self.ArmPVControl = None

    def build(
            self,
            armJoints = [],  # 0: shoulder, 1: elbow, 2: wrist
            armPVLocator = '',
            rootJoint = '',
            chestEndJoint = '',
            rigScale = 1.0
            ):
        
        armParent = SEJointHelper.getFirstParentJoint(armJoints[0])

        # Create clavicle rotation control.
        if armParent:
            flipScaleX = False
            offsetX = 16.5
            if self.RigSide == SERigEnum.eRigSide.RS_Right:
                flipScaleX = True
                offsetX *= -1

            clavRotationControl = SERigControl.RigRotationControl(
                                     rigSide = self.RigSide,
                                     rigType = SERigEnum.eRigType.RT_Clavicle,
                                     rigFacing = SERigEnum.eRigFacing.RF_Z,
                                     prefix = self.Prefix + '_Clav_Rotation', 
                                     scale = rigScale * 4.5, 
                                     translateTo = armParent,
                                     parent = self.FKControlGroup, 
                                     lockChannels = ['s', 't', 'v'],
                                     flipScaleX = flipScaleX
                                     )
            clavRotationControl.adjustControlGroupOffset(offsetX, 10, -10)
            self.ClavRotationControl = clavRotationControl

            # Control the clavicle joint.
            cmds.orientConstraint(clavRotationControl.ControlObject, armParent, mo = 1)

            # Attach clavicle control group to chest end joint.
            if cmds.objExists(chestEndJoint):
                cmds.parentConstraint(chestEndJoint, clavRotationControl.ControlGroup, mo = 1)

        # Create arm IK main control.
        flipScaleXYZ = False
        if self.RigSide == SERigEnum.eRigSide.RS_Right:
            flipScaleXYZ = True
        armIKMainControl = SERigControl.RigCircleControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_Wrist,
                                rigFacing = SERigEnum.eRigFacing.RF_X,
                                prefix = self.Prefix + '_IK_Main', 
                                scale = rigScale * 8, 
                                translateTo = armJoints[2],
                                rotateTo = armJoints[2], 
                                parent = self.IKControlGroup, 
                                lockChannels = ['s', 'v'],
                                flipScaleX = flipScaleXYZ,
                                flipScaleY = flipScaleXYZ,
                                flipScaleZ = flipScaleXYZ
                                )
        self.ArmIKMainControl = armIKMainControl

        # Create IK arm joints.
        ikShoulderJoint = cmds.duplicate(armJoints[0], n = SERigNaming.sIKPrefix + armJoints[0], parentOnly = True)[0]
        ikElbowJoint = cmds.duplicate(armJoints[1], n = SERigNaming.sIKPrefix + armJoints[1], parentOnly = True)[0]
        ikWristJoint = cmds.duplicate(armJoints[2], n = SERigNaming.sIKPrefix + armJoints[2], parentOnly = True)[0]
        cmds.parent(ikWristJoint, ikElbowJoint)
        cmds.parent(ikElbowJoint, ikShoulderJoint)

        ikJoints = [ikShoulderJoint, ikElbowJoint, ikWristJoint]

        # Create IK handle.
        wristIK = cmds.ikHandle(n = self.Prefix + 'Wrist' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', sj = ikShoulderJoint, ee = ikWristJoint)[0]
        cmds.hide(wristIK)
        cmds.parent(wristIK, self.RigPartsGrp)
        cmds.pointConstraint(armIKMainControl.ControlObject, wristIK, mo = 0)
        cmds.poleVectorConstraint(armPVLocator, wristIK)

        # Attach ik joints to current rig component.
        ikJointsGroup = cmds.group(n = self.Prefix + '_IK_JointsGrp', em = 1, p = self.JointsGrp)
        cmds.parent(ikShoulderJoint, ikJointsGroup)

        if armParent:
            cmds.parentConstraint(armParent, ikJointsGroup, mo = 1)

        # Create FK arm joints.
        fkShoulderJoint = cmds.duplicate(armJoints[0], n = SERigNaming.sFKPrefix + armJoints[0], parentOnly = True)[0]
        fkElbowJoint = cmds.duplicate(armJoints[1], n = SERigNaming.sFKPrefix + armJoints[1], parentOnly = True)[0]
        fkWristJoint = cmds.duplicate(armJoints[2], n = SERigNaming.sFKPrefix + armJoints[2], parentOnly = True)[0]
        cmds.parent(fkWristJoint, fkElbowJoint)
        cmds.parent(fkElbowJoint, fkShoulderJoint)

        fkJoints = [fkShoulderJoint, fkElbowJoint, fkWristJoint]
        fkRigTypes = [SERigEnum.eRigType.RT_Shoulder, SERigEnum.eRigType.RT_Elbow, SERigEnum.eRigType.RT_Wrist]

        # Create FK arm controls.
        preParent = self.FKControlGroup
        curScaleYZ = 10
        curFKJnt = None
        nextFKJnt = None
        for i in range(len(fkJoints) - 1):
            curFKJnt = fkJoints[i]
            nextFKJnt = fkJoints[i + 1]
            curFKJntLoc = SEMathHelper.getWorldPosition(curFKJnt)
            nextFKJntLoc = SEMathHelper.getWorldPosition(nextFKJnt)
            distance = SEMathHelper.getDistance3(curFKJntLoc, nextFKJntLoc)

            curFKControl = SERigControl.RigCubeControl(
                                    rigSide = self.RigSide,
                                    rigType = fkRigTypes[i],
                                    prefix = SERigNaming.sFKPrefix + self.Prefix + str(i), 
                                    translateTo = curFKJnt,
                                    rotateTo = curFKJnt,
                                    scale = rigScale*20,
                                    parent = preParent,
                                    lockChannels = ['t', 's', 'v'],
                                    cubeScaleX = distance,
                                    cubeScaleY = curScaleYZ,
                                    cubeScaleZ = curScaleYZ,
                                    transparency = 0.85
                                    )
            self.FKArmControls.append(curFKControl)

            cmds.orientConstraint(curFKControl.ControlObject, curFKJnt)
            cmds.pointConstraint(curFKControl.ControlObject, curFKJnt)

            preParent = curFKControl.ControlObject
            curScaleYZ *= 0.9

        # Create Wrist FK control.
        curFKControl = SERigControl.RigCubeControl(
                                rigSide = self.RigSide,
                                rigType = fkRigTypes[2],
                                prefix = SERigNaming.sFKPrefix + self.Prefix + str(2), 
                                translateTo = nextFKJnt,
                                rotateTo = nextFKJnt,
                                scale = rigScale*20,
                                parent = preParent,
                                lockChannels = ['t', 's', 'v'],
                                cubeScaleX = curScaleYZ,
                                cubeScaleY = curScaleYZ,
                                cubeScaleZ = curScaleYZ,
                                transparency = 0.85
                                )
        self.FKArmControls.append(curFKControl)

        cmds.orientConstraint(curFKControl.ControlObject, nextFKJnt)
        cmds.pointConstraint(curFKControl.ControlObject, nextFKJnt)

        # Create arm PV control.
        armPVControl = SERigControl.RigDiamondControl(
                                 rigSide = self.RigSide,
                                 rigType = SERigEnum.eRigType.RT_ArmPV,
                                 rigFacing = SERigEnum.eRigFacing.RF_Y,
                                 prefix = self.Prefix + '_PV', 
                                 scale = rigScale * 15, 
                                 translateTo = armPVLocator,
                                 parent = self.ControlsGrp, 
                                 lockChannels = ['s', 'r', 'v'],
                                 flipScaleX = flipScaleX
                                 )
        self.ArmPVControl = armPVControl
        
        # Move arm PV locator from builder scene to this component.
        cmds.parent(armPVLocator, self.RigPartsGrp)
        cmds.pointConstraint(armPVControl.ControlObject, armPVLocator)
        cmds.hide(armPVLocator)

        # Attach FK joints to current rig component.
        fkJointsGroup = cmds.group(n = self.Prefix + '_FK_JointsGrp', em = 1, p = self.JointsGrp)
        cmds.parent(fkJoints[0], fkJointsGroup)

        if armParent:
            cmds.parentConstraint(armParent, fkJointsGroup, mo = 1)

        # Create FK IK blenders.
        if self.BaseRig:
            for i in range(len(armJoints)):
                blender = cmds.createNode("blendColors")
                cmds.connectAttr(ikJoints[i] + '.r', blender + '.color1', f = 1)
                cmds.connectAttr(fkJoints[i] + '.r', blender + '.color2', f = 1)
                cmds.connectAttr(blender + '.output', armJoints[i] + '.r', f = 1)

                blenderControlAttr = self.BaseRig.getArmIKFKSwitch(self.RigSide)
                cmds.connectAttr(blenderControlAttr, blender + '.blender')

            # Attach FK arm controls to base rig attach point.
            fkArmAttachPoint = SEJointHelper.getFirstParentJoint(armJoints[0])
            if fkArmAttachPoint and len(self.FKArmControls) > 0:
                cmds.parentConstraint(fkArmAttachPoint, self.FKArmControls[0].ControlGroup, mo = 1)

#-----------------------------------------------------------------------------
# Rig Human Hand Class
# Sun Che
#-----------------------------------------------------------------------------
class RigHumanHand(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.FKFingerControls = []

    def build(
            self,
            fingers = [],
            rootJoint = '',
            armFKFingerAttachPoint = '',
            rigScale = 1.0
            ):

        fkFingerControlGroup = cmds.group(n = self.Prefix + SERigNaming.s_FKPrefix + 'Finger' + SERigNaming.sControlGroup, em = 1, 
                                          p = self.FKControlGroup)

        # Attach fk fingers to the arm.
        if cmds.objExists(armFKFingerAttachPoint):
            cmds.parentConstraint(armFKFingerAttachPoint, fkFingerControlGroup)

        for finger in fingers:

            fingerJoints = SEJointHelper.listHierarchy(finger, withEndJoints = True)
            fkJoints = fingerJoints

            # Create FK finger controls.
            preParent = fkFingerControlGroup
            curScaleYZ = 2.5
            curFKJnt = None
            nextFKJnt = None
            curFKFingerControls = []
            for i in range(len(fkJoints) - 1):
                curFKJnt = fkJoints[i]
                nextFKJnt = fkJoints[i + 1]
                curFKJntLoc = SEMathHelper.getWorldPosition(curFKJnt)
                nextFKJntLoc = SEMathHelper.getWorldPosition(nextFKJnt)
                distance = SEMathHelper.getDistance3(curFKJntLoc, nextFKJntLoc)

                curFKControl = SERigControl.RigCubeControl(
                                        rigSide = self.RigSide,
                                        rigType = SERigEnum.eRigType.RT_Hand,
                                        prefix = SERigNaming.sFKPrefix + fingerJoints[0] + str(i), 
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
                curFKFingerControls.append(curFKControl)

                cmds.orientConstraint(curFKControl.ControlObject, curFKJnt)
                cmds.pointConstraint(curFKControl.ControlObject, curFKJnt)

                preParent = curFKControl.ControlObject

            self.FKFingerControls.append(curFKFingerControls)