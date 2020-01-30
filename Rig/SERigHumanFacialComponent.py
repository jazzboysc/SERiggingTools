import maya.cmds as cmds
import pymel.core.general

from ..Base.SERigComponent import RigComponent
from ..Base import SERigControl
from ..Base import SERigEnum
from ..Base import SERigNaming
from ..Utils import SEStringHelper
from ..Utils import SEMathHelper
from ..Utils import SEJointHelper
from ..Utils import SERigObjectTypeHelper
from ..Utils import SEConstraintHelper

facialControlsTable = {}
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_InnerBrow, SERigEnum.eRigSide.RS_Left, 0)]       = 'Brow_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_InnerBrow, SERigEnum.eRigSide.RS_Right, 0)]      = 'Brow_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_OuterBrow, SERigEnum.eRigSide.RS_Left, 0)]       = 'Brow_L_002_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_OuterBrow, SERigEnum.eRigSide.RS_Right, 0)]      = 'Brow_R_002_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_UpperLid, SERigEnum.eRigSide.RS_Left, 0)]        = 'UpperLid_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_UpperLid, SERigEnum.eRigSide.RS_Right, 0)]       = 'UpperLid_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_LowerLid, SERigEnum.eRigSide.RS_Left, 0)]        = 'LowerLid_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_LowerLid, SERigEnum.eRigSide.RS_Right, 0)]       = 'LowerLid_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_OuterEyeCorner, SERigEnum.eRigSide.RS_Left, 0)]  = 'EyeCorner_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_OuterEyeCorner, SERigEnum.eRigSide.RS_Right, 0)] = 'EyeCorner_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Nosewing, SERigEnum.eRigSide.RS_Left, 0)]        = 'Nosewing_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Nosewing, SERigEnum.eRigSide.RS_Right, 0)]       = 'Nosewing_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Muzzle, SERigEnum.eRigSide.RS_Left, 0)]          = 'Muzzle_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Muzzle, SERigEnum.eRigSide.RS_Right, 0)]         = 'Muzzle_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_UpperLip, SERigEnum.eRigSide.RS_Left, 0)]        = 'UpperLip_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_UpperLip, SERigEnum.eRigSide.RS_Center, 0)]      = 'UpperLip_C_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_UpperLip, SERigEnum.eRigSide.RS_Right, 0)]       = 'UpperLip_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_LowerLip, SERigEnum.eRigSide.RS_Left, 0)]        = 'LowerLip_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_LowerLip, SERigEnum.eRigSide.RS_Center, 0)]      = 'LowerLip_C_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_LowerLip, SERigEnum.eRigSide.RS_Right, 0)]       = 'LowerLip_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Mouth, SERigEnum.eRigSide.RS_Center, 0)]         = 'Mouth_C_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_MouthCorner, SERigEnum.eRigSide.RS_Left, 0)]     = 'MouthCorner_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_MouthCorner, SERigEnum.eRigSide.RS_Right, 0)]    = 'MouthCorner_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_MouthCorner, SERigEnum.eRigSide.RS_Left, 1)]     = 'MouthCorner_L_002_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_MouthCorner, SERigEnum.eRigSide.RS_Right, 1)]    = 'MouthCorner_R_002_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Jaw, SERigEnum.eRigSide.RS_Center, 0)]           = 'Jaw_C_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Cheek, SERigEnum.eRigSide.RS_Left, 0)]           = 'Cheek_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Cheek, SERigEnum.eRigSide.RS_Right, 0)]          = 'Cheek_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Chin, SERigEnum.eRigSide.RS_Left, 0)]            = 'Chin_L_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Chin, SERigEnum.eRigSide.RS_Left, 1)]            = 'Chin_L_002_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Chin, SERigEnum.eRigSide.RS_Center, 0)]          = 'Chin_C_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Chin, SERigEnum.eRigSide.RS_Right, 0)]           = 'Chin_R_001_Ctrl'
facialControlsTable[(SERigEnum.eRigFacialControlType.RFCT_Chin, SERigEnum.eRigSide.RS_Right, 1)]           = 'Chin_R_002_Ctrl'

#-----------------------------------------------------------------------------
def getFacialControlObject(facialControlType, rigSide, controlIndex):
    controlObject = None 
    try:
        controlObject = facialControlsTable[(facialControlType, rigSide, controlIndex)]
    except:
        cmds.warning('Facial control object not found.')

    return controlObject
#-----------------------------------------------------------------------------
def getFacialControlObjectTranslateRemappingNode(facialControlObject, suffix, channel):
    remappingNode = facialControlObject + '_' + channel + suffix
    if cmds.objExists(remappingNode):
        return remappingNode
    else:
        cmds.warning('Facial control translate remapping node not found.')
        return None
