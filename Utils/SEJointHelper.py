import maya.cmds as cmds
import maya.OpenMaya as om
import pymel.core as pm

from ..Base import SERigEnum
from ..Base import SERigNaming
from . import SERigObjectTypeHelper

#-----------------------------------------------------------------------------
def findRelatedSkinCluster(skinObject):
    sc = pm.mel.findRelatedSkinCluster(skinObject)
    if sc != '':
        return sc
    return None
#-----------------------------------------------------------------------------
def selectSkinJointsFromSelectedSkinObject():
    res = cmds.ls(sl = 1)
    if len(res) > 0:
        sc = findRelatedSkinCluster(res[0])
        jnts = cmds.skinCluster(sc, q = 1, inf = 1)
        cmds.select(jnts, r = 1)
    else:
        cmds.warning('Please select a skin object.')
#-----------------------------------------------------------------------------
def listHierarchy(topJoint, withEndJoints = True):

    listedJoints = cmds.listRelatives(topJoint, type = 'joint', ad = True)
    listedJoints.append(topJoint)
    listedJoints.reverse()

    res = listedJoints[:]

    if not withEndJoints:
        res = [j for j in listedJoints if cmds.listRelatives(j, c = 1, type = 'joint')]

    return res
#-----------------------------------------------------------------------------
def duplicateHierarchy(topJoint, newPrefix = ''):

    res = []

    newJoints = cmds.duplicate(topJoint, n = newPrefix + topJoint, parentOnly = False, renameChildren = True)
    res.append(newJoints[0])
    for i in range(len(newJoints) - 1):
        oldName = newJoints[i + 1][:-1]
        newName = newPrefix + oldName
        cmds.rename(newJoints[i + 1], newName)
        res.append(newName)

    return res
#-----------------------------------------------------------------------------
def getJointSide(joint):

    token = joint.split('_')
    if token[0] == 'L' or token[0] == 'l':
        return SERigEnum.eRigSide.RS_Left
    elif token[0] == 'R' or token[0] == 'r':
        return SERigEnum.eRigSide.RS_Right
    elif token[0] == 'C' or token[0] == 'c':
        return SERigEnum.eRigSide.RS_Center
    else:
        return SERigEnum.eRigSide.RS_Unknown
#-----------------------------------------------------------------------------
def getFirstChildJoint(parent):

    # Find child joint.
    childJoint = None

    childJointList = cmds.listRelatives(parent, c = 1, type = 'joint')
    if childJointList != None:
        childJoint = childJointList[0]

    return childJoint
#-----------------------------------------------------------------------------
def getFirstChildGroup(parent):

    # Find child group.
    childGroup = None

    childGroupList = cmds.listRelatives(parent, c = 1, type = 'transform')
    if childGroupList != None:
        childGroup = childGroupList[0]

    return childGroup
#-----------------------------------------------------------------------------
def getFirstParentJoint(child):

    parentJoint = None
    parentJointList = cmds.listRelatives(child, p = 1, type = 'joint')
    if parentJointList == None:
        print('No parent joint found for:' + child)
    else:
        parentJoint = parentJointList[0]

    return parentJoint
