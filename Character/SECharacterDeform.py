import maya.cmds as cmds
import maya.mel as mel
import os

from ..Base import SERigNaming
from ..Base import SERigEnum
from ..ThirdParty import bSkinSaver
from ..Utils import SEStringHelper
from ..Utils import SEMathHelper
from ..Utils import SEJointHelper

skinWeightsDir = 'Weights/SkinCluster'
skinWeightsExt = '.swt'

def createUpperLimbSlaveJoints(upperLimbSlaveMasterJnts = [], lowerLimbTopJoint = ''):

    slaveJnts = []

    preParent = None
    for masterJnt in upperLimbSlaveMasterJnts:

        cmds.select(cl = 1)
        curSlaveJoint = cmds.joint(n = SERigNaming.sSlavePrefix + masterJnt)
        cmds.delete(cmds.parentConstraint(masterJnt, curSlaveJoint, mo = 0))
        cmds.makeIdentity(curSlaveJoint, apply = True)
        
        pc = cmds.pointConstraint(masterJnt, curSlaveJoint, mo = 0)
        oc = cmds.orientConstraint(masterJnt, curSlaveJoint, mo = 0)

        curSlaveJntsInfo = (curSlaveJoint, pc, oc)
        slaveJnts.append(curSlaveJntsInfo)

        if preParent:
            cmds.parent(curSlaveJoint, preParent)
        preParent = curSlaveJoint

    if len(slaveJnts) > 1:
        cmds.delete(slaveJnts[-1][1])

        if cmds.objExists(lowerLimbTopJoint):
            cmds.pointConstraint(lowerLimbTopJoint, slaveJnts[-1][0], mo = 0)

    return slaveJnts

def createSlaveJointsHelper(masterJnts = []):

    slaveJnts = []

    preParent = None
    for masterJnt in masterJnts:

        cmds.select(cl = 1)
        curSlaveJoint = cmds.joint(n = SERigNaming.sSlavePrefix + masterJnt)
        cmds.delete(cmds.parentConstraint(masterJnt, curSlaveJoint, mo = 0))
        cmds.makeIdentity(curSlaveJoint, apply = True)
        
        pc = cmds.pointConstraint(masterJnt, curSlaveJoint, mo = 0)
        oc = cmds.orientConstraint(masterJnt, curSlaveJoint, mo = 0)

        curSlaveJntsInfo = (curSlaveJoint, pc, oc)
        slaveJnts.append(curSlaveJntsInfo)

        if preParent:
            cmds.parent(curSlaveJoint, preParent)
        preParent = curSlaveJoint

    return slaveJnts

def createSlaveJointsHelperNoHierarchy(masterJnts = []):

    slaveJnts = []

    for masterJnt in masterJnts:

        cmds.select(cl = 1)
        curSlaveJoint = cmds.joint(n = SERigNaming.sSlavePrefix + masterJnt)
        cmds.delete(cmds.parentConstraint(masterJnt, curSlaveJoint, mo = 0))
        cmds.makeIdentity(curSlaveJoint, apply = True)
        
        pc = cmds.pointConstraint(masterJnt, curSlaveJoint, mo = 0)
        oc = cmds.orientConstraint(masterJnt, curSlaveJoint, mo = 0)

        curSlaveJntsInfo = (curSlaveJoint, pc, oc)
        slaveJnts.append(curSlaveJntsInfo)

    return slaveJnts

