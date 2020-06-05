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