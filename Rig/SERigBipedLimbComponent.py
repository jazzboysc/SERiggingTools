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
# Rig Human Limb Base Class
# Sun Che
#-----------------------------------------------------------------------------
class RigHumanLimb(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.LimbIKMainControl = None
        self.LimbIKMainRotationControl = None
        self.LimbIKMainControlSyncTarget = None
        self.LimbPVControl = None
        self.PVLocatorSync = None
        self.LimbFKControls = []
        self.LimbFKControlSyncTargets = []


    @staticmethod
    def getFKSyncTargets(rigHumanLimb):

        res = []
        
        if cmds.objExists(rigHumanLimb):
            if cmds.attributeQuery(SERigNaming.sPrefixAttr, n = rigHumanLimb, ex = 1):

                prefixAttr = cmds.getAttr(rigHumanLimb + '.' + SERigNaming.sPrefixAttr)
                FKSyncTargetsAttr = prefixAttr + SERigNaming.sFKSyncTargets

                if cmds.attributeQuery(FKSyncTargetsAttr, n = rigHumanLimb, ex = 1):
                    compoundRes = cmds.getAttr(rigHumanLimb + '.' + FKSyncTargetsAttr)[0]
                    for i in range(len(compoundRes)):
                        curAttr = prefixAttr + SERigNaming.sFKSyncTarget + str(i)
                        curAttrValue = cmds.listConnections(rigHumanLimb + '.' + curAttr)
                        res.append(curAttrValue[0])
                else:
                    cmds.error('Attribute does not exist.')

            else:
                cmds.error('Attribute does not exist.')
        else:
            cmds.error('Rig component does not exist.')

        return res


    @staticmethod
    def getFKSyncSources(rigHumanLimb):

        res = []
        
        if cmds.objExists(rigHumanLimb):
            if cmds.attributeQuery(SERigNaming.sPrefixAttr, n = rigHumanLimb, ex = 1):

                prefixAttr = cmds.getAttr(rigHumanLimb + '.' + SERigNaming.sPrefixAttr)
                FKSyncSourcesAttr = prefixAttr + SERigNaming.sFKSyncSources

                if cmds.attributeQuery(FKSyncSourcesAttr, n = rigHumanLimb, ex = 1):
                    compoundRes = cmds.getAttr(rigHumanLimb + '.' + FKSyncSourcesAttr)[0]
                    for i in range(len(compoundRes)):
                        curAttr = prefixAttr + SERigNaming.sFKSyncSource + str(i)
                        curAttrValue = cmds.listConnections(rigHumanLimb + '.' + curAttr)
                        res.append(curAttrValue[0])
                else:
                    cmds.error('Attribute does not exist.')

            else:
                cmds.error('Attribute does not exist.')
        else:
            cmds.error('Rig component does not exist.')

        return res


    @staticmethod
    def getIKMainControl(rigHumanLimb):

        res = None
        if cmds.objExists(rigHumanLimb):
            if cmds.attributeQuery(SERigNaming.sIKMainControl, n = rigHumanLimb, ex = 1):
                res = cmds.listConnections(rigHumanLimb + '.' + SERigNaming.sIKMainControl)[0]
            else:
                cmds.error('Attribute does not exist.')
        else:
            cmds.error('Rig component does not exist.')

        return res


    @staticmethod
    def getIKMainRotationControl(rigHumanLimb):

        res = None
        if cmds.objExists(rigHumanLimb):
            if cmds.attributeQuery(SERigNaming.sIKMainRotationControl, n = rigHumanLimb, ex = 1):
                res = cmds.listConnections(rigHumanLimb + '.' + SERigNaming.sIKMainRotationControl)[0]
            else:
                cmds.error('Attribute does not exist.')
        else:
            cmds.error('Rig component does not exist.')

        return res


    @staticmethod
    def getPVControl(rigHumanLimb):

        res = None
        if cmds.objExists(rigHumanLimb):
            if cmds.attributeQuery(SERigNaming.sPVControl, n = rigHumanLimb, ex = 1):
                res = cmds.listConnections(rigHumanLimb + '.' + SERigNaming.sPVControl)[0]
            else:
                cmds.error('Attribute does not exist.')
        else:
            cmds.error('Rig component does not exist.')

        return res


    @staticmethod
    def getIKMainControlSyncTarget(rigHumanLimb):

        res = None
        if cmds.objExists(rigHumanLimb):
            if cmds.attributeQuery(SERigNaming.sIKMainControlSyncTarget, n = rigHumanLimb, ex = 1):
                res = cmds.listConnections(rigHumanLimb + '.' + SERigNaming.sIKMainControlSyncTarget)[0]
            else:
                cmds.error('Attribute does not exist.')
        else:
            cmds.error('Rig component does not exist.')

        return res


    @staticmethod
    def getPVLocatorSyncTarget(rigHumanLimb):

        res = None
        if cmds.objExists(rigHumanLimb):
            if cmds.attributeQuery(SERigNaming.sPVLocatorSyncTarget, n = rigHumanLimb, ex = 1):
                res = cmds.listConnections(rigHumanLimb + '.' + SERigNaming.sPVLocatorSyncTarget)[0]
            else:
                cmds.error('Attribute does not exist.')
        else:
            cmds.error('Rig component does not exist.')

        return res


    def createPVLocatorSync(self, limbPVLocator, parentJoint):

        if cmds.objExists(limbPVLocator) and cmds.objExists(parentJoint):

            self.PVLocatorSync = cmds.duplicate(limbPVLocator, n = limbPVLocator + SERigNaming.s_Sync, rr = True, po = True)[0]
            cmds.parent(self.PVLocatorSync, w = 1) # Parent to world space first.
            cmds.parent(self.PVLocatorSync, self.RigPartsGrp)
            cmds.parentConstraint(parentJoint, self.PVLocatorSync, mo = 1)
            cmds.hide(self.PVLocatorSync)

        else:
            print('Cannot create limb PV locator sync.')


    @staticmethod
    def syncIKToFK(rigHumanLimb):

        LimbIKMainControl = RigHumanLimb.getIKMainControl(rigHumanLimb)
        LimbIKMainControlSyncTarget = RigHumanLimb.getIKMainControlSyncTarget(rigHumanLimb)
        LimbPVControl = RigHumanLimb.getPVControl(rigHumanLimb)
        PVLocatorSync = RigHumanLimb.getPVLocatorSyncTarget(rigHumanLimb)
        LimbIKMainRotationControl = RigHumanLimb.getIKMainRotationControl(rigHumanLimb)

        if LimbIKMainControl and LimbIKMainControlSyncTarget and LimbPVControl and PVLocatorSync and LimbIKMainRotationControl:

            cmds.delete(cmds.pointConstraint(PVLocatorSync, LimbPVControl))
            cmds.delete(cmds.pointConstraint(LimbIKMainControlSyncTarget, LimbIKMainControl))
            cmds.delete(cmds.orientConstraint(LimbIKMainControlSyncTarget, LimbIKMainRotationControl))

        else:
            print('Delegates not created.')


    @staticmethod
    def syncFKToIK(rigHumanLimb):
        
        LimbFKControls = RigHumanLimb.getFKSyncSources(rigHumanLimb)
        LimbFKControlSyncTargets = RigHumanLimb.getFKSyncTargets(rigHumanLimb)
        numFKControls = len(LimbFKControls)
        numFKControlTargets = len(LimbFKControlSyncTargets)

        if numFKControls == numFKControlTargets:

            for fkControl, fkControlTarget in zip(LimbFKControls, LimbFKControlSyncTargets):
                cmds.delete(cmds.orientConstraint(fkControlTarget, fkControl))

        else:
            print('The numbers of FK control sources and targets do not match.')


    def createDelegateAttributes(self):

        # FK to IK
        
        FKSyncTargetsAttr = self.Prefix + 'FKSyncTargets'
        FKSyncSourcesAttr = self.Prefix + 'FKSyncSources'
        
        numTargets = len(self.LimbFKControlSyncTargets)
        numSources = len(self.LimbFKControls)

        if numTargets != numSources:
            cmds.error('The number of FK sync targets does not match the number of FK sync sources')
            return

        # Create compound message attribute for FK sync targets.
        cmds.addAttr(self.TopGrp, ln = FKSyncTargetsAttr, nc = numTargets, at = 'compound')
        for i in range(numTargets):
            curTargetAttr = self.Prefix + 'FKSyncTarget' + str(i)
            cmds.addAttr(self.TopGrp, ln = curTargetAttr, at = 'message', p = FKSyncTargetsAttr)

        # Create compound message attributes for FK sync sources.
        cmds.addAttr(self.TopGrp, ln = FKSyncSourcesAttr, nc = numSources, at = 'compound')
        for i in range(numSources):
            curSourceAttr = self.Prefix + 'FKSyncSource' + str(i)
            cmds.addAttr(self.TopGrp, ln = curSourceAttr, at = 'message', p = FKSyncSourcesAttr)

        # Connect sub message attributes to sync targets and sources.
        i = 0
        for fkControl, fkControlTarget in zip(self.LimbFKControls, self.LimbFKControlSyncTargets):
            curTargetAttr = self.Prefix + 'FKSyncTarget' + str(i)
            cmds.connectAttr(fkControlTarget + '.message', self.TopGrp + '.' + curTargetAttr)
            curSourceAttr = self.Prefix + 'FKSyncSource' + str(i)
            cmds.connectAttr(fkControl.ControlObject + '.message', self.TopGrp + '.' + curSourceAttr)
            i += 1

        # IK to FK

        # Create message attributes for IK sync targets and sources.
        cmds.addAttr(self.TopGrp, ln = 'IKMainControl', at = 'message')
        cmds.addAttr(self.TopGrp, ln = 'IKMainRotationControl', at = 'message')
        cmds.addAttr(self.TopGrp, ln = 'PVControl', at = 'message')
        cmds.addAttr(self.TopGrp, ln = 'IKMainControlSyncTarget', at = 'message')
        cmds.addAttr(self.TopGrp, ln = 'PVLocatorSyncTarget', at = 'message')

        # Connect message attributes to sync targets and sources.
        cmds.connectAttr(self.LimbIKMainControl.ControlObject + '.message', self.TopGrp + '.' + 'IKMainControl')
        cmds.connectAttr(self.LimbIKMainRotationControl.ControlObject + '.message', self.TopGrp + '.' + 'IKMainRotationControl')
        cmds.connectAttr(self.LimbPVControl.ControlObject + '.message', self.TopGrp + '.' + 'PVControl')
        cmds.connectAttr(self.LimbIKMainControlSyncTarget.ControlObject + '.message', self.TopGrp + '.' + 'IKMainControlSyncTarget')
        cmds.connectAttr(self.PVLocatorSync + '.message', self.TopGrp + '.' + 'PVLocatorSyncTarget')



#-----------------------------------------------------------------------------
# Rig Human Leg Class
# Sun Che
#-----------------------------------------------------------------------------
class RigHumanLeg(RigHumanLimb):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_LegComponent
                 ):

        RigHumanLimb.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.FootHelperJointsGroup = cmds.group(n = prefix + '_FootHelperJointsGrp', p = self.JointsGrp, em = 1)
        self.FootHelperJoints = None
        self.AnkleIKRotationControl = None
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
            rigScale = 1.0,
            fkControlScaleYZ = 19,
            fkControlScaleYZMultiplier = 0.75,
            fkControlTransparency = 0.85,
            ballIKTwistLeft = 90,
            ballIKTwistRight = 270,
            toeIKTwistLeft = 90,
            toeIKTwistRight = 0
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
                                rigType = SERigEnum.eRigType.RT_FootIKMain,
                                prefix = self.Prefix + '_IK_Main', 
                                scale = rigScale * 55, 
                                matchBoundingBoxScale = True,
                                scaleX = footSize,
                                scaleZ = footSize,
                                translateTo = self.FootHelperJoints[SERigNaming.sFootBaseJnt],
                                rotateTo = self.FootHelperJoints[SERigNaming.sFootBaseJnt],
                                parent = self.IKControlGroup, 
                                lockChannels = ['s', 'r', 'v'],
                                flipScaleX = flipScaleXYZ,
                                flipScaleY = flipScaleXYZ,
                                flipScaleZ = flipScaleXYZ
                                )
        self.FootIKMainControl = footIKMainControl
        self.LimbIKMainControl = footIKMainControl
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.FootIKMainControl.ControlGroup, 'FootIKMainControl')

        if self.RigSide == SERigEnum.eRigSide.RS_Right:
            ikMainControlOffsetX = -0.5
        else:
            ikMainControlOffsetX = 0.5
        footIKMainControl.adjustControlGroupOffset(ikMainControlOffsetX, 0, -5)

        # Adjust main IK control's pivot to ankle's position.
        SEMathHelper.movePivotTo(footIKMainControl.ControlObject, legJoints[-3])

        # Create ankle IK rotation control.
        ankleIKRotationControl = SERigControl.RigCircleControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_AnkleIKRotation,
                                rigFacing = SERigEnum.eRigFacing.RF_X,
                                prefix = self.Prefix + '_IK_Rotation', 
                                scale = rigScale * 9, 
                                translateTo = legJoints[-3],
                                rotateTo = legJoints[-3], 
                                parent = footIKMainControl.ControlObject, 
                                lockChannels = ['s', 't', 'v']
                                )
        self.AnkleIKRotationControl = ankleIKRotationControl
        self.LimbIKMainRotationControl = ankleIKRotationControl
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.AnkleIKRotationControl.ControlGroup, 'AnkleIKRotationControl')

        # Create foot base swive control.
        flipScaleX = False
        if self.RigSide == SERigEnum.eRigSide.RS_Right:
            flipScaleX = True

        footBaseSwiveControl = SERigControl.RigCircleControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_FootBaseSwive,
                                rigFacing = SERigEnum.eRigFacing.RF_Y,
                                prefix = self.Prefix + '_FootBaseSwive', 
                                scale = rigScale * 3.5, 
                                translateTo = self.FootHelperJoints[SERigNaming.sFootBaseSwiveJnt],
                                parent = footIKMainControl.ControlObject, 
                                lockChannels = ['s', 't', 'rx', 'rz', 'v'],
                                flipScaleX = flipScaleX
                                )
        self.FootBaseSwiveControl = footBaseSwiveControl
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.FootBaseSwiveControl.ControlGroup, 'FootBaseSwiveControl')

        # Create foot toe swive control.
        footToeSwiveControl = SERigControl.RigCircleControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_FootToeSwive,
                                rigFacing = SERigEnum.eRigFacing.RF_Y,
                                prefix = self.Prefix + '_ToeSwive', 
                                scale = rigScale * 6, 
                                translateTo = self.FootHelperJoints[SERigNaming.sFootToeSwiveJnt],
                                parent = footIKMainControl.ControlObject, 
                                lockChannels = ['s', 't', 'rx', 'rz', 'v'],
                                flipScaleX = flipScaleX
                                )
        self.FootToeSwiveControl = footToeSwiveControl
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.FootToeSwiveControl.ControlGroup, 'FootToeSwiveControl')

        # Create foot rotation control.
        footRotationControl = SERigControl.RigRotationControl(
                                 rigSide = self.RigSide,
                                 rigType = SERigEnum.eRigType.RT_FootRotation,
                                 rigFacing = SERigEnum.eRigFacing.RF_Z,
                                 prefix = self.Prefix + '_Rotation', 
                                 scale = rigScale * 6, 
                                 translateTo = self.FootHelperJoints[SERigNaming.sFootBaseJnt],
                                 parent = footIKMainControl.ControlObject, 
                                 lockChannels = ['s', 't', 'v'],
                                 flipScaleX = flipScaleX
                                 )
        self.FootRotationControl = footRotationControl
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.FootRotationControl.ControlGroup, 'FootRotationControl')

        footRotationControl.adjustControlGroupOffset(0, 8, -15)

        # Create leg PV control.
        legPVControl = SERigControl.RigDiamondControl(
                                 rigSide = self.RigSide,
                                 rigType = SERigEnum.eRigType.RT_LegPV,
                                 rigFacing = SERigEnum.eRigFacing.RF_Y,
                                 prefix = self.Prefix + '_PV', 
                                 scale = rigScale * 15, 
                                 translateTo = legPVLocator,
                                 parent = self.IKControlGroup, 
                                 lockChannels = ['s', 'r', 'v'],
                                 flipScaleX = flipScaleX
                                 )
        self.LegPVControl = legPVControl
        self.LimbPVControl = legPVControl
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.LegPVControl.ControlGroup, 'LegPVControl')
        
        # Move leg PV locator from builder scene to this component.
        cmds.parent(legPVLocator, self.RigPartsGrp)
        cmds.pointConstraint(legPVControl.ControlObject, legPVLocator)
        cmds.hide(legPVLocator)

        # Attach foot helper joints to ankle IK rotation control.
        cmds.parentConstraint(ankleIKRotationControl.ControlObject, self.FootHelperJointsGroup, mo = 1)

        # Create IK leg joints.
        ikJoints = SEJointHelper.duplicateHierarchy(legJoints[0], SERigNaming.sIKPrefix)
        cmds.hide(ikJoints[0])

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
            cmds.setAttr(ballIK + '.twist', ballIKTwistLeft)
        else:
            cmds.setAttr(ballIK + '.twist', ballIKTwistRight)

        toeIK = cmds.ikHandle(n = self.Prefix + 'Toe' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', sj = ikJoints[3], ee = ikJoints[4])[0]
        cmds.hide(toeIK)
        cmds.parent(toeIK, self.RigPartsGrp)
        cmds.pointConstraint(self.FootHelperJoints[SERigNaming.sFootToeProxy], toeIK, mo = 0)
        cmds.poleVectorConstraint(self.FootHelperJoints[SERigNaming.sToeProxyPVlocator], toeIK)
        if self.RigSide == SERigEnum.eRigSide.RS_Left:
            cmds.setAttr(toeIK + '.twist', toeIKTwistLeft)
        else:
            cmds.setAttr(toeIK + '.twist', toeIKTwistRight)

        # Attach ik joints to current rig component.
        ikJointsGroup = cmds.group(n = self.Prefix + '_IK_JointsGrp', em = 1, p = self.JointsGrp)
        cmds.parent(ikJoints[0], ikJointsGroup)
        ikJointsParent = SEJointHelper.getFirstParentJoint(legJoints[0])
        cmds.parentConstraint(ikJointsParent, ikJointsGroup, mo = 1)

        # Create FK leg joints.
        fkJoints = SEJointHelper.duplicateHierarchy(legJoints[0], SERigNaming.sFKPrefix)
        cmds.hide(fkJoints[0])

        # Create FK leg controls.
        preParent = self.FKControlGroup
        curScaleYZ = fkControlScaleYZ
        for i in range(len(fkJoints) - 1):
            curFKJnt = fkJoints[i]
            nextFKJnt = fkJoints[i + 1]
            curFKJntLoc = SEMathHelper.getWorldPosition(curFKJnt)
            nextFKJntLoc = SEMathHelper.getWorldPosition(nextFKJnt)
            distance = SEMathHelper.getDistance3(curFKJntLoc, nextFKJntLoc)

            curFKControl = SERigControl.RigCubeControl(
                                    rigSide = self.RigSide,
                                    rigType = SERigEnum.eRigType.RT_LegFK,
                                    rigControlIndex = i,
                                    prefix = SERigNaming.sFKPrefix + self.Prefix + str(i), 
                                    translateTo = curFKJnt,
                                    rotateTo = curFKJnt,
                                    scale = rigScale*20,
                                    parent = preParent,
                                    lockChannels = ['t', 's', 'v'],
                                    cubeScaleX = distance,
                                    cubeScaleY = curScaleYZ,
                                    cubeScaleZ = curScaleYZ,
                                    transparency = fkControlTransparency
                                    )
            self.FKLegControls.append(curFKControl)
            SERigObjectTypeHelper.linkRigObjects(self.TopGrp, curFKControl.ControlGroup, 'FKLegControl' + str(i))

            cmds.orientConstraint(curFKControl.ControlObject, curFKJnt)
            cmds.pointConstraint(curFKControl.ControlObject, curFKJnt)

            preParent = curFKControl.ControlObject
            curScaleYZ *= fkControlScaleYZMultiplier

        # IK main control sync target delegate.
        self.LimbIKMainControlSyncTarget = self.FKLegControls[2]

        # Attach fk joints to current rig component.
        fkJointsGroup = cmds.group(n = self.Prefix + '_FK_JointsGrp', em = 1, p = self.JointsGrp)
        cmds.parent(fkJoints[0], fkJointsGroup)
        fkJointsParent = SEJointHelper.getFirstParentJoint(legJoints[0])
        cmds.parentConstraint(fkJointsParent, fkJointsGroup, mo = 1)

        # FK control delegate.
        for fkLegControl in self.FKLegControls:
            self.LimbFKControls.append(fkLegControl)

        # FK control sync target delegate.
        ikJointsForDelegate = ikJoints[:-1] # Remove toe joint
        for ikJointTarget in ikJointsForDelegate:
            self.LimbFKControlSyncTargets.append(ikJointTarget)

        # Create PV sync.
        self.createPVLocatorSync(legPVLocator, fkJoints[1])

        # Create FK IK blenders.
        if self.BaseRig:
            for i in range(len(legJoints)):
                blender = cmds.createNode("blendColors")
                cmds.connectAttr(ikJoints[i] + '.r', blender + '.color1', f = 1)
                cmds.connectAttr(fkJoints[i] + '.r', blender + '.color2', f = 1)
                cmds.connectAttr(blender + '.output', legJoints[i] + '.r', f = 1)

                blenderControlAttr = self.BaseRig.getLegIKFKSwitch(self.RigSide)
                cmds.connectAttr(blenderControlAttr, blender + '.blender')

            # Attach FK controls to the pelvis.
            fkAttachPoint = SEJointHelper.getFirstParentJoint(legJoints[0])
            if fkAttachPoint:
                locatorHipLocal = cmds.spaceLocator(n = 'locator_' + self.Prefix + '_HipLocal')[0]
                cmds.delete(cmds.parentConstraint(legJoints[0], locatorHipLocal))
                cmds.parent(locatorHipLocal, self.RigPartsGrp)
                cmds.parentConstraint(fkAttachPoint, locatorHipLocal, mo = 1)
                cmds.hide(locatorHipLocal)

                locatorHipWorld = cmds.spaceLocator(n = 'locator_' + self.Prefix + '_HipWorld')[0]
                cmds.delete(cmds.parentConstraint(legJoints[0], locatorHipWorld))
                cmds.parent(locatorHipWorld, self.RigPartsGrp)
                cmds.hide(locatorHipWorld)

                # FK leg control 0 follows the position of locatorHipLocal.
                cmds.pointConstraint(locatorHipLocal, self.FKLegControls[0].ControlGroup, mo = 0)

                blender = cmds.createNode("blendColors")
                cmds.connectAttr(locatorHipLocal + '.r', blender + '.color2', f = 1)
                cmds.connectAttr(locatorHipWorld + '.r', blender + '.color1', f = 1)
                cmds.connectAttr(blender + '.output', self.FKLegControls[0].ControlGroup + '.r', f = 1)

                blenderControlAttr = self.BaseRig.getLegFKLocalToWorldSwitch(self.RigSide)
                if blenderControlAttr:
                    cmds.connectAttr(blenderControlAttr, blender + '.blender')
                else:
                    cmds.error('Blender Control Attribute not found.')

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

        # Create IK/FK control group auto hide expression.

        mainCtrlAutoHideAt = ''
        mainCtrlIKFKSwitchAt = ''
        if self.RigSide == SERigEnum.eRigSide.RS_Left:
            mainCtrlAutoHideAt = SERigNaming.sLeftLegIKFKAutoHide
            mainCtrlIKFKSwitchAt = SERigNaming.sLeftLegIKFKSwitch
        else:
            mainCtrlAutoHideAt = SERigNaming.sRightLegIKFKAutoHide
            mainCtrlIKFKSwitchAt = SERigNaming.sRightLegIKFKSwitch

        mainControl = SERigNaming.sMainControlPrefix + SERigNaming.sControl
        ikfkAutoHideEN = SERigNaming.sExpressionPrefix + self.Prefix + 'IKFKAutoHide'
        ikfkAutoHideES = 'if( ' + mainControl + '.' + mainCtrlAutoHideAt + ' )'
        ikfkAutoHideES += '\n{\n'
        ikfkAutoHideES += '\t' + self.FKControlGroup + '.visibility = 1 - int(' + mainControl + '.' + mainCtrlIKFKSwitchAt + ');'
        ikfkAutoHideES += '\n'
        ikfkAutoHideES += '\t' + self.IKControlGroup + '.visibility = int(' + mainControl + '.' + mainCtrlIKFKSwitchAt + ');'
        ikfkAutoHideES += '\n}\nelse\n{\n'
        ikfkAutoHideES += '\t' + self.FKControlGroup + '.visibility = 1;'
        ikfkAutoHideES += '\n'
        ikfkAutoHideES += '\t' + self.IKControlGroup + '.visibility = 1;'
        ikfkAutoHideES += '\n}'

        cmds.expression(n = ikfkAutoHideEN, s = ikfkAutoHideES, ae = 1)

        # Create delegate message attributes on top group.
        self.createDelegateAttributes()


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
class RigHumanArm(RigHumanLimb):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_ArmComponent
                 ):

        RigHumanLimb.__init__(self, prefix, baseRig, rigSide, rigType)

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
            rigScale = 1.0,
            fkControlScaleYZ = 10,
            fkControlScaleYZMultiplier = 0.9,
            fkControlTransparency = 0.85
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
            SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.ClavRotationControl.ControlGroup, 'ClavRotationControl')

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
                                rigType = SERigEnum.eRigType.RT_ArmIKMain,
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
        self.LimbIKMainControl = armIKMainControl
        self.LimbIKMainRotationControl = armIKMainControl
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.ArmIKMainControl.ControlGroup, 'ArmIKMainControl')

        # Create IK arm joints.
        ikShoulderJoint = cmds.duplicate(armJoints[0], n = SERigNaming.sIKPrefix + armJoints[0], parentOnly = True)[0]
        ikElbowJoint = cmds.duplicate(armJoints[1], n = SERigNaming.sIKPrefix + armJoints[1], parentOnly = True)[0]
        ikWristJoint = cmds.duplicate(armJoints[2], n = SERigNaming.sIKPrefix + armJoints[2], parentOnly = True)[0]
        cmds.parent(ikWristJoint, ikElbowJoint)
        cmds.parent(ikElbowJoint, ikShoulderJoint)
        cmds.hide(ikShoulderJoint)

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

        # Create ik wrist rotation constraint.
        cmds.orientConstraint(armIKMainControl.ControlObject, ikWristJoint)

        # Create FK arm joints.
        fkShoulderJoint = cmds.duplicate(armJoints[0], n = SERigNaming.sFKPrefix + armJoints[0], parentOnly = True)[0]
        fkElbowJoint = cmds.duplicate(armJoints[1], n = SERigNaming.sFKPrefix + armJoints[1], parentOnly = True)[0]
        fkWristJoint = cmds.duplicate(armJoints[2], n = SERigNaming.sFKPrefix + armJoints[2], parentOnly = True)[0]
        cmds.parent(fkWristJoint, fkElbowJoint)
        cmds.parent(fkElbowJoint, fkShoulderJoint)
        cmds.hide(fkShoulderJoint)

        fkJoints = [fkShoulderJoint, fkElbowJoint, fkWristJoint]
        fkRigTypes = [SERigEnum.eRigType.RT_ShoulderFK, SERigEnum.eRigType.RT_ElbowFK, SERigEnum.eRigType.RT_WristFK]

        # Create FK arm controls.
        preParent = self.FKControlGroup
        curScaleYZ = fkControlScaleYZ
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
                                    transparency = fkControlTransparency
                                    )
            self.FKArmControls.append(curFKControl)
            SERigObjectTypeHelper.linkRigObjects(self.TopGrp, curFKControl.ControlGroup, 'FKArmControl' + str(i))

            cmds.orientConstraint(curFKControl.ControlObject, curFKJnt)
            cmds.pointConstraint(curFKControl.ControlObject, curFKJnt)

            preParent = curFKControl.ControlObject
            curScaleYZ *= fkControlScaleYZMultiplier

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
                                transparency = fkControlTransparency
                                )
        self.FKArmControls.append(curFKControl)
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, curFKControl.ControlGroup, 'FKWristControl')

        cmds.orientConstraint(curFKControl.ControlObject, nextFKJnt)
        cmds.pointConstraint(curFKControl.ControlObject, nextFKJnt)

        # FK control delegate.
        for fkArmControl in self.FKArmControls:
            self.LimbFKControls.append(fkArmControl)

        # FK control sync target delegate.
        for ikJoint in ikJoints:
            self.LimbFKControlSyncTargets.append(ikJoint)

        # IK main control sync target delegate.
        self.LimbIKMainControlSyncTarget = self.FKArmControls[-1]

        # Create PV sync.
        self.createPVLocatorSync(armPVLocator, fkElbowJoint)

        # Create arm PV control.
        armPVControl = SERigControl.RigDiamondControl(
                                 rigSide = self.RigSide,
                                 rigType = SERigEnum.eRigType.RT_ArmPV,
                                 rigFacing = SERigEnum.eRigFacing.RF_Y,
                                 prefix = self.Prefix + '_PV', 
                                 scale = rigScale * 15, 
                                 translateTo = armPVLocator,
                                 parent = self.IKControlGroup, 
                                 lockChannels = ['s', 'r', 'v'],
                                 flipScaleX = flipScaleX
                                 )
        self.ArmPVControl = armPVControl
        self.LimbPVControl = armPVControl
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.ArmPVControl.ControlGroup, 'ArmPVControl')
        
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

            # Attach FK arm control 0 to the clavicle.
            fkArmAttachPoint = SEJointHelper.getFirstParentJoint(armJoints[0])
            if fkArmAttachPoint and len(self.FKArmControls) > 0:
                locatorShoulderLocal = cmds.spaceLocator(n = 'locator_' + self.Prefix + '_ShoulderLocal')[0]
                cmds.delete(cmds.parentConstraint(armJoints[0], locatorShoulderLocal))
                cmds.parent(locatorShoulderLocal, self.RigPartsGrp)
                cmds.parentConstraint(fkArmAttachPoint, locatorShoulderLocal, mo = 1)
                cmds.hide(locatorShoulderLocal)

                locatorShoulderWorld = cmds.spaceLocator(n = 'locator_' + self.Prefix + '_ShoulderWorld')[0]
                cmds.delete(cmds.parentConstraint(armJoints[0], locatorShoulderWorld))
                cmds.parent(locatorShoulderWorld, self.RigPartsGrp)
                cmds.hide(locatorShoulderWorld)

                # FK arm control 0 follows the position of locatorShoulderLocal.
                cmds.pointConstraint(locatorShoulderLocal, self.FKArmControls[0].ControlGroup, mo = 0)

                blender = cmds.createNode("blendColors")
                cmds.connectAttr(locatorShoulderLocal + '.r', blender + '.color2', f = 1)
                cmds.connectAttr(locatorShoulderWorld + '.r', blender + '.color1', f = 1)
                cmds.connectAttr(blender + '.output', self.FKArmControls[0].ControlGroup + '.r', f = 1)

                blenderControlAttr = self.BaseRig.getArmFKLocalToWorldSwitch(self.RigSide)
                if blenderControlAttr:
                    cmds.connectAttr(blenderControlAttr, blender + '.blender')
                else:
                    cmds.error('Blender Control Attribute not found.')

        # Create IK/FK control group auto hide expression.

        mainCtrlAutoHideAt = ''
        mainCtrlIKFKSwitchAt = ''
        if self.RigSide == SERigEnum.eRigSide.RS_Left:
            mainCtrlAutoHideAt = SERigNaming.sLeftArmIKFKAutoHide
            mainCtrlIKFKSwitchAt = SERigNaming.sLeftArmIKFKSwitch
        else:
            mainCtrlAutoHideAt = SERigNaming.sRightArmIKFKAutoHide
            mainCtrlIKFKSwitchAt = SERigNaming.sRightArmIKFKSwitch

        mainControl = SERigNaming.sMainControlPrefix + SERigNaming.sControl
        ikfkAutoHideEN = SERigNaming.sExpressionPrefix + self.Prefix + 'IKFKAutoHide'
        ikfkAutoHideES = 'if( ' + mainControl + '.' + mainCtrlAutoHideAt + ' )'
        ikfkAutoHideES += '\n{\n'
        ikfkAutoHideES += '\t' + self.FKArmControls[0].ControlGroup + '.visibility = 1 - int(' + mainControl + '.' + mainCtrlIKFKSwitchAt + ');'
        ikfkAutoHideES += '\n'
        ikfkAutoHideES += '\t' + self.IKControlGroup + '.visibility = int(' + mainControl + '.' + mainCtrlIKFKSwitchAt + ');'
        ikfkAutoHideES += '\n}\nelse\n{\n'
        ikfkAutoHideES += '\t' + self.FKArmControls[0].ControlGroup + '.visibility = 1;'
        ikfkAutoHideES += '\n'
        ikfkAutoHideES += '\t' + self.IKControlGroup + '.visibility = 1;'
        ikfkAutoHideES += '\n}'

        cmds.expression(n = ikfkAutoHideEN, s = ikfkAutoHideES, ae = 1)

        # Create delegate message attributes on top group.
        self.createDelegateAttributes()


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
                 rigType = SERigEnum.eRigType.RT_HandComponent
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

        fkFingerTypes = [SERigEnum.eRigType.RT_ThumbFK, SERigEnum.eRigType.RT_IndexFK, SERigEnum.eRigType.RT_MiddleFK, 
                         SERigEnum.eRigType.RT_RingFK, SERigEnum.eRigType.RT_PinkyFK]
        curFingerTypeIndex = 0
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
                                        rigType = fkFingerTypes[curFingerTypeIndex],
                                        rigControlIndex = i,
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
                curAttrPrefix = finger[:-1]
                SERigObjectTypeHelper.linkRigObjects(self.TopGrp, curFKControl.ControlGroup, curAttrPrefix + 'FKControl' + str(i))

                cmds.orientConstraint(curFKControl.ControlObject, curFKJnt)
                cmds.pointConstraint(curFKControl.ControlObject, curFKJnt)

                preParent = curFKControl.ControlObject

            self.FKFingerControls.append(curFKFingerControls)

            curFingerTypeIndex += 1