#-----------------------------------------------------------------------------
def createNewParentJoint(child, alignNewParentToOldParent = False):
    newParent = None
    if cmds.objExists(child):
        oldParent = getFirstParentJoint(child)

        # Create a new parent for the child.
        newParent = cmds.createNode('joint', n = child + '_Par')
        if alignNewParentToOldParent and oldParent:
            cmds.delete(cmds.parentConstraint(oldParent, newParent, mo = 0))
        else:
            cmds.delete(cmds.parentConstraint(child, newParent, mo = 0))

        cmds.parent(child, newParent)
        cmds.makeIdentity(newParent, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        # Parent new parent to old parent.
        if oldParent:
            cmds.parent(newParent, oldParent)

    return newParent
#-----------------------------------------------------------------------------
def isZeroRotation(joint, epsilon = 0.0001):
    res = False

    if cmds.objExists(joint):
        rx = cmds.getAttr(joint + '.rotateX')
        ry = cmds.getAttr(joint + '.rotateY')
        rz = cmds.getAttr(joint + '.rotateZ')
        dx = abs(rx)
        dy = abs(ry)
        dz = abs(rz)

        if dx <= epsilon and dy <= epsilon and dz <= epsilon:
            res = True

    return res
#-----------------------------------------------------------------------------
def createJointAlongCurve(curve, jointCount = 2, jointName = ''):
    joints = []

    if cmds.objExists(curve):
        if jointCount < 2:
            jointCount = 2

        preParent = None
        for i in range(0, jointCount):
            cmds.select(cl = True)
            if jointName == '':
                curJoint = cmds.joint()
            else:
                curJoint = cmds.joint(n = jointName + str(i))
            motionPath = cmds.pathAnimation(curJoint, c = curve, fractionMode = True)
            cmds.cutKey(motionPath + '.u', time = ())
            cmds.setAttr(motionPath + '.u', i*(1.0/(jointCount - 1)))
            cmds.delete(curJoint + '.tx', icn = True)
            cmds.delete(curJoint + '.ty', icn = True)
            cmds.delete(curJoint + '.tz', icn = True)
            cmds.delete(motionPath)

            if preParent:
                cmds.parent(curJoint, preParent)

            preParent = curJoint
            joints.append(curJoint)

        cmds.joint(joints[0], e = True, oj = 'xyz', sao = 'yup', ch = True, zso = True)
    else:
        cmds.warning('Cannot find curve:' + curve)

    return joints
#-----------------------------------------------------------------------------
def adjustIKTwist(ikHandle, 
                  startJoint, 
                  startTwistValue = -270, 
                  endTwistValue = 270, 
                  twistValueStep = 90,
                  epsilon = 0.4):
    isZeroRot = isZeroRotation(startJoint, epsilon = epsilon)
    if isZeroRot:
        print('No need twisting IK value for: %s' % startJoint)
        return

    twistValues = range(startTwistValue, endTwistValue + twistValueStep, twistValueStep)
    for twistValue in twistValues:
        cmds.setAttr(ikHandle + '.twist', twistValue)
        isZeroRot = isZeroRotation(startJoint, epsilon = epsilon)
        if isZeroRot:
            print('Twisting IK value succeeded for: %s' % startJoint)
            break

    if isZeroRot == False:
        cmds.error('Twisting IK value failed for: %s' % startJoint)

#-----------------------------------------------------------------------------
def getFacialJoints():
    facialJnts = ['L_Eye',                 # 0
                  'R_Eye',                 # 1
                  'C_UpperTeeth',          # 2 
                  'L_EyelidUpper',         # 3
                  'L_EyelidLower',         # 4
                  'R_EyelidUpper',         # 5
                  'R_EyelidLower',         # 6
                  'C_Jaw',                 # 7
                  'C_JawOffset',           # 8
                  'C_JawEnd',              # 9
                  'C_LowerTeeth',          # 10
                  'C_LowerLipBegin',       # 11
                  'C_LowerLipEnd',         # 12
                  'C_UpperLipBegin',       # 13
                  'C_UpperLipEnd',         # 14
                  'L_EyelidUpperEnd',      # 15
                  'L_EyelidLowerEnd',      # 16
                  'R_EyelidUpperEnd',      # 17
                  'R_EyelidLowerEnd']      # 18

    return facialJnts
#-----------------------------------------------------------------------------
def getFacialJawJoint(facialJoints):
    jawJoint = facialJoints[7]
    return jawJoint
#-----------------------------------------------------------------------------
def getFacialJawOffsetJoint(facialJoints):
    jawOffsetJoint = facialJoints[8]
    return jawOffsetJoint
#-----------------------------------------------------------------------------
def getFacialLowerLipBeginJoint(facialJoints):
    lowerLipBeginJoint = facialJoints[11]
    return lowerLipBeginJoint
#-----------------------------------------------------------------------------
def getFacialLowerLipEndJoint(facialJoints):
    lowerLipEndJoint = facialJoints[12]
    return lowerLipEndJoint
#-----------------------------------------------------------------------------
def getFacialUpperLipBeginJoint(facialJoints):
    upperLipBeginJoint = facialJoints[13]
    return upperLipBeginJoint
#-----------------------------------------------------------------------------
def getFacialUpperLipEndJoint(facialJoints):
    upperLipEndJoint = facialJoints[14]
    return upperLipEndJoint
#-----------------------------------------------------------------------------
def getFacialLeftEyeJoint(facialJoints):
    leftEyeJoint = facialJoints[0]
    return leftEyeJoint
#-----------------------------------------------------------------------------
def getFacialLeftEyelidUpperJoint(facialJoints):
    leftEyelidUpperJoint = facialJoints[3]
    return leftEyelidUpperJoint
#-----------------------------------------------------------------------------
def getFacialLeftEyelidUpperEndJoint(facialJoints):
    leftEyelidUpperEndJoint = facialJoints[15]
    return leftEyelidUpperEndJoint
#-----------------------------------------------------------------------------
def getFacialLeftEyelidLowerJoint(facialJoints):
    leftEyelidLowerJoint = facialJoints[4]
    return leftEyelidLowerJoint
#-----------------------------------------------------------------------------
def getFacialLeftEyelidLowerEndJoint(facialJoints):
    leftEyelidLowerEndJoint = facialJoints[16]
    return leftEyelidLowerEndJoint
#-----------------------------------------------------------------------------
def getFacialRightEyeJoint(facialJoints):
    rightEyeJoint = facialJoints[1]
    return rightEyeJoint
#-----------------------------------------------------------------------------
def getFacialRightEyelidUpperJoint(facialJoints):
    rightEyelidUpperJoint = facialJoints[5]
    return rightEyelidUpperJoint
#-----------------------------------------------------------------------------
def getFacialRightEyelidUpperEndJoint(facialJoints):
    rightEyelidUpperEndJoint = facialJoints[17]
    return rightEyelidUpperEndJoint
#-----------------------------------------------------------------------------
def getFacialRightEyelidLowerJoint(facialJoints):
    rightEyelidLowerJoint = facialJoints[6]
    return rightEyelidLowerJoint
#-----------------------------------------------------------------------------
def getFacialRightEyelidLowerEndJoint(facialJoints):
    rightEyelidLowerEndJoint = facialJoints[18]
    return rightEyelidLowerEndJoint

#-----------------------------------------------------------------------------
def getBuilderSpineJoints():
    spineJnts = ['C_Pelvis', 'C_Spine_0', 'C_Spine_1', 'C_Spine_2', 'C_Spine_3', 'C_ChestBegin']
    return spineJnts
#-----------------------------------------------------------------------------
def getBuilderUpperChestJoints():
    upperChestJnts = ['L_Clav', 'R_Clav', 'C_ChestEnd', 'L_Breast', 'R_Breast']
    return upperChestJnts
#-----------------------------------------------------------------------------
def getBuilderChestEndJoint():
    return ['C_ChestEnd']
#-----------------------------------------------------------------------------
def getSlaveChestEndJoint():
    builderJnt = getBuilderChestEndJoint()[0]
    slaveJnt = SERigNaming.sSlavePrefix + builderJnt
    return [slaveJnt]
#-----------------------------------------------------------------------------
def getBuilderBreastJoints():
    return ['L_Breast', 'R_Breast']
#-----------------------------------------------------------------------------
def getSlaveBreastJoints():
    slaveJnts = []

    builderJnts = getBuilderBreastJoints()
    for jnt in builderJnts:
        slaveJnt = SERigNaming.sSlavePrefix + jnt
        slaveJnts.append(slaveJnt)

    return slaveJnts
#-----------------------------------------------------------------------------
def getBuilderLeftLegJoints():
    leftLegJnts = ['L_Hip', 'L_Knee', 'L_Ankle', 'L_Ball', 'L_Toe']
    return leftLegJnts
#-----------------------------------------------------------------------------
def getBuilderRightLegJoints():
    rightLegJnts = ['R_Hip', 'R_Knee', 'R_Ankle', 'R_Ball', 'R_Toe']
    return rightLegJnts
#-----------------------------------------------------------------------------
def getBuilderLeftArmJoints():
    leftArmJnts = ['L_Shoulder', 'L_Elbow', 'L_Wrist']
    return leftArmJnts
#-----------------------------------------------------------------------------
def getBuilderRightArmJoints():
    rightArmJnts = ['R_Shoulder', 'R_Elbow', 'R_Wrist']
    return rightArmJnts
#-----------------------------------------------------------------------------
def getBuilderLeftHandJoints():
    leftHandJnts = ['L_Thumb_0', 'L_Index_0', 'L_Middle_0', 'L_Ring_0', 'L_Pinky_0']
    return leftHandJnts
#-----------------------------------------------------------------------------
def getBuilderRightHandJoints():
    rightHandJnts = ['R_Thumb_0', 'R_Index_0', 'R_Middle_0', 'R_Ring_0', 'R_Pinky_0']
    return rightHandJnts
#-----------------------------------------------------------------------------
def getBuilderNeckJoints():
    neckJnts = ['C_Neck_0', 'C_Neck_1', 'C_Head', 'C_FacialRoot']
    return neckJnts
#-----------------------------------------------------------------------------
def getBuilderUpperBodyUpperLimbJoints():
    upperBodyUpperLimbJoints = ['L_Shoulder', 'R_Shoulder']
    return upperBodyUpperLimbJoints
#-----------------------------------------------------------------------------
def getBuilderUpperBodyLowerLimbJoints():
    upperBodyLowerLimbJoints = ['L_Elbow', 'R_Elbow']
    return upperBodyLowerLimbJoints
#-----------------------------------------------------------------------------
def getBuilderLowerBodyUpperLimbJoints():
    lowerBodyUpperLimbJoints = ['L_Hip', 'R_Hip']
    return lowerBodyUpperLimbJoints
#-----------------------------------------------------------------------------
def getBuilderLowerBodyLowerLimbJoints():
    lowerBodyLowerLimbJoints = ['L_Knee', 'R_Knee']
    return lowerBodyLowerLimbJoints
#-----------------------------------------------------------------------------
def jointAddTag(jnt, tag):
    labelType = cmds.getAttr(jnt + '.type')
    if labelType != 18:
        cmds.setAttr(jnt + '.type', 18)
        cmds.setAttr(jnt + '.otherType', tag, type = 'string')
        return

    jntTags = cmds.getAttr(jnt + '.otherType')
    tagExist = jntTags.find(tag)

    if tagExist == -1:
        if len(jntTags) > 0:
            jntTags = jntTags + SERigNaming.sTagSeparator + tag
        else:
            jntTags = tag
        cmds.setAttr(jnt + '.otherType', jntTags, type = 'string')
    else:
        cmds.warning('Tag already exists.')
#-----------------------------------------------------------------------------
def jointRemoveTag(jnt, tag):
    labelType = cmds.getAttr(jnt + '.type')
    if labelType != 18:
        cmds.warning('Joint label type is not custom tag type.')
        return

    jntTags = cmds.getAttr(jnt + '.otherType')
    tagExist = jntTags.find(tag)
    if tagExist == -1:
        cmds.warning('Tag does not exist.')

    curTags = jntTags.split(SERigNaming.sTagSeparator)
    newTags = []
    
    for curTag in curTags:
        if curTag != tag:
            newTags.append(curTag)
        
    jntTags = ''
    if len(newTags) > 0:
        for i in range(len(newTags) - 1):
            jntTags = jntTags + newTags[i] + SERigNaming.sTagSeparator
        jntTags += newTags[-1]

    cmds.setAttr(jnt + '.otherType', jntTags, type = 'string')
#-----------------------------------------------------------------------------
def jointHasTag(jnt, tag):
    jntTags = cmds.getAttr(jnt + '.otherType')
    if jntTags.find(tag) >= 0:
        return True
        
    return False
#-----------------------------------------------------------------------------
def isBodyDeformationJoint(jnt, includeBreast = False, includeNeckMuscle = False, includeLimeEnd = False, includeChestEnd = False):
    res = True

    jntTag = cmds.getAttr(jnt + '.otherType')

    if jntTag == SERigNaming.sJointTagSlaveRoot:
        res = False

    elif jntTag == SERigNaming.sJointTagFacialRoot:
        res = False

    elif jntTag == SERigNaming.sJointTagFacialBase:
        res = False
    
    elif jntTag == SERigNaming.sJointTagSlaveBreast and includeBreast == False:
        res = False

    elif jntTag == SERigNaming.sJointTagSlaveChestEnd and includeChestEnd == False:
        res = False

    elif (jntTag == SERigNaming.sJointTagSlaveToeEnd or jntTag == SERigNaming.sJointTagSlaveFingerEnd) and includeLimeEnd == False:
        res = False

    elif jntTag == SERigNaming.sJointTagSlaveNeckMuscle and includeNeckMuscle == False:
        res = False

    return res
#-----------------------------------------------------------------------------
def isFacialBaseJoint(jnt):
    return jointHasTag(jnt, SERigNaming.sJointTagFacialBase)
#-----------------------------------------------------------------------------
def getSelectedRigCharacterGroup():
    # Get selected rig character.
    selected = cmds.ls(sl = True)
    if selected:
        selected = selected[0]
    else:
        cmds.warning('Please select a rig character top group.')
        return None

    characterGroup = ''
    if SERigObjectTypeHelper.isRigCharacterGroup(selected):
        characterGroup = selected
    else:
        cmds.warning('Please select a rig character top group.')
        return None

    return characterGroup
#-----------------------------------------------------------------------------
def getBodyDeformationJoints(includeBreast = False, includeNeckMuscle = False, includeLimeEnd = False, includeChestEnd = False):
    characterGroup = getSelectedRigCharacterGroup()
    if characterGroup == None:
        return None

    # Get deformation joints from deformation group based on specific rules passed in to the function.
    deformationGrp = SERigObjectTypeHelper.getCharacterDeformationGroup(characterGroup)
    if deformationGrp:
        slaveJoints = cmds.listRelatives(deformationGrp, type = 'joint', ad = True)
        deformationJoints = []

        for jnt in slaveJoints:
            res = isBodyDeformationJoint(jnt, includeBreast, includeNeckMuscle, includeLimeEnd, includeChestEnd)
            if  res == True:
                deformationJoints.append(jnt)

        return deformationJoints

    else:
        cmds.warning('Deformation group not found.')
        return None
#-----------------------------------------------------------------------------
def getFacialBaseJoints():
    characterGroup = getSelectedRigCharacterGroup()
    if characterGroup == None:
        cmds.warning('Character group not found.')
        return None

    masterJointsGrp = SERigObjectTypeHelper.getCharacterMasterJointsGroup(characterGroup)
    if masterJointsGrp:
        masterJoints = cmds.listRelatives(masterJointsGrp, type = 'joint', ad = True)
        facialBaseJoints = []

        for jnt in masterJoints:
            res = isFacialBaseJoint(jnt)
            if  res == True:
                facialBaseJoints.append(jnt)

        return facialBaseJoints

    else:
        cmds.warning('Master joints group not found.')
        return None        
#-----------------------------------------------------------------------------
def getSlaveFacialRootJoint(characterGroup):
    slaveJointsGrp = SERigObjectTypeHelper.getCharacterDeformationGroup(characterGroup)
    if slaveJointsGrp:
        slaveJoints = cmds.listRelatives(slaveJointsGrp, type = 'joint', ad = True)
        for slaveJoint in slaveJoints:
            if jointHasTag(slaveJoint, SERigNaming.sJointTagFacialRoot):
                return slaveJoint

    cmds.warning('Slave joints group not found.')
    return None
#-----------------------------------------------------------------------------
def getEyeBlockingSphereRadius(blockingSphere):
    shapeBB = cmds.exactWorldBoundingBox(blockingSphere)
    shapeSizeX = (shapeBB[3] - shapeBB[0]) * 0.5
    return shapeSizeX
#-----------------------------------------------------------------------------
def createJointRotationRemapping(joint, suffix, channel, input0 = 0, output0 = 0, input1 = 1, output1 = 1):
    remappingNode = None

    if cmds.objExists(joint):
        nodeName = joint + '_' + channel + suffix
        if cmds.objExists(nodeName):
            cmds.warning('Joint rotation remapping node already created.')
            return nodeName

        remappingNode = cmds.createNode('animCurveUU', n = nodeName)
        cmds.setKeyframe(remappingNode, float = input0, value = output0, itt = 'linear', ott = 'linear')
        cmds.setKeyframe(remappingNode, float = input1, value = output1, itt = 'linear', ott = 'linear')
        cmds.keyTangent(remappingNode, weightedTangents = False)

        cmds.connectAttr(joint + '.' + channel, remappingNode + '.input', f = 1)

    else:
        cmds.warning('Joint not found.')

    return remappingNode
#-----------------------------------------------------------------------------
def getMeshVertices(mesh):
    cmds.select(cl = True)
    om.MGlobal.selectByName(mesh)
    sList = om.MSelectionList()

    om.MGlobal.getActiveSelectionList(sList)
    item = om.MDagPath()
    sList.getDagPath(0, item)
    item.extendToShape()

    fnMesh = om.MFnMesh(item)

    vertices = om.MPointArray()
    fnMesh.getPoints(vertices, om.MSpace.kObject)
    return vertices
#-----------------------------------------------------------------------------
def createFacialSkinProxyJoints(cageMesh, facialMesh):
    if not cmds.objExists(cageMesh) or not cmds.objExists(facialMesh):
        cmds.error('Cage mesh or facial mesh does not exist.')
        return

    rigCharacterGroup = SERigObjectTypeHelper.findRelatedRigCharacterGroup(facialMesh)
    if rigCharacterGroup == None:
        cmds.error('Facial mesh does not belong to a character rig.')
        return

    facialRootJoint = getSlaveFacialRootJoint(rigCharacterGroup)
    if facialRootJoint == None:
        cmds.error('Slave facial root joint not found.')
        return

    # Possibly remove the skin cluster and related skin joints if the facial mesh is skinned.
    facialMeshSC = findRelatedSkinCluster(facialMesh)
    if facialMeshSC:
        cmds.warning('Facial mesh already skinned, removing old skin cluster and deleting old influence joints.')
        jnts = cmds.skinCluster(facialMeshSC, q = 1, inf = 1)
        cmds.skinCluster(facialMesh, e = True, ub = True)
        cmds.delete(jnts)

    vertices = getMeshVertices(cageMesh)
    proxyJnts = []
    for i in range(vertices.length()):
        proxyJnt = cmds.createNode('joint', n = SERigNaming.sFacialProxyJointPrefix + str(i))
        proxyJnts.append(proxyJnt)
        
        # Tagging facial skin proxy joints.
        jointAddTag(proxyJnt, SERigNaming.sJointTagFacialProxy)
        cmds.setAttr(proxyJnt + '.radius', 0.35)

        # Moving proxy joints in position.
        cmds.setAttr(proxyJnt + '.tx', vertices[i].x)
        cmds.setAttr(proxyJnt + '.ty', vertices[i].y)
        cmds.setAttr(proxyJnt + '.tz', vertices[i].z)

    cmds.parent(proxyJnts, facialRootJoint)
    cmds.makeIdentity(proxyJnts, apply = True)

    # Create a one-to-one influence relationship between cage mesh vertices and skin proxy joints. 
    cageMeshSC = cmds.skinCluster(proxyJnts, cageMesh, toSelectedBones = True, skinMethod = 0, normalizeWeights = 2, maximumInfluences = 1)[0]

    # Bind skin proxy joints to facial mesh.
    facialMeshSC = cmds.skinCluster(proxyJnts, facialMesh, toSelectedBones = True, skinMethod = 0, normalizeWeights = 2, maximumInfluences = 4)[0]

    # Query mesh current uv set.
    cageMeshCurUVSet = cmds.polyUVSet(cageMesh, query = True, currentUVSet = True)[0]
    facialMeshCurUVSet = cmds.polyUVSet(facialMesh, query = True, currentUVSet = True)[0]

    # Transfer cage mesh's skin weights to facial mesh based on their current uv sets.
    cmds.copySkinWeights(ss = cageMeshSC, ds = facialMeshSC, noMirror = True, surfaceAssociation = 'closestPoint', 
        uvSpace = (cageMeshCurUVSet, facialMeshCurUVSet), influenceAssociation = 'closestJoint', normalize = True)

    # We have done skin weights transfer, unbind cage mesh's skin.
    cmds.skinCluster(cageMesh, e = True, ub = True)
#-----------------------------------------------------------------------------
def createFacialSkinProxyJointsFromSelection(deleteCageMesh = True):
    selected = cmds.ls(sl = True)
    if len(selected) != 2:
        cmds.error('Please select cage mesh and facial mesh.')
        return

    cageMesh = selected[0]
    facialMesh = selected[1]

    cmds.setAttr(cageMesh + '.tx', 0.0)
    cmds.setAttr(cageMesh + '.ty', 0.0)
    cmds.setAttr(cageMesh + '.tz', 0.0)
    cmds.setAttr(cageMesh + '.rx', 0.0)
    cmds.setAttr(cageMesh + '.ry', 0.0)
    cmds.setAttr(cageMesh + '.rz', 0.0)
    cmds.setAttr(cageMesh + '.sx', 1.0)
    cmds.setAttr(cageMesh + '.sy', 1.0)
    cmds.setAttr(cageMesh + '.sz', 1.0)    

    createFacialSkinProxyJoints(cageMesh, facialMesh)

    if deleteCageMesh:
        cmds.delete(cageMesh)
    
#-----------------------------------------------------------------------------