#-----------------------------------------------------------------------------
def createFacialControlObjectTranslateRemapping(facialControlObject, suffix, channel, input0 = 0, output0 = 0, input1 = 1, output1 = 1, nodeType = 'animCurveUU'):
    remappingNode = None

    if cmds.objExists(facialControlObject):
        nodeName = facialControlObject + '_' + channel + suffix
        if cmds.objExists(nodeName):
            cmds.warning('Facial control translate remapping node already created.')
            return nodeName

        remappingNode = cmds.createNode(nodeType, n = nodeName)
        cmds.setKeyframe(remappingNode, float = input0, value = output0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(remappingNode, float = input1, value = output1, itt = 'linear', ott = 'linear')
        cmds.keyTangent(remappingNode, weightedTangents = False)

        cmds.connectAttr(facialControlObject + '.' + channel, remappingNode + '.input', f = 1)

    else:
        cmds.warning('Facial control object not found.')

    return remappingNode
#-----------------------------------------------------------------------------
def connectFacialWrinkleMapAttrToMaterialAttr():
    facialObject = cmds.ls(sl = True)
    if facialObject:
        facialObject = facialObject[0]
    else:
        cmds.warning('Please select facial mesh.')
        return

    facialMaterial = getFacialMaterial()

    if facialObject and facialMaterial:
        try:
            for attr in SERigNaming.gWM_AttrList:
                cmds.connectAttr(facialObject + '.' + attr, facialMaterial + '.' + attr)
        except:
            cmds.warning('Cannot connect attributes.')

#-----------------------------------------------------------------------------
def getFacialMaterial():
    res = None

    selectedTransform = pymel.core.general.selected()
    if selectedTransform:
        selectedTransform = selectedTransform[0]
    else:
        cmds.warning('Please select facial mesh.')
        return

    shape = str(selectedTransform.getShape())

    shadeEng = cmds.listConnections(shape, type = 'shadingEngine')
    connections = cmds.listConnections(shadeEng)
    materials = cmds.ls(connections, materials = True)
    unique_materials_set = set(materials)
    materials = list(unique_materials_set)

    if len(materials) > 0:
        res = materials[0]

    return res

#-----------------------------------------------------------------------------
def createFacialWrinkleMapAttributes():
    facialObject = cmds.ls(sl = True)[0]

    for attr in SERigNaming.gWM_AttrList:
        cmds.addAttr(facialObject, ln = attr, at = 'float', k = 1, dv = 0.0, hasMinValue = True, min = 0.0, hasMaxValue = True, max = 1.0)
        cmds.setAttr(facialObject + '.' + attr, cb = 1)

#-----------------------------------------------------------------------------
def getFacialActionUnitAttrName(bufferObject, actionUnitType):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.auAttrList[actionUnitType]
    else:
        cmds.warning('Buffer object does not exist: ' + bufferObject)

    return res
#-----------------------------------------------------------------------------
def getFaceControlsUIGroup():
    # TODO:
    # Hard coded for now.
    if cmds.objExists('FaceControls_Grp'):
        return 'FaceControls_Grp'
    else:
        cmds.warning('Face controls UI group does not exist.')
        return None
#-----------------------------------------------------------------------------
def getFaceControlsOffsetControl():
    # TODO:
    # Hard coded for now.
    if cmds.objExists('FaceControls_Offset_Ctrl'):
        return 'FaceControls_Offset_Ctrl'
    else:
        cmds.warning('Face controls offset control does not exist.')
        return None
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
def createEyelidMotionLogic(auDataBuffer, leftEyeJoint, rightEyeJoint, leftEyelidUpperJoint, rightEyelidUpperJoint, 
                            leftEyelidLowerJoint, rightEyelidLowerJoint):

    if cmds.objExists(auDataBuffer) and cmds.objExists(leftEyeJoint) and cmds.objExists(rightEyeJoint) and \
       cmds.objExists(leftEyelidUpperJoint) and cmds.objExists(rightEyelidUpperJoint) and \
       cmds.objExists(leftEyelidLowerJoint) and cmds.objExists(rightEyelidLowerJoint):

        # Upper eyelid AU05.
        au05LAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_05_L)
        animCurveAu05L = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAu05L, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAu05L, float = 1.0, value = 8.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAu05L, weightedTangents = False)
        cmds.connectAttr(au05LAttr, animCurveAu05L + '.input')

        au05RAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_05_R)
        animCurveAu05R = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAu05R, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAu05R, float = 1.0, value = 8.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAu05R, weightedTangents = False)
        cmds.connectAttr(au05RAttr, animCurveAu05R + '.input')

        # Upper eyelid AU06.
        au06LAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_06_L)
        animCurveAu06L = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAu06L, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAu06L, float = 1.0, value = -7.23, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAu06L, weightedTangents = False)
        cmds.connectAttr(au06LAttr, animCurveAu06L + '.input')

        au06RAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_06_R)
        animCurveAu06R = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAu06R, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAu06R, float = 1.0, value = -7.23, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAu06R, weightedTangents = False)
        cmds.connectAttr(au06RAttr, animCurveAu06R + '.input')

        # Upper eyelid blink.
        blinkLAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Blink_L)
        animCurveAuBlinkL = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAuBlinkL, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAuBlinkL, float = 1.0, value = -27.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAuBlinkL, weightedTangents = False)
        cmds.connectAttr(blinkLAttr, animCurveAuBlinkL + '.input')

        blinkRAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Blink_R)
        animCurveAuBlinkR = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAuBlinkR, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAuBlinkR, float = 1.0, value = -27.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAuBlinkR, weightedTangents = False)
        cmds.connectAttr(blinkRAttr, animCurveAuBlinkR + '.input')

        # Upper eyelid Eye base.
        animCurveEyeBaseL = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveEyeBaseL, float = -45.0, value = -45.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveEyeBaseL, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveEyeBaseL, weightedTangents = False)
        cmds.connectAttr(leftEyeJoint + '.rotateZ', animCurveEyeBaseL + '.input', f = 1)

        animCurveEyeBaseR = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveEyeBaseR, float = -45.0, value = -45.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveEyeBaseR, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveEyeBaseR, weightedTangents = False)
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


        # lower eyelid AU06.
        au06LAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_06_L)
        animCurveAu06L = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAu06L, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAu06L, float = 1.0, value = 15.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAu06L, weightedTangents = False)
        cmds.connectAttr(au06LAttr, animCurveAu06L + '.input')

        au06RAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_06_R)
        animCurveAu06R = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAu06R, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAu06R, float = 1.0, value = 15.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAu06R, weightedTangents = False)
        cmds.connectAttr(au06RAttr, animCurveAu06R + '.input')

        # lower eyelid AU07.
        au07LAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_07_L)
        animCurveAu07L = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAu07L, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAu07L, float = 1.0, value = 12.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAu07L, weightedTangents = False)
        cmds.connectAttr(au07LAttr, animCurveAu07L + '.input')

        au07RAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_07_R)
        animCurveAu07R = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAu07R, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAu07R, float = 1.0, value = 12.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAu07R, weightedTangents = False)
        cmds.connectAttr(au07RAttr, animCurveAu07R + '.input')

        # lower eyelid blink.
        blinkLAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Blink_L)
        animCurveAuBlinkL = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAuBlinkL, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAuBlinkL, float = 1.0, value = 2.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAuBlinkL, weightedTangents = False)
        cmds.connectAttr(blinkLAttr, animCurveAuBlinkL + '.input')

        blinkRAttr = getFacialActionUnitAttrName(auDataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Blink_R)
        animCurveAuBlinkR = cmds.createNode('animCurveUA')
        cmds.setKeyframe(animCurveAuBlinkR, float = 0.0, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(animCurveAuBlinkR, float = 1.0, value = 2.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(animCurveAuBlinkR, weightedTangents = False)
        cmds.connectAttr(blinkRAttr, animCurveAuBlinkR + '.input')

        # Blend all drivers together using blend weighted nodes for lower eyelid joints.
        leftLowerEyelidBlend = cmds.createNode('blendWeighted')
        cmds.connectAttr(animCurveAu06L + '.output', leftLowerEyelidBlend + '.input[0]', f = 1)
        cmds.connectAttr(animCurveAu07L + '.output', leftLowerEyelidBlend + '.input[1]', f = 1)
        cmds.connectAttr(animCurveAuBlinkL + '.output', leftLowerEyelidBlend + '.input[2]', f = 1)

        rightLowerEyelidBlend = cmds.createNode('blendWeighted')
        cmds.connectAttr(animCurveAu06R + '.output', rightLowerEyelidBlend + '.input[0]', f = 1)
        cmds.connectAttr(animCurveAu07R + '.output', rightLowerEyelidBlend + '.input[1]', f = 1)
        cmds.connectAttr(animCurveAuBlinkR + '.output', rightLowerEyelidBlend + '.input[2]', f = 1)

        cmds.connectAttr(leftLowerEyelidBlend + '.output', leftEyelidLowerJoint + '.rotateZ', f = 1)
        cmds.connectAttr(rightLowerEyelidBlend + '.output', rightEyelidLowerJoint + '.rotateZ', f = 1)

    else:
        cmds.warning('Failed creating eyelid motion logic.')
#-----------------------------------------------------------------------------
def createEyeballRotationTrackingLogic(eyeBlockingSphere, eyeEndIkJoint, rigSide, inFACS_DataBuffer):
    if cmds.objExists(eyeBlockingSphere) and cmds.objExists(eyeEndIkJoint):
        locatorEyeEnd = cmds.spaceLocator(n = 'locator_' + eyeEndIkJoint)[0]
        cmds.delete(cmds.pointConstraint(eyeEndIkJoint, locatorEyeEnd, mo = 0))
        cmds.parent(locatorEyeEnd, eyeEndIkJoint)

        attrList = ['L', 'R', 'U', 'D']
        for attr in attrList:
            cmds.addAttr(locatorEyeEnd, ln = attr, at = 'float', k = 1, dv = 0.0, hasMinValue = True, min = 0.0, hasMaxValue = True, max = 1.0)
            cmds.setAttr(locatorEyeEnd + '.' + attr, cb = 1)

        locatorEyeEndShape = cmds.listRelatives(locatorEyeEnd, s = 1)[0]
        eyeBlockingSphereShape = cmds.listRelatives(eyeBlockingSphere, s = 1)[0]
        cpos = cmds.createNode('closestPointOnSurface')
        cmds.connectAttr(locatorEyeEndShape + '.worldPosition[0]', cpos + '.inPosition', f = 1)
        cmds.connectAttr(eyeBlockingSphereShape + '.worldSpace[0]', cpos + '.inputSurface', f = 1)

        # Get neutral uv position.
        neutralU = cmds.getAttr(cpos + '.parameterU')
        neutralV = cmds.getAttr(cpos + '.parameterV')

        minV = neutralV - 0.25
        maxV = neutralV + 0.25
        minU = neutralU - 0.5
        maxU = neutralU + 0.5

        # Create uv remapping animCurve nodes.

        # Turn left.
        eyeTurnLeftAnimCurveName = ''
        if rigSide == SERigEnum.eRigSide.RS_Left:
            eyeTurnLeftAnimCurveName = SERigNaming.sLeftEyeTurnLeftAnimCurve
        else:
            eyeTurnLeftAnimCurveName = SERigNaming.sRightEyeTurnLeftAnimCurve

        eyeTurnLeftAnimCurve = cmds.createNode('animCurveUL', n = eyeTurnLeftAnimCurveName)
        cmds.setKeyframe(eyeTurnLeftAnimCurve, float = neutralV, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(eyeTurnLeftAnimCurve, float = minV, value = 1.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(eyeTurnLeftAnimCurve, weightedTangents = False)

        cmds.connectAttr(cpos + '.parameterV', eyeTurnLeftAnimCurve + '.input', f = 1)
        cmds.connectAttr(eyeTurnLeftAnimCurve + '.output', locatorEyeEnd + '.L', f = 1)

        # Turn right.
        eyeTurnRightAnimCurveName = ''
        if rigSide == SERigEnum.eRigSide.RS_Left:
            eyeTurnRightAnimCurveName = SERigNaming.sLeftEyeTurnRightAnimCurve
        else:
            eyeTurnRightAnimCurveName = SERigNaming.sRightEyeTurnRightAnimCurve

        eyeTurnRightAnimCurve = cmds.createNode('animCurveUL', n = eyeTurnRightAnimCurveName)
        cmds.setKeyframe(eyeTurnRightAnimCurve, float = neutralV, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(eyeTurnRightAnimCurve, float = maxV, value = 1.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(eyeTurnRightAnimCurve, weightedTangents = False)

        cmds.connectAttr(cpos + '.parameterV', eyeTurnRightAnimCurve + '.input', f = 1)
        cmds.connectAttr(eyeTurnRightAnimCurve + '.output', locatorEyeEnd + '.R', f = 1)

        # Turn up.
        eyeTurnUpAnimCurveName = ''
        if rigSide == SERigEnum.eRigSide.RS_Left:
            eyeTurnUpAnimCurveName = SERigNaming.sLeftEyeTurnUpAnimCurve
        else:
            eyeTurnUpAnimCurveName = SERigNaming.sRightEyeTurnUpAnimCurve

        eyeTurnUpAnimCurve = cmds.createNode('animCurveUL', n = eyeTurnUpAnimCurveName)
        cmds.setKeyframe(eyeTurnUpAnimCurve, float = neutralU, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(eyeTurnUpAnimCurve, float = maxU, value = 1.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(eyeTurnUpAnimCurve, weightedTangents = False)

        cmds.connectAttr(cpos + '.parameterU', eyeTurnUpAnimCurve + '.input', f = 1)
        cmds.connectAttr(eyeTurnUpAnimCurve + '.output', locatorEyeEnd + '.U', f = 1)

        # Turn down.
        eyeTurnDownAnimCurveName = ''
        if rigSide == SERigEnum.eRigSide.RS_Left:
            eyeTurnDownAnimCurveName = SERigNaming.sLeftEyeTurnDownAnimCurve
        else:
            eyeTurnDownAnimCurveName = SERigNaming.sRightEyeTurnDownAnimCurve

        eyeTurnDownAnimCurve = cmds.createNode('animCurveUL', n = eyeTurnDownAnimCurveName)
        cmds.setKeyframe(eyeTurnDownAnimCurve, float = neutralU, value = 0.0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(eyeTurnDownAnimCurve, float = minU, value = 1.0, itt = 'linear', ott = 'linear')
        cmds.keyTangent(eyeTurnDownAnimCurve, weightedTangents = False)

        cmds.connectAttr(cpos + '.parameterU', eyeTurnDownAnimCurve + '.input', f = 1)
        cmds.connectAttr(eyeTurnDownAnimCurve + '.output', locatorEyeEnd + '.D', f = 1)

        if cmds.objExists(inFACS_DataBuffer):
            tempBufferInputL = None
            tempBufferInputR = None
            tempBufferInputU = None
            tempBufferInputD = None
            if rigSide == SERigEnum.eRigSide.RS_Left:
                tempBufferInputL = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookLeft)
                tempBufferInputR = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookRight)
                tempBufferInputU = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookUp)
                tempBufferInputD = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookDown)
            else:
                tempBufferInputL = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookLeft)
                tempBufferInputR = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookRight)
                tempBufferInputU = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookUp)
                tempBufferInputD = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookDown)
                        
            cmds.connectAttr(locatorEyeEnd + '.L', tempBufferInputL)
            cmds.connectAttr(locatorEyeEnd + '.R', tempBufferInputR)
            cmds.connectAttr(locatorEyeEnd + '.D', tempBufferInputD)
            cmds.connectAttr(locatorEyeEnd + '.U', tempBufferInputU)
        else:
            cmds.warning('createEyeballRotationTrackingLogic: FACS data buffer does not exist.')

#-----------------------------------------------------------------------------
def createFACS_DataBuffer(facialComponentGroup):
    prefix = SERigObjectTypeHelper.getCharacterComponentPrefix(facialComponentGroup)
    rigPartsGroup = SERigObjectTypeHelper.getCharacterComponentRigPartsGroup(facialComponentGroup)

    if prefix == None or rigPartsGroup == None:
        cmds.error('Failed creating FACS data buffer for: ' + facialComponentGroup)
        return None

    bufferName = prefix + '_FACS_DataBufferGrp'
    if cmds.objExists(bufferName):
        # TODO: 
        # Delete the existing buffer?
        cmds.warning('FACS data buffer already exists.')
        return bufferName

    # Create a new data buffer.
    dataBufferGroup = cmds.group(n = bufferName, em = 1, p = rigPartsGroup)

    singleAttributeLockList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']
    for attr in singleAttributeLockList:
        cmds.setAttr(dataBufferGroup + '.' + attr, l = 1, k = 0, cb = 0)

    for attr in SERigNaming.auAttrList:
        cmds.addAttr(dataBufferGroup, ln = attr, at = 'float', k = 1, dv = 0.0, hasMinValue = True, min = 0.0, hasMaxValue = True, max = 1.0)
        cmds.setAttr(dataBufferGroup + '.' + attr, cb = 1)

    SERigObjectTypeHelper.linkRigObjects(facialComponentGroup, dataBufferGroup, SERigNaming.sFACS_DataBufferAttr)

    return dataBufferGroup
#-----------------------------------------------------------------------------
def getFACS_DataBuffer(facialComponentGroup):
    if cmds.objExists(facialComponentGroup):
        try:
            res = cmds.listConnections(facialComponentGroup + '.' + SERigNaming.sFACS_DataBufferAttr)[0]
            return res
        except:
            cmds.warning('Cannot find facial component: ' + facialComponentGroup + ' FACS data buffer')
            return None
    else:
        cmds.warning('Cannot find facial component: ' + facialComponentGroup)
        return None
#-----------------------------------------------------------------------------
def createFACS_FacialControlLogic(inFACS_DataBuffer, facialJoints):
    # Inner brows controls (tx, ty).
    leftInnerBrowControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_InnerBrow, SERigEnum.eRigSide.RS_Left, 0)
    if leftInnerBrowControlObj:
        remappingNode = createFacialControlObjectTranslateRemapping(leftInnerBrowControlObj, '_remapping', 'tx', -1, 1, 0, 0)
        tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_04_L)
        cmds.connectAttr(remappingNode + '.output', tempBufferInput)

        remappingNode = createFacialControlObjectTranslateRemapping(leftInnerBrowControlObj, '_remapping', 'ty', 1, 1, 0, 0)
        tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_01_L)
        cmds.connectAttr(remappingNode + '.output', tempBufferInput)

    rightInnerBrowControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_InnerBrow, SERigEnum.eRigSide.RS_Right, 0)
    if rightInnerBrowControlObj:
        remappingNode = createFacialControlObjectTranslateRemapping(rightInnerBrowControlObj, '_remapping', 'tx', -1, 1, 0, 0)
        tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_04_R)
        cmds.connectAttr(remappingNode + '.output', tempBufferInput)

        remappingNode = createFacialControlObjectTranslateRemapping(rightInnerBrowControlObj, '_remapping', 'ty', 1, 1, 0, 0)
        tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_01_R)
        cmds.connectAttr(remappingNode + '.output', tempBufferInput)

    # Outer brows controls (ty).
    leftOuterBrowControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_OuterBrow, SERigEnum.eRigSide.RS_Left, 0)
    if leftOuterBrowControlObj:
        remappingNode = createFacialControlObjectTranslateRemapping(leftOuterBrowControlObj, '_remapping', 'ty')
        tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_02_L)
        cmds.connectAttr(remappingNode + '.output', tempBufferInput)

    rightOuterBrowControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_OuterBrow, SERigEnum.eRigSide.RS_Right, 0)
    if rightOuterBrowControlObj:
        remappingNode = createFacialControlObjectTranslateRemapping(rightOuterBrowControlObj, '_remapping', 'ty')
        tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_02_R)
        cmds.connectAttr(remappingNode + '.output', tempBufferInput)

    # Upper eyelid controls (ty).
    leftUpperEyelidControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_UpperLid, SERigEnum.eRigSide.RS_Left, 0)
    unitConversionNodeL = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeL + '.conversionFactor', -1.0)
    cmds.connectAttr(leftUpperEyelidControlObj + '.ty', unitConversionNodeL + '.input')

    rightUpperEyelidControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_UpperLid, SERigEnum.eRigSide.RS_Right, 0)
    unitConversionNodeR = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeR + '.conversionFactor', -1.0)
    cmds.connectAttr(rightUpperEyelidControlObj + '.ty', unitConversionNodeR + '.input')

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    cmds.connectAttr(unitConversionNodeL + '.output', clampNode + '.inputR')
    cmds.connectAttr(unitConversionNodeR + '.output', clampNode + '.inputG')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Blink_L)
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Blink_R)
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 0.5)
    cmds.setAttr(clampNode + '.maxG', 0.5)

    cmds.connectAttr(leftUpperEyelidControlObj + '.ty', clampNode + '.inputR')
    cmds.connectAttr(rightUpperEyelidControlObj + '.ty', clampNode + '.inputG')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_05_L)
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_05_R)
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    # Lower eyelid controls (ty).
    leftLowerEyelidControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_LowerLid, SERigEnum.eRigSide.RS_Left, 0)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_07_L)
    cmds.connectAttr(leftLowerEyelidControlObj + '.ty', tempBufferInput)

    rightLowerEyelidControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_LowerLid, SERigEnum.eRigSide.RS_Right, 0)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_07_R)
    cmds.connectAttr(rightLowerEyelidControlObj + '.ty', tempBufferInput)

    # Eye corner controls (tx).
    leftOuterEyeCornerControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_OuterEyeCorner, SERigEnum.eRigSide.RS_Left, 0)
    unitConversionNodeL = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeL + '.conversionFactor', -1.0)
    cmds.connectAttr(leftOuterEyeCornerControlObj + '.tx', unitConversionNodeL + '.input')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_06_L)
    cmds.connectAttr(unitConversionNodeL + '.output', tempBufferInput)

    rightOuterEyeCornerControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_OuterEyeCorner, SERigEnum.eRigSide.RS_Right, 0)
    unitConversionNodeR = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeR + '.conversionFactor', -1.0)
    cmds.connectAttr(rightOuterEyeCornerControlObj + '.tx', unitConversionNodeR + '.input')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_06_R)
    cmds.connectAttr(unitConversionNodeR + '.output', tempBufferInput)

    # Nosewing controls (tx, ty).
    leftNosewingControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Nosewing, SERigEnum.eRigSide.RS_Left, 0)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_09_L)
    cmds.connectAttr(leftNosewingControlObj + '.ty', tempBufferInput)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_11_L)
    cmds.connectAttr(leftNosewingControlObj + '.tx', tempBufferInput)

    rightNosewingControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Nosewing, SERigEnum.eRigSide.RS_Right, 0)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_09_R)
    cmds.connectAttr(rightNosewingControlObj + '.ty', tempBufferInput)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_11_R)
    cmds.connectAttr(rightNosewingControlObj + '.tx', tempBufferInput)

    # Muzzle controls (ty).
    leftMuzzleControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Muzzle, SERigEnum.eRigSide.RS_Left, 0)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_10_L)
    cmds.connectAttr(leftMuzzleControlObj + '.ty', tempBufferInput)

    rightMuzzleControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Muzzle, SERigEnum.eRigSide.RS_Right, 0)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_10_R)
    cmds.connectAttr(rightMuzzleControlObj + '.ty', tempBufferInput)

    # Lip and mouth controls.
    leftUpperlipControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_UpperLip, SERigEnum.eRigSide.RS_Left, 0)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_10_OL)
    cmds.connectAttr(leftUpperlipControlObj + '.ty', tempBufferInput)

    rightUpperlipControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_UpperLip, SERigEnum.eRigSide.RS_Right, 0)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_10_OR)
    cmds.connectAttr(rightUpperlipControlObj + '.ty', tempBufferInput)

    # AU 22,23 U (tz).
    centerUpperlipControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_UpperLip, SERigEnum.eRigSide.RS_Center, 0)
    centerUpperlipControlRemappingNodeAU23U = createFacialControlObjectTranslateRemapping(centerUpperlipControlObj, '_AU23U', 'tz', -1, 1, 0, 0)
    centerUpperlipControlRemappingNodeAU22U = createFacialControlObjectTranslateRemapping(centerUpperlipControlObj, '_AU22U', 'tz', 1, 1, 0, 0)

    mouthControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Mouth, SERigEnum.eRigSide.RS_Center, 0)
    mouthControlRemappingNodeAU23U = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU23U', 'tz', -1, 1, 0, 0)
    mouthControlRemappingNodeAU22U = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU22U', 'tz', 1, 1, 0, 0)
    
    au23UBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(centerUpperlipControlRemappingNodeAU23U + '.output', au23UBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU23U + '.output', au23UBlend + '.input[1]', f = 1)

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_23_U)
    cmds.connectAttr(au23UBlend + '.output', clampNode + '.inputR')
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    au22UBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(centerUpperlipControlRemappingNodeAU22U + '.output', au22UBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU22U + '.output', au22UBlend + '.input[1]', f = 1)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_22_U)
    cmds.connectAttr(au22UBlend + '.output', clampNode + '.inputG')
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    # AU 17,28 U (ty).
    centerUpperlipControlRemappingNodeAU17U = createFacialControlObjectTranslateRemapping(centerUpperlipControlObj, '_AU17U', 'ty', 1, 1, 0, 0)
    centerUpperlipControlRemappingNodeAU28U = createFacialControlObjectTranslateRemapping(centerUpperlipControlObj, '_AU28U', 'ty', -1, 1, 0, 0)

    mouthControlRemappingNodeAU17U = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU17U', 'ty', 1, 1, 0, 0)
    mouthControlRemappingNodeAU28U = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU28U', 'ty', -1, 1, 0, 0)

    au17UBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(centerUpperlipControlRemappingNodeAU17U + '.output', au17UBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU17U + '.output', au17UBlend + '.input[1]', f = 1)

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_17_U)
    cmds.connectAttr(au17UBlend + '.output', clampNode + '.inputR')
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    au28UBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(centerUpperlipControlRemappingNodeAU28U + '.output', au28UBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU28U + '.output', au28UBlend + '.input[1]', f = 1)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_28_U)
    cmds.connectAttr(au28UBlend + '.output', clampNode + '.inputG')
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    # AU 22,23 D.
    centerLowerlipControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_LowerLip, SERigEnum.eRigSide.RS_Center, 0)
    centerLowerlipControlRemappingNodeAU23D = createFacialControlObjectTranslateRemapping(centerLowerlipControlObj, '_AU23D', 'tz', -1, 1, 0, 0)
    centerLowerlipControlRemappingNodeAU22D = createFacialControlObjectTranslateRemapping(centerLowerlipControlObj, '_AU22D', 'tz', 1, 1, 0, 0)    

    mouthControlRemappingNodeAU23D = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU23D', 'tz', -1, 1, 0, 0)
    mouthControlRemappingNodeAU22D = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU22D', 'tz', 1, 1, 0, 0)

    au23DBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(centerLowerlipControlRemappingNodeAU23D + '.output', au23DBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU23D + '.output', au23DBlend + '.input[1]', f = 1)

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_23_D)
    cmds.connectAttr(au23DBlend + '.output', clampNode + '.inputR')
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    au22DBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(centerLowerlipControlRemappingNodeAU22D + '.output', au22DBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU22D + '.output', au22DBlend + '.input[1]', f = 1)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_22_D)
    cmds.connectAttr(au22DBlend + '.output', clampNode + '.inputG')
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    # AU 17,28 D (ty).
    centerLowerlipControlRemappingNodeAU17D = createFacialControlObjectTranslateRemapping(centerLowerlipControlObj, '_AU17D', 'ty', 1, 1, 0, 0)
    centerLowerlipControlRemappingNodeAU28D = createFacialControlObjectTranslateRemapping(centerLowerlipControlObj, '_AU28D', 'ty', -1, 1, 0, 0)

    mouthControlRemappingNodeAU17D = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU17D', 'ty', 1, 1, 0, 0)
    mouthControlRemappingNodeAU28D = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU28D', 'ty', -1, 1, 0, 0)

    au17DBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(centerLowerlipControlRemappingNodeAU17D + '.output', au17DBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU17D + '.output', au17DBlend + '.input[1]', f = 1)

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_17_D)
    cmds.connectAttr(au17DBlend + '.output', clampNode + '.inputR')
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    au28DBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(centerLowerlipControlRemappingNodeAU28D + '.output', au28DBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU28D + '.output', au28DBlend + '.input[1]', f = 1)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_28_D)
    cmds.connectAttr(au28DBlend + '.output', clampNode + '.inputG')
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    # AU 12 L,18 R (tx).
    rightMouthCornerControl01Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_MouthCorner, SERigEnum.eRigSide.RS_Right, 0)
    leftMouthCornerControl02Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_MouthCorner, SERigEnum.eRigSide.RS_Left, 1)
    rightMouthCornerControl01RemappingNodeAU18R = createFacialControlObjectTranslateRemapping(rightMouthCornerControl01Obj, '_AU18R', 'tx', -1, 0.7, 0, 0)
    leftMouthCornerControl02RemappingNodeAU12L = createFacialControlObjectTranslateRemapping(leftMouthCornerControl02Obj, '_AU12L', 'tx', 1, 1, 0, 0)
    mouthControlRemappingNodeAU18R = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU18R', 'tx', 1, 1, 0, 0)
    mouthControlRemappingNodeAU12L = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU12L', 'tx', 1, 1, 0, 0)

    au12LBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(leftMouthCornerControl02RemappingNodeAU12L + '.output', au12LBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU12L + '.output', au12LBlend + '.input[1]', f = 1)

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_12_L)
    cmds.connectAttr(au12LBlend + '.output', clampNode + '.inputR')
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    au18RBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(rightMouthCornerControl01RemappingNodeAU18R + '.output', au18RBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU18R + '.output', au18RBlend + '.input[1]', f = 1)

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_18_R)
    cmds.connectAttr(au18RBlend + '.output', clampNode + '.inputR')
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    # AU 12 R,18 L (tx).
    leftMouthCornerControl01Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_MouthCorner, SERigEnum.eRigSide.RS_Left, 0)
    rightMouthCornerControl02Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_MouthCorner, SERigEnum.eRigSide.RS_Right, 1)
    leftMouthCornerControl01RemappingNodeAU18L = createFacialControlObjectTranslateRemapping(leftMouthCornerControl01Obj, '_AU18L', 'tx', -1, 0.7, 0, 0)
    rightMouthCornerControl02RemappingNodeAU12R = createFacialControlObjectTranslateRemapping(rightMouthCornerControl02Obj, '_AU12R', 'tx', 1, 1, 0, 0)
    mouthControlRemappingNodeAU18L = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU18L', 'tx', -1, 1, 0, 0)
    mouthControlRemappingNodeAU12R = createFacialControlObjectTranslateRemapping(mouthControlObj, '_AU12R', 'tx', -1, 1, 0, 0)

    au12RBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(rightMouthCornerControl02RemappingNodeAU12R + '.output', au12RBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU12R + '.output', au12RBlend + '.input[1]', f = 1)

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_12_R)
    cmds.connectAttr(au12RBlend + '.output', clampNode + '.inputR')
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    au18LBlend = cmds.createNode('blendWeighted')
    cmds.connectAttr(leftMouthCornerControl01RemappingNodeAU18L + '.output', au18LBlend + '.input[0]', f = 1)
    cmds.connectAttr(mouthControlRemappingNodeAU18L + '.output', au18LBlend + '.input[1]', f = 1)

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_18_L)
    cmds.connectAttr(au18LBlend + '.output', clampNode + '.inputR')
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    # AU 15 (ty).
    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    unitConversionNodeL = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeL + '.conversionFactor', -1.0)
    cmds.connectAttr(leftMouthCornerControl01Obj + '.ty', unitConversionNodeL + '.input')
    
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_15_L)
    cmds.connectAttr(unitConversionNodeL + '.output', clampNode + '.inputR')
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    unitConversionNodeR = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeR + '.conversionFactor', -1.0)
    cmds.connectAttr(rightMouthCornerControl01Obj + '.ty', unitConversionNodeR + '.input')
    
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_15_R)
    cmds.connectAttr(unitConversionNodeR + '.output', clampNode + '.inputG')
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    # AU 14 (tx).
    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_14_L)
    cmds.connectAttr(leftMouthCornerControl01Obj + '.tx', clampNode + '.inputR')
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_14_R)
    cmds.connectAttr(rightMouthCornerControl01Obj + '.tx', clampNode + '.inputG')
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    # AU 13 (ty).
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_13_L)
    cmds.connectAttr(leftMouthCornerControl02Obj + '.ty', tempBufferInput)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_13_R)
    cmds.connectAttr(rightMouthCornerControl02Obj + '.ty', tempBufferInput)

    # AU 12 OL, OR (ty).
    leftLowerLipControl01Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_LowerLip, SERigEnum.eRigSide.RS_Left, 0)
    unitConversionNodeL = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeL + '.conversionFactor', -1.0)
    cmds.connectAttr(leftLowerLipControl01Obj + '.ty', unitConversionNodeL + '.input')
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_12_OL)
    cmds.connectAttr(unitConversionNodeL + '.output', tempBufferInput)

    rightLowerLipControl01Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_LowerLip, SERigEnum.eRigSide.RS_Right, 0)
    unitConversionNodeR = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeR + '.conversionFactor', -1.0)
    cmds.connectAttr(rightLowerLipControl01Obj + '.ty', unitConversionNodeR + '.input')
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_12_OR)
    cmds.connectAttr(unitConversionNodeR + '.output', tempBufferInput)

    # Cheek controls (tx).
    leftCheekControl01Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Cheek, SERigEnum.eRigSide.RS_Left, 0)
    rightCheekControl01Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Cheek, SERigEnum.eRigSide.RS_Right, 0)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Puff_L)
    cmds.connectAttr(leftCheekControl01Obj + '.tx', tempBufferInput)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Puff_R)
    cmds.connectAttr(rightCheekControl01Obj + '.tx', tempBufferInput)

    unitConversionNodeL = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeL + '.conversionFactor', -2.0)
    cmds.connectAttr(leftCheekControl01Obj + '.tx', unitConversionNodeL + '.input')

    unitConversionNodeR = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeR + '.conversionFactor', -2.0)
    cmds.connectAttr(rightCheekControl01Obj + '.tx', unitConversionNodeR + '.input')

    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    cmds.connectAttr(unitConversionNodeL + '.output', clampNode + '.inputR')
    cmds.connectAttr(unitConversionNodeR + '.output', clampNode + '.inputG')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Shrink_L)
    cmds.connectAttr(clampNode + '.outputR', tempBufferInput)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_Shrink_R)
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    # Chin center control (ty).
    chinCenterControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Chin, SERigEnum.eRigSide.RS_Center, 0)
    
    clampNode = cmds.createNode('clamp')
    cmds.setAttr(clampNode + '.maxR', 1.0)
    cmds.setAttr(clampNode + '.maxG', 1.0)

    cmds.connectAttr(chinCenterControlObj + '.ty', clampNode + '.inputR')
    # TODO:
    # Hard coded control name for now.
    cmds.connectAttr(clampNode + '.outputR', 'FK_OnFace_LipClose_Ctrl.ty')

    unitConversionNode = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNode + '.conversionFactor', -1.0)
    cmds.connectAttr(chinCenterControlObj + '.ty', unitConversionNode + '.input')
    cmds.connectAttr(unitConversionNode + '.output', clampNode + '.inputG')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_25_D)
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_25_U)
    cmds.connectAttr(clampNode + '.outputG', tempBufferInput)

    # Chin controls (ty).
    leftChinControl01Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Chin, SERigEnum.eRigSide.RS_Left, 0)
    rightChinControl01Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Chin, SERigEnum.eRigSide.RS_Right, 0)
    leftChinControl02Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Chin, SERigEnum.eRigSide.RS_Left, 1)
    rightChinControl02Obj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Chin, SERigEnum.eRigSide.RS_Right, 1)

    unitConversionNodeL = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeL + '.conversionFactor', -1.0)
    cmds.connectAttr(leftChinControl01Obj + '.ty', unitConversionNodeL + '.input')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_16_L)
    cmds.connectAttr(unitConversionNodeL + '.output', tempBufferInput)

    unitConversionNodeR = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeR + '.conversionFactor', -1.0)
    cmds.connectAttr(rightChinControl01Obj + '.ty', unitConversionNodeR + '.input')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_16_R)
    cmds.connectAttr(unitConversionNodeR + '.output', tempBufferInput)

    unitConversionNodeL = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeL + '.conversionFactor', -1.0)
    cmds.connectAttr(leftChinControl02Obj + '.ty', unitConversionNodeL + '.input')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_20_L)
    cmds.connectAttr(unitConversionNodeL + '.output', tempBufferInput)

    unitConversionNodeR = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNodeR + '.conversionFactor', -1.0)
    cmds.connectAttr(rightChinControl02Obj + '.ty', unitConversionNodeR + '.input')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_20_R)
    cmds.connectAttr(unitConversionNodeR + '.output', tempBufferInput)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_20_NL)
    cmds.connectAttr(leftChinControl02Obj + '.tx', tempBufferInput)

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_20_NR)
    cmds.connectAttr(rightChinControl02Obj + '.tx', tempBufferInput)

    # Jaw control (tx, ty, tz).
    jawControlObj = getFacialControlObject(SERigEnum.eRigFacialControlType.RFCT_Jaw, SERigEnum.eRigSide.RS_Center, 0)

    # TODO:
    # Hard coded control name for now.
    onFaceJawControlObj = 'IK_OnFace_Jaw_Ctrl'
    cmds.connectAttr(jawControlObj + '.tx', onFaceJawControlObj + '.tx')
    cmds.connectAttr(jawControlObj + '.ty', onFaceJawControlObj + '.ty')
    cmds.connectAttr(jawControlObj + '.tz', onFaceJawControlObj + '.tz')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_24)
    jawControlRemappingNodeAU24 = createFacialControlObjectTranslateRemapping(onFaceJawControlObj, '_AU24', 'ty', 0.05, 0, 0.25, 1)
    cmds.connectAttr(jawControlRemappingNodeAU24 + '.output', tempBufferInput)

    unitConversionNode = cmds.createNode('unitConversion')
    cmds.setAttr(unitConversionNode + '.conversionFactor', 0.1)
    cmds.connectAttr(onFaceJawControlObj + '.jawForward', unitConversionNode + '.input')

    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_JawForward)
    cmds.connectAttr(unitConversionNode + '.output', tempBufferInput)

    # TODO:
    # Hard coded control drive group name for now (AU28D,AU28U).
    onFaceJawControlDriveGroup = 'IK_OnFace_Jaw_DrvGrp'
    multiplyNode = cmds.createNode('multiplyDivide', n = 'AU28_DU_Multiply')
    tempBufferOutput_28D = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_28_D)
    tempBufferOutput_28U = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_28_U)
    cmds.connectAttr(tempBufferOutput_28D, multiplyNode + '.input1X')
    cmds.connectAttr(tempBufferOutput_28U, multiplyNode + '.input2X')
    jawDrvRemappingNodeAU28 = createFacialControlObjectTranslateRemapping(multiplyNode, '', 'outputX', 0, 0, 1, -0.3, nodeType = 'animCurveUL')
    cmds.connectAttr(jawDrvRemappingNodeAU28 + '.output', onFaceJawControlDriveGroup + '.ty')

    # AU 26 Fix, LipClose Fix.
    jawJoint = SEJointHelper.getFacialJawJoint(facialJoints)
    jawJointRemappingNodeAU26Fix = SEJointHelper.createJointRotationRemapping(jawJoint, 'AU26_Fix', 'rz', 0, 0, -22, 1)
    tempBufferInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_26_Fix)
    cmds.connectAttr(jawJointRemappingNodeAU26Fix + '.output', tempBufferInput)

    tempBufferAU26FixOutput = tempBufferInput
    tempBufferLipCloseOutput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_LipClose)
    tempBufferAU26CloseFixInput = getFacialActionUnitAttrName(inFACS_DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_26_CloseFix)

    mulNode = cmds.createNode('multiplyDivide')
    cmds.setAttr(mulNode + '.operation', 1)
    cmds.connectAttr(tempBufferAU26FixOutput, mulNode + '.input1X')
    cmds.connectAttr(tempBufferLipCloseOutput, mulNode + '.input2X')
    cmds.connectAttr(mulNode + '.outputX', tempBufferAU26CloseFixInput)


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
        self.JawPosControl = None
        self.JawMidPosControl = None
        self.OnFaceIKJawControl = None
        self.OnFaceLipCloseControl = None
        self.LeftEyeIkControl = None
        self.RightEyeIkControl = None

        self.IKJointsGroup = None
        self.OnFaceIkControlGroup = None
        self.OnFaceFkControlGroup = None
        self.DataBuffer = None

        self.GeneratedFacialBaseJoints = []

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
            cmds.makeIdentity(ikChinJoint01, apply = True)

            # Offset the rotation a little bit such that the RP IK handle can work on the joint chain properly.
            cmds.setAttr(ikChinJoint01 + '.rotateZ', -0.5)
            cmds.makeIdentity(ikChinJoint01, apply = True)
                
            cmds.select(cl = 1)
            ikChinJoint02 = cmds.joint(n = SERigNaming.sIKPrefix + 'Chin_2')
            cmds.delete(cmds.parentConstraint(ikChinJoint01, ikChinJoint02, mo = 0))
            cmds.setAttr(ikChinJoint02 + '.radius', 0.5)

            p1 = SEMathHelper.getWorldPosition(ikChinJoint01)
            p3 = SEMathHelper.getWorldPosition(ikChinJoint03)
            halfDis = 0.5 * SEMathHelper.getDistance3(p1, p3)
            cmds.move(halfDis, 0.0, 0.0, ikChinJoint02, r = 1, os = 1)

            cmds.delete(cmds.aimConstraint(ikChinJoint03, ikChinJoint02, offset = [0, 0, 0], w = 1, aim = [1, 0, 0], u = [0, 1, 0], 
                                            worldUpType = 'scene'))
            cmds.makeIdentity(ikChinJoint02, apply = True)

            cmds.delete(cmds.orientConstraint(ikChinJoint02, ikChinJoint03, mo = 0))

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

            # Create IK handle.
            chinBulgeIK = cmds.ikHandle(n = self.Prefix + 'ChinBulge' + SERigNaming.s_IKHandle, sol = 'ikRPsolver', 
                                        sj = ikChinJoint01, ee = ikChinJoint03)[0]
            cmds.poleVectorConstraint(locatorChinIkPV, chinBulgeIK)
            SEJointHelper.adjustIKTwist(chinBulgeIK, ikChinJoint01)
            cmds.hide(chinBulgeIK)

            cmds.parentConstraint(jawEndJoint, ikChinJoint01, mo = 1)
            cmds.parent(chinBulgeIK, throatIk_OffsetGrp)

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

        # Setup FACS face controls.
        faceControlsUIGroup = getFaceControlsUIGroup()
        if faceControlsUIGroup == None:
            cmds.warning('Failed building facial system, face controls UI group does not exist.')
            return

        cmds.delete(cmds.pointConstraint(facialAttachPoint, faceControlsUIGroup, mo = 0))
        cmds.parent(faceControlsUIGroup, self.ControlsGrp)
        cmds.parentConstraint(facialAttachPoint, faceControlsUIGroup, mo = 1)

        faceControlsOffsetControl = getFaceControlsOffsetControl()
        if faceControlsOffsetControl:
            cmds.setAttr(faceControlsOffsetControl + '.tx', 0.0)
            cmds.setAttr(faceControlsOffsetControl + '.ty', -1.25)
            cmds.setAttr(faceControlsOffsetControl + '.tz', 0.25)

        # Create facial proxy joint control group.
        faceProxyJointControlsGroup = cmds.group(n = SERigNaming.sFaceProxyJointControlsGroup, em = 1)
        cmds.delete(cmds.pointConstraint(facialAttachPoint, faceProxyJointControlsGroup, mo = 0))
        cmds.parent(faceProxyJointControlsGroup, self.ControlsGrp)
        cmds.parentConstraint(facialAttachPoint, faceProxyJointControlsGroup, mo = 1)
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, faceProxyJointControlsGroup, SERigNaming.sFaceProxyControlGroupAttr, SERigNaming.sFaceProxyControlGroupOwnerAttr)

        # Create facial proxy joint control rivet group.
        faceProxyJointControlRivetsGroup = cmds.group(n = SERigNaming.sFaceProxyJointControlRivetsGroup, em = 1)
        cmds.delete(cmds.pointConstraint(facialAttachPoint, faceProxyJointControlRivetsGroup, mo = 0))
        cmds.parent(faceProxyJointControlRivetsGroup, self.RigPartsFixedGrp)
        cmds.makeIdentity(faceProxyJointControlRivetsGroup, apply = True, t = 1, r = 1, s = 1)
        cmds.setAttr(faceProxyJointControlRivetsGroup + '.it', 0)
        cmds.hide(faceProxyJointControlRivetsGroup)
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, faceProxyJointControlRivetsGroup, SERigNaming.sFaceProxyControlRivetGroupAttr, SERigNaming.sFaceProxyControlRivetGroupOwnerAttr)

        # Get input facial guide joints.
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
        leftEyelidUpperEndJoint = SEJointHelper.getFacialLeftEyelidUpperEndJoint(facialJoints)
        leftEyelidLowerEndJoint = SEJointHelper.getFacialLeftEyelidLowerEndJoint(facialJoints)
        rightEyelidUpperEndJoint = SEJointHelper.getFacialRightEyelidUpperEndJoint(facialJoints)
        rightEyelidLowerEndJoint = SEJointHelper.getFacialRightEyelidLowerEndJoint(facialJoints)

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

        # Lock jaw offset joint's motion. Later when jaw IK handle is created on jaw and jaw end joints, we don't want jaw offset joint rotate.
        lockAttrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
        for attr in lockAttrList:
            cmds.setAttr(jawOffsetJoint + '.' + attr, l = True)

        # Create data buffer group.
        self.DataBuffer = createFACS_DataBuffer(self.TopGrp)

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
        self.JawPosControl = jawPosControl

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
        self.JawMidPosControl = jawMidPosControl

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
        self.OnFaceIKJawControl = onFaceIKJawControl
        cmds.hide(onFaceIKJawControl.ControlGroup)

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
        self.OnFaceLipCloseControl = onFaceLipCloseControl

        onFaceLipCloseControlOffsetGrp = onFaceLipCloseControl.InsertNewGroup(groupName = onFaceLipCloseControl.Prefix + SERigNaming.sOffsetGroup)
        cmds.move(0.0, 2.0, 0.0, onFaceLipCloseControlOffsetGrp, r = 1, os = 1)
        cmds.transformLimits(onFaceLipCloseControl.ControlObject, ty = (0.0, 1.0), ety = (True, True))

        # For now, connect the control's ty to the data buffer attribute directly.
        dataBufferLipCloseAttr = getFacialActionUnitAttrName(self.DataBuffer, SERigEnum.eRigFacialActionUnitType.AU_LipClose)
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

        # Place left IK eye end joint via blocking sphere radius.
        leftEyeBSRadius = 2.0
        if cmds.objExists(SERigNaming.sLeftEyeBlockingSphere):
            leftEyeBSRadius = SEJointHelper.getEyeBlockingSphereRadius(SERigNaming.sLeftEyeBlockingSphere)
            cmds.parent(SERigNaming.sLeftEyeBlockingSphere, self.RigPartsGrp)
            cmds.parentConstraint(facialAttachPoint, SERigNaming.sLeftEyeBlockingSphere, mo = 1)
            cmds.hide(SERigNaming.sLeftEyeBlockingSphere)
        else:
            cmds.warning('Left eye blocking sphere not found.')

        cmds.setAttr(leftEyeEndIkJoint + '.translateX', leftEyeBSRadius)
        cmds.makeIdentity(leftEyeEndIkJoint, apply = True)
        cmds.setAttr(leftEyeEndIkJoint + '.radius', 0.5)

        # Create left eyeball rotation tracking logic.
        if cmds.objExists(SERigNaming.sLeftEyeBlockingSphere):
            createEyeballRotationTrackingLogic(SERigNaming.sLeftEyeBlockingSphere, leftEyeEndIkJoint, SERigEnum.eRigSide.RS_Left, self.DataBuffer)

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

        # Place right IK eye end joint via blocking sphere radius.
        rightEyeBSRadius = 2.0
        if cmds.objExists(SERigNaming.sRightEyeBlockingSphere):
            rightEyeBSRadius = SEJointHelper.getEyeBlockingSphereRadius(SERigNaming.sRightEyeBlockingSphere)
            cmds.parent(SERigNaming.sRightEyeBlockingSphere, self.RigPartsGrp)
            cmds.parentConstraint(facialAttachPoint, SERigNaming.sRightEyeBlockingSphere, mo = 1)
            cmds.hide(SERigNaming.sRightEyeBlockingSphere)
        else:
            cmds.warning('Right eye blocking sphere not found.')

        cmds.setAttr(rightEyeEndIkJoint + '.translateX', -rightEyeBSRadius)
        cmds.makeIdentity(rightEyeEndIkJoint, apply = True)
        cmds.setAttr(rightEyeEndIkJoint + '.radius', 0.5)

        # Create right eyeball rotation tracking logic.
        if cmds.objExists(SERigNaming.sRightEyeBlockingSphere):
            createEyeballRotationTrackingLogic(SERigNaming.sRightEyeBlockingSphere, rightEyeEndIkJoint, SERigEnum.eRigSide.RS_Right, self.DataBuffer)

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
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.EyesAimIKControl.ControlGroup, 'EyesAimControl', 'ControlOwner')

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
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, leftEyeIkControl.ControlGroup, 'OnFaceLeftEyeControl', 'ControlOwner')
        self.LeftEyeIkControl = leftEyeIkControl

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
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, rightEyeIkControl.ControlGroup, 'OnFaceRightEyeControl', 'ControlOwner')
        self.RightEyeIkControl = rightEyeIkControl

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

        # Create eyelid motion logic.
        createEyelidMotionLogic(self.DataBuffer, leftEyeJoint, rightEyeJoint, leftEyelidUpperJoint, rightEyelidUpperJoint, 
                                leftEyelidLowerJoint, rightEyelidLowerJoint)

        # Tagging facial base joints.
        facialBaseJnts = [jawOffsetJoint, lowerLipBlendJoint, upperLipBlendJoint, leftEyelidUpperEndJoint, leftEyelidLowerEndJoint, rightEyelidUpperEndJoint, rightEyelidLowerEndJoint]
        facialBaseNeckJnts = SEJointHelper.getBuilderNeckJoints()
        facialBaseNeckJnts = facialBaseNeckJnts[0:-1]  # Exclude facial root joint
        facialBaseJnts = facialBaseJnts + facialBaseNeckJnts
        for facialBaseJnt in facialBaseJnts:
            cmds.setAttr(facialBaseJnt + '.type', 18)
            cmds.setAttr(facialBaseJnt + '.otherType', SERigNaming.sJointTagFacialBase, type = 'string')

        self.GeneratedFacialBaseJoints.append(lowerLipBlendJoint)
        self.GeneratedFacialBaseJoints.append(upperLipBlendJoint)

        # Create FACS face controls logic.
        facialBuilderJoints = SEJointHelper.getFacialBuilderJoints()
        createFACS_FacialControlLogic(self.DataBuffer, facialBuilderJoints)

        # Create controls visibility expression.
        mainControl = SERigNaming.sMainControlPrefix + SERigNaming.sControl
        controlsVisEN = SERigNaming.sExpressionPrefix + self.Prefix + 'ControlsVis'
        tempExpressionTail = mainControl + '.' + SERigNaming.sFacialControlsVisibilityAttr + ';'
        controlsVisES = self.ControlsGrp + '.visibility = ' + tempExpressionTail
        cmds.expression(n = controlsVisEN, s = controlsVisES, ae = 1)