def build(
          baseRig, 
          mainProjectPath, 
          sceneScale = 1.0,
          loadSkinWeights = False,
          applyDeltaMushDeformer = False,
          deltaMushGeometry = '',
          applyWrapDeformer = False,
          wrappedObjects = [],
          wrapperObject = '',
          upperBodyUpperLimbKnobCount = 2, 
          upperBodyLowerLimbKnobCount = 2,
          lowerBodyUpperLimbKnobCount = 2,
          lowerBodyLowerLimbKnobCount = 1,
          upperBodyUpperLimbJoints = [],
          upperBodyLowerLimbJoints = [],
          lowerBodyUpperLimbJoints = [],
          lowerBodyLowerLimbJoints = [],
          spineJnts = [],
          upperChestJnts = [],
          leftLegJnts = [],
          rightLegJnts = [],
          leftFootHelperJoints = [],
          rightFootHelperJoints = [],
          leftArmJnts = [],
          rightArmJnts = [],
          leftHandJnts = [],
          rightHandJnts = [],
          neckJnts = [],
          facialJnts = [],
          rootJnt = ''
          ):

    # Create twist joints for all the limbs.
    upperBodyUpperLimbSlaveMasterJnts = []
    for i in upperBodyUpperLimbJoints:
        curUpperLimbSlaveMasterJnts = createUpperLimbTwistJoints(baseRig, i, knobCount = upperBodyUpperLimbKnobCount)
        upperBodyUpperLimbSlaveMasterJnts.append(curUpperLimbSlaveMasterJnts)

    upperBodyLowerLimbSlaveMasterJnts = []
    for i in upperBodyLowerLimbJoints:
        curLowerLimbSlaveMasterJnts = createLowerLimbTwistJoints(baseRig, i, knobCount = upperBodyLowerLimbKnobCount)
        upperBodyLowerLimbSlaveMasterJnts.append(curLowerLimbSlaveMasterJnts)

    lowerBodyUpperLimbSlaveMasterJnts = []
    for i in lowerBodyUpperLimbJoints:
        curUpperLimbSlaveMasterJnts = createUpperLimbTwistJoints(baseRig, i, twistJointRadiusScale = 2.0, knobCount = lowerBodyUpperLimbKnobCount)
        lowerBodyUpperLimbSlaveMasterJnts.append(curUpperLimbSlaveMasterJnts)

    lowerBodyLowerLimbSlaveMasterJnts = []
    for i in lowerBodyLowerLimbJoints:
        curLowerLimbSlaveMasterJnts = createLowerLimbTwistJoints(baseRig, i, twistJointRadiusScale = 2.0, knobCount = lowerBodyLowerLimbKnobCount)
        lowerBodyLowerLimbSlaveMasterJnts.append(curLowerLimbSlaveMasterJnts)

    # Create slave joints.

    # Create arm slaves.
    leftUpperArmSlaveJnts = createUpperLimbSlaveJoints(upperBodyUpperLimbSlaveMasterJnts[0], upperBodyLowerLimbSlaveMasterJnts[0][0])
    rightUpperArmSlaveJnts = createUpperLimbSlaveJoints(upperBodyUpperLimbSlaveMasterJnts[1], upperBodyLowerLimbSlaveMasterJnts[1][0])
    leftLowerArmSlaveJnts = createSlaveJointsHelper(upperBodyLowerLimbSlaveMasterJnts[0])
    rightLowerArmSlaveJnts = createSlaveJointsHelper(upperBodyLowerLimbSlaveMasterJnts[1])

    cmds.parent(leftLowerArmSlaveJnts[0][0], leftUpperArmSlaveJnts[-1][0])
    cmds.parent(rightLowerArmSlaveJnts[0][0], rightUpperArmSlaveJnts[-1][0])

    # Create hand slaves and parent them to the arm slaves.
    leftHandSlaveJnts = []
    for fingerTopJoint in leftHandJnts:
        curFingerMasterJnts = SEJointHelper.listHierarchy(fingerTopJoint)
        curFingerSlaveJnts = createSlaveJointsHelper(curFingerMasterJnts)
        cmds.parent(curFingerSlaveJnts[0][0], leftLowerArmSlaveJnts[-1][0])

    rightHandSlaveJnts = []
    for fingerTopJoint in rightHandJnts:
        curFingerMasterJnts = SEJointHelper.listHierarchy(fingerTopJoint)
        curFingerSlaveJnts = createSlaveJointsHelper(curFingerMasterJnts)
        cmds.parent(curFingerSlaveJnts[0][0], rightLowerArmSlaveJnts[-1][0])

    # Create leg slaves.
    leftUpperLegSlaveJnts = createUpperLimbSlaveJoints(lowerBodyUpperLimbSlaveMasterJnts[0], lowerBodyLowerLimbSlaveMasterJnts[0][0])
    rightUpperLegSlaveJnts = createUpperLimbSlaveJoints(lowerBodyUpperLimbSlaveMasterJnts[1], lowerBodyLowerLimbSlaveMasterJnts[1][0])
    leftLowerLegSlaveJnts = createSlaveJointsHelper(lowerBodyLowerLimbSlaveMasterJnts[0])
    rightLowerLegSlaveJnts = createSlaveJointsHelper(lowerBodyLowerLimbSlaveMasterJnts[1])

    # Parent leg slaves to spine.
    cmds.parent(leftLowerLegSlaveJnts[0][0], leftUpperLegSlaveJnts[-1][0])
    cmds.parent(rightLowerLegSlaveJnts[0][0], rightUpperLegSlaveJnts[-1][0])

    # Create spine slaves.
    spineSlaveJnts = createSlaveJointsHelper(spineJnts)

    cmds.parent(leftUpperLegSlaveJnts[0][0], spineSlaveJnts[0][0])
    cmds.parent(rightUpperLegSlaveJnts[0][0], spineSlaveJnts[0][0])

    # Create neck slaves and parent them to the spine slave.
    neckSlaveJnts = createSlaveJointsHelper(neckJnts)

    cmds.parent(neckSlaveJnts[0][0], spineSlaveJnts[-1][0])

    # Create facial slaves and parent them to the neck slave.
    facialSlaveJnts = createSlaveJointsHelperNoHierarchy(facialJnts)

    for facialSlaveJoint in facialSlaveJnts:
        cmds.parent(facialSlaveJoint[0], neckSlaveJnts[-1][0])

    # Create upper chest slaves and parent them to the spine.
    upperChestSlaveJnts = createSlaveJointsHelperNoHierarchy(upperChestJnts)
    for upperChestSlaveJointInfo in upperChestSlaveJnts:
        cmds.parent(upperChestSlaveJointInfo[0], spineSlaveJnts[-1][0])

    # Parent arm slaves to upper chest slaves.
    cmds.parent(leftUpperArmSlaveJnts[0][0], upperChestSlaveJnts[0][0])
    cmds.parent(rightUpperArmSlaveJnts[0][0], upperChestSlaveJnts[1][0])

    # Create foot slaves and parent them to the leg slaves.
    leftFootJnts = leftLegJnts[3:]
    leftFootSlaveJnts = createSlaveJointsHelper(leftFootJnts)
    
    rightFootJnts = rightLegJnts[3:]
    rightFootSlaveJnts = createSlaveJointsHelper(rightFootJnts)

    cmds.parent(leftFootSlaveJnts[0][0], leftLowerLegSlaveJnts[-1][0])
    cmds.parent(rightFootSlaveJnts[0][0], rightLowerLegSlaveJnts[-1][0])


    # Load skin weights.
    if loadSkinWeights:
        geoList = _getModelGeoObjects(baseRig.ModelGrp)
        loadSkinWeights(baseRig.getCharacterName(), mainProjectPath, geoList)

    # Apply delta mush deformer.
    if applyDeltaMushDeformer:
        _applyDeltaMush(deltaMushGeometry)

    # Wrap hi-res body mesh.
    if applyWrapDeformer:
        _applyWrapDeformer(wrappedObjects, wrapperObject)

