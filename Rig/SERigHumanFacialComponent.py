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
# Rig Human Facial System Class
# Sun Che
#-----------------------------------------------------------------------------
class RigHumanFacialSystem(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Center,
                 rigType = SERigEnum.eRigType.RT_NeckComponent
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.EyesAimIKControl = None
        self.IKJointsGroup = None
        self.OnFaceIkControlGroup = None
        self.OnFaceFkControlGroup = None

    def _createChinBulgeIKSystem(self, jawEndJoint, throatJoint):
        if cmds.objExists(jawEndJoint) and cmds.objExists(throatJoint):
            cmds.select(cl = 1)
            ikChinJoint01 = cmds.joint(n = SERigNaming.sIKPrefix + 'Chin_1')
            cmds.delete(cmds.pointConstraint(jawEndJoint, ikChinJoint01, mo = 0))
            cmds.parent(ikChinJoint01, self.IKJointsGroup)
            cmds.setAttr(ikChinJoint01 + '.radius', 0.5)

            cmds.select(cl = 1)
            ikChinJoint03 = cmds.joint(n = SERigNaming.sIKPrefix + 'Chin_3')
            cmds.delete(cmds.pointConstraint(throatJoint, ikChinJoint03, mo = 0))
            cmds.setAttr(ikChinJoint03 + '.radius', 0.5)

            locatorChinIkPV = cmds.spaceLocator(n = 'locator_Chin_IK_PV')[0]
            cmds.delete(cmds.pointConstraint(ikChinJoint01, locatorChinIkPV, mo = 0))
            cmds.move(0, -5.0, 2.5, locatorChinIkPV, r = 1, os = 1)
            cmds.parent(locatorChinIkPV, self.RigPartsGrp)
            cmds.parentConstraint(jawEndJoint, locatorChinIkPV, mo = 1)
            cmds.hide(locatorChinIkPV)

            cmds.delete(cmds.aimConstraint(ikChinJoint03, ikChinJoint01, offset = [0, 0, 0], w = 1, aim = [1, 0, 0], u = [0, 1, 0], 
                                            worldUpType = 'object', worldUpObject = locatorChinIkPV))

            cmds.delete(cmds.orientConstraint(ikChinJoint01, ikChinJoint03, mo = 0))
                
            cmds.select(cl = 1)
            ikChinJoint02 = cmds.joint(n = SERigNaming.sIKPrefix + 'Chin_2')
            cmds.delete(cmds.parentConstraint(ikChinJoint01, ikChinJoint02, mo = 0))
            cmds.setAttr(ikChinJoint02 + '.radius', 0.5)

            p1 = SEMathHelper.getWorldPosition(ikChinJoint01)
            p3 = SEMathHelper.getWorldPosition(ikChinJoint03)
            halfDis = 0.5 * SEMathHelper.getDistance3(p1, p3)
            cmds.move(halfDis, 0.0, 0.0, ikChinJoint02, r = 1, os = 1)

            cmds.parent(ikChinJoint02, ikChinJoint01)
            cmds.parent(ikChinJoint03, ikChinJoint02)
            cmds.makeIdentity(ikChinJoint01, apply = True)

            throatIk_PCST_grp = cmds.group(n = 'ThroatIk_PCST_Grp', em = 1, p = self.RigPartsGrp)
            cmds.parentConstraint(throatJoint, throatIk_PCST_grp)
            throatIk_OffsetGrp = cmds.group(n = 'ThroatIk_OffsetGrp', em = 1, p = throatIk_PCST_grp)

            chinBulgeIK = cmds.ikHandle(n = self.Prefix + 'ChinBulge' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', sj = ikChinJoint01, ee = ikChinJoint03)[0]
            cmds.poleVectorConstraint(locatorChinIkPV, chinBulgeIK)
            cmds.hide(chinBulgeIK)

            cmds.parentConstraint(jawEndJoint, ikChinJoint01, mo = 1)
            cmds.parent(chinBulgeIK, throatIk_OffsetGrp)


    def build(
            self,
            facialJoints = [],  # []
            jawEndJoint = '',
            throatJoint = '',
            rootJoint = '',
            facialAttachPoint = '',
            rigScale = 1.0,
            createChinBulgeIKSystem = True
            ):
        print('Building facial system...')

        # Create IK joints group.
        ikJointsGroup = cmds.group(n = self.Prefix + '_IK_JointsGrp', em = 1, p = self.JointsGrp)
        self.IKJointsGroup = ikJointsGroup

        # Create on-face IK control group.
        onFaceIkCtrlGrp = cmds.group(n = self.Prefix + '_OnFace_IK' + SERigNaming.sControlGroup, em = 1, p = self.IKControlGroup)
        cmds.parentConstraint(facialAttachPoint, onFaceIkCtrlGrp, mo = 0)
        self.OnFaceIkControlGroup = onFaceIkCtrlGrp

        # Create on-face FK control group.
        onFaceFkCtrlGrp = cmds.group(n = self.Prefix + '_OnFace_FK' + SERigNaming.sControlGroup, em = 1, p = self.FKControlGroup)
        cmds.parentConstraint(facialAttachPoint, onFaceFkCtrlGrp, mo = 0)
        self.OnFaceFkControlGroup = onFaceFkCtrlGrp

        # Possibly create chin bulge ik joints.
        if createChinBulgeIKSystem:
            self._createChinBulgeIKSystem(jawEndJoint, throatJoint)

        # Create on-face jaw IK control.
        onFaceIKJawControl = SERigControl.RigCubeControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_OnFaceIK,
                                rigControlIndex = 0,
                                prefix = SERigNaming.sFKPrefix + 'OnFace_JawIK', 
                                translateTo = jawEndJoint,
                                rotateTo = jawEndJoint,
                                scale = rigScale,
                                parent = onFaceIkCtrlGrp,
                                lockChannels = ['r', 's', 'v'],
                                cubeScaleX = 1.0,
                                cubeScaleY = 2.0,
                                cubeScaleZ = 2.0,
                                transparency = 0.75
                                )