#-----------------------------------------------------------------------------
def createFacialSkinProxyJointsAndControlsFromSelection(deleteCageMesh = True, controlScale = 0.2):
    selected = cmds.ls(sl = True)
    if len(selected) != 2:
        cmds.error('Please select cage mesh and facial mesh.')
        return

    cageMesh = selected[0]
    facialMesh = selected[1]

    tx = cmds.getAttr(cageMesh + '.tx')
    ty = cmds.getAttr(cageMesh + '.ty')
    tz = cmds.getAttr(cageMesh + '.tz')
    rx = cmds.getAttr(cageMesh + '.rx')
    ry = cmds.getAttr(cageMesh + '.ry')
    rz = cmds.getAttr(cageMesh + '.rz')
    sx = cmds.getAttr(cageMesh + '.sx')
    sy = cmds.getAttr(cageMesh + '.sy')
    sz = cmds.getAttr(cageMesh + '.sz')

    cmds.setAttr(cageMesh + '.tx', 0.0)
    cmds.setAttr(cageMesh + '.ty', 0.0)
    cmds.setAttr(cageMesh + '.tz', 0.0)
    cmds.setAttr(cageMesh + '.rx', 0.0)
    cmds.setAttr(cageMesh + '.ry', 0.0)
    cmds.setAttr(cageMesh + '.rz', 0.0)
    cmds.setAttr(cageMesh + '.sx', 1.0)
    cmds.setAttr(cageMesh + '.sy', 1.0)
    cmds.setAttr(cageMesh + '.sz', 1.0)

    proxyJnts = SEJointHelper.createFacialSkinProxyJoints(cageMesh, facialMesh)

    if deleteCageMesh:
        cmds.delete(cageMesh)
    else:
        cmds.setAttr(cageMesh + '.tx', tx)
        cmds.setAttr(cageMesh + '.ty', ty)
        cmds.setAttr(cageMesh + '.tz', tz)
        cmds.setAttr(cageMesh + '.rx', rx)
        cmds.setAttr(cageMesh + '.ry', ry)
        cmds.setAttr(cageMesh + '.rz', rz)
        cmds.setAttr(cageMesh + '.sx', sx)
        cmds.setAttr(cageMesh + '.sy', sy)
        cmds.setAttr(cageMesh + '.sz', sz)

    # Delete old proxy joint controls.
    rigCharacterGroup = SERigObjectTypeHelper.findRelatedRigCharacterGroup(facialMesh)
    CharacterFacialComponent = SERigObjectTypeHelper.getCharacterFacialComponentGroup(rigCharacterGroup)
    proxyJointControlsGroup = SERigObjectTypeHelper.getFaceProxyJointControlsGroup(CharacterFacialComponent)
    proxyGroupChildren = cmds.listRelatives(proxyJointControlsGroup, c = True, type = 'transform')
    for child in proxyGroupChildren:
        if SERigObjectTypeHelper.isRigControlGroup(child):
            cmds.delete(child)
    
    # Create new proxy joint controls.
    controlIndex = 0
    for proxyJnt in proxyJnts:
        tempName = 'FaceProxy_' + str(controlIndex)
        proxyJointControl = SERigControl.RigSphereControl(
                                rigSide = SERigEnum.eRigSide.RS_Unknown,
                                rigType = SERigEnum.eRigType.RT_OnFaceProxy,
                                rigFacing = SERigEnum.eRigFacing.RF_Z,
                                rigControlIndex = controlIndex,
                                prefix = tempName, 
                                translateTo = proxyJnt,
                                rotateTo = proxyJnt,
                                scale = controlScale,
                                parent = proxyJointControlsGroup,
                                lockChannels = ['r', 's', 'v'],
                                overrideControlColor = True,
                                controlColor = (0.0, 0.0, 0.2)
                                )
        rivetDrvGroup = proxyJointControl.InsertNewGroup(tempName + '_Rivet' + SERigNaming.sDriverGroup)
        if rivetDrvGroup:
            SERigObjectTypeHelper.linkRigObjects(proxyJointControl.ControlGroup, rivetDrvGroup, SERigNaming.sFaceProxyControlRivetDriverGroupAttr, 
                SERigNaming.sFaceProxyControlRivetDriverGroupOwnerAttr)
        else:
            cmds.error('Failed linking rivet drive group for ' + proxyJointControl.ControlGroup)

        # Additional driver group reserved for animator.
        proxyJointControl.InsertNewGroup(tempName + SERigNaming.sDriverGroup)
        cmds.parentConstraint(proxyJointControl.ControlObject, proxyJnt, mo = 0)

        controlIndex += 1

    cmds.select(cl = True)