def _applyDeltaMush(geometry):
    res = cmds.deltaMush(geometry, smoothingIterations = 50)[0]
    return res

def _applyWrapDeformer(wrappedObjects, wrapperObject):
    cmds.select(wrappedObjects)
    cmds.select(wrapperObject, add = 1)
    mel.eval('doWrapArgList "7" { "1", "0", "1", "2", "1", "1", "0", "0" }')

def _getModelGeoObjects(modelGrp):
    res = [cmds.listRelatives(shape, p = 1)[0] for shape in cmds.listRelatives(modelGrp, ad = 1, type = 'mesh')]
    return res

def createUpperLimbTwistJoints(
                               baseRig, 
                               upperLimbJoint, 
                               twistJointRadiusScale = 4.0, 
                               knobCount = 2, 
                               maxKnobCount = 5
                               ):
    # If this function succeeded, joints upon which slave joints will be created are returned through this list.
    slaveMasters = []

    if baseRig == None or upperLimbJoint == None:
        print('Unable to create upper limb twist joints.')
        return

    prefix = upperLimbJoint

    # Find child joint.
    childJoint = SEJointHelper.getFirstChildJoint(upperLimbJoint)
    if childJoint == None:
        print('No child joint found for upper limb:' + upperLimbJoint)
        return

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

    slaveMasters.append(twistBeginJoint)

    # Create twist knobs.
    if knobCount > 0 and knobCount < maxKnobCount:
        twistBeginJointPos = SEMathHelper.getWorldPosition(twistBeginJoint)
        twistEndJointPos = SEMathHelper.getWorldPosition(twistEndJoint)
        
        distance = SEMathHelper.getDistance3(twistBeginJointPos, twistEndJointPos)
        delta = distance / (knobCount + 1)

        jointSide = SEJointHelper.getJointSide(upperLimbJoint)
        if jointSide == SERigEnum.eRigSide.RS_Right:
            delta *= -1

        w0 = 1
        w1 = knobCount
        for j in range(1, knobCount + 1):
            knobJoint = cmds.duplicate(upperLimbJoint, n = prefix + SERigNaming.s_TwistKnob + str(j), parentOnly = True)[0]
            cmds.parent(knobJoint, upperLimbJoint)
            cmds.setAttr(knobJoint + '.tx', delta*j)
            cmds.setAttr(knobJoint + '.radius', origJntRadius * twistJointRadiusScale)
            cmds.color(knobJoint, ud = 1)

            # Create twist knobs' orient constraint.
            oc = cmds.orientConstraint(upperLimbJoint, twistBeginJoint, knobJoint, mo = False)[0]
            cmds.setAttr(oc + '.' + upperLimbJoint + 'W0', w0)
            cmds.setAttr(oc + '.' + twistBeginJoint + 'W1', w1)
            w0 += 1
            w1 -= 1

            slaveMasters.append(knobJoint)

    slaveMasters.append(upperLimbJoint)

    if 0:
        print('Slave master joints:')
        for i in slaveMasters:
            print(i)

    return slaveMasters

