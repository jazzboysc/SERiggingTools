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

    leftEyeLidLowerAnimCurves = SERigHumanFacialComponent.getLeftEyeLidLowerAnimCurves(rigCharacterGroup)
    rigCustomData['leftEyeLidLowerAnimCurves'] = []

    for animCurve in leftEyeLidLowerAnimCurves:
        keyframeCount = cmds.keyframe(animCurve, q = True, keyframeCount = True)
        driverKeys = cmds.keyframe(animCurve, q = True, floatChange = True)
        drivenKeys = cmds.keyframe(animCurve, q = True, valueChange = True)

        keyFrames = []
        for i in range(keyframeCount):
            keyFrames.append((driverKeys[i], drivenKeys[i]))

        rigCustomData['leftEyeLidLowerAnimCurves'].append(keyFrames)

    rightEyeLidLowerAnimCurves = SERigHumanFacialComponent.getRightEyeLidLowerAnimCurves(rigCharacterGroup)
    rigCustomData['rightEyeLidLowerAnimCurves'] = []

    for animCurve in rightEyeLidLowerAnimCurves:
        keyframeCount = cmds.keyframe(animCurve, q = True, keyframeCount = True)
        driverKeys = cmds.keyframe(animCurve, q = True, floatChange = True)
        drivenKeys = cmds.keyframe(animCurve, q = True, valueChange = True)

        keyFrames = []
        for i in range(keyframeCount):
            keyFrames.append((driverKeys[i], drivenKeys[i]))

        rigCustomData['rightEyeLidLowerAnimCurves'].append(keyFrames)

    # Get shape inverters for corrective blendshapes.
    rigCustomData['meshCBSs'] = {}

    shapeInverters = cmds.ls(type = 'cvShapeInverter')
    at = 'controlTransTable'
    for shapeInverter in shapeInverters:
        correctiveMesh = cmds.listConnections(shapeInverter + '.correctiveMesh', s = True)[0]
        
        tempStr = str(cmds.getAttr(shapeInverter + '.' + at))
        curControlTransTable = cPickle.loads(tempStr)
        rigCustomData['meshCBSs'][correctiveMesh] = curControlTransTable

    # Debug output.
    for key in rigCustomData:
        print('Exporting ' + key + ': ')
        print(rigCustomData[key])

    # Rig custom data serialization.
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

    # Rig custom data deserialization.
    fileName = fileFolderPath + '/' + rigCharacterGroup + '.serig'
    try:
        f = open(fileName, 'rb')
        rigCustomData = cPickle.load(f)
        f.close()
    except:
        cmds.warning('Failed importing rig custom data for: ' + rigCharacterGroup)
        return

    # Debug output.
    for key in rigCustomData:
        print('Importing: ')
        print(key + ': ')
        print(rigCustomData[key])

    # Remove redundant proxy controls.
    curProxyJointControls = SERigObjectTypeHelper.getFaceProxyJointControls(rigCharacterGroup)

    for curProxyJointControl in curProxyJointControls:
        if not curProxyJointControl in rigCustomData['ProxyJointControls']:
            SERigHumanFacialComponent._removeFaceProxyControlInfluence(curProxyJointControl)
            print('Redundant proxy control deleted: ' + curProxyJointControl)

    # Restore eyelid animation curves.
    leftEyeLidUpperAnimCurves = SERigHumanFacialComponent.getLeftEyeLidUpperAnimCurves(rigCharacterGroup)
    for i, animCurve in enumerate(leftEyeLidUpperAnimCurves):
        keyValueList = rigCustomData['leftEyeLidUpperAnimCurves'][i]
        for keyValue in keyValueList:
            cmds.setKeyframe(animCurve, float = keyValue[0], value = keyValue[1], itt = 'linear', ott = 'linear')

    leftEyeLidLowerAnimCurves = SERigHumanFacialComponent.getLeftEyeLidLowerAnimCurves(rigCharacterGroup)
    for i, animCurve in enumerate(leftEyeLidLowerAnimCurves):
        keyValueList = rigCustomData['leftEyeLidLowerAnimCurves'][i]
        for keyValue in keyValueList:
            cmds.setKeyframe(animCurve, float = keyValue[0], value = keyValue[1], itt = 'linear', ott = 'linear')

    rightEyeLidUpperAnimCurves = SERigHumanFacialComponent.getRightEyeLidUpperAnimCurves(rigCharacterGroup)
    for i, animCurve in enumerate(rightEyeLidUpperAnimCurves):
        keyValueList = rigCustomData['rightEyeLidUpperAnimCurves'][i]
        for keyValue in keyValueList:
            cmds.setKeyframe(animCurve, float = keyValue[0], value = keyValue[1], itt = 'linear', ott = 'linear')

    rightEyeLidLowerAnimCurves = SERigHumanFacialComponent.getRightEyeLidLowerAnimCurves(rigCharacterGroup)
    for i, animCurve in enumerate(rightEyeLidLowerAnimCurves):
        keyValueList = rigCustomData['rightEyeLidLowerAnimCurves'][i]
        for keyValue in keyValueList:
            cmds.setKeyframe(animCurve, float = keyValue[0], value = keyValue[1], itt = 'linear', ott = 'linear')

#-----------------------------------------------------------------------------