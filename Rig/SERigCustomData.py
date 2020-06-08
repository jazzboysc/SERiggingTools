import maya.cmds as cmds
import pymel.core.general
import re
import cPickle

from ..Base import SERigNaming
from ..Utils import SEJointHelper
from ..Utils import SERigObjectTypeHelper
from . import SERigHumanFacialComponent

#-----------------------------------------------------------------------------
def exportRigCustomData():
    rigCharacterGroup = SEJointHelper.getSelectedRigCharacterGroup()
    if rigCharacterGroup == None:
        return

    fileResult = cmds.fileDialog2(fm = 3)
    if fileResult != None:        
        _exportRigCustomData(rigCharacterGroup, fileResult[0])
#-----------------------------------------------------------------------------
def _exportRigCustomData(rigCharacterGroup, fileFolderPath):
    rigCustomData = {}
    
    # Get face proxy control names.
    proxyJointControls = SERigObjectTypeHelper.getFaceProxyJointControls(rigCharacterGroup)
    rigCustomData['ProxyJointControls'] = proxyJointControls

    # Get eyelid animation curves.
    leftEyeLidUpperAnimCurves = SERigHumanFacialComponent.getLeftEyeLidUpperAnimCurves(rigCharacterGroup)
    rigCustomData['leftEyeLidUpperAnimCurves'] = []

    for animCurve in leftEyeLidUpperAnimCurves:
        keyframeCount = cmds.keyframe(animCurve, q = True, keyframeCount = True)
        driverKeys = cmds.keyframe(animCurve, q = True, floatChange = True)
        drivenKeys = cmds.keyframe(animCurve, q = True, valueChange = True)

        keyFrames = []
        for i in range(keyframeCount):
            keyFrames.append((driverKeys[i], drivenKeys[i]))

        rigCustomData['leftEyeLidUpperAnimCurves'].append(keyFrames)

    rightEyeLidUpperAnimCurves = SERigHumanFacialComponent.getRightEyeLidUpperAnimCurves(rigCharacterGroup)
    rigCustomData['rightEyeLidUpperAnimCurves'] = []

    for animCurve in rightEyeLidUpperAnimCurves:
        keyframeCount = cmds.keyframe(animCurve, q = True, keyframeCount = True)
        driverKeys = cmds.keyframe(animCurve, q = True, floatChange = True)
        drivenKeys = cmds.keyframe(animCurve, q = True, valueChange = True)

        keyFrames = []
        for i in range(keyframeCount):
            keyFrames.append((driverKeys[i], drivenKeys[i]))

        rigCustomData['rightEyeLidUpperAnimCurves'].append(keyFrames)


    for key in rigCustomData:
        print key, rigCustomData[key]

    fileName = fileFolderPath + '/' + rigCharacterGroup + '.serig'
    try:
        f = open(fileName, 'wb')
        cPickle.dump(rigCustomData, f)
        f.close()
    except:
        cmds.warning('Failed exporting rig custom data for: ' + rigCharacterGroup)

#-----------------------------------------------------------------------------
def importRigCustomData():
    rigCharacterGroup = SEJointHelper.getSelectedRigCharacterGroup()
    if rigCharacterGroup == None:
        return

    fileResult = cmds.fileDialog2(fm = 3)
    if fileResult != None:        
        _importRigCustomData(rigCharacterGroup, fileResult[0])
#-----------------------------------------------------------------------------
def _importRigCustomData(rigCharacterGroup, fileFolderPath):
    rigCustomData = {}

    fileName = fileFolderPath + '/' + rigCharacterGroup + '.serig'
    try:
        f = open(fileName, 'rb')
        rigCustomData = cPickle.load(f)
        f.close()
    except:
        cmds.warning('Failed importing rig custom data for: ' + rigCharacterGroup)
        return

    curProxyJointControls = SERigObjectTypeHelper.getFaceProxyJointControls(rigCharacterGroup)

    # Remove redundant proxy controls.
    for curProxyJointControl in curProxyJointControls:
        if not curProxyJointControl in rigCustomData['ProxyJointControls']:
            SERigHumanFacialComponent._removeFaceProxyControlInfluence(curProxyJointControl)
            print('Redundant proxy control deleted: ' + curProxyJointControl)
#-----------------------------------------------------------------------------