def createLowerLimbTwistJoints(
                               baseRig, 
                               lowerLimbJoint, 
                               twistJointRadiusScale = 3.0, 
                               knobCount = 2, 
                               maxKnobCount = 5
                               ):

    # If this function succeeded, joints upon which slave joints will be created are returned through this list.
    slaveMasters = []

    if baseRig == None or lowerLimbJoint == None:
        print('Unable to create lower limb twist joints.')
        return slaveMasters

    prefix = lowerLimbJoint

    # Find child joint.
    childJoint = SEJointHelper.getFirstChildJoint(lowerLimbJoint)
    if childJoint == None:
        print('No child joint found for lower limb:' + lowerLimbJoint)
        return slaveMasters

    # Create twist end joints.
    twistBeginJoint = cmds.duplicate(lowerLimbJoint, n = prefix + SERigNaming.s_TwistBegin, parentOnly = True)[0]
    twistEndJoint = cmds.duplicate(lowerLimbJoint, n = prefix + SERigNaming.s_TwistEnd, parentOnly = True)[0]
    cmds.delete(cmds.pointConstraint(childJoint, twistBeginJoint))

    # Adjust twist end joints.
    origJntRadius = cmds.getAttr(lowerLimbJoint + '.radius')

    # Set new radius and color for twist end joints.
    for i in [twistBeginJoint, twistEndJoint]:
        cmds.setAttr(i + '.radius', origJntRadius * twistJointRadiusScale)
        cmds.color(i, ud = 8)

    # Parent twist end joints.
    cmds.parent(twistEndJoint, twistBeginJoint)
    cmds.parent(twistBeginJoint, lowerLimbJoint)

    # Create single chain IK.
    twistIK = cmds.ikHandle(n = prefix + SERigNaming.s_TwistIKHandle, sol = 'ikSCsolver', sj = twistBeginJoint, ee = twistEndJoint)[0]
    cmds.hide(twistIK)
    cmds.parent(twistIK, childJoint)
    cmds.pointConstraint(lowerLimbJoint, twistIK)

    slaveMasters.append(lowerLimbJoint)

    # Create twist knobs.
    if knobCount > 0 and knobCount < maxKnobCount:
        twistBeginJointPos = SEMathHelper.getWorldPosition(twistBeginJoint)
        twistEndJointPos = SEMathHelper.getWorldPosition(twistEndJoint)
        
        distance = SEMathHelper.getDistance3(twistBeginJointPos, twistEndJointPos)
        delta = distance / (knobCount + 1)

        jointSide = SEJointHelper.getJointSide(lowerLimbJoint)
        if jointSide == SERigEnum.eRigSide.RS_Right:
            delta *= -1

        w0 = knobCount
        w1 = 1
        for j in range(1, knobCount + 1):
            knobJoint = cmds.duplicate(lowerLimbJoint, n = prefix + SERigNaming.s_TwistKnob + str(j), parentOnly = True)[0]
            cmds.parent(knobJoint, lowerLimbJoint)
            cmds.setAttr(knobJoint + '.tx', delta*j)
            cmds.setAttr(knobJoint + '.radius', origJntRadius * twistJointRadiusScale)
            cmds.color(knobJoint, ud = 8)

            # Create twist knobs' orient constraint.
            oc = cmds.orientConstraint(lowerLimbJoint, twistBeginJoint, knobJoint, mo = False)[0]
            cmds.setAttr(oc + '.' + lowerLimbJoint + 'W0', w0)
            cmds.setAttr(oc + '.' + twistBeginJoint + 'W1', w1)
            w0 -= 1
            w1 += 1

            slaveMasters.append(knobJoint)

    slaveMasters.append(twistBeginJoint)
    slaveMasters.append(childJoint)

    if 0:
        print('Slave master joints:')
        for i in slaveMasters:
            print(i)

    return slaveMasters


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