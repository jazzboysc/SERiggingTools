import maya.cmds as cmds
import pymel.core as pm

from . import SERigObjectTypeHelper
from . import SEJointHelper
from ..Base import SERigNaming

#-----------------------------------------------------------------------------
def bakeRigCharacterAnimation(bakeSlaveJoints = True, bakeBlendshapes = True, timeRange = (0, 0), useTimeSliderRange = True, 
                              importReference = True, reloadReference = False, deleteRigAfterBaking = True, 
                              sampleJointBy = 2, sampleBlendShapeBy = 4):
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
    
    # Possibly import reference.
    if importReference:
        for ref in refs:
            curRN = cmds.referenceQuery(ref, referenceNode = True)
            rnNamespace = cmds.referenceQuery(curRN, namespace = True)
            rnNamespace = rnNamespace[1:] + ':'
            if rnNamespace == curNS:
                cmds.file(importReference = True, referenceNode = curRN)


    newTimeRange = timeRange
    if useTimeSliderRange:
        minTime = cmds.playbackOptions(q = True, minTime = True)
        maxTime = cmds.playbackOptions(q = True, maxTime = True)
        newTimeRange = (minTime, maxTime)

    # Possibly bake slave joints' animation.
    deformationGrp = SERigObjectTypeHelper.getCharacterDeformationGroup(characterGroup)
    if deformationGrp and bakeSlaveJoints:
        slaveJoints = cmds.listRelatives(deformationGrp, type = 'joint', ad = True)
        
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

        cmds.bakeResults(toBeBaked, t = newTimeRange, sampleBy = sampleBlendShapeBy)

        #for bs in blendShapes:
        #    weightAttrNames = cmds.listAttr(bs + '.weight', m = True)
        #
        #    cmds.bakeResults(bs, at = weightAttrNames, simulation = True, t = newTimeRange, sampleBy = 1, 
        #                     oversamplingRate = 1, disableImplicitControl = True, preserveOutsideKeys = True, 
        #                     sparseAnimCurveBake = False, removeBakedAttributeFromLayer = False, removeBakedAnimFromLayer = False,
        #                     bakeOnOverrideLayer = False, minimizeRotation = True)
        #    print('Blendshape node baked: ' + bs)

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
            cmds.delete(characterGroup)
#-----------------------------------------------------------------------------