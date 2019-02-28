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
def getAuLipCloseAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_LipClose_Attr

    return res
#-----------------------------------------------------------------------------
def getAu01LAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_01_L_Attr

    return res
#-----------------------------------------------------------------------------
def getAu01RAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_01_R_Attr

    return res
#-----------------------------------------------------------------------------

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
                 rigType = SERigEnum.eRigType.RT_FacialComponent
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.EyesAimIKControl = None
        self.IKJointsGroup = None
        self.OnFaceIkControlGroup = None
        self.OnFaceFkControlGroup = None
        self.DataBuffer = None

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


    def _createDataBuffer(self):
        dataBufferGroup = cmds.group(n = self.Prefix + '_DataBufferGrp', em = 1, p = self.RigPartsGrp)
        self.DataBuffer = dataBufferGroup

        auAttrList = [SERigNaming.sAU_01_L_Attr,
                      SERigNaming.sAU_01_R_Attr,
                      SERigNaming.sAU_02_L_Attr,
                      SERigNaming.sAU_02_R_Attr,
                      SERigNaming.sAU_LipClose_Attr]

        for attr in auAttrList:
            cmds.addAttr(dataBufferGroup, ln = attr, at = 'float', k = 1, dv = 0.0, hasMinValue = True, min = 0.0, hasMaxValue = True, max = 1.0)
            cmds.setAttr(dataBufferGroup + '.' + attr, cb = 1)


    def build(
            self,
            facialJoints = [],
            jawEndJoint = '',
            throatJoint = '',
            rootJoint = '',
            facialAttachPoint = '',
            rigScale = 1.0,
            createChinBulgeIKSystem = True
            ):
        print('Building facial system...')

        jawJoint = SEJointHelper.getFacialJawJoint(facialJoints)
        jawOffsetJoint = SEJointHelper.getFacialJawOffsetJoint(facialJoints)
        lowerLipBeginJoint = SEJointHelper.getFacialLowerLipBeginJoint(facialJoints)
        lowerLipEndJoint   = SEJointHelper.getFacialLowerLipEndJoint(facialJoints)
        upperLipBeginJoint = SEJointHelper.getFacialUpperLipBeginJoint(facialJoints)
        upperLipEndJoint   = SEJointHelper.getFacialUpperLipEndJoint(facialJoints)

        checkList = [jawJoint, jawOffsetJoint, lowerLipBeginJoint, lowerLipEndJoint, upperLipBeginJoint, upperLipEndJoint]
        for obj in checkList:
            if not cmds.objExists(obj):
                cmds.warning('Failed building facial system, cannot find:' + obj)
                return

        # Create lower and upper lips' blend joints.
        cmds.select(cl = 1)
        lowerLipBlendJoint = cmds.joint(n = lowerLipEndJoint + 'Blend')
        cmds.delete(cmds.parentConstraint(lowerLipEndJoint, lowerLipBlendJoint, mo = 0))
        cmds.parent(lowerLipBlendJoint, lowerLipEndJoint)
        cmds.makeIdentity(lowerLipBlendJoint, apply = True)
        cmds.setAttr(lowerLipBlendJoint + '.radius', 0.5)

        cmds.select(cl = 1)
        upperLipBlendJoint = cmds.joint(n = upperLipEndJoint + 'Blend')
        cmds.delete(cmds.parentConstraint(upperLipEndJoint, upperLipBlendJoint, mo = 0))
        cmds.parent(upperLipBlendJoint, upperLipEndJoint)
        cmds.makeIdentity(upperLipBlendJoint, apply = True)
        cmds.setAttr(upperLipBlendJoint + '.radius', 0.5)

        # Lock jaw offset joint's motion.
        lockAttrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
        for attr in lockAttrList:
            cmds.setAttr(jawOffsetJoint + '.' + attr, l = True)

        # Create data buffer group.
        self._createDataBuffer()

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

        # Create jaw position joint.
        cmds.select(cl = 1)
        jawPosJoint = cmds.joint(n = 'C_JawPos')
        cmds.delete(cmds.parentConstraint(jawJoint, jawPosJoint, mo = 0))
        cmds.parent(jawPosJoint, facialAttachPoint)
        cmds.makeIdentity(jawPosJoint, apply = True)
        cmds.parent(jawJoint, jawPosJoint)
        cmds.parent(lowerLipBeginJoint, jawPosJoint)
        cmds.setAttr(jawPosJoint + '.radius', 0.5)

        # Create jaw mid-position joint.
        cmds.select(cl = 1)
        jawMidPosJoint = cmds.joint(n = 'C_JawMidPos')
        cmds.delete(cmds.parentConstraint(jawJoint, jawMidPosJoint, mo = 0))
        cmds.parent(jawMidPosJoint, facialAttachPoint)
        cmds.makeIdentity(jawMidPosJoint, apply = True)
        cmds.setAttr(jawMidPosJoint + '.radius', 0.5)

        # Create mid lower lip joints.
        cmds.select(cl = 1)
        midLowerLipBeginJoint = cmds.joint(n = 'C_MidLowerLipBegin')
        cmds.delete(cmds.parentConstraint(lowerLipBeginJoint, midLowerLipBeginJoint, mo = 0))
        cmds.parent(midLowerLipBeginJoint, jawMidPosJoint)
        cmds.makeIdentity(midLowerLipBeginJoint, apply = True)
        cmds.setAttr(midLowerLipBeginJoint + '.radius', 0.5)

        cmds.select(cl = 1)
        midLowerLipEndJoint = cmds.joint(n = 'C_MidLowerLipEnd')
        cmds.delete(cmds.parentConstraint(lowerLipEndJoint, midLowerLipEndJoint, mo = 0))
        cmds.parent(midLowerLipEndJoint, midLowerLipBeginJoint)
        cmds.makeIdentity(midLowerLipEndJoint, apply = True)
        cmds.setAttr(midLowerLipEndJoint + '.radius', 0.5)

        # Create mid upper lip joints.
        cmds.select(cl = 1)
        midUpperLipBeginJoint = cmds.joint(n = 'C_MidUpperLipBegin')
        cmds.delete(cmds.parentConstraint(upperLipBeginJoint, midUpperLipBeginJoint, mo = 0))
        cmds.parent(midUpperLipBeginJoint, jawMidPosJoint)
        cmds.makeIdentity(midUpperLipBeginJoint, apply = True)
        cmds.setAttr(midUpperLipBeginJoint + '.radius', 0.5)

        cmds.select(cl = 1)
        midUpperLipEndJoint = cmds.joint(n = 'C_MidUpperLipEnd')
        cmds.delete(cmds.parentConstraint(upperLipEndJoint, midUpperLipEndJoint, mo = 0))
        cmds.parent(midUpperLipEndJoint, midUpperLipBeginJoint)
        cmds.makeIdentity(midUpperLipEndJoint, apply = True)
        cmds.setAttr(midUpperLipEndJoint + '.radius', 0.5)

        # Create jaw position control.
        jawPosControl = SERigControl.RigCubeControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_OnFaceFK,
                                rigControlIndex = SERigEnum.eRigFacialControlID.RFCID_JawPos,
                                prefix = SERigNaming.sFKPrefix + 'OnFace_JawPosFK', 
                                translateTo = jawPosJoint,
                                rotateTo = jawPosJoint,
                                scale = rigScale,
                                parent = onFaceFkCtrlGrp,
                                lockChannels = ['r', 's', 'v'],
                                cubeScaleX = 4.0,
                                cubeScaleY = 2.0,
                                cubeScaleZ = 4.0,
                                transparency = 0.5,
                                overrideControlColor = True,
                                controlColor = (0.9, 0.4, 0.75)
                                )
        cmds.pointConstraint(jawPosControl.ControlObject, jawPosJoint, mo = 0)
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, jawPosControl.ControlGroup, 'JawPositionControl', 'ControlOwner')

        # Create jaw mid position control.
        jawMidPosControl = SERigControl.RigCubeControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_OnFaceFK,
                                rigControlIndex = SERigEnum.eRigFacialControlID.RFCID_JawMidPos,
                                prefix = SERigNaming.sFKPrefix + 'OnFace_JawMidPosFK', 
                                translateTo = jawMidPosJoint,
                                rotateTo = jawMidPosJoint,
                                scale = rigScale,
                                parent = onFaceFkCtrlGrp,
                                lockChannels = ['r', 's', 'v'],
                                cubeScaleX = 4.0,
                                cubeScaleY = 4.0,
                                cubeScaleZ = 2.0,
                                transparency = 0.5,
                                overrideControlColor = True,
                                controlColor = (0.4, 0.9, 0.75)
                                )
        cmds.pointConstraint(jawMidPosControl.ControlObject, jawMidPosJoint, mo = 0)
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, jawMidPosControl.ControlGroup, 'JawMidPositionControl', 'ControlOwner')

        # Possibly create chin bulge ik joints.
        if createChinBulgeIKSystem:
            self._createChinBulgeIKSystem(jawEndJoint, throatJoint)

        # Create on-face jaw IK control.
        onFaceIKJawControlTransGrp = cmds.group(n = self.Prefix + '_OnFaceIKJaw_TransGrp', em = 1, p = self.OnFaceIkControlGroup)
        cmds.delete(cmds.parentConstraint(jawJoint, onFaceIKJawControlTransGrp, mo = 0))
        onFaceIKJawControlTransOffsetGrp = cmds.group(n = self.Prefix + '_OnFaceIKJaw_TransOffsetGrp', em = 1, p = onFaceIKJawControlTransGrp)
        cmds.delete(cmds.parentConstraint(jawJoint, onFaceIKJawControlTransOffsetGrp, mo = 0))

        onFaceIKJawControl = SERigControl.RigCubeControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_OnFaceIK,
                                rigControlIndex = SERigEnum.eRigFacialControlID.RFCID_JawIK,
                                prefix = SERigNaming.sIKPrefix + 'OnFace_JawIK', 
                                translateTo = jawEndJoint,
                                rotateTo = jawEndJoint,
                                scale = rigScale,
                                parent = onFaceIKJawControlTransOffsetGrp,
                                lockChannels = ['r', 's', 'v'],
                                cubeScaleX = 1.0,
                                cubeScaleY = 2.0,
                                cubeScaleZ = 2.0,
                                transparency = 0.2,
                                overrideControlColor = True,
                                controlColor = (0.9, 0.4, 0.75)
                                )
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, onFaceIKJawControl.ControlGroup, 'OnFaceIkJawControl', 'ControlOwner')

        offsetGrpName = onFaceIKJawControl.Prefix + SERigNaming.sOffsetGroup
        resOffsetGrp = onFaceIKJawControl.InsertNewGroup(offsetGrpName)
        driverGrpName = onFaceIKJawControl.Prefix + SERigNaming.sDriverGroup
        resDriverGrp = onFaceIKJawControl.InsertNewGroup(driverGrpName)
        cmds.setAttr(resOffsetGrp + '.translateX', 2.0)
        cmds.setAttr(resOffsetGrp + '.rotateZ', 20.0)
        cmds.addAttr(onFaceIKJawControl.ControlObject, ln = SERigNaming.sJawForwardAttr, at = 'float', k = 0, dv = 0.0, 
                     hasMinValue = True, min = 0.0, hasMaxValue = True, max = 1.0)
        cmds.setAttr(onFaceIKJawControl.ControlObject + '.' + SERigNaming.sJawForwardAttr, cb = 0)
        cmds.transformLimits(onFaceIKJawControl.ControlObject, tx = (0, 1), etx = (True, True), ty = (-4.5, 0.25), ety = (True, True), tz = (-1, 1), etz = (True, True))
        cmds.addAttr(onFaceIKJawControl.ControlObject, ln = SERigNaming.sJawForwardFactorAttr, at = 'float', k = 1, dv = 0.03, 
                     hasMinValue = True, min = 0.0, hasMaxValue = True, max = 0.1)

        mulNode = cmds.createNode('multiplyDivide')
        cmds.setAttr(mulNode + '.operation', 1)
        cmds.setAttr(mulNode + '.input1X', 10.0)
        cmds.connectAttr(onFaceIKJawControl.ControlObject + '.tx', mulNode + '.input2X')
        cmds.connectAttr(mulNode + '.outputX', onFaceIKJawControl.ControlObject + '.' + SERigNaming.sJawForwardAttr)

        mulNode = cmds.createNode('multiplyDivide')
        cmds.setAttr(mulNode + '.operation', 1)
        cmds.connectAttr(onFaceIKJawControl.ControlObject + '.' + SERigNaming.sJawForwardFactorAttr, mulNode + '.input1X')
        cmds.connectAttr(onFaceIKJawControl.ControlObject + '.' + SERigNaming.sJawForwardAttr, mulNode + '.input2X')
        cmds.connectAttr(mulNode + '.outputX', onFaceIKJawControlTransOffsetGrp + '.tx')

        mulNode = cmds.createNode('multiplyDivide')
        cmds.setAttr(mulNode + '.operation', 1)
        cmds.connectAttr(onFaceIKJawControl.ControlObject + '.' + SERigNaming.sJawForwardFactorAttr, mulNode + '.input1X')
        cmds.connectAttr(onFaceIKJawControl.ControlObject + '.' + SERigNaming.sJawForwardAttr, mulNode + '.input2X')
        cmds.connectAttr(mulNode + '.outputX', jawPosControl.ControlObject + '.tx')

        mulNode0 = cmds.createNode('multiplyDivide')
        cmds.setAttr(mulNode0 + '.operation', 1)
        cmds.setAttr(mulNode0 + '.input1X', 0.5)
        mulNode1 = cmds.createNode('multiplyDivide')
        cmds.setAttr(mulNode1 + '.operation', 1)
        cmds.connectAttr(onFaceIKJawControl.ControlObject + '.' + SERigNaming.sJawForwardFactorAttr, mulNode1 + '.input1X')
        cmds.connectAttr(onFaceIKJawControl.ControlObject + '.' + SERigNaming.sJawForwardAttr, mulNode1 + '.input2X')
        cmds.connectAttr(mulNode1 + '.outputX', mulNode0 + '.input2X')
        cmds.connectAttr(mulNode0 + '.outputX', jawMidPosControl.ControlObject + '.tx')

        # Create jaw IK PV locator.
        jawIKPV = cmds.spaceLocator(n = 'locator_' + self.Prefix + '_JawIK_PV')[0]
        cmds.delete(cmds.parentConstraint(facialAttachPoint, jawIKPV, mo = 0))
        cmds.move(0.0, -10.0, 0.0, jawIKPV, r = 1, os = 1)
        cmds.parent(jawIKPV, self.RigPartsGrp)
        cmds.parentConstraint(facialAttachPoint, jawIKPV, mo = 1)
        cmds.hide(jawIKPV)

        # Create jaw IK offset group.
        jawIKOffsetGrp = cmds.group(n = self.Prefix + '_JawIK_OffsetGrp', em = 1, p = self.RigPartsGrp)
        cmds.delete(cmds.parentConstraint(jawEndJoint, jawIKOffsetGrp, mo = 0))
        cmds.parentConstraint(onFaceIKJawControl.ControlObject, jawIKOffsetGrp, mo = 1)

        # Create jaw IK handle.
        jawIK = cmds.ikHandle(n = self.Prefix + 'Jaw' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', sj = jawJoint, ee = jawEndJoint)[0]
        cmds.hide(jawIK)
        cmds.delete(cmds.parentConstraint(jawIKOffsetGrp, jawIK, mo = 0))
        cmds.parent(jawIK, jawIKOffsetGrp)
        cmds.poleVectorConstraint(jawIKPV, jawIK)
        SEJointHelper.adjustIKTwist(jawIK, jawJoint)

        # Rotate lower, mid lower and mid upper lips via jaw joint.
        cmds.connectAttr(jawJoint + '.rotate', lowerLipBeginJoint + '.rotate')
        unitConversionNode = cmds.createNode('unitConversion')
        cmds.setAttr(unitConversionNode + '.conversionFactor', 0.5)
        cmds.connectAttr(jawJoint + '.rotate', unitConversionNode + '.input')
        cmds.connectAttr(unitConversionNode + '.output', midLowerLipBeginJoint + '.rotate')
        cmds.connectAttr(unitConversionNode + '.output', midUpperLipBeginJoint + '.rotate')
        
        # Create blend for lower and upper lips.
        reverseNode = cmds.createNode('reverse')
        cmds.connectAttr(self.DataBuffer + '.' + SERigNaming.sAU_LipClose_Attr, reverseNode + '.inputX')

        pc = cmds.parentConstraint(upperLipEndJoint, midUpperLipEndJoint, upperLipBlendJoint)[0]
        cmds.connectAttr(self.DataBuffer + '.' + SERigNaming.sAU_LipClose_Attr, pc + '.' + midUpperLipEndJoint + 'W1')
        cmds.connectAttr(reverseNode + '.outputX', pc + '.' + upperLipEndJoint + 'W0')

        pc = cmds.parentConstraint(lowerLipEndJoint, midLowerLipEndJoint, lowerLipBlendJoint)[0]
        cmds.connectAttr(self.DataBuffer + '.' + SERigNaming.sAU_LipClose_Attr, pc + '.' + midLowerLipEndJoint + 'W1')
        cmds.connectAttr(reverseNode + '.outputX', pc + '.' + lowerLipEndJoint + 'W0')

        # Create on-face lip close control.
        onFaceLipCloseControl = SERigControl.RigCubeControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_OnFaceFK,
                                rigControlIndex = SERigEnum.eRigFacialControlID.RFCID_LipCloseFK,
                                prefix = SERigNaming.sFKPrefix + 'OnFace_LipCloseFK', 
                                translateTo = onFaceIKJawControl.ControlObject,
                                rotateTo = onFaceIKJawControl.ControlObject,
                                scale = rigScale,
                                parent = onFaceIKJawControl.ControlObject,
                                lockChannels = ['tx', 'tz', 'r', 's', 'v'],
                                cubeScaleX = 0.5,
                                cubeScaleY = 1.0,
                                cubeScaleZ = 1.0,
                                transparency = 0.2,
                                overrideControlColor = True,
                                controlColor = (0.2, 0.8, 0.4)
                                )
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, onFaceLipCloseControl.ControlGroup, 'OnFaceLipCloseControl', 'ControlOwner')
        onFaceLipCloseControlOffsetGrp = onFaceLipCloseControl.InsertNewGroup(groupName = onFaceLipCloseControl.Prefix + SERigNaming.sOffsetGroup)
        cmds.move(0.0, 2.0, 0.0, onFaceLipCloseControlOffsetGrp, r = 1, os = 1)
        cmds.transformLimits(onFaceLipCloseControl.ControlObject, ty = (0.0, 1.0), ety = (True, True))

        # For now, connect the control's ty to the data buffer attribute directly.
        dataBufferLipCloseAttr = getAuLipCloseAttrName(self.DataBuffer)
        cmds.connectAttr(onFaceLipCloseControl.ControlObject + '.ty', dataBufferLipCloseAttr)