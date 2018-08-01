import maya.cmds as cmds
import os

from ..Base import SERigNaming
from ..ThirdParty import bSkinSaver
from ..Utils import SEStringHelper
from ..Utils import SEMathHelper

skinWeightsDir = 'Weights/SkinCluster'
skinWeightsExt = '.swt'

def build(baseRig, mainProjectPath, sceneScale = 1.0, upperLimbJoints = []):
    # Make twist joints.
    #makeTwistJoints(baseRig, twistJointParents)
    #for i in upperLimbJoints:
    createUpperLimbTwistJoints(baseRig, 'L_Shoulder')

    # Load skin weights.

    # Apply mush deformer.

    # Wrap hi-res body mesh.

def createUpperLimbTwistJoints(baseRig, upperLimbJoint, twistJointRadiusScale = 4.0, knobCount = 2, maxKnobCount = 5):
    if baseRig == None or upperLimbJoint == None:
        print('Unable to make upper limb twist joints.')
        return

    prefix = upperLimbJoint

    # Find child joint.
    childJointList = cmds.listRelatives(upperLimbJoint, c = 1, type = 'joint')
    if childJointList == None:
        print('No child joint found for upper limb:' + upperLimbJoint)
        return
    childJoint = childJointList[0]

    # Find parent joint.
    parentJoint = None
    parentJointList = cmds.listRelatives(upperLimbJoint, p = 1, type = 'joint')
    if parentJointList == None:
        print('No parent joint found for upper limb:' + upperLimbJoint)
    else:
        parentJoint = parentJointList[0]

    # Create twist end joints.
    twistBeginJoint = cmds.duplicate(upperLimbJoint, n = prefix + SERigNaming.s_TwistBegin, parentOnly = True)[0]
    twistEndJoint = cmds.duplicate(upperLimbJoint, n = prefix + SERigNaming.s_TwistEnd, parentOnly = True)[0]
    cmds.delete(cmds.pointConstraint(childJoint, twistEndJoint))

    # Adjust twist end joints.
    origJntRadius = cmds.getAttr(upperLimbJoint + '.radius')

    # Set new radius and color for twist end joints.
    for i in [twistBeginJoint, twistEndJoint]:
        cmds.setAttr(i + '.radius', origJntRadius * twistJointRadiusScale)
        cmds.color(i, ud = 1)

    # Parent twist end joints.
    cmds.parent(twistEndJoint, twistBeginJoint)

    # Create single chain IK.
    twistIK = cmds.ikHandle(n = prefix + SERigNaming.s_TwistIKHandle, sol = 'ikSCsolver', sj = twistBeginJoint, ee = twistEndJoint)[0]
    cmds.hide(twistIK)
    cmds.pointConstraint(childJoint, twistIK)

    if parentJoint:
        cmds.parent(twistIK, parentJoint)

    # Create twist knobs.
    if knobCount > 0 and knobCount < maxKnobCount:
        twistBeginJointPos = SEMathHelper.getWorldPosition(twistBeginJoint)
        twistEndJointPos = SEMathHelper.getWorldPosition(twistEndJoint)
        
        distance = SEMathHelper.getDistance3(twistBeginJointPos, twistEndJointPos)
        delta = distance / (knobCount + 1)

        for j in range(1, knobCount + 1):
            knobJoint = cmds.duplicate(upperLimbJoint, n = prefix + SERigNaming.s_TwistKnob + str(j), parentOnly = True)[0]
            cmds.parent(knobJoint, upperLimbJoint)
            cmds.setAttr(knobJoint + '.tx', delta*j)
            cmds.setAttr(knobJoint + '.radius', origJntRadius * twistJointRadiusScale)
            cmds.color(knobJoint, ud = 1)
            

def makeTwistJoints(baseRig, parentJoints, twistJointRadiusScale = 2.0):
    if baseRig == None or len(parentJoints) == 0:
        print('Unable to make twist joints.')
        return

    twistJointsMainGrp = cmds.group(n = SERigNaming.sTwistJointsGroup, p = baseRig.JointsGrp, em = 1)
    
    for parentJnt in parentJoints:
        #prefix = SEStringHelper.SE_RemoveSuffix(parentJnt)
        #prefix = prefix[:-1]
        prefix = parentJnt
        childJnt = cmds.listRelatives(parentJnt, c = 1, type = 'joint')[0]

        # Make twist joints.
        twistJntGrp = cmds.group(n = prefix + SERigNaming.s_TwistJointsGroup, p = twistJointsMainGrp, em = 1)

        twistParentJnt = cmds.duplicate(parentJnt, n = prefix + '_Twist1_jnt', parentOnly = True)[0]
        twistChildJnt = cmds.duplicate(childJnt, n = prefix + '_Twist2_jnt', parentOnly = True)[0]

        # Adjust twist joints.
        origJntRadius = cmds.getAttr(parentJnt + '.radius')
        print origJntRadius

        # Set new radius and color for twist joints.
        for j in [twistParentJnt, twistChildJnt]:
            cmds.setAttr(j + '.radius', origJntRadius * twistJointRadiusScale)
            cmds.color(j, ud = 1)

        # Parent twist joints.
        cmds.parent(twistChildJnt, twistParentJnt)
        cmds.parent(twistParentJnt, twistJntGrp)

        # Attach twist joints.
        cmds.pointConstraint(parentJnt, twistParentJnt)

        # Make single chain IK.
        twistIK = cmds.ikHandle(n = prefix + '_TwistJoint_ikh', sol = 'ikSCsolver', sj = twistParentJnt, ee = twistChildJnt)[0]
        cmds.hide(twistIK)
        cmds.parent(twistIK, twistJntGrp)
        cmds.parentConstraint(childJnt, twistIK)





def saveSkinWeights(characterName, mainProjectPath, geoList = []):
    for obj in geoList:
        # Weights file path.
        weightFilePath = os.path.join(mainProjectPath, characterName, skinWeightsDir, obj + skinWeightsExt)

        # Save skin weights.
        cmds.select(obj)
        bSkinSaver.bSaveSkinValues(weightFilePath)

def loadSkinWeights(characterName, mainProjectPath, geoList = []):
    # Get weight file paths.
    weightFileDir = os.path.join(mainProjectPath, characterName, skinWeightsDir)
    weightFiles = os.listdir(weightFileDir)

    # Load skin weights.
    for weightFile in weightFiles:
        extRes = os.path.splitext(weightFile)

        # Check extension format.
        if not extRes > 1:
            continue

        # Check skin weight file.
        if not extRes[1] == skinWeightsExt:
            continue

        # Check geometry list.
        if geoList and not extRes[0] in geoList:
            continue

        # Check if the object exists.
        if not cmds.objExists(extRes[0]):
            continue

        weightFileFullPath = os.path.join(weightFileDir, weightFile)
        bSkinSaver.bLoadSkinValues(loadOnSelection = False, inputFile = weightFileFullPath)