#-----------------------------------------------------------------------------
def createFacialProxyControlRivetConstraints(surfaceGeometry, rigCharacterGroup):
    CharacterFacialComponent = SERigObjectTypeHelper.getCharacterFacialComponentGroup(rigCharacterGroup)
    rivetsGroup = SERigObjectTypeHelper.getFaceProxyControlRivetsGroup(CharacterFacialComponent)
    
    # Possibly delete old rivets first.
    oldRivets = cmds.listRelatives(rivetsGroup, c = True)
    if oldRivets:
        cmds.warning('Deleting old face proxy control rivets.')
        for oldRivet in oldRivets:
            cmds.delete(oldRivet)

    # Create rivet constraints for face proxy joint controls.
    proxyJointControlsGroup = SERigObjectTypeHelper.getFaceProxyJointControlsGroup(CharacterFacialComponent)
    proxyGroupChildren = cmds.listRelatives(proxyJointControlsGroup, c = True, type = 'transform')
    for child in proxyGroupChildren:
        if SERigObjectTypeHelper.isRigControlGroup(child):
            rivetDriveGroup = SERigObjectTypeHelper.getFaceProxyControlRivetDriverGroup(child)
            if rivetDriveGroup:
                rc = SEConstraintHelper.createRivetConstraint(surfaceGeometry, rivetDriveGroup, hideChannels = ['t', 'r', 's'])
                if rc:
                    cmds.parent(rc, rivetsGroup)
                else:
                    cmds.warning('Failed creating rivet constraint for ' + child)

    print('Face proxy control rivets created, parenting them to facial rivets group.')
#-----------------------------------------------------------------------------