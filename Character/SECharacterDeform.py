import maya.cmds as cmds
import os

from ..Base import SERigNaming
from ..ThirdParty import bSkinSaver
from ..Utils import SEStringHelper

skinWeightsDir = 'Weights/SkinCluster'
skinWeightsExt = '.swt'

def build(baseRig, mainProjectPath, sceneScale = 1.0, twistJointParents = []):
    # Make twist joints.
    makeTwistJoints(baseRig, twistJointParents)

    # Load skin weights.

    # Apply mush deformer.

    # Wrap hi-res body mesh.

    pass

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