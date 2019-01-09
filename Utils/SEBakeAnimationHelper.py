import maya.cmds as cmds
from . import SERigObjectTypeHelper
from ..Base import SERigNaming

def bakeSlaveJointAnimation(characterGroup, timeRange = (0, 0), useTimeSliderRange = True):
    deformationGrp = SERigObjectTypeHelper.getCharacterDeformationGroup(characterGroup)
    if deformationGrp:
        slaveJoints = cmds.listRelatives(deformationGrp, type = 'joint', ad = True)
        
        newTimeRange = timeRange
        if useTimeSliderRange:
            minTime = cmds.playbackOptions(q = True, minTime = True)
            maxTime = cmds.playbackOptions(q = True, maxTime = True)
            newTimeRange = (minTime, maxTime)

        cmds.bakeResults(slaveJoints, simulation = True, t = newTimeRange, sampleBy = 1,
                         oversamplingRate = 1, disableImplicitControl = True, preserveOutsideKeys = True,
                         sparseAnimCurveBake = False, removeBakedAttributeFromLayer = False, removeBakedAnimFromLayer = False,
                         bakeOnOverrideLayer = False, minimizeRotation = True, controlPoints = False, shape = True)