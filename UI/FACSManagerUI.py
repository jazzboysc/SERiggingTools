from PySide2 import QtCore, QtGui, QtWidgets , QtUiTools
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.mel as mel
import sys
import maya.cmds as cmds
import maya.OpenMayaUI as mui
import shiboken2
import os
import time
import functools
import math
import difflib
import re

import cPickle

from ..Character import SECharacter
from ..Base import SERigNaming
from ..Utils import SEDeformerHelper as DeformerHelper
from ..Utils import SEJointHelper as JointHelper
from ..Utils import SERigObjectTypeHelper as RigObjectTypeHelper
from ..Utils import SEFacsHelper as FacsHelper
from ..Rig import SERigBipedLimbComponent
from ..Rig import SERigHumanFacialComponent

import UIConfig


# .ui File Path & Assets File Path
uiRootFile = os.path.dirname(UIConfig.__file__)
uifile_path = uiRootFile + "/FACSManager.ui"
auRootFile = os.path.dirname(uiRootFile) + "/Assets/Presets/AU/"
faceCageRootFile = os.path.dirname(uiRootFile) + "/Assets/Presets/FaceCage/"
faceWeightFootFile = os.path.dirname(uiRootFile) + "/Assets/Presets/Weight/"

# global variables
AUjob_id_list = []
nameDel_id_list = []
popHelp = None


#-----------------------------------------------------------------------------
def maya_main_window():
    """
    Return the Maya Main Window Widget as a Python object
    """
    main_window = mui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(main_window), QtWidgets.QWidget)

class BackendThread(QtCore.QObject):
    update_data = QtCore.Signal(str)

class FACSManagerUI(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent = maya_main_window()):
        super(FACSManagerUI, self).__init__(parent)
        self.setWindowTitle("FACS Manager")     
        #self.setObjectName('FACS Manager UI')
        self.importedAU = []
        self.time_job_id = -1
        self.mode_job_id = -1
        self.nameChange_job_id = -1
        self.mask_bs = -1
        self.ctrlDataList = {}
        self.auDataList = {}
        self.skipBuild = 0
        self.facsControlMode = 1
        
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        uifile = QtCore.QFile(uifile_path)
        uifile.open(QtCore.QFile.ReadOnly)
        self.uiWindow = QtUiTools.QUiLoader().load(uifile, parentWidget = self)
        uifile.close()
        
        self.uiWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setInitialUI()
        self.setButtonsCallBack()
        #QtWidgets.QApplication.exit()
        
        #return uiWindow
    
    def run(self):
        #self.show(dockable = True)
        self.show()
    
        # Initiate the UI   
    def setInitialUI(self):
        # set ui size
        self.resizeUIWindowSize(600, 650)
        
        # Initiate AU Button
        self.uiWindow.hideShowBuildPageBtn.setHidden(True)
        self.uiWindow.addAUFixCBSBtn.setHidden(True)
        self.uiWindow.connectionMapStackedWidget.setHidden(True)
        self.hideAUSliders()
        self.uiWindow.tipBuildWidget.hide()
        self.uiWindow.confirmNamesBtn.hide()

        # Initiate RightWidget
        #self.uiWindow.RightSideStackedWidget.hide()
        self.uiWindow.auConnectWarnLabel.hide()
        self.enableAUManagerTab(False)

        # Initiate Pre-Build Warn Labels
        self.uiWindow.facialTargetWarnLabel.hide()
        self.uiWindow.auBaseWarnLabel.hide()
        self.uiWindow.facialBaseWarnLabel.hide()
        self.uiWindow.faceCageWarnLabel.hide()
        self.uiWindow.lod0WarnLabel.hide()
        self.uiWindow.lod1WarnLabel.hide()

        # Initiate Icons
        self.uiWindow.icon1.setPixmap(QtGui.QPixmap((uiRootFile +"/iconTick.png")))
        self.uiWindow.icon2.setPixmap(QtGui.QPixmap((uiRootFile +"/iconTick.png")))
        self.uiWindow.icon3.setPixmap(QtGui.QPixmap((uiRootFile +"/iconTick.png")))
        self.uiWindow.icon4.setPixmap(QtGui.QPixmap((uiRootFile +"/iconTick.png")))
        self.uiWindow.icon5.setPixmap(QtGui.QPixmap((uiRootFile +"/iconTick.png")))
        self.uiWindow.icon6.setPixmap(QtGui.QPixmap((uiRootFile +"/iconTick.png")))
        self.uiWindow.icon1.hide()
        self.uiWindow.icon2.hide()
        self.uiWindow.icon3.hide()
        self.uiWindow.icon4.hide()
        self.uiWindow.icon5.hide()
        self.uiWindow.icon6.hide()
        #self.uiWindow.faceBG.setPixmap(QtGui.QPixmap((uiRootFile +"/face.png")))

        # Initiate rig character group
        rigCharacterName = self.getRigCharacterName()
        if rigCharacterName == []:
            self.uiWindow.rigCharacterGrpLineEdit.setReadOnly(False)
            self.uiWindow.rigCharacterGrpLineEdit.textEdited.connect(self.checkRigCharacterGroupValid)
            self.uiWindow.rigCharacterWarnLabel.show()
        else:
            self.uiWindow.rigCharacterGrpLineEdit.setText(self.getRigCharacterName()) 
            self.uiWindow.rigCharacterGrpLineEdit.setReadOnly(True)
            self.uiWindow.rigCharacterWarnLabel.hide()
            self.checkRigCharacterGroupValid()
            

        ## Initiate FACS Control Mode 
        self.updateControlModeDisplay()
        self.createScriptJobForSwitchControlMode()

    def resizeUIWindowSize(self, width, height):
        self.uiWindow.resize(width, height)
        self.uiWindow.setMaximumSize(width, height)
        self.resize(width, height)
    #----------------------------------- Check if built by this tool -----------------------------------        
    def isRigBuiltByThisTool(self):
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        if not cmds.objExists(rigCharacterGrp):
            return False
        
        characterName = RigObjectTypeHelper.getRigCharacterName(rigCharacterGrp)
        mainCtrl = RigObjectTypeHelper.getRigGlobalControlObject(characterName, u'RS_Center', u'RT_Global',0)
        if mainCtrl:
            if cmds.objExists(mainCtrl + '.' + SERigNaming.sFACS_ControlModeAttr):
                return True
            else:
                return False 
        else:
            return False

    #----------------------------------- Pre-Build Related -----------------------------------    
    # If Rig Character Group Name is Valid, enable next period.        
    def checkRigCharacterGroupValid(self):
        name = self.uiWindow.rigCharacterGrpLineEdit.text()
        if cmds.objExists(name):
            self.uiWindow.rigCharacterGrpLineEdit.setReadOnly(True)
            self.uiWindow.rigCharacterWarnLabel.hide()
            
            
            nodeName = name + '.' + SERigNaming.sFACS_BuildSuccessAttr
            nodeName2 = name + '.' + SERigNaming.sFACS_NameListAttr
            if cmds.objExists(nodeName) and cmds.objExists(nodeName2):
                scFlag = cmds.getAttr(nodeName)
                if scFlag == 1:
                    self.fillPrebuildNamesByCache()
                    self.setFACSBuildSuccess()
                else:
                    self.enablePrebuildFacialBase()
                    self.createScriptJobForPreBuildNameChanges()
            else:
                CharacterFacialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(name)
                faceProxyRivetGrp = RigObjectTypeHelper.getFaceProxyControlRivetsGroup(CharacterFacialComponent)
                proxyGroupChildren = cmds.listRelatives(faceProxyRivetGrp, c = True, type = 'transform') 
                if proxyGroupChildren:
                    if len(proxyGroupChildren) > 0:
                        self.uiWindow.tipBuildWidget.show()
                    else:
                        self.enablePrebuildFacialBase()
                        self.createScriptJobForPreBuildNameChanges()
                else:
                    self.enablePrebuildFacialBase()
                    self.createScriptJobForPreBuildNameChanges()
    
    def checkFacialTargetValid(self):
        name = self.uiWindow.facialTargetLineEdit.text()
        if cmds.objExists(name):
            self.uiWindow.facialTargetWarnLabel.hide()
            self.uiWindow.icon1.show()
            self.enablePrebuildAUBase()
            self.createScriptJobForPreBuildNameDeleted(name)
        else:
            self.uiWindow.facialTargetWarnLabel.show()
            self.uiWindow.facialTargetWarnLabel.setText('*Warning: Cannot find the "%s" mesh in the scene.' %name)
            self.uiWindow.icon1.hide()
            self.disableShowConnectMap()
    
    def checkAUBaseValid(self):
        name = self.uiWindow.auBaseLineEdit.text()
        if cmds.objExists(name):
            self.uiWindow.auBaseWarnLabel.hide()
            self.uiWindow.icon2.show()
            self.enablePrebuildFaceCage()
            self.createScriptJobForPreBuildNameDeleted(name)
        else:
            self.uiWindow.auBaseWarnLabel.show()
            self.uiWindow.auBaseWarnLabel.setText('*Warning: Cannot find the "%s" mesh in the scene.' %name)
            self.uiWindow.icon2.hide()
            self.disableShowConnectMap()

    def checkFacialBaseValid(self):
        name = self.uiWindow.facialBaseLineEdit.text()
        if cmds.objExists(name):
            if self.isUnderRigCharacterGroup(name):
                self.uiWindow.facialBaseWarnLabel.hide()
                self.enablePrebuildFacialTarget()
                self.uiWindow.icon3.show()
                self.createScriptJobForPreBuildNameDeleted(name)
            else:
                rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
                modelGrp = RigObjectTypeHelper.getCharacterModelGroup(rigCharacterGrp)
                if modelGrp != None:
                    cmds.parent(name, modelGrp)
                else:
                    cmds.parent(name, rigCharacterGrp)
                self.checkFacialBaseValid()
        else:
            self.uiWindow.facialBaseWarnLabel.show()
            self.uiWindow.facialBaseWarnLabel.setText('*Warning: Cannot find the "%s" mesh in the scene.' %name)
            self.uiWindow.icon3.hide()
            self.disableShowConnectMap()

    def checkFaceCageValid(self):
        name = self.uiWindow.faceCageLineEdit.text()
        if cmds.objExists(name):
            self.uiWindow.faceCageWarnLabel.hide()
            self.enablePrebuildLOD0()
            self.uiWindow.icon4.show()
            self.createScriptJobForPreBuildNameDeleted(name)
        else:
            self.uiWindow.faceCageWarnLabel.show()
            self.uiWindow.faceCageWarnLabel.setText('*Warning: Cannot find the "%s" mesh in the scene.' %name)
            self.uiWindow.icon4.hide()
            self.disableShowConnectMap()
    
    def checkFaceLOD0Valid(self):
        name = self.uiWindow.lod0LineEdit.text()
        if cmds.objExists(name):
            self.uiWindow.lod0WarnLabel.hide()
            self.uiWindow.icon5.show()
            self.enablePrebuildLOD1()
            self.createScriptJobForPreBuildNameDeleted(name)
        else:
            self.uiWindow.lod0WarnLabel.show()
            self.uiWindow.lod0WarnLabel.setText('*Warning: Cannot find the "%s" mesh in the scene.' %name)
            self.uiWindow.icon5.hide()
            self.disableShowConnectMap()
    
    def checkFaceLOD1Valid(self):
        name = self.uiWindow.lod1LineEdit.text()
        
        if cmds.objExists(name):
            self.uiWindow.lod1WarnLabel.hide()
            self.uiWindow.icon6.show()
            if self.isNamesValid():
                if self.skipBuild == 0:
                    self.enableAUConfig()
                elif self.skipBuild == 1:
                    self.uiWindow.confirmNamesBtn.show()
                self.createScriptJobForPreBuildNameDeleted(name)
        else:
            self.uiWindow.lod1WarnLabel.show()
            self.uiWindow.lod1WarnLabel.setText('*Warning: Cannot find the "%s" mesh in the scene.' %name)
            self.uiWindow.icon6.hide()
            self.disableShowConnectMap()
            
    
    # check if DataBuffer has connected to AU BlendShape
    def isAUConnectedSuccess(self):
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        try:
            facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(rigCharacterGrp)
            controlMode = FacsHelper.getFACS_ControlMode(facialComponent)
            res = cmds.listConnections("{}.{}".format(controlMode, SERigNaming.sFACS_AUConnectedAttr))
        except:
            return False
        
        #print res
        if res:
            return True
        else:
            return False
    
    # check if input object is under the rig character group
    def isUnderRigCharacterGroup(self, inObject):
        if not cmds.objExists(inObject):
            return False

        rigCharacterName = self.uiWindow.rigCharacterGrpLineEdit.text()
        curParent = cmds.listRelatives(inObject, p = True)
        while curParent:
            curParent = curParent[0]
            if rigCharacterName == curParent:
                return True
            curParent = cmds.listRelatives(curParent, p = True)
        
        return False

    def lockNamesCallback(self):
        if self.isNamesValid():
            self.uiWindow.importFacialTargetBtn.setEnabled(False)
            self.uiWindow.importAUBaseBtn.setEnabled(False)
            self.uiWindow.importFacialBaseBtn.setEnabled(False)
            self.uiWindow.importFaceCageBtn.setEnabled(False)
            self.uiWindow.facialTargetLineEdit.setEnabled(False)
            self.uiWindow.auBaseLineEdit.setEnabled(False)
            self.uiWindow.facialBaseLineEdit.setEnabled(False)
            self.uiWindow.faceCageLineEdit.setEnabled(False)
            self.uiWindow.lod0LineEdit.setEnabled(False)
            self.uiWindow.lod1LineEdit.setEnabled(False)
            ft = self.uiWindow.facialTargetLineEdit.text()
            ab = self.uiWindow.auBaseLineEdit.text()
            fb = self.uiWindow.facialBaseLineEdit.text()
            fc = self.uiWindow.faceCageLineEdit.text()
            lod0 = self.uiWindow.lod0LineEdit.text()
            lod1 = self.uiWindow.lod1LineEdit.text()
            auClean = self.uiWindow.cleanAULineEdit.text()
            faceClean = self.uiWindow.cleanFaceLineEdit.text()

            nameList = [fb, ft, ab, fc, lod0, lod1, auClean, faceClean]
            self.lockObj(nameList)

            self.killScriptJobForNameDelete()
            if cmds.scriptJob(ex = self.nameChange_job_id):
                cmds.scriptJob(kill = self.nameChange_job_id, force = True)
        else:
            return

    def lockObj(self, inputList):
        for obj in inputList:
            if cmds.objExists(obj):
                cmds.lockNode(obj, lock = True)
        
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        nodeName = rigCharacterGrp + '.' + SERigNaming.sFACS_NameListAttr
        cmds.select(rigCharacterGrp, r = True)
        if cmds.objExists(nodeName):
            if cmds.getAttr(nodeName) == None or cmds.getAttr(nodeName) == []:
                cmds.setAttr(nodeName, type = 'stringArray', *([len(inputList)] + inputList))
        else:
            cmds.addAttr(longName = SERigNaming.sFACS_NameListAttr, dt = 'stringArray')
            cmds.setAttr(nodeName, type = 'stringArray', *([len(inputList)] + inputList))

        #print cmds.getAttr(nodeName)
    def unlockObj(self, inputList):
        for obj in inputList:
            cmds.lockNode(obj, lock = False)
        
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        nodeName = rigCharacterGrp + '.' + SERigNaming.sFACS_NameListAttr
        cmds.select(rigCharacterGrp, r = True)
        if cmds.objExists(nodeName):
            cmds.setAttr(nodeName, 0, type = 'stringArray')

    def createAUandFaceCleanMesh(self):
        auBase = self.uiWindow.auBaseLineEdit.text()
        faceLOD0 = self.uiWindow.lod0LineEdit.text()
        auClean = cmds.duplicate( auBase, rr = True, n = 'AUBaseClean' )
        faceClean = cmds.duplicate( faceLOD0, rr = True, n = 'Face_LOD0_Clean' )
        self.uiWindow.cleanAULineEdit.setText(auClean[0])
        self.uiWindow.cleanFaceLineEdit.setText(faceClean[0])
        cmds.hide(auClean)
        cmds.hide(faceClean)

        print 'create clean.'

    def hideAUSliders(self, auName = None):
        if auName == None:
            for auType in DeformerHelper.facialActionUnitTypeList:
                key = SERigNaming.auAttrList[auType]
                sliderName = key + 'Slider'
                executeStr = "{}.{}.{}.{}".format('self', 'uiWindow', sliderName, 'hide()')
                executeStr2 = "{}.{}.{}.{}".format('self', 'uiWindow', key, 'hide()')
                try:
                    exec(executeStr)
                    exec(executeStr2)
                except:
                    pass
        else:
            try:
                executeStr = "{}.{}.{}.{}".format('self', 'uiWindow', auName, 'hide()')
                exec(executeStr)
            except:
                pass
    #------------------------------------------------------
    def createScriptJobForPreBuildNameChanges(self):
        if self.nameChange_job_id == -1:
            cmds.scriptJob(e = ("NameChanged", self.updateStatesForPrebuildNames))
    
    def createScriptJobForPreBuildNameDeleted(self, curName):
        newID = cmds.scriptJob(runOnce = True, nd = [curName, self.updateStatesForPrebuildNames])
    
    def updateStatesForPrebuildNames(self):
        if self.uiWindow.facialBaseLineEdit.text() != '':
            self.checkFacialBaseValid()
        if self.uiWindow.facialTargetLineEdit.text() != '':
            self.checkFacialTargetValid()
        if self.uiWindow.auBaseLineEdit.text() != '':
            self.checkAUBaseValid()
        if self.uiWindow.faceCageLineEdit.text() != '':
            self.checkFaceCageValid()
        if self.uiWindow.lod0LineEdit.text() != '':
            self.checkFaceLOD0Valid()
        if self.uiWindow.lod1LineEdit.text() != '':
            self.checkFaceLOD1Valid()
    

    #------------------------------------------------------
    def tabChangedCallback(self):
        currentIndex = self.uiWindow.mainTabWidget.currentIndex()
        if currentIndex == 0:
            self.uiWindow.connectionMapStackedWidget.hide()
            self.resizeUIWindowSize(600, 650)
            #print '1'
        elif currentIndex == 1:
            self.uiWindow.connectionMapStackedWidget.hide()
            if self.uiWindow.AUListStackedWidget.currentIndex() == 0:
                self.resizeUIWindowSize(600, 650)
                #print '2'
            elif self.uiWindow.AUListStackedWidget.currentIndex() == 1:
                self.resizeUIWindowSize(750, 800)
                self.resizeUIWindowSize(750, 800)
                #print '3'

    #------------------------------------------------------
    def skipBuildConfirmBtnCallback(self):
        self.uiWindow.tipBuildWidget.hide()
        self.skipBuild = 1
        self.enablePrebuildFacialBase()
    
    def normalBuildProcessBtnCallback(self):
        self.uiWindow.tipBuildWidget.hide()
        self.skipBuild = 0
        self.enablePrebuildFacialBase()

    def confirmNamesAndSkipBuildCallback(self):
        self.uiWindow.confirmNamesBtn.hide()

        # create ctrl mode switch and AU reconnect
        self.addSliderControlModeCallback()

        # Set success
        self.setFACSBuildSuccess()

        # lock Names
        self.lockNamesCallback()

    #------------------------------------------------------
    def enablePrebuildFacialTarget(self):
        self.uiWindow.facialTargetLineEdit.setEnabled(True)
        self.uiWindow.facialTargetLineEdit.setReadOnly(False)
        self.uiWindow.facialTargetLineEdit.setStyleSheet("QLineEdit { background-color : #2b2b2b; }")
        self.uiWindow.importFacialTargetBtn.setEnabled(True)
        
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        nodeName = rigCharacterGrp + '.' + SERigNaming.sFACS_NameListAttr
        if cmds.objExists(nodeName):
            nameList = cmds.getAttr(nodeName)
            self.uiWindow.facialTargetLineEdit.setText(nameList[1])
            self.checkFacialTargetValid()
        else:
            res = cmds.ls(type = 'transform')
            similarityRes = self.getMostSimilarString('FacialTarget', res) 
            autoFillName = similarityRes[0]
            #print 'facialTarget:' + str(similarityRes[1])
            if autoFillName != '':
                self.uiWindow.facialTargetLineEdit.setText(autoFillName)
                self.checkFacialTargetValid()

    def enablePrebuildAUBase(self):
        self.uiWindow.auBaseLineEdit.setEnabled(True)
        self.uiWindow.auBaseLineEdit.setReadOnly(False)
        self.uiWindow.auBaseLineEdit.setStyleSheet("QLineEdit { background-color : #2b2b2b; }")
        self.uiWindow.importAUBaseBtn.setEnabled(True)
        
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        nodeName = rigCharacterGrp + '.' + SERigNaming.sFACS_NameListAttr
        if cmds.objExists(nodeName):
            nameList = cmds.getAttr(nodeName)
            self.uiWindow.auBaseLineEdit.setText(nameList[2])
            self.checkAUBaseValid()
        else:
            res = cmds.ls(type = 'transform')
            similarityRes = self.getMostSimilarString('AUBase', res)
            autoFillName = similarityRes[0]
            #print 'AUBase:' + str(similarityRes[1])
            if autoFillName != '' and similarityRes[1]>=0.75:
                self.uiWindow.auBaseLineEdit.setText(autoFillName)
                self.checkAUBaseValid()

    def enablePrebuildFacialBase(self):
        self.uiWindow.facialBaseLineEdit.setEnabled(True)
        self.uiWindow.facialBaseLineEdit.setReadOnly(False)
        #self.uiWindow.createFacialBaseBtn.setEnabled(True)
        self.uiWindow.facialBaseLineEdit.setStyleSheet("QLineEdit { background-color : #2b2b2b; }")
        self.uiWindow.importFacialBaseBtn.setEnabled(True)
        
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        nodeName = rigCharacterGrp + '.' + SERigNaming.sFACS_NameListAttr
        if cmds.objExists(nodeName):
            nameList = cmds.getAttr(nodeName)
            self.uiWindow.facialBaseLineEdit.setText(nameList[0])
            self.checkFacialBaseValid()
        else:
            res = cmds.ls(type = 'transform')
            similarityRes = self.getMostSimilarString('FacialBase', res)
            autoFillName = similarityRes[0]
            #print 'FacialBase:' + str(similarityRes[1])
            if autoFillName != '' and similarityRes[1]>=0.75:
                self.uiWindow.facialBaseLineEdit.setText(autoFillName)
                self.checkFacialBaseValid()        
        
    def enablePrebuildFaceCage(self):
        self.uiWindow.faceCageLineEdit.setEnabled(True)
        self.uiWindow.faceCageLineEdit.setReadOnly(False)
        self.uiWindow.faceCageLineEdit.setStyleSheet("QLineEdit { background-color : #2b2b2b; }")
        self.uiWindow.importFaceCageBtn.setEnabled(True)

        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        nodeName = rigCharacterGrp + '.' + SERigNaming.sFACS_NameListAttr
        if cmds.objExists(nodeName):
            nameList = cmds.getAttr(nodeName)
            self.uiWindow.faceCageLineEdit.setText(nameList[3])
            self.checkFaceCageValid()
        else:
            res = cmds.ls(type = 'transform')
            similarityRes = self.getMostSimilarString('FaceCage', res)
            autoFillName = similarityRes[0]
            #print 'FaceCage:' + str(similarityRes[1]         )
            if autoFillName != '' and similarityRes[1]>=0.75:
                self.uiWindow.faceCageLineEdit.setText(autoFillName)
                self.checkFaceCageValid()         

    def enablePrebuildLOD0(self):
        self.uiWindow.lod0LineEdit.setEnabled(True)
        self.uiWindow.lod0LineEdit.setReadOnly(False)
        self.uiWindow.lod0LineEdit.setStyleSheet("QLineEdit { background-color : #2b2b2b; }")
        if self.uiWindow.lod0LineEdit.text() != '':
            self.checkFaceLOD0Valid()
        
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        nodeName = rigCharacterGrp + '.' + SERigNaming.sFACS_NameListAttr
        if cmds.objExists(nodeName):
            nameList = cmds.getAttr(nodeName)
            self.uiWindow.lod0LineEdit.setText(nameList[4])
            self.checkFaceLOD0Valid()
        

    def enablePrebuildLOD1(self):
        self.uiWindow.lod1LineEdit.setEnabled(True)
        self.uiWindow.lod1LineEdit.setReadOnly(False)
        self.uiWindow.lod1LineEdit.setStyleSheet("QLineEdit { background-color : #2b2b2b; }")
        if self.uiWindow.lod1LineEdit.text() != '':
            self.checkFaceLOD1Valid()
        
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        nodeName = rigCharacterGrp + '.' + SERigNaming.sFACS_NameListAttr
        if cmds.objExists(nodeName):
            nameList = cmds.getAttr(nodeName)
            self.uiWindow.lod1LineEdit.setText(nameList[5])
            self.checkFaceLOD1Valid()       

    def enableAUConfig(self):        
        AUBaseName = self.uiWindow.auBaseLineEdit.text()
        bs = DeformerHelper.getConnectedInputBlendshapeNode(AUBaseName)
        if bs == None:
            self.uiWindow.auConnectWarnLabel.show()
            self.uiWindow.auConnectWarnLabel.setText('*Warning: Please add blendshapes to "%s" mesh first.'%AUBaseName)
            cmds.select(AUBaseName, r = True)
            if self.time_job_id == -1:
                self.createScriptJobForAUBlendShape()
        else:
            self.enableShowConnectMap()
            rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
            nodeName = rigCharacterGrp + '.' + SERigNaming.sFACS_NameListAttr
            if cmds.objExists(nodeName):
                if self.isAUConnectedSuccess():
                    self.enableBuild()
                    self.uiWindow.auConnectBtn.setText('Reconnect')
                    self.resizeUIWindowSize(600, 650) 
                    self.lockNamesCallback()  
            else:
                if not self.isRigBuiltByThisTool():
                    self.confirmNamesAndSkipBuildCallback()            
            
        
    def enableShowConnectMap(self):
        if self.uiWindow.mainTabWidget.currentIndex() == 1:
            return
        
        self.uiWindow.auConnectWarnLabel.hide()
        self.uiWindow.noneMapBtn.setEnabled(True)
        self.uiWindow.customMapBtn.setEnabled(True)
        self.uiWindow.auConnectBtn.setEnabled(True)

        self.uiWindow.connectionMapStackedWidget.setCurrentIndex(1)
        self.uiWindow.connectionMapStackedWidget.show()
        self.showDefaultConnectMap()
        self.switchConnectMapCallback()
    
    def disableShowConnectMap(self):
        if self.uiWindow.mainTabWidget.currentIndex() == 1:
            return
        
        self.uiWindow.auConnectWarnLabel.hide()
        self.uiWindow.noneMapBtn.setEnabled(False)
        self.uiWindow.customMapBtn.setEnabled(False)
        self.uiWindow.auConnectBtn.setEnabled(False)

        self.uiWindow.connectionMapStackedWidget.hide()
        self.resizeUIWindowSize(600,650)
        #print '4'

    def enableBuild(self):
        self.uiWindow.connectionMapStackedWidget.hide()
        self.uiWindow.facialBaseWeightImportComboBox.setEnabled(True)
        self.uiWindow.buildBtn.setEnabled(True)
        self.uiWindow.maxInfluenceSpinBox.setEnabled(True)
        
        #self.uiWindow.facialBaseWeightImportComboBox.addItem("None")
        faceWeightList = os.listdir(faceWeightFootFile)
        for weight in faceWeightList:
            if ".xml" not in weight and ".json" not in weight:
                faceWeightList.remove(weight)
            else:
                self.uiWindow.facialBaseWeightImportComboBox.addItem(weight)
        if len(faceWeightList) > 0:
            self.uiWindow.facialBaseWeightImportComboBox.setCurrentIndex(0)

    def createScriptJobForAUBlendShape(self):
        self.time_job_id = cmds.scriptJob(cu = True, e = ("idle", self.checkAUHasBlendShape))
    
    def checkAUHasBlendShape(self):
        if self.mask_bs != -1:
            return
        AUBaseName = self.uiWindow.auBaseLineEdit.text()
        if cmds.objExists(AUBaseName):
            bs = DeformerHelper.getConnectedInputBlendshapeNode(AUBaseName)
            if bs != None:
                self.enableShowConnectMap()
                print 'created blendshape'
                self.mask_bs = 1

    #-----------------------------------------------------
    def importFacialTargetCallback(self):
        before = set(cmds.ls(type = 'transform'))
        multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
        fileNamePath = cmds.fileDialog2(fm = 1, fileFilter = multipleFilters)[0]
        #cmds.file(fileNamePath, i = True, namespace = fileNamePath[:-3])
        namespace = 'facialTarget'
        cmds.file(fileNamePath, i = True, namespace = namespace)
        cmds.namespace(rm = namespace, mnp = True)
        after = set(cmds.ls(type = 'transform'))
        importedMeshes = after - before

        cmds.select(clear = True)
        if importedMeshes != {}:
            cmds.select(importedMeshes, add = True)
            DeformerHelper.batchRemovePrefix()
        
        after = set(cmds.ls(type = 'transform'))
        importedMeshes = after - before
        facialTargetName = ''
        for name in importedMeshes:
            facialTargetName = name
            break
        
        self.uiWindow.facialTargetLineEdit.setText(facialTargetName)
        self.checkFacialTargetValid()

    def importAUBaseCallback(self):
        before = set(cmds.ls(type = 'transform'))
        multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
        fileNamePath = cmds.fileDialog2(fm = 1, fileFilter = multipleFilters, startingDirectory = auRootFile)[0]
        
        fileType = fileNamePath[-3:]
        if fileType == '.ma':
            fileType = 'mayaAscii'
        elif fileType == 'mb':
            fileType = 'mayaBinary'
        split = fileNamePath.split('/')
        index = len(split) - 1
        fileName = split[index][:-3]

        namespace = 'AUs'
        cmds.file(fileNamePath, i = True, type = fileType, ignoreVersion = True, ra = True, mergeNamespacesOnClash = False, namespace = namespace) #, options = 'v=0;p=17;f=0', pr = True, itr = "combine"
        cmds.namespace(rm = namespace, mnp = True)
        after = set(cmds.ls(type = 'transform'))
        importedMeshes = after - before
        cmds.select(clear = True)
        if importedMeshes != {}:
            cmds.select(importedMeshes, add = True)
            DeformerHelper.batchRemovePrefix()
        after = set(cmds.ls(type = 'transform'))
        importedMeshes = after - before
        cmds.select(clear = True)
        for obj in importedMeshes:
            getShape = cmds.listRelatives(obj, shapes=True)
            if getShape != None:
                self.importedAU.append(obj)
            else:
                cmds.select(obj, add = True)
        sldel = cmds.ls(sl = True)

        newGrp = cmds.group(self.importedAU, n = 'ImportedAUGrp')
        similarityAUBase = self.getMostSimilarString('AUBase', self.importedAU)
        if similarityAUBase[1] > 0.7:
            self.uiWindow.auBaseLineEdit.setText(similarityAUBase[0])
            self.checkAUBaseValid()
        self.storeAUsToCustomMap()
        cmds.delete(sldel)

    def importFacialBaseCallback(self):
        before = set(cmds.ls(type = 'transform'))
        multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
        fileNamePath = cmds.fileDialog2(fm = 1, fileFilter = multipleFilters)[0]
        namespace = 'facialBase'
        cmds.file(fileNamePath, i = True, namespace = namespace)
        cmds.namespace(rm = namespace, mnp = True)
        after = set(cmds.ls(type = 'transform'))
        importedMeshes = after - before

        rigCharacterGroup = self.uiWindow.rigCharacterGrpLineEdit.text()
        cmds.parent(importedMeshes, rigCharacterGroup)

        cmds.select(clear = True)
        if importedMeshes != {}:
            cmds.select(importedMeshes, add = True)
            DeformerHelper.batchRemovePrefix()

        after = set(cmds.ls(type = 'transform'))
        importedMeshes = after - before
        for name in importedMeshes:
            self.uiWindow.facialBaseLineEdit.setText(name)
            self.checkFacialBaseValid()
            break

    def importFaceCageCallback(self):
        before = set(cmds.ls(type = 'transform'))
        multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
        fileNamePath = cmds.fileDialog2(fm = 1, fileFilter = multipleFilters, startingDirectory = faceCageRootFile)[0]
        namespace = 'FaceCage'
        #print namespace
        cmds.file(fileNamePath, i = True, namespace = namespace)
        cmds.namespace(rm = namespace, mnp = True)
        after = set(cmds.ls(type = 'transform'))
        importedMeshes = after - before

        cmds.select(clear = True)
        if importedMeshes != {}:
            cmds.select(importedMeshes, add = True)
            DeformerHelper.batchRemovePrefix()

        after = set(cmds.ls(type = 'transform'))
        importedMeshes = after - before
        for name in importedMeshes:
            self.uiWindow.faceCageLineEdit.setText(name)
            self.checkFaceCageValid()
            break

    def createFacialBaseFromAUBase(self):
        auBase = self.uiWindow.auBaseLineEdit.text()
        if cmds.objExists(auBase):
            res = cmds.duplicate( auBase, rr = True, n = 'facialBase' )
            self.uiWindow.facialBaseLineEdit.setText(res[0])
            self.checkFacialBaseValid()

    #-----------------------------------------------------
    # getRigCharacterGroupName
    def getRigCharacterName(self):
        try:
            characterGrpName = RigObjectTypeHelper.listRigCharacterGroups()[0]
            return characterGrpName
        except:
            cmds.warning('No Rig Character Group found. Please check your file.')
            return []
    
    #-----------------------------------------------------
    def storeAUsToCustomMap(self, tokenSeparator = '_'):
        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(characterRigGrp)
        customMapBuffer = FacsHelper.getFACS_CustomConnectionMapBuffer(facialComponent)

        for name in self.importedAU:
            res = self.getMostSimilarString(name, SERigNaming.auAttrList)
            if res[1] >= 0.7:
                key = res[0]
                attrName = customMapBuffer + '.' + key
                if cmds.getAttr(attrName) == '' or cmds.getAttr(attrName) == None:
                    cmds.setAttr(attrName, name, type = 'string')

    #-----------------------------------------------------
    def compareSimilarStringByNumberOrder(self, matchName, string1, string2):
        resString = string1
        matchNum = re.sub("\D", "", matchName)
        num1 = re.sub("\D", "", string1)
        num2 = re.sub("\D", "", string2)
        if not matchNum:
            return resString
        if not num1:
            if num2:
                resString = string2
                return resString
            else:
                return resString
        else:
            if not num2:
                return resString
            else:                
                if abs(int(num1) - int(matchNum)) < abs(int(num2) - int(matchNum)):
                    resString = string1
                else:
                    resString = string2
                
                return resString 

    def string_similarity(self, string1, string2):
        return difflib.SequenceMatcher(None, string1, string2).quick_ratio()
    
    def getMostSimilarString(self, matchName, compareList):
        maxSim = 0
        maxName = ''
        maxSameNameList = []
        for name in compareList:
            value = self.string_similarity(name, matchName)
            if value > maxSim:
                maxSim = value
                maxName = name
            elif value == maxSim:
                res = self.compareSimilarStringByNumberOrder(matchName, maxName, name)
                if res == name:
                    maxName = name
                    maxSim = value

        return [maxName, maxSim]

    #---------------------------------------------------------------------------------------- 
    # Iniate All the CallBack Function of Buttons
    def setButtonsCallBack(self):
       
        #"AU Connect" button
        self.uiWindow.auConnectBtn.clicked.connect(self.auConnectBtnCallback)

        #"Build" button
        self.uiWindow.buildBtn.clicked.connect(self.buildBtnCallback)

        #define labels
        self.uiWindow.facialTargetLineEdit.textChanged.connect(self.checkFacialTargetValid)
        self.uiWindow.auBaseLineEdit.textChanged.connect(self.checkAUBaseValid)
        self.uiWindow.facialBaseLineEdit.textChanged.connect(self.checkFacialBaseValid)
        self.uiWindow.faceCageLineEdit.textChanged.connect(self.checkFaceCageValid)
        self.uiWindow.lod0LineEdit.textChanged.connect(self.checkFaceLOD0Valid)
        self.uiWindow.lod1LineEdit.textChanged.connect(self.checkFaceLOD1Valid)

        #"Import" buttons
        self.uiWindow.importFacialTargetBtn.clicked.connect(self.importFacialTargetCallback)
        self.uiWindow.importAUBaseBtn.clicked.connect(self.importAUBaseCallback)
        self.uiWindow.importFacialBaseBtn.clicked.connect(self.importFacialBaseCallback)
        self.uiWindow.importFaceCageBtn.clicked.connect(self.importFaceCageCallback)
        
        #self.uiWindow.createFacialBaseBtn.clicked.connect(self.createFacialBaseFromAUBase)

        #"Control Mode" button
        self.uiWindow.controllerRadioBtn.clicked.connect(self.switchContrlModeCallback)
        self.uiWindow.sliderRadioBtn.clicked.connect(self.switchContrlModeCallback)

        #Switch connect map button 
        self.uiWindow.noneMapBtn.clicked.connect(self.switchConnectMapCallback)
        self.uiWindow.customMapBtn.clicked.connect(self.switchConnectMapCallback)

        #"OK" confirm map button
        #self.uiWindow.confirmMapBtn.clicked.connect(self.confirmConnectMapCallback)

        #"Export" connect map button
        self.uiWindow.exportMapBtn.clicked.connect(self.exportCustomConnectMap)

        #"Import" connect map button
        self.uiWindow.importMapBtn.clicked.connect(self.importCustomConnectMap)

        #"Hide Show Custom Map" button
        #self.uiWindow.hideShowBuildPageBtn.clicked.connect(self.hideShowBuildPage)

        #"auto fill" button
        self.uiWindow.autoFillAUBtn.clicked.connect(self.autoFillCustomAUsCallback)
        self.uiWindow.clearAUBtn.clicked.connect(self.clearCustomAUsCallback)

        #"Arrange AUs" button
        self.uiWindow.arrangeAUBtn.clicked.connect(self.arrangeAUsCallback)
        self.uiWindow.offsetLineEdit.returnPressed.connect(self.changeArrangeOffsetCallback)
        self.uiWindow.offsetLineEdit.setValidator(QtGui.QDoubleValidator())

        #"Remove Facial Subjoint Controllers" button
        self.uiWindow.removeSubJointBtn.clicked.connect(self.batchRemoveSubJointControllersCallback)

        #"Remove Prefix" button
        self.uiWindow.removePrefixBtn.clicked.connect(self.batchRemovePrefixBtnCallback)

        #"Update Symmetrical BS For AU" button
        self.uiWindow.updateSymAUBtn.clicked.connect(self.updateSymAUCallback)
        self.uiWindow.updateSymFaceBtn.clicked.connect(self.updateSymFaceCallback)

        #"display switch" 
        self.uiWindow.auNameRadioBtn.clicked.connect(self.updateSliderAUList)
        self.uiWindow.aliasRadioBtn.clicked.connect(self.updateSliderAUList)
        self.uiWindow.meshNameRadioBtn.clicked.connect(self.updateSliderAUList)
        
        #MainTab
        self.uiWindow.mainTabWidget.currentChanged.connect(self.tabChangedCallback)

        #"Add AU Control Mode" button
        self.uiWindow.yesBuiltBtn.clicked.connect(self.skipBuildConfirmBtnCallback)
        self.uiWindow.noBuiltBtn.clicked.connect(self.normalBuildProcessBtnCallback)
        self.uiWindow.confirmNamesBtn.clicked.connect(self.confirmNamesAndSkipBuildCallback)

        #'Help' Buttons
        self.uiWindow.facialBaseHelpBtn.clicked.connect(functools.partial(self.popHelpWindow, 0))
        self.uiWindow.facialTargetHelpBtn.clicked.connect(functools.partial(self.popHelpWindow, 1))
        self.uiWindow.faceCageBtn.clicked.connect(functools.partial(self.popHelpWindow, 3))
    
    #------------------------------ Pop Help Window Related ------------------------------
    def popHelpWindow(self, showType):
        global popHelp
        if popHelp != None:
            popHelp.close()
        
        popHelp = PopHelpWidget()
        popHelp.resize(500, 600)
        popHelp.show()

        if showType == 0:
            popHelp.imageBG.setPixmap(QtGui.QPixmap((uiRootFile +"/Help_FacialBase.png")))
        elif showType == 1:
            popHelp.imageBG.setPixmap(QtGui.QPixmap((uiRootFile +"/Help_FacialTarget.png")))
        elif showType == 2:
            popHelp.imageBG.setPixmap(QtGui.QPixmap((uiRootFile +"/Help_FacialBase.png")))
        elif showType == 3:
            popHelp.imageBG.setPixmap(QtGui.QPixmap((uiRootFile +"/Help_FaceCage.png")))

    #----------------------------------- Build Related -----------------------------------
    # Define Callback: AU Connect Button
    def auConnectBtnCallback(self):
        if self.isAUConnectedSuccess():
            self.disconnectAUConnection()
        else:
            self.createAUandFaceCleanMesh()
        
        self.uiWindow.connectionMapStackedWidget.hide()  

        cmds.select(clear = True)
        AUBaseName = self.uiWindow.auBaseLineEdit.text()
        FacialBaseName = self.uiWindow.facialBaseLineEdit.text() 
        cmds.select(FacialBaseName, r = True)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        cmds.select(clear = True)

        # match source to target
        cmds.select(AUBaseName, r = True)
        cmds.select(FacialBaseName, add = True)
        DeformerHelper.matchSourceBlendshapesToTarget()

        if self.uiWindow.noneMapBtn.isChecked():
            DeformerHelper.connectFACSDataBufferToAUBlendshape()
        else:
            self.confirmConnectMapCallback()
            characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
            facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(characterRigGrp)
            customMapBuffer = FacsHelper.getFACS_CustomConnectionMapBuffer(facialComponent)
            customMap = {}
            for auType in DeformerHelper.facialActionUnitTypeList:
                key = SERigNaming.auAttrList[auType]
                value = cmds.getAttr(customMapBuffer + '.' + key)
                customMap[key] = value
            DeformerHelper.connectFACSDataBufferToAUBlendshape(customMap)

      
        self.uiWindow.auConnectBtn.setText('Reconnect')
        self.enableBuild()
        self.lockNamesCallback()
        self.resizeUIWindowSize(600, 650) 
        #print '5'          

    def disconnectAUConnection(self):
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(rigCharacterGrp)
        controlMode = FacsHelper.getFACS_ControlMode(facialComponent)
        if not cmds.objExists("{}.{}".format(controlMode, SERigNaming.sFACS_AUConnectedAttr)):
            return
        
        res = cmds.listConnections("{}.{}".format(controlMode, SERigNaming.sFACS_AUConnectedAttr))
        if res:
            linkedAttr = SERigNaming.sFACS_AUConnectedAttr + SERigNaming.sOwnerSuffix
            deleteList = []
            facsDataBuffer = FacsHelper.getFACS_DataBuffer(facialComponent)
            for auType in DeformerHelper.facialActionUnitTypeList:
                key = SERigNaming.auAttrList[auType]
                srcCtrlData = FacsHelper.getFacialActionUnitAttrName(facsDataBuffer, auType)   
                if srcCtrlData:
                    condition = cmds.listConnections(srcCtrlData, type = 'condition')
                    if condition != None:
                        clamp = cmds.listConnections("{}.{}".format(condition[0], 'outColorR'), type = 'clamp')
                        if clamp != None:
                            deleteList.append(condition[0])
                            deleteList.append(clamp[0])

            cmds.delete(deleteList)
            cmds.deleteAttr(controlMode, at = SERigNaming.sFACS_AUConnectedAttr)
            cmds.deleteAttr(res, at = linkedAttr)


    # Define Callback: Face Rig Build
    def buildBtnCallback(self):
        facialTargetName = self.uiWindow.facialTargetLineEdit.text()
        auBaseName = self.uiWindow.auBaseLineEdit.text()
        rigGroupName = self.uiWindow.rigCharacterGrpLineEdit.text()
        facialBaseName = self.uiWindow.facialBaseLineEdit.text()
        faceCageName = self.uiWindow.faceCageLineEdit.text()
        lod1Name = self.uiWindow.lod1LineEdit.text()
        lod0Name = self.uiWindow.lod0LineEdit.text()
        # Pre 1: update Names Match First
        if self.isNamesValid() == False:
            cmds.warning("Please check the Pre-build Area names again.")
            return

        #Pre 2: Freeze Face Cage
        #cmds.select(faceCageName, r = True)
        #cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        #cmds.select(clear = True)
        try:
            #Step 1: Blend Shape-AU Base & Facial Target
            cmds.select(auBaseName, r = True)
            cmds.select(facialTargetName, add = True)
            cmds.select(facialBaseName, add = True)
            cmds.blendShape(w=[(0, 1), (1, 1)])
        
            #Step 2: Select Skeletons
            cmds.select(rigGroupName, r = True)
            jnts = JointHelper.getSlaveFacialBaseJointsFromSelectedRigCharacterGroup()
            cmds.select(jnts, r = True)

            #Step 3: Bind Skin For FacialBase
            cmds.select(self.uiWindow.facialBaseLineEdit.text(), add = True)
            cmds.skinCluster(tsb=True, bm=0, sm=0, nw=1)
        
            #Step 4: Import Deformer Weight into FacialBase Skin Cluster
            faceCluster = mel.eval('findRelatedSkinCluster ' + facialBaseName)
            faceWeightFileName = self.uiWindow.facialBaseWeightImportComboBox.itemText(self.uiWindow.facialBaseWeightImportComboBox.currentIndex())
            if faceWeightFileName != None:
                faceWeightFilePath = faceWeightFootFile + faceWeightFileName
                cmds.deformerWeights(faceWeightFileName, p = faceWeightFootFile, im = True, deformer = faceCluster)  

            #Step 5: Triangulate FacialBase To FacialBaseTri and add blendshape
            faceTriName = cmds.duplicate(facialBaseName, n = facialBaseName + "Tri")[0]
            cmds.polyTriangulate(faceTriName)
            cmds.select(facialBaseName, r = True)
            cmds.select(faceTriName, add = True)
            cmds.blendShape(w=[(0, 1)])

            #Step 6: Create FacialSkin Proxy Joints&Controllers; and Rivet them to FacialBaseTri Mesh
            cmds.select(faceCageName, r = True)
            cmds.select(lod1Name, add = True)
            maxInfluence = self.uiWindow.maxInfluenceSpinBox.value()
            SERigHumanFacialComponent.createFacialSkinProxyJointsAndControlsFromSelection(maxInfluence, False, 0.2)
            SERigHumanFacialComponent.createFacialProxyControlRivetConstraints(faceTriName, rigGroupName)

            #Step 7: Create 
            print "Build Success."

            #Step 8: Mark Success For Rig Character Grp
            self.setFACSBuildSuccess()

        except Exception as e:
            print e
            cmds.warning('Build Failed.')
            return

    # Check if All the names are matched with meshes in the scene
    def isNamesValid(self):
        res = []
        res.append( cmds.objExists(self.uiWindow.facialTargetLineEdit.text()) )
        res.append( cmds.objExists(self.uiWindow.auBaseLineEdit.text()) )
        res.append( cmds.objExists(self.uiWindow.facialBaseLineEdit.text()) )
        res.append( cmds.objExists(self.uiWindow.faceCageLineEdit.text()) )
        res.append( cmds.objExists(self.uiWindow.lod0LineEdit.text()) )
        res.append( cmds.objExists(self.uiWindow.lod1LineEdit.text()) )
        
        for r in res:
            if r == False:
                return False
        
        return True
    
    # switch the layout of the UI after build success
    def layoutDefaultBuildSuccess(self):
        self.enableBuildTab(False)
        self.uiWindow.mainTabWidget.setCurrentIndex(1)
        self.uiWindow.connectionMapStackedWidget.hide()
        if self.uiWindow.AUListStackedWidget.currentIndex() == 0:
            self.resizeUIWindowSize(600, 650)
            #print '6'
        else:
            self.resizeUIWindowSize(750, 800)
    
    def enableBuildTab(self, boolValue):
        self.uiWindow.importFacialTargetBtn.setEnabled(boolValue)
        self.uiWindow.importAUBaseBtn.setEnabled(boolValue)
        self.uiWindow.importFacialBaseBtn.setEnabled(boolValue)
        self.uiWindow.importFaceCageBtn.setEnabled(boolValue)
        self.uiWindow.maxInfluenceSpinBox.setEnabled(boolValue)
        self.uiWindow.facialTargetLineEdit.setEnabled(boolValue)
        self.uiWindow.auBaseLineEdit.setEnabled(boolValue)
        self.uiWindow.facialBaseLineEdit.setEnabled(boolValue)
        self.uiWindow.faceCageLineEdit.setEnabled(boolValue)
        self.uiWindow.lod0LineEdit.setEnabled(boolValue)
        self.uiWindow.lod1LineEdit.setEnabled(boolValue)
        self.uiWindow.noneMapBtn.setEnabled(boolValue)
        self.uiWindow.customMapBtn.setEnabled(boolValue)
        self.uiWindow.auConnectBtn.setEnabled(boolValue)
        self.uiWindow.facialBaseWeightImportComboBox.setEnabled(boolValue)
        self.uiWindow.buildBtn.setEnabled(boolValue)
    
    def enableAUManagerTab(self, boolValue):
        self.hideAUSliders()
        self.uiWindow.controllerRadioBtn.setEnabled(boolValue)
        self.uiWindow.sliderRadioBtn.setEnabled(boolValue)
        self.uiWindow.auNameRadioBtn.setEnabled(boolValue)
        self.uiWindow.aliasRadioBtn.setEnabled(boolValue)
        self.uiWindow.meshNameRadioBtn.setEnabled(boolValue)
        self.uiWindow.arrangeAUBtn.setEnabled(boolValue)
        self.uiWindow.updateSymAUBtn.setEnabled(boolValue)
        self.uiWindow.updateSymFaceBtn.setEnabled(boolValue)
        self.uiWindow.cleanAULineEdit.setEnabled(boolValue)
        self.uiWindow.cleanFaceLineEdit.setEnabled(boolValue)
        self.uiWindow.removeSubJointBtn.setEnabled(boolValue)
        self.uiWindow.offsetLineEdit.setEnabled(boolValue)
    
    def setFACSBuildSuccess(self):
        self.layoutDefaultBuildSuccess()
        self.synAUList()
        self.enableAUManagerTab(True)
        
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        nodeName = rigCharacterGrp + '.' + SERigNaming.sFACS_BuildSuccessAttr
        cmds.select(rigCharacterGrp, r = True)
        if cmds.objExists(nodeName):
            cmds.setAttr(nodeName, 1)
        else:
            cmds.addAttr(longName = SERigNaming.sFACS_BuildSuccessAttr, dv = 1)

        nodeName2 = rigCharacterGrp + '.' + SERigNaming.sFACS_NameListAttr
        if cmds.objExists(nodeName2):
            auClean = cmds.getAttr(nodeName2)[6]
            faceClean = cmds.getAttr(nodeName2)[7]
            self.uiWindow.cleanAULineEdit.setText(auClean)
            self.uiWindow.cleanFaceLineEdit.setText(faceClean)
    
    def fillPrebuildNamesByCache(self):
        name = self.uiWindow.rigCharacterGrpLineEdit.text()
        nodeName = name + '.' + SERigNaming.sFACS_NameListAttr
        nameList = cmds.getAttr(nodeName)
        self.uiWindow.facialBaseLineEdit.setText(nameList[0])
        self.uiWindow.facialTargetLineEdit.setText(nameList[1])
        self.uiWindow.auBaseLineEdit.setText(nameList[2])
        
        self.uiWindow.faceCageLineEdit.setText(nameList[3])
        self.uiWindow.lod0LineEdit.setText(nameList[4])
        self.uiWindow.lod1LineEdit.setText(nameList[5])
        self.uiWindow.cleanAULineEdit.setText(nameList[6])
        self.uiWindow.cleanFaceLineEdit.setText(nameList[7])

    #----------------------------------- Delete Event ------------------------------------
    # Close Window Event
    def closeEvent(self, event):
        '''
        reply = QtWidgets.QMessageBox.question(self,
            'FACS MANAGER',
            "Do you want to Exit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        '''
        self.killScriptJobForAUWeight()
        self.killScriptJobForNameDelete()

        if self.isRigBuiltByThisTool():
            self.confirmConnectMapCallback()
        
        if cmds.scriptJob(ex = self.mode_job_id):
            cmds.scriptJob(kill = self.mode_job_id)

        if cmds.scriptJob(ex = self.time_job_id):
            cmds.scriptJob(kill = self.time_job_id, force = True)

        if cmds.scriptJob(ex = self.nameChange_job_id):
            cmds.scriptJob(kill = self.nameChange_job_id, force = True)

    #----------------------------------- AU Related --------------------------------------
    # Synchronize items in AU List
    def synAUList(self):
        # Get AU Object Name From ConnectMap
        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        auBaseObj = self.uiWindow.auBaseLineEdit.text()

        # toolUsed = True
        # # Check if the FACS is built without using FACS build tool
        # if not self.isRigBuiltByThisTool():
        #     toolUsed = False
        
        # Make Sure AU Base Name Correct
        if not cmds.ls(auBaseObj):
            cmds.warning("Please enter the correct AUBase Name.")
            return
        
        # Make Sure AUBase Mesh Has Input BlendShape Node
        #if  toolUsed:
        auBlendShapeNode = DeformerHelper.getConnectedInputBlendshapeNode(auBaseObj)
        if auBlendShapeNode == None:
            cmds.warning('Cannot Find BlendShape node in AuBase.')
            return

        # Get FACS Ctrl DATA & AU DATA
        try:
            facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(characterRigGrp)
            facsCtrlBuffer = FacsHelper.getFACS_DataBuffer(facialComponent)
            facsAUBuffer = FacsHelper.getFACS_AUBuffer(facialComponent)
            controlMode = FacsHelper.getFACS_ControlMode(facialComponent)
            customMapBuffer = FacsHelper.getFACS_CustomConnectionMapBuffer(facialComponent)
        except Exception as e:
            print e
            return

        # Make Sure AU Has Connected
        try:
            res = cmds.listConnections("{}.{}".format(controlMode, SERigNaming.sFACS_AUConnectedAttr))
            if res == None:
                cmds.warning('Data Buffer has not been connected to AU Blendshape. ')
                return
        except:
            cmds.warning('Data Buffer has not been connected to AU Blendshape. ')
            return

        # Read buffer node info according to control mode    
        self.ctrlDataList = {}
        self.auDataList = {}
        connectMap = {}
        
        if not self.isAUConnectedSuccess():
            if self.uiWindow.noneMapBtn.isChecked():
                connectMap = DeformerHelper.dataBufferAUsToBlendshapeAUsTable
            elif self.uiWindow.customMapBtn.isChecked():
                connectMap = DeformerHelper.dataBufferAUsToBlendshapeAUsTable
                for name in connectMap:
                    connectMap[name] = cmds.getAttr(customMapBuffer + '.' + name)
        else:
            isUsingCustom = cmds.getAttr(controlMode + '.' + SERigNaming.sFACS_IsUsingCustomMapAttr)
            #print isUsingCustom
            if not isUsingCustom:
                connectMap = DeformerHelper.dataBufferAUsToBlendshapeAUsTable
                #print 'default map'
            else:
                connectMap = DeformerHelper.dataBufferAUsToBlendshapeAUsTable
                for name in connectMap:
                    connectMap[name] = cmds.getAttr(customMapBuffer + '.' + name)
                    #print connectMap[name]
                #print 'custom map'

        for auType in DeformerHelper.facialActionUnitTypeList:
            key = SERigNaming.auAttrList[auType]
            value = connectMap[key]
            alias = DeformerHelper.AUsAliasTable[key]

            ctrlData = [FacsHelper.getFacialActionUnitAttrName(facsCtrlBuffer, auType), alias, key]
            auData =  [FacsHelper.getFacialActionUnitAttrName(facsAUBuffer, auType), alias, key]

            bsTargetName = DeformerHelper.getBlendshapTargetNameByMatchName(auBlendShapeNode, value, True)
            if bsTargetName and ctrlData and auData:
                self.auDataList[value] = auData
                self.ctrlDataList[value] = ctrlData

        # Show AUs
        if self.uiWindow.controllerRadioBtn.isChecked():
            self.showControllerAUList()
        else: 
            self.showSliderAUList()



    def createScriptJobForSwitchControlMode(self):
        if not self.isRigBuiltByThisTool():
            return

        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(characterRigGrp)
        controlModeGrp = FacsHelper.getFACS_ControlMode(facialComponent)
        if controlModeGrp == None:
            return

        self.mode_job_id = cmds.scriptJob(attributeChange = ["{}.{}".format(controlModeGrp, SERigNaming.sFACS_ControlModeAttr), self.updateControlModeDisplay])

    # When the mode in MainCtrl Changes, it also changes
    def updateControlModeDisplay(self):
        if not self.isRigBuiltByThisTool():
            return

        if not self.isAUConnectedSuccess():
            return
        
        #print 'trigger'
        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(characterRigGrp)
        controlModeGrp = FacsHelper.getFACS_ControlMode(facialComponent)

        mode = cmds.getAttr(controlModeGrp + '.' + SERigNaming.sFACS_ControlModeAttr)
        if mode == 1:
            self.uiWindow.controllerRadioBtn.setChecked(True)
            self.killScriptJobForAUWeight()
            self.facsControlMode = 1
            if self.uiWindow.mainTabWidget.currentIndex() == 1:
                self.synAUList()
        elif mode == 0:
            self.uiWindow.sliderRadioBtn.setChecked(True)
            self.killScriptJobForAUWeight()
            self.facsControlMode = 0
            if self.uiWindow.mainTabWidget.currentIndex() == 1:
                self.synAUList()

    def showOnlyControllerMode(self):
        #self.uiWindow.addSliderControlModeBtn.show()
        self.uiWindow.sliderRadioBtn.hide()
        self.uiWindow.sliderRadioBtn.setEnabled(False)
        self.uiWindow.controllerRadioBtn.setEnabled(False)

    # If the file is not built by FACS tool before, then need to add control mode switch manually
    def addSliderControlModeCallback(self):
        rigCharacterGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(rigCharacterGrp)
        
        AUBaseName = self.uiWindow.auBaseLineEdit.text()
        FacialBaseName = self.uiWindow.facialBaseLineEdit.text() 
        
        auBlendShape = DeformerHelper.getConnectedInputBlendshapeNode(AUBaseName)
        if auBlendShape == None:
            cmds.warning('Cannot Find BlendShape node in AuBase.')
            return

        # Firstly, disconnect the link between BlendShapes and FACS_Data_Buffer
        facsDataBuffer = FacsHelper.getFACS_DataBuffer(facialComponent)
        for auType in DeformerHelper.facialActionUnitTypeList:
            key = SERigNaming.auAttrList[auType]
            value = DeformerHelper.dataBufferAUsToBlendshapeAUsTable[key]
            srcCtrlData = FacsHelper.getFacialActionUnitAttrName(facsDataBuffer, auType)   
            if srcCtrlData:
                #cmds.disconnectAttr(srcCtrlData, auBlendShape + '.' +)
                bsNode = DeformerHelper.getBlendshapTargetNameByMatchName(auBlendShape, value, True)
                if bsNode:
                    print bsNode
                    try:
                        cmds.disconnectAttr(srcCtrlData, bsNode)
                    except:
                        pass

        # Secondly, create AUBuffer and Control Mode Switch Node and Custom Data Map
        if FacsHelper.getFACS_AUBuffer(facialComponent) == None:
            SERigHumanFacialComponent.createFACS_AUBuffer(facialComponent)
        if FacsHelper.getFACS_ControlMode(facialComponent) == None:
            SERigHumanFacialComponent.createFACS_ControlModeSwitch(facialComponent)
        if FacsHelper.getFACS_CustomConnectionMapBuffer(facialComponent) == None:
            SERigHumanFacialComponent.createCustomConnectionMapBuffer(facialComponent)

        # Thirdly, connect data and blendshape
        cmds.select(AUBaseName, r = True)
        cmds.select(FacialBaseName, add = True)
        DeformerHelper.connectFACSDataBufferToAUBlendshape()

        # Fourthly, create clean meshes
        self.createAUandFaceCleanMesh()

        # Fifthly, update UI layout
        self.uiWindow.sliderRadioBtn.show()
        self.uiWindow.sliderRadioBtn.setEnabled(True)
        self.uiWindow.controllerRadioBtn.setEnabled(True)

        # add script Job
        if self.mode_job_id == -1:
            self.createScriptJobForSwitchControlMode()
        

    # Define Callback: Switch Control Mode
    def switchContrlModeCallback(self):
        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        if not cmds.objExists(characterRigGrp):
            cmds.warning('Switch Failed.')
            return
        characterName = RigObjectTypeHelper.getRigCharacterName(characterRigGrp)
        mainCtrl = RigObjectTypeHelper.getRigGlobalControlObject(characterName, u'RS_Center', u'RT_Global',0)
        self.facsControlMode = cmds.getAttr(mainCtrl + '.' + SERigNaming.sFACS_ControlModeAttr)
        if mainCtrl:
            if self.uiWindow.controllerRadioBtn.isChecked():
                cmds.setAttr(mainCtrl + '.' + SERigNaming.sFACS_ControlModeAttr, 1)
                self.resizeUIWindowSize(600, 650)
                #print '7'

            elif self.uiWindow.sliderRadioBtn.isChecked():
                cmds.setAttr(mainCtrl + '.' + SERigNaming.sFACS_ControlModeAttr, 0)
                self.resizeUIWindowSize(750, 800)
                self.resizeUIWindowSize(750, 800)

    def showControllerAUList(self):
        self.resizeUIWindowSize(600, 650)
        self.uiWindow.auListTreeWidget.clear()
        #print 'len:' + str(len(self.ctrlDataList))
        for name in self.ctrlDataList:
            weightNodeName = self.ctrlDataList[name][0]
            alias = self.ctrlDataList[name][1]
            item = CustomAUListItem(self.uiWindow.auListTreeWidget, name, alias, weightNodeName, 1)
        for column in range(self.uiWindow.auListTreeWidget.columnCount()):
            self.uiWindow.auListTreeWidget.resizeColumnToContents(column)
        
        self.uiWindow.AUListStackedWidget.setCurrentIndex(0)

    def showSliderAUList(self):
        '''
        self.uiWindow.auListTreeWidget.clear()
        for name in self.auDataList:
            weightNodeName = self.auDataList[name][0]
            alias = self.auDataList[name][1]
            item = CustomAUListItem(self.uiWindow.auListTreeWidget, name, alias, weightNodeName, 0)
        
        for column in range(self.uiWindow.auListTreeWidget.columnCount()):
            self.uiWindow.auListTreeWidget.resizeColumnToContents(column)
        '''
        self.resizeUIWindowSize(750, 800)
        self.resizeUIWindowSize(750, 800)
        self.uiWindow.AUListStackedWidget.setCurrentIndex(1)
        self.updateSliderAUList()

    def updateSliderAUList(self):
        self.hideAUSliders()
        for meshName in self.auDataList:
            weightNodeName = self.auDataList[meshName][0]
            alias = self.auDataList[meshName][1]
            auName = self.auDataList[meshName][2]
            sliderName = auName + 'Slider'

            # get display mode
            displayName = auName
            if self.uiWindow.auNameRadioBtn.isChecked():
                displayName = auName
            elif self.uiWindow.meshNameRadioBtn.isChecked():
                displayName = meshName
            elif self.uiWindow.aliasRadioBtn.isChecked():
                displayName = alias
                if alias == '' or alias == None:
                    displayName = '*' + auName
            
            if displayName[-1] == 'L' or displayName[-1] == 'R':
                displayName = displayName[:-1]
                if displayName[-1] == '_':
                    displayName = displayName[:-1]
                    
            # get weight
            weight = abs(cmds.getAttr(weightNodeName))
            sValue = weight * 100

            # show used au sliders
            try:
                exec("{}.{}.{}.{}".format('self', 'uiWindow', sliderName, 'show()'))
                exec("{}.{}.{}.{}({})".format('self', 'uiWindow', sliderName, 'setValue', sValue))
                exec("{}.{}.{}({}({},{},{}))".format('self.uiWindow', sliderName, 'valueChanged.connect', 'functools.partial', 'self.auSliderValueChange', 'weightNodeName', 'sliderName'))
                #print "{}.{}.{}({}({},{},{}))".format('self.uiWindow', sliderName, 'valueChanged.connect', 'functools.partial', 'self.auSliderValueChange', 'weightNodeName', 'sliderName')
                try:
                    exec("{}.{}.{}.{}".format('self', 'uiWindow', auName, 'show()'))
                    try:
                        exec("{}.{}.{}.{}({})".format('self', 'uiWindow', auName, 'setText', 'displayName'))
                    except:
                        pass
                except:
                    side = auName[-1]
                    if side == 'L':
                        side = 'R'
                    elif side == 'R':
                        side = 'L'    
                    symName = auName[:-1] + side
                    try:
                        exec("{}.{}.{}.{}".format('self', 'uiWindow', symName, 'show()'))
                        try:
                            exec("{}.{}.{}.{}({})".format('self', 'uiWindow', symName, 'setText', 'displayName'))
                        except:
                            pass
                    except:
                        pass
            except Exception as e:
                #print auName
                print e
                pass
            
            
    def auSliderValueChange(self, weightNode, sliderName, *args):
        getSliderValueStr = "{} = {}.{}.{}".format('sliderValue', 'self.uiWindow', sliderName, 'value()')
        exec(getSliderValueStr)
        weightValue = sliderValue * 0.01
        cmds.setAttr(weightNode, weightValue)


    def autoFillCustomAUsCallback(self):
        self.uiWindow.customConnectMapTreeWidget.clear()
        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(characterRigGrp)
        customMapBuffer = FacsHelper.getFACS_CustomConnectionMapBuffer(facialComponent)

        auBase = self.uiWindow.auBaseLineEdit.text()
        blsNode = cmds.listConnections(auBase + '.inMesh')
        if blsNode:
            blsNode = blsNode[0]
            attr = blsNode + '.w[{}]'
            weightCount = cmds.blendShape(blsNode, q = True, wc = True)
            for index in xrange(weightCount):
                aliasName = cmds.aliasAttr(attr.format(index), q = True)
                res = self.getMostSimilarString(aliasName, SERigNaming.auAttrList)
                if res[1] >= 0.7:
                    cmds.setAttr(customMapBuffer + '.' + res[0], aliasName, type = 'string')
                    if not cmds.objExists(aliasName):
                        nameInScene = self.findClosestNameInScene(aliasName, 0.9)
                        if nameInScene:
                            cmds.setAttr(customMapBuffer + '.' + res[0], nameInScene, type = 'string')
                else:
                    lastName = cmds.getAttr(customMapBuffer + '.' + res[0])
                    if lastName == '' or lastName == None:
                        cmds.setAttr(customMapBuffer + '.' + res[0], '', type = 'string')
            
            self.showCustomConnectMap()
        else:
            cmds.warning("AutoFill Failed: Fail to find blendshape Node in AUBase Mesh")
            return

    def clearCustomAUsCallback(self):
        self.uiWindow.customConnectMapTreeWidget.clear()
        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(characterRigGrp)
        customMapBuffer = FacsHelper.getFACS_CustomConnectionMapBuffer(facialComponent)

        for autype in DeformerHelper.facialActionUnitTypeList:
            key = SERigNaming.auAttrList[autype]
            value = ''
            alias = DeformerHelper.AUsAliasTable[key]
            item = CustomConnectionMapItem(self.uiWindow.customConnectMapTreeWidget, key, alias, value)
            cmds.setAttr(customMapBuffer + '.' + key, '', type = 'string')
    
    def findClosestNameInScene(self, findName, matchThreshold = 0.9):
        res = cmds.ls(type = 'transform')
        sim = self.getMostSimilarString(findName, res)
        if sim[1] >= matchThreshold:
            return sim[0]
        else:
            return None
    
    #-------------------------------------------------------------------------------------
    # Kill all AU Script Jobs
    def killScriptJobForAUWeight(self):
        global AUjob_id_list
        if AUjob_id_list != []:
            cmds.scriptJob(kill = AUjob_id_list)
            AUjob_id_list = []
    
    def killScriptJobForNameDelete(self):
        global nameDel_id_list
        if nameDel_id_list != []:
            cmds.scriptJob(kill = nameDel_id_list)
            nameDel_id_list = []

    #--------------------------------- Connect Map Related -------------------------------
    # switch Connect Map Between Default to 
    def switchConnectMapCallback(self):
        if self.uiWindow.noneMapBtn.isChecked():
            self.confirmConnectMapCallback()
            self.uiWindow.connectionMapStackedWidget.setCurrentIndex(1)
            self.uiWindow.connectionMapStackedWidget.show()
            self.showDefaultConnectMap()
            self.resizeUIWindowSize(1200,650)
            self.resizeUIWindowSize(1200,650)
        elif self.uiWindow.customMapBtn.isChecked():
            self.uiWindow.connectionMapStackedWidget.setCurrentIndex(0)
            self.uiWindow.connectionMapStackedWidget.show()
            self.showCustomConnectMap()
            self.resizeUIWindowSize(1200,650)
            self.resizeUIWindowSize(1200,650)
            
    def showCustomConnectMap(self):
        self.uiWindow.customConnectMapTreeWidget.clear()
        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        if characterRigGrp == None:
            cmds.warn('No character Rig Group Found.')
            return
        facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(characterRigGrp)
        customMapBuffer = FacsHelper.getFACS_CustomConnectionMapBuffer(facialComponent)
        
        for auType in DeformerHelper.facialActionUnitTypeList:
            key = SERigNaming.auAttrList[auType]
            value = cmds.getAttr(customMapBuffer + '.' + key)
            alias = DeformerHelper.AUsAliasTable[key]
            item = CustomConnectionMapItem(self.uiWindow.customConnectMapTreeWidget, key, alias, value)
        
        for column in range( self.uiWindow.customConnectMapTreeWidget.columnCount() ):
            self.uiWindow.customConnectMapTreeWidget.resizeColumnToContents( column )

    def showDefaultConnectMap(self):
        self.uiWindow.defaultConnectMapTreeWidget.clear()
        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        if characterRigGrp == None:
            cmds.warn('No character Rig Group Found.')
            return
        
        connectMap = DeformerHelper.dataBufferAUsToBlendshapeAUsTable
        for auType in DeformerHelper.facialActionUnitTypeList:
            key = SERigNaming.auAttrList[auType]
            value = connectMap[key]
            alias = DeformerHelper.AUsAliasTable[key]
            item = DefaultConnectionMapItem(self.uiWindow.defaultConnectMapTreeWidget, key, alias, value)
        
        for column in range( self.uiWindow.defaultConnectMapTreeWidget.columnCount() ):
            self.uiWindow.defaultConnectMapTreeWidget.resizeColumnToContents( column )
        
        self.getDefaultConnectMapMatchRate()

    def confirmConnectMapCallback(self):
        #self.uiWindow.customConnectMapTreeWidget.setHeaderLabels(['AU', 'Alias', 'Custom AU Mesh Name'])
        customMapTable = {}
        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        if characterRigGrp == None:
            cmds.warn('No character Rig Group Found.')
            return
        
        facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(characterRigGrp)
        customMapBuffer = FacsHelper.getFACS_CustomConnectionMapBuffer(facialComponent)

        item = QtWidgets.QTreeWidgetItemIterator(self.uiWindow.customConnectMapTreeWidget)
        for i in item:
            auName = str(i.value().name)
            customName = str(i.value().customEdit.text())
            cmds.setAttr(customMapBuffer + '.' + auName, customName, type = 'string')
            customMapTable[auName] = customName
        return customMapTable

    def exportCustomConnectMap(self):
        customMap = self.confirmConnectMapCallback()
        #print customMap
        if customMap:
            fileResult = cmds.fileDialog2()[0]
            splitData = fileResult.split('.')
            if len(splitData) > 1:
                fileResult = splitData[0]
            DeformerHelper.exportCustomConnectMap(fileResult, customMap)

    def importCustomConnectMap(self):
        characterRigGrp = self.uiWindow.rigCharacterGrpLineEdit.text()
        if characterRigGrp == None:
            cmds.warn('Cannot find character Rig Group.')
            return
        facialComponent = RigObjectTypeHelper.getCharacterFacialComponentGroup(characterRigGrp)
        customMapBuffer = FacsHelper.getFACS_CustomConnectionMapBuffer(facialComponent)
        
        fileResult = cmds.fileDialog2(fm=1, fileFilter = '*.seccm')[0]
        mapData = DeformerHelper.importCustomConnectMap(fileResult)
        if mapData:
            for auType in DeformerHelper.facialActionUnitTypeList:
                key = SERigNaming.auAttrList[auType]
                value = mapData[key]
                if value:
                    cmds.setAttr(customMapBuffer + '.' + key, value, type = 'string')
            self.showCustomConnectMap()
    
    def getDefaultConnectMapMatchRate(self):
        totalCounts = 0
        matchCounts = 0
        for auType in DeformerHelper.facialActionUnitTypeList:
            key = SERigNaming.auAttrList[auType]
            value = DeformerHelper.dataBufferAUsToBlendshapeAUsTable[key]
            if value != '' and value != None:
                totalCounts = totalCounts + 1
                if cmds.objExists(value):
                    matchCounts = matchCounts + 1
        
        matchRate = 100 * matchCounts / totalCounts
        matchRate = round(matchRate, 1)
        #print matchRate
        strMatch = 'Match Rate: ' + str(matchRate) + '% (' + str(matchCounts) + '/' + str(totalCounts) + ')'
        self.uiWindow.defaultMapMatchRateLabel.setText(strMatch)
        if matchRate > 75:
            self.uiWindow.defaultMapMatchRateLabel.setStyleSheet('QLabel {color : green; }')
        elif matchRate > 25:
            self.uiWindow.defaultMapMatchRateLabel.setStyleSheet('QLabel {color : #dcce87; }')
        else:
            self.uiWindow.defaultMapMatchRateLabel.setStyleSheet('QLabel {color : red; }')
                

    #--------------------------------- Miscellaneous Functions Related -------------------------------
    def arrangeAUsCallback(self):
        cmds.select(clear = True)
        AUBaseName = self.uiWindow.auBaseLineEdit.text()
        if not cmds.objExists(AUBaseName):
            return
        
        offset = float(self.uiWindow.offsetLineEdit.text())
        baseX = cmds.getAttr(AUBaseName + ".tx" )
        baseY = cmds.getAttr(AUBaseName + ".ty")
        baseZ = cmds.getAttr(AUBaseName + ".tz")
        if self.ctrlDataList != {} and self.auDataList != {}:
            for name in self.ctrlDataList:
                cmds.select(name, add = True)

            usedAUs = cmds.ls(sl = True)
            counts = len(usedAUs)
            column =  math.ceil(math.sqrt(counts))
            print column
            for i in range(counts):
                au = usedAUs[i]
                thisRow =  i // column
                thisColumn = i - thisRow * column + 1
                offsetX = offset * thisColumn
                offsetY = offset * thisRow
                cmds.setAttr(au + '.tx', baseX + offsetX)
                cmds.setAttr(au + '.ty', baseY + offsetY)
                cmds.setAttr(au + '.tz', baseZ)

    def changeArrangeOffsetCallback(self):
        self.arrangeAUsCallback()

    def batchRemoveSubJointControllersCallback(self):
        SERigHumanFacialComponent.removeFaceProxyControlInfluence()

    # Define Callback: Batch Remove Prefix Button    
    def batchRemovePrefixBtnCallback(self):
        DeformerHelper.batchRemovePrefix()
    
    def updateSymAUCallback(self):
        cleanMeshName = self.uiWindow.cleanAULineEdit.text()
        if cmds.objExists(cleanMeshName):
            DeformerHelper.updateSymmetricalBlendshape(cleanMeshName)
        else:
            cmds.warning('Cannot find the clean Mesh Name.')
    
    def updateSymFaceCallback(self):
        cleanMeshName = self.uiWindow.cleanFaceLineEdit.text()
        if cmds.objExists(cleanMeshName):
            DeformerHelper.updateSymmetricalBlendshape(cleanMeshName)
        else:
            cmds.warning('Cannot find the clean Mesh Name.')
#------------------------------------------------------------------------------------
def openFACSManagerWindow():
    facs_ui = FACSManagerUI()
    #facs_ui.resize( 600, 650 ) #1300, 800
    facs_ui.setMinimumSize( 270, 270 )
    facs_ui.run()
 
# AUList Item: include AUObject Name, Alias, Weight
class CustomAUListItem(QtWidgets.QTreeWidgetItem):
    def __init__( self, parent, name, alias , weightNode, controlMode): # parent is item's qtWidget; name is item's name
        super( CustomAUListItem, self).__init__(parent)
        self.name = name
        self.alias = alias
        self.weightNode = weightNode
        self.controlMode = controlMode
        if alias == '' or alias == None:
            self.alias = '*' + name
        self.initUIContent()

    def sliderChangeValue(self):
        sliderValue = self.slider.value()
        if self.controlMode == 0:
            self.lineEdit.setText(str(sliderValue*0.001)) #0-1000 -> 0-1
            weightValue = sliderValue * 0.001
            cmds.setAttr(self.weightNode, weightValue)
        else:
            weightValue = self.getWeightValue()
            self.slider.setValue(weightValue * 1000)

    def lineEditChangeValue(self):
        if self.controlMode == 0:
            textValue = self.lineEdit.text()
            weightValue = float(textValue)
            lvalue = weightValue * 1000
            self.slider.setValue(lvalue)
            cmds.setAttr(self.weightNode, weightValue)
        else:
            weightValue = self.getWeightValue()
            self.lineEdit.setText(str(weightValue))
    
    def getWeightValue(self):
        weight = cmds.getAttr(self.weightNode)
        return weight

    def createScriptJobForDisplayCtrlMode(self):
        global AUjob_id_list
        job_id = cmds.scriptJob(attributeChange = [self.weightNode, self.synBlendValueInCtrlMode])  #parent = 'FACS Manager UIWorkspaceControl', 
        AUjob_id_list.append(job_id)

    def synBlendValueInCtrlMode(self):
        oriValue = cmds.getAttr(self.weightNode)
        value = round(oriValue, 3)
        self.slider.setValue(value * 1000)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setText(str(value))
        self.lineEdit.setReadOnly(True)

    def initUIContent(self):
        # Column 0 - Text
        self.setText(0, self.name)
        
        # Column 1 - LineEdit Alias
        self.aliasEdit = QtWidgets.QLineEdit()
        self.aliasEdit.setText(self.alias)
        self.aliasEdit.setReadOnly(True)
        self.treeWidget().setItemWidget(self, 1, self.aliasEdit)

        # Column 2 - Slider & LineEdit
        weight = abs(cmds.getAttr(self.weightNode))
        lvalue = weight * 1000
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(1000)
        self.slider.valueChanged.connect(self.sliderChangeValue) #QSlider{background: #5F4141;}\n  qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);
        self.slider.setStyleSheet(".QSlider::groove:horizontal{border: 2px solid #393939; height: 4px; background: #404040;}\n QSlider::handle:horizontal {background: #1f1f1f; border: 1px solid #999999; height: 1px; width: 10px; margin: -8px 0;}")
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setText(str(weight))
        self.lineEdit.setMaximumWidth(50)
        self.lineEdit.setMaxLength(5)
        self.lineEdit.setStyleSheet("QLineEdit { background: black}")
        self.lineEdit.returnPressed.connect(self.lineEditChangeValue) #.connect

        self.weightWidget = QtWidgets.QWidget()
        self.weightLayout = QtWidgets.QHBoxLayout()
        self.weightLayout.addWidget(self.lineEdit)
        self.weightLayout.addWidget(self.slider)
        self.weightWidget.setLayout(self.weightLayout)
        self.treeWidget().setItemWidget(self, 2, self.weightWidget)
        self.slider.setValue(lvalue)

        if self.controlMode == 0:
            self.lineEdit.setReadOnly(False)
            self.lineEdit.setStyleSheet("QLineEdit{background: black}")
        else:
            self.lineEdit.setReadOnly(True)
            self.lineEdit.setStyleSheet("QLineEdit{background: #f1f1a5; color: black}")
            self.createScriptJobForDisplayCtrlMode()

        self.treeWidget().setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)

# Custom AU ConnectionMap Item: 
class CustomConnectionMapItem(QtWidgets.QTreeWidgetItem):
    def __init__( self, parent, name, aliasName, customName): # parent is item's qtWidget; name is item's name
        super( CustomConnectionMapItem, self).__init__(parent)
        self.name = name
        self.aliasName = aliasName
        self.customName = customName
        if aliasName == '' or aliasName == None:
            self.aliasName = '*' + self.name
        self.initUIContent()

    def initUIContent(self):
        # Column 0&1 - Text AUName & Text Alias
        self.setText(0, self.name)
        self.setText(1, self.aliasName)

        # Column 2 - LineEdit Custom Name
        self.customEdit = QtWidgets.QLineEdit()
        self.customEdit.textEdited.connect(self.textChangeUnsaved)
        if self.customName == None:
            self.customEdit.setText("")
        else:
            self.customEdit.setText(self.customName)
        self.treeWidget().setItemWidget(self, 2, self.customEdit)

        self.treeWidget().setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)    
        self.textChangeUnsaved()

    def textChangeUnsaved(self):   
        #self.treeWidget().setHeaderLabels(['AU', 'Alias', 'Custom AU Mesh Name*'])
        value = self.customEdit.text()
        if value != '':
            if not cmds.objExists(value):
                self.customEdit.setStyleSheet("QLineEdit{color: red}")
            else:
                self.customEdit.setStyleSheet("QLineEdit{color: white}")


# Default AU ConnectionMap Item: 
class DefaultConnectionMapItem(QtWidgets.QTreeWidgetItem):
    def __init__( self, parent, name, aliasName, defaultName): # parent is item's qtWidget; name is item's name
        super( DefaultConnectionMapItem, self).__init__(parent)
        self.name = name
        self.aliasName = aliasName
        self.defaultName = defaultName
        if aliasName == '' or aliasName == None:
            self.aliasName = '*' + self.name
        self.initUIContent()

    def initUIContent(self):
        # Column 0&1&2 - Text AUName & Text Alias & Default Name
        self.setText(0, self.name)
        self.setText(1, self.aliasName)
        self.setText(2, self.defaultName)
        if not cmds.objExists(self.defaultName):
            self.setTextColor(2, 'red')

        self.treeWidget().setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)    


class PopHelpWidget(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    toolname = 'helpWindow'
    def __init__(self, parent = None):
        super(PopHelpWidget, self).__init__(parent)
        mayaMainWindowPtr = mui.MQtUtil.mainWindow()
        self.mayaMainWindow = shiboken2.wrapInstance(long(mayaMainWindowPtr), QtWidgets.QMainWindow)

        self.setWindowTitle("Help")     
        self.setObjectName('HelpWindowDockable')
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.setGeometry(500, 300, 600, 400)
        
        self.setMinimumHeight(120)
        self.setMinimumWidth(100)
        self.setMaximumHeight(600)
        self.setMaximumWidth(500)

        self.imageBG = QtWidgets.QLabel()
        self.imageBG.setPixmap(QtGui.QPixmap((uiRootFile +"/Help_FacialBase.png")))
        self.imageBG.setScaledContents(True)
        self.layout.addWidget(self.imageBG)

        


        

    



