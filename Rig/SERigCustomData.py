import maya.cmds as cmds
import pymel.core.general
import re
import cPickle

from ..Base import SERigNaming
from ..Utils import SEJointHelper
from ..Utils import SERigObjectTypeHelper
from ..ThirdParty import cvshapeinverter
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

        # Get corrective mesh.
        correctiveMesh = cmds.listConnections(shapeInverter + '.correctiveMesh', s = True)[0]
        
        # Get control transformation table.
        tempStr = str(cmds.getAttr(shapeInverter + '.' + at))
        curControlTransTable = cPickle.loads(tempStr)

        # Possibly get deformed mesh.
        deformedMesh = cvshapeinverter.getShapeInverterDeformedMesh(shapeInverter)

        rigCustomData['meshCBSs'][correctiveMesh] = (curControlTransTable, deformedMesh)

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
def _importRigCustomData(rigCharacterGroup, fileFolderPath, removeRedundantProxyControls = True, restoreEyelidAnimationCurves = True, restoreShapeInverters = False):
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
        print('Importing ' + key + ': ')
        print(rigCustomData[key])

    # Remove redundant proxy controls.
    if removeRedundantProxyControls:
        curProxyJointControls = SERigObjectTypeHelper.getFaceProxyJointControls(rigCharacterGroup)

        for curProxyJointControl in curProxyJointControls:
            if not curProxyJointControl in rigCustomData['ProxyJointControls']:
                SERigHumanFacialComponent._removeFaceProxyControlInfluence(curProxyJointControl)
                print('Redundant proxy control deleted: ' + curProxyJointControl)

    # Restore eyelid animation curves.
    if restoreEyelidAnimationCurves:
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

    # Restore shape inverters.
    if restoreShapeInverters:
        for meshCBS in rigCustomData['meshCBSs']:
            shapeInverter = cmds.listConnections(meshCBS + '.outMesh', d = True)
            if shapeInverter == None:

                SERigHumanFacialComponent._resetFaceControls(rigCharacterGroup)
                SERigHumanFacialComponent._resetFaceProxyControls(rigCharacterGroup)

                controlTransTable = rigCustomData['meshCBSs'][meshCBS][0]
                deformedMesh = rigCustomData['meshCBSs'][meshCBS][1]

                # Pose the rig for base deformation.
                for transModifiedControl in controlTransTable:
                    trans = controlTransTable[transModifiedControl]

                    if cmds.objExists(transModifiedControl):
                        forceSetAttr(transModifiedControl + '.tx', trans[0])
                        forceSetAttr(transModifiedControl + '.ty', trans[1])
                        forceSetAttr(transModifiedControl + '.tz', trans[2])
                        forceSetAttr(transModifiedControl + '.rx', trans[3])
                        forceSetAttr(transModifiedControl + '.ry', trans[4])
                        forceSetAttr(transModifiedControl + '.rz', trans[5])

                    else:
                        cmds.warning('Control Object does not exist: ' + transModifiedControl)

                # Create shape inverter.
                if cmds.objExists(deformedMesh) and cmds.objExists(meshCBS):
                    cvshapeinverter.invert(deformedMesh, meshCBS)
                else:
                    cmds.warning('Cannot restore shape inverter for: ' + deformedMesh + ' and ' + meshCBS)

                cmds.refresh()

            else:
                cmds.warning('Shape inverter already exists for: ' + meshCBS)

        SERigHumanFacialComponent._resetFaceControls(rigCharacterGroup)
        SERigHumanFacialComponent._resetFaceProxyControls(rigCharacterGroup)

#-----------------------------------------------------------------------------
def forceSetAttr(objAttr, value):
    try:
        cmds.setAttr(objAttr, value)
    except:
        pass
#-----------------------------------------------------------------------------