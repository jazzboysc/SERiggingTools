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
def getAuBlinkLAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_Blink_L_Attr

    return res
#-----------------------------------------------------------------------------
def getAuBlinkRAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_Blink_R_Attr

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
def getAu02LAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_02_L_Attr

    return res
#-----------------------------------------------------------------------------
def getAu02RAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_02_R_Attr

    return res
#-----------------------------------------------------------------------------
def getAu05LAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_05_L_Attr

    return res
#-----------------------------------------------------------------------------
def getAu05RAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_05_R_Attr

    return res
#-----------------------------------------------------------------------------
def getAu06LAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_06_L_Attr

    return res
#-----------------------------------------------------------------------------
def getAu06RAttrName(bufferObject):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.sAU_06_R_Attr

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
            cmds.hide(ikChinJoint01)

            cmds.select(cl = 1)
            ikChinJoint03 = cmds.joint(n = SERigNaming.sIKPrefix + 'Chin_3')
            cmds.delete(cmds.pointConstraint(throatJoint, ikChinJoint03, mo = 0))
            cmds.setAttr(ikChinJoint03 + '.radius', 0.5)

            cmds.delete(cmds.aimConstraint(ikChinJoint03, ikChinJoint01, offset = [0, 0, 0], w = 1, aim = [1, 0, 0], u = [0, 1, 0], 
                                            worldUpType = 'scene'))

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

            locatorChinIkPV = cmds.spaceLocator(n = 'locator_Chin_IK_PV')[0]
            cmds.delete(cmds.parentConstraint(ikChinJoint01, locatorChinIkPV, mo = 0))
            cmds.parent(locatorChinIkPV, ikChinJoint01)
            cmds.move(0, -5.0, 0.0, locatorChinIkPV, r = 1, os = 1)
            cmds.parent(locatorChinIkPV, self.RigPartsGrp)
            cmds.parentConstraint(jawEndJoint, locatorChinIkPV, mo = 1)
            cmds.hide(locatorChinIkPV)

            throatIk_PCST_grp = cmds.group(n = 'ThroatIk_PCST_Grp', em = 1, p = self.RigPartsGrp)
            cmds.parentConstraint(throatJoint, throatIk_PCST_grp)
            throatIk_OffsetGrp = cmds.group(n = 'ThroatIk_OffsetGrp', em = 1, p = throatIk_PCST_grp)

            chinBulgeIK = cmds.ikHandle(n = self.Prefix + 'ChinBulge' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', 
                                        sj = ikChinJoint01, ee = ikChinJoint03)[0]
            cmds.poleVectorConstraint(locatorChinIkPV, chinBulgeIK)
            #SEJointHelper.adjustIKTwist(chinBulgeIK, ikChinJoint01)
            cmds.hide(chinBulgeIK)

            cmds.parentConstraint(jawEndJoint, ikChinJoint01, mo = 1)
            cmds.parent(chinBulgeIK, throatIk_OffsetGrp)


    def _createDataBuffer(self):
        dataBufferGroup = cmds.group(n = self.Prefix + '_DataBufferGrp', em = 1, p = self.RigPartsGrp)
        self.DataBuffer = dataBufferGroup

        singleAttributeLockList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']
        for attr in singleAttributeLockList:
            cmds.setAttr(self.DataBuffer + '.' + attr, l = 1, k = 0, cb = 0)

        auAttrList = [SERigNaming.sAU_01_L_Attr,
                      SERigNaming.sAU_01_R_Attr,
                      SERigNaming.sAU_02_L_Attr,
                      SERigNaming.sAU_02_R_Attr,
                      SERigNaming.sAU_05_L_Attr,
                      SERigNaming.sAU_05_R_Attr,
                      SERigNaming.sAU_06_L_Attr,
                      SERigNaming.sAU_06_R_Attr,
                      SERigNaming.sAU_Blink_L_Attr,
                      SERigNaming.sAU_Blink_R_Attr,
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
            createChinBulgeIKSystem = True,
            headAimIkControl = None
            ):
        print('Building facial system...')

        if not headAimIkControl and not cmds.objExists(headAimIkControl.ControlGroup):
            cmds.warning('Failed building facial system, head aim IK control does not exist.')
            return

        # Get input facial joints.
        jawJoint = SEJointHelper.getFacialJawJoint(facialJoints)
        jawOffsetJoint = SEJointHelper.getFacialJawOffsetJoint(facialJoints)
        lowerLipBeginJoint = SEJointHelper.getFacialLowerLipBeginJoint(facialJoints)
        lowerLipEndJoint   = SEJointHelper.getFacialLowerLipEndJoint(facialJoints)
        upperLipBeginJoint = SEJointHelper.getFacialUpperLipBeginJoint(facialJoints)
        upperLipEndJoint   = SEJointHelper.getFacialUpperLipEndJoint(facialJoints)
        leftEyeJoint = SEJointHelper.getFacialLeftEyeJoint(facialJoints)
        leftEyelidUpperJoint = SEJointHelper.getFacialLeftEyelidUpperJoint(facialJoints)
        leftEyelidLowerJoint = SEJointHelper.getFacialLeftEyelidLowerJoint(facialJoints)
        rightEyeJoint = SEJointHelper.getFacialRightEyeJoint(facialJoints)
        rightEyelidUpperJoint = SEJointHelper.getFacialRightEyelidUpperJoint(facialJoints)
        rightEyelidLowerJoint = SEJointHelper.getFacialRightEyelidLowerJoint(facialJoints)

        checkList = [jawJoint, jawOffsetJoint, lowerLipBeginJoint, lowerLipEndJoint, upperLipBeginJoint, upperLipEndJoint,
                     leftEyeJoint, leftEyelidUpperJoint, leftEyelidLowerJoint, rightEyeJoint, rightEyelidUpperJoint, rightEyelidLowerJoint]
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
                                prefix = SERigNaming.sFKPrefix + 'OnFace_JawPos', 
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
                                prefix = SERigNaming.sFKPrefix + 'OnFace_JawMidPos', 
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
                                prefix = SERigNaming.sIKPrefix + 'OnFace_Jaw', 
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
                                prefix = SERigNaming.sFKPrefix + 'OnFace_LipClose', 
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

        # Create IK eye joints.
        cmds.select(cl = 1)
        leftEyeIkJoint = cmds.joint(n = SERigNaming.sIKPrefix + 'L_Eye')
        cmds.delete(cmds.pointConstraint(leftEyeJoint, leftEyeIkJoint, mo = 0))
        cmds.parent(leftEyeIkJoint, self.IKJointsGroup)
        cmds.setAttr(leftEyeIkJoint + '.rotateY', -90.0)
        cmds.makeIdentity(leftEyeIkJoint, apply = True)
        cmds.setAttr(leftEyeIkJoint + '.radius', 0.5)
        cmds.parentConstraint(facialAttachPoint, leftEyeIkJoint, mo = 1)
        cmds.hide(leftEyeIkJoint)

        cmds.select(cl = 1)
        leftEyeEndIkJoint = cmds.joint(n = SERigNaming.sIKPrefix + 'L_EyeEnd')
        cmds.delete(cmds.parentConstraint(leftEyeIkJoint, leftEyeEndIkJoint, mo = 0))
        cmds.parent(leftEyeEndIkJoint, leftEyeIkJoint)
        cmds.setAttr(leftEyeEndIkJoint + '.translateX', 2.0)
        cmds.makeIdentity(leftEyeEndIkJoint, apply = True)
        cmds.setAttr(leftEyeEndIkJoint + '.radius', 0.5)

        cmds.select(cl = 1)
        rightEyeIkJoint = cmds.joint(n = SERigNaming.sIKPrefix + 'R_Eye')
        cmds.delete(cmds.pointConstraint(rightEyeJoint, rightEyeIkJoint, mo = 0))
        cmds.parent(rightEyeIkJoint, self.IKJointsGroup)
        cmds.setAttr(rightEyeIkJoint + '.rotateX', 180.0)
        cmds.setAttr(rightEyeIkJoint + '.rotateY', 90.0)
        cmds.makeIdentity(rightEyeIkJoint, apply = True)
        cmds.setAttr(rightEyeIkJoint + '.radius', 0.5)
        cmds.parentConstraint(facialAttachPoint, rightEyeIkJoint, mo = 1)
        cmds.hide(rightEyeIkJoint)

        cmds.select(cl = 1)
        rightEyeEndIkJoint = cmds.joint(n = SERigNaming.sIKPrefix + 'R_EyeEnd')
        cmds.delete(cmds.parentConstraint(rightEyeIkJoint, rightEyeEndIkJoint, mo = 0))
        cmds.parent(rightEyeEndIkJoint, rightEyeIkJoint)
        cmds.setAttr(rightEyeEndIkJoint + '.translateX', -2.0)
        cmds.makeIdentity(rightEyeEndIkJoint, apply = True)
        cmds.setAttr(rightEyeEndIkJoint + '.radius', 0.5)

        # Create eye base locators.
        locatorLeftEyeBase = cmds.spaceLocator(n = 'locator_L_EyeBase')[0]
        cmds.delete(cmds.parentConstraint(leftEyeIkJoint, locatorLeftEyeBase, mo = 0))
        cmds.parent(locatorLeftEyeBase, self.RigPartsGrp)
        cmds.parentConstraint(facialAttachPoint, locatorLeftEyeBase, mo = 1)
        cmds.hide(locatorLeftEyeBase)

        locatorRightEyeBase = cmds.spaceLocator(n = 'locator_R_EyeBase')[0]
        cmds.delete(cmds.parentConstraint(rightEyeIkJoint, locatorRightEyeBase, mo = 0))
        cmds.parent(locatorRightEyeBase, self.RigPartsGrp)
        cmds.parentConstraint(facialAttachPoint, locatorRightEyeBase, mo = 1)
        cmds.hide(locatorRightEyeBase)

        # Create IK eye PVs.
        locatorLeftEyeIkPV = cmds.spaceLocator(n = 'locator_IK_L_EyePV')[0]
        cmds.delete(cmds.parentConstraint(leftEyeIkJoint, locatorLeftEyeIkPV, mo = 0))
        cmds.parent(locatorLeftEyeIkPV, leftEyeIkJoint)
        cmds.move(0.0, -2.0, 0.0, locatorLeftEyeIkPV, r = 1, os = 1)
        cmds.parent(locatorLeftEyeIkPV, self.RigPartsGrp)
        cmds.parentConstraint(facialAttachPoint, locatorLeftEyeIkPV, mo = 1)
        cmds.hide(locatorLeftEyeIkPV)

        locatorRightEyeIkPV = cmds.spaceLocator(n = 'locator_IK_R_EyePV')[0]
        cmds.delete(cmds.parentConstraint(rightEyeIkJoint, locatorRightEyeIkPV, mo = 0))
        cmds.parent(locatorRightEyeIkPV, rightEyeIkJoint)
        cmds.move(0.0, 2.0, 0.0, locatorRightEyeIkPV, r = 1, os = 1)
        cmds.parent(locatorRightEyeIkPV, self.RigPartsGrp)
        cmds.parentConstraint(facialAttachPoint, locatorRightEyeIkPV, mo = 1)
        cmds.hide(locatorRightEyeIkPV)

        # Create eye IK handles.
        leftEyeIkHandle = cmds.ikHandle(n = self.Prefix + '_L_Eye' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', 
                                        sj = leftEyeIkJoint, ee = leftEyeEndIkJoint)[0]
        cmds.poleVectorConstraint(locatorLeftEyeIkPV, leftEyeIkHandle)
        cmds.hide(leftEyeIkHandle)
        cmds.parent(leftEyeIkHandle, self.RigPartsGrp)
        SEJointHelper.adjustIKTwist(leftEyeIkHandle, leftEyeIkJoint)

        rightEyeIkHandle = cmds.ikHandle(n = self.Prefix + '_R_Eye' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', 
                                        sj = rightEyeIkJoint, ee = rightEyeEndIkJoint)[0]
        cmds.poleVectorConstraint(locatorRightEyeIkPV, rightEyeIkHandle)
        cmds.hide(rightEyeIkHandle)
        cmds.parent(rightEyeIkHandle, self.RigPartsGrp)
        SEJointHelper.adjustIKTwist(rightEyeIkHandle, rightEyeIkJoint)

        # Create IK eye base control.
        self.EyesAimIKControl = SERigControl.RigFlatHexagonControl(
                                rigSide = self.RigSide,
                                rigType = SERigEnum.eRigType.RT_OnFaceIK,
                                rigControlIndex = SERigEnum.eRigFacialControlID.RFCID_EyesAimIK,
                                rigFacing = SERigEnum.eRigFacing.RF_Z,
                                prefix = self.Prefix + '_IK_EyesAim', 
                                scale = rigScale * 0.8, 
                                translateTo = headAimIkControl.ControlObject,
                                rotateTo = headAimIkControl.ControlObject, 
                                parent = self.OnFaceIkControlGroup, 
                                lockChannels = ['s', 'r', 'tz', 'v'],
                                preRotateY = 90
                                )
        cmds.parentConstraint(headAimIkControl.ControlObject, self.EyesAimIKControl.ControlGroup, mo = 0)
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.EyesAimIKControl.ControlGroup, 'EyesAimIKControl', 'ControlOwner')

        # Create IK eye controls.
        leftEyeIkControl = SERigControl.RigCircleControl(
                            rigSide = SERigEnum.eRigSide.RS_Left,
                            rigType = SERigEnum.eRigType.RT_OnFaceIK,
                            rigControlIndex = SERigEnum.eRigFacialControlID.RFCID_LeftEyeAimIK,
                            prefix = SERigNaming.sIKPrefix + 'OnFace_L_Eye', 
                            scale = rigScale * 0.8, 
                            translateTo = leftEyeEndIkJoint,
                            rotateTo = leftEyeEndIkJoint,
                            parent = leftEyeEndIkJoint, 
                            lockChannels = ['tx', 'r', 's', 'v'])
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, leftEyeIkControl.ControlGroup, 'OnFaceLeftEyeIkControl', 'ControlOwner')

        # Then parent the control to our component and position it to align with the IK eye base control.
        cmds.parent(leftEyeIkControl.ControlGroup, self.OnFaceIkControlGroup)
        cmds.delete(cmds.pointConstraint(self.EyesAimIKControl.ControlObject, leftEyeIkControl.ControlGroup, skip = ['y', 'z'], mo = 0))
        cmds.pointConstraint(self.EyesAimIKControl.ControlObject, leftEyeIkControl.ControlGroup, mo = 1)
        cmds.pointConstraint(leftEyeIkControl.ControlObject, leftEyeIkHandle, mo = 0)

        rightEyeIkControl = SERigControl.RigCircleControl(
                            rigSide = SERigEnum.eRigSide.RS_Right,
                            rigType = SERigEnum.eRigType.RT_OnFaceIK,
                            rigControlIndex = SERigEnum.eRigFacialControlID.RFCID_RightEyeAimIK,
                            prefix = SERigNaming.sIKPrefix + 'OnFace_R_Eye', 
                            scale = rigScale * 0.8, 
                            translateTo = rightEyeEndIkJoint,
                            rotateTo = rightEyeEndIkJoint,
                            parent = rightEyeEndIkJoint, 
                            lockChannels = ['tx', 'r', 's', 'v'])
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, rightEyeIkControl.ControlGroup, 'OnFaceRightEyeIkControl', 'ControlOwner')

        # Then parent the control to our component and position it to align with the IK eye base control.
        cmds.parent(rightEyeIkControl.ControlGroup, self.OnFaceIkControlGroup)
        cmds.delete(cmds.pointConstraint(self.EyesAimIKControl.ControlObject, rightEyeIkControl.ControlGroup, skip = ['y', 'z'], mo = 0))
        cmds.pointConstraint(self.EyesAimIKControl.ControlObject, rightEyeIkControl.ControlGroup, mo = 1)
        cmds.pointConstraint(rightEyeIkControl.ControlObject, rightEyeIkHandle, mo = 0)

        # Create eye base joint motion logic.
        oc = cmds.orientConstraint(locatorLeftEyeBase, leftEyeIkJoint, leftEyeJoint, mo = 1)[0]
        cmds.setAttr(oc + '.interpType', 2)
        cmds.setAttr(oc + '.' + locatorLeftEyeBase + 'W0', 0.6)
        cmds.setAttr(oc + '.' + leftEyeIkJoint + 'W1', 0.4)

        oc = cmds.orientConstraint(locatorRightEyeBase, rightEyeIkJoint, rightEyeJoint, mo = 1)[0]
        cmds.setAttr(oc + '.interpType', 2)
        cmds.setAttr(oc + '.' + locatorRightEyeBase + 'W0', 0.6)
        cmds.setAttr(oc + '.' + rightEyeIkJoint + 'W1', 0.4)

        # Create eye lid motion logic.
        if self.DataBuffer:
            # AU05.
            au05LAttr = getAu05LAttrName(self.DataBuffer)
            animCurveAu05L = cmds.createNode('animCurveUA')
            cmds.connectAttr(au05LAttr, animCurveAu05L + '.input')

            au05RAttr = getAu05RAttrName(self.DataBuffer)
            animCurveAu05R = cmds.createNode('animCurveUA')
            cmds.connectAttr(au05RAttr, animCurveAu05R + '.input')

            # AU06.
            au06LAttr = getAu06LAttrName(self.DataBuffer)
            animCurveAu06L = cmds.createNode('animCurveUA')
            cmds.connectAttr(au06LAttr, animCurveAu06L + '.input')

            au06RAttr = getAu06RAttrName(self.DataBuffer)
            animCurveAu06R = cmds.createNode('animCurveUA')
            cmds.connectAttr(au06RAttr, animCurveAu06R + '.input')

            # Blink.
            blinkLAttr = getAuBlinkLAttrName(self.DataBuffer)
            animCurveAuBlinkL = cmds.createNode('animCurveUA')
            cmds.connectAttr(blinkLAttr, animCurveAuBlinkL + '.input')

            blinkRAttr = getAuBlinkRAttrName(self.DataBuffer)
            animCurveAuBlinkR = cmds.createNode('animCurveUA')
            cmds.connectAttr(blinkRAttr, animCurveAuBlinkR + '.input')

            # Eye base.
            animCurveEyeBaseL = cmds.createNode('animCurveUA')
            cmds.connectAttr(leftEyeJoint + '.rotateZ', animCurveEyeBaseL + '.input', f = 1)

            animCurveEyeBaseR = cmds.createNode('animCurveUA')
            cmds.connectAttr(rightEyeJoint + '.rotateZ', animCurveEyeBaseR + '.input', f = 1)

            # Blend all drivers together using blend weighted nodes for upper eyelid joints.
            leftUpperEyelidBlend = cmds.createNode('blendWeighted')
            cmds.connectAttr(animCurveAu05L + '.output', leftUpperEyelidBlend + '.input[0]', f = 1)
            cmds.connectAttr(animCurveAu06L + '.output', leftUpperEyelidBlend + '.input[1]', f = 1)
            cmds.connectAttr(animCurveAuBlinkL + '.output', leftUpperEyelidBlend + '.input[2]', f = 1)
            cmds.connectAttr(animCurveEyeBaseL + '.output', leftUpperEyelidBlend + '.input[3]', f = 1)

            rightUpperEyelidBlend = cmds.createNode('blendWeighted')
            cmds.connectAttr(animCurveAu05R + '.output', rightUpperEyelidBlend + '.input[0]', f = 1)
            cmds.connectAttr(animCurveAu06R + '.output', rightUpperEyelidBlend + '.input[1]', f = 1)
            cmds.connectAttr(animCurveAuBlinkR + '.output', rightUpperEyelidBlend + '.input[2]', f = 1)
            cmds.connectAttr(animCurveEyeBaseR + '.output', rightUpperEyelidBlend + '.input[3]', f = 1)

            cmds.connectAttr(leftUpperEyelidBlend + '.output', leftEyelidUpperJoint + '.rotateZ', f = 1)
            cmds.connectAttr(rightUpperEyelidBlend + '.output', rightEyelidUpperJoint + '.rotateZ', f = 1)