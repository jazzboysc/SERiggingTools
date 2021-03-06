import maya.cmds as cmds
import pymel.core as pm

from . import SERigObjectTypeHelper
from . import SEJointHelper
from ..Base import SERigNaming

#-----------------------------------------------------------------------------
def bakeRigCharacterAnimation(bakeSlaveJoints = True, bakeBlendshapes = True, timeRange = (0, 0), useTimeSliderRange = True, 
                              importReference = True, reloadReference = False, deleteRigAfterBaking = True, 
                              sampleJointBy = 2, sampleBlendShapeBy = 4, cleanupUnskinnedSlaveLeafJoints = True, excludeTags = [],
                              cleanupBindPose = True):
    # Get selected rig character and its namespace.
    selected = cmds.ls(sl = True)
    if selected:
        selected = selected[0]
    else:
        print('Please select a rig character top group.')
        return

    curNS = ''
    characterGroup = ''
    if SERigObjectTypeHelper.isRigCharacterGroup(selected):
        curNS = pm.selected()[0].namespace()
        characterGroup = selected
        print('Selected namespace:' + curNS)
        print('Selected rig character group:' + characterGroup)
    else:
        print('Please select a rig character top group.')
        return
    
    # Query all the rig reference.
    refs = cmds.file(q = True, r = True)

    # Possibly reload reference.
    if reloadReference:
        for ref in refs:
            curRN = cmds.referenceQuery(ref, referenceNode = True)
            rnNamespace = cmds.referenceQuery(curRN, namespace = True)
            rnNamespace = rnNamespace[1:] + ':'
            if rnNamespace == curNS:
                cmds.file(ref, loadReferenceDepth = 'asPrefs', loadReference = curRN)
                print('Reload rig reference: ' + curRN)
    
    # Possibly import reference.
    if importReference:
        for ref in refs:
            curRN = cmds.referenceQuery(ref, referenceNode = True)
            rnNamespace = cmds.referenceQuery(curRN, namespace = True)
            rnNamespace = rnNamespace[1:] + ':'
            if rnNamespace == curNS:
                cmds.file(importReference = True, referenceNode = curRN)
                print('Import rig reference: ' + curRN)


    newTimeRange = timeRange
    if useTimeSliderRange:
        minTime = cmds.playbackOptions(q = True, minTime = True)
        maxTime = cmds.playbackOptions(q = True, maxTime = True)
        newTimeRange = (minTime, maxTime)
    print('Baked time range: ' + str(minTime) + ',' + str(maxTime))

    # Possibly bake slave joints' animation.
    deformationGrp = SERigObjectTypeHelper.getCharacterDeformationGroup(characterGroup)
    slaveJoints = []
    if deformationGrp and bakeSlaveJoints:
        slaveJoints = cmds.listRelatives(deformationGrp, type = 'joint', ad = True)
        
        print('Slave joints animation baked.')
        cmds.bakeResults(slaveJoints, simulation = True, t = newTimeRange, sampleBy = sampleJointBy,
                         oversamplingRate = 1, disableImplicitControl = True, preserveOutsideKeys = True,
                         sparseAnimCurveBake = False, removeBakedAttributeFromLayer = False, removeBakedAnimFromLayer = False,
                         bakeOnOverrideLayer = False, minimizeRotation = True, controlPoints = False, shape = True)

    # Possibly bake blendshapes' animation.
    if bakeBlendshapes:
        blendShapes = SERigObjectTypeHelper.getSpecificObjectsUnderNamespace(type = 'blendShape', namespace = curNS)
        
        toBeBaked = []
        for bs in blendShapes:
            temp = bs + '.weight'
            toBeBaked.append(temp)

        if len(toBeBaked) > 0:
            print('Blendshape nodes animation baked.')
            cmds.bakeResults(toBeBaked, t = newTimeRange, sampleBy = sampleBlendShapeBy)

        #for bs in blendShapes:
        #    weightAttrNames = cmds.listAttr(bs + '.weight', m = True)
        #
        #    cmds.bakeResults(bs, at = weightAttrNames, simulation = True, t = newTimeRange, sampleBy = 1, 
        #                     oversamplingRate = 1, disableImplicitControl = True, preserveOutsideKeys = True, 
        #                     sparseAnimCurveBake = False, removeBakedAttributeFromLayer = False, removeBakedAnimFromLayer = False,
        #                     bakeOnOverrideLayer = False, minimizeRotation = True)
        #    print('Blendshape node baked: ' + bs)

    slaveRoot = None
    if deformationGrp and importReference and deleteRigAfterBaking:
        slaveRoot = SEJointHelper.getFirstChildJoint(deformationGrp)
        if slaveRoot:
            cmds.parent(slaveRoot, w = True)
        else:
            cmds.warning('Slave joint root not found for:' + deformationGrp)

        modelGrp = SERigObjectTypeHelper.getCharacterModelGroup(characterGroup)
        if modelGrp:
            modelRootGrp = SEJointHelper.getFirstChildGroup(modelGrp)
            if modelRootGrp:
                cmds.parent(modelRootGrp, w = True)
            else:
                cmds.warning('Model root not found for:' + modelGrp)

            print('Remove character rig: ' + characterGroup)
            cmds.delete(characterGroup)

    if cleanupUnskinnedSlaveLeafJoints:
        SEJointHelper.removeUnskinnedSlaveLeafJoints(slaveJoints, excludeTags)

    if cleanupBindPose:
        cleanupBindPoseForSlaveJoints(slaveJoints, slaveRoot)
#-----------------------------------------------------------------------------
def cleanupBindPoseForSlaveJoints(slaveJoints = [], slaveRoot = None):
    bindPoseNodes = set()
    for slaveJoint in slaveJoints:
        if cmds.objExists(slaveJoint):
            curBindPoseNodes = cmds.listConnections(slaveJoint, t = 'dagPose')

            if curBindPoseNodes:
                for curBindPoseNode in curBindPoseNodes:
                    bindPoseNodes.add(curBindPoseNode)

    for bindPoseNode in bindPoseNodes:
        if cmds.objExists(bindPoseNode):
            print('Remove old bind pose node: ' + bindPoseNode)
            cmds.delete(bindPoseNode)

    if slaveRoot:
        res = cmds.dagPose(slaveRoot, save = True, name = 'bindPose')
        print('New bind pose node created: ' + res)
#-----------------------------------------------------------------------------
def _cleanupBindPoseForCharacter(characterGroup):
    if not SERigObjectTypeHelper.isRigCharacterGroup(characterGroup):
        cmds.warning('Please select a character rig group.')
        return

    deformationGrp = SERigObjectTypeHelper.getCharacterDeformationGroup(characterGroup)
    slaveJoints = []
    slaveRoot = None
    if deformationGrp:
        slaveJoints = cmds.listRelatives(deformationGrp, type = 'joint', ad = True)
        slaveRoot = SEJointHelper.getFirstChildJoint(deformationGrp)
        cleanupBindPoseForSlaveJoints(slaveJoints, slaveRoot)
#-----------------------------------------------------------------------------
def cleanupBindPoseForCharacter():
    selected = cmds.ls(sl = True)
    if len(selected) == 1:
        selected = selected[0]
    else:
        cmds.warning('Please select a character rig group.')
        return

    _cleanupBindPoseForCharacter(selected)
#-----------------------------------------------------------------------------