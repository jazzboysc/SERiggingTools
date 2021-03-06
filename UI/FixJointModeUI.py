import maya.cmds as cmds
from ..Utils import SEJointOrientHelper as orientHelper
import os
import SERiggingTools.UI.CreateRigUI as CreateRigUI
import UIConfig
import maya.OpenMayaUI as MayaUi
import shiboken2
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

qtVersion = cmds.about(qtVersion =True)

if qtVersion.startswith("4") or type(qtVersion) not in [str,unicode]:
    from PySide import QtCore,QtGui,QtWidgets,QtUiTools
else:
    from PySide2 import QtCore,QtGui,QtWidgets,QtUiTools

#load file path 
uiRootPath = os.path.dirname(UIConfig.__file__)
uiFilePath = uiRootPath + "\FixJointModeUI.ui"
helpUiPath = uiRootPath + "\modeHelp_01.ui"
helpPicPath = uiRootPath + "\modeHelp_01.png"

fjmWindow = None

def getMayaWindow():
    ptr = MayaUi.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)
    
def openFixJointModeWindow():
    global fjmWindow
    if fjmWindow != None:
        fjmWindow.close()
    fjmWindow = FixJointModeWindow()
    fjmWindow.show()
    
class FixJointModeWindow(MayaQWidgetDockableMixin,QtWidgets.QDialog):
    def  __init__(self, parent = getMayaWindow()):
        super(FixJointModeWindow, self).__init__()
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

        #load UI file
        uiFile = QtCore.QFile(uiFilePath)
        uiFile.open(QtCore.QFile.ReadOnly)
        self.ui = QtUiTools.QUiLoader().load(uiFile,parentWidget = self)
        uiFile.close()
        uiFile = QtCore.QFile(uiFilePath)
        uiFile.open(QtCore.QFile.ReadOnly)
        self.helpUi = QtUiTools.QUiLoader().load(helpUiPath)
        uiFile.close()
        
        #load picture
        self.helpUi.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.helpUi.picture_LB.setPixmap(QtGui.QPixmap(helpPicPath))
        
        #initial window
        self.minSize = QtCore.QSize(467, 507)
        self.setFixedSize(self.minSize)
        self.setWindowTitle("Fix Joint Mode")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
              
        #connect signal to function
        self.ui.mode_Chk.stateChanged.connect(self.modeChanged)
        self.ui.debug_Chk.stateChanged.connect(self.debugMode)
        self.ui.addIK_Btn.clicked.connect(self.addIK)
        self.ui.showIK_Btn.clicked.connect(self.showIK)
        self.ui.defaultIK_Btn.clicked.connect(self.defaultIK)
        self.ui.clearIK_Btn.clicked.connect(self.clearIK)
        self.ui.sktPath_Btn.clicked.connect(self.importBrowser)
        self.ui.buttonGroup.buttonClicked.connect(self.pAxisBG)
        self.ui.buttonGroup_2.buttonClicked.connect(self.sAxisBG)
        self.ui.buttonGroup_3.buttonClicked.connect(self.sAxisOrientBG)
        self.ui.comboBox_1.currentIndexChanged.connect(self.pAxisBG)
        self.ui.comboBox_2.currentIndexChanged.connect(self.sAxisBG)
        self.ui.comboBox_3.currentIndexChanged.connect(self.sAxisOrientBG)
        self.ui.addMirror_Btn.clicked.connect(self.addMirror)
        self.ui.showMirror_Btn.clicked.connect(self.showMirror)
        self.ui.defaultMirror_Btn.clicked.connect(self.defaultMirror)
        self.ui.clearMirror_Btn.clicked.connect(self.clearMirror)
        self.ui.mirror_Btn.clicked.connect(self.mirror)
        self.ui.exportBrowse_Btn.clicked.connect(self.exportBrowser)
        self.ui.export_Btn.clicked.connect(self.exportBuilder)
        self.ui.tool_Btn.clicked.connect(self.OpenCreateRigUI)
        self.ui.help_Btn.clicked.connect(self.helpWindow)
        
        #set radio id     
        self.ui.buttonGroup.setId(self.ui.radioButton_01,0)
        self.ui.buttonGroup.setId(self.ui.radioButton_02,1)
        self.ui.buttonGroup.setId(self.ui.radioButton_03,2)
        self.ui.buttonGroup_2.setId(self.ui.radioButton_11,0)
        self.ui.buttonGroup_2.setId(self.ui.radioButton_12,1)
        self.ui.buttonGroup_2.setId(self.ui.radioButton_13,2)
        self.ui.buttonGroup_3.setId(self.ui.radioButton_21,0)
        self.ui.buttonGroup_3.setId(self.ui.radioButton_22,1)
        self.ui.buttonGroup_3.setId(self.ui.radioButton_23,2)
        self.ui.buttonGroup_4.setId(self.ui.radioButton_31,0)
        self.ui.buttonGroup_4.setId(self.ui.radioButton_32,1)
        self.ui.buttonGroup_4.setId(self.ui.radioButton_33,2)
       
        self.initialAxis()  
        orientHelper.fjm.switchMode(True)
        
    def closeEvent(self, event):
        orientHelper.fjm.switchMode(False)
               
    def helpWindow(self):
        self.helpUi.show()
        
    def modeChanged(self):
        if self.ui.mode_Chk.isChecked():
            orientHelper.fjm.switchMode(True)
            self.ui.modeTip_Label.setText("""<html><head/><body><p align="justify"><span style=" color:#00ff00;">FixJointMode already switch on.
            </span></p><p align="justify"><span style=" color:#00ff00;">You can rotate and move the Joint</span></p></body></html>""")
        else:
            orientHelper.fjm.switchMode(False)
            self.ui.modeTip_Label.setText("""<html><head/><body><p align="justify"><span style=" color:#ff0000;">FixJointMode already switch off.
            </span></p><p align="justify"><span style=" color:#ff0000;">Don`t rotate and move any Joint </span></p></body></html>""")

    def debugMode(self):
        if self.ui.debug_Chk.isChecked():
            orientHelper.fjm.switchDebugPlane(True)        
        else:
            orientHelper.fjm.switchDebugPlane(False)
    
    def addIK(self):
        orientHelper.fjm.addIKGroups()

    def showIK(self):
        orientHelper.fjm.displayIKGroups() 
        
    def defaultIK(self):
        orientHelper.fjm.defaultIKGroup()
        
    def clearIK(self):
        orientHelper.fjm.clearIKGroups()
        
    def importBrowser(self):
        filePath = cmds.fileDialog2(fileMode = 1)
        if filePath is None:
            print "The import path is not indicated"
        else: 
            cmds.file(filePath,i = True)
            self.ui.sktPath_LE.setText(filePath[0])
            self.saveJntLockedAttr()
        
    def exportBrowser(self):
        exportPath = cmds.fileDialog2(fileMode = 0,fileFilter = "*.ma")
        if exportPath is None:
            print "The export path is not indicated"
        else:
            if exportPath[0].find("_Builder.ma") ==-1:
                exportPath = exportPath[0].replace(".ma","_Builder.ma")
            else:
                exportPath = exportPath[0]
            self.ui.exportPath_LE.setText(exportPath)
        
    def exportBuilder(self):
        exportPath = self.ui.exportPath_LE.text()
        selected = cmds.ls(sl = True)
        if exportPath == "":
            print "Export Fail, The export path is not indicated"
        elif selected == []:
            print "Export Fail, The group to be exported is not selected" 
        else:
            start = exportPath.rfind("/")
            end = exportPath.rfind("_Builder.ma")
            cmds.rename(exportPath[start+1:end]+"_BuilderGrp")
            cmds.file(exportPath,exportSelected = True,type = "mayaAscii")
            print "Export Success! Export to "+exportPath
        
    def pAxisBG(self):
        id = self.ui.buttonGroup.checkedId()
        orientHelper.fjm.primaryAxis = [0,0,0]
        orientHelper.fjm.primaryAxis[id] = self.ui.comboBox_1.currentIndex()*2-1
   
    def sAxisBG(self):
        id = self.ui.buttonGroup_2.checkedId()
        orientHelper.fjm.secondaryAxis = [0,0,0]
        orientHelper.fjm.secondaryAxis[id] = self.ui.comboBox_2.currentIndex()*2-1
               
    def sAxisOrientBG(self):
        id = self.ui.buttonGroup_3.checkedId()
        orientHelper.fjm.secondaryAxisOrient = [0,0,0]
        orientHelper.fjm.secondaryAxisOrient[id] = self.ui.comboBox_3.currentIndex()*2-1
            
    def addMirror(self):
        orientHelper.fjm.addMirror()

    def showMirror(self):
        orientHelper.fjm.displayMirror() 
        
    def defaultMirror(self):
        orientHelper.fjm.defaultMirror()
        
    def clearMirror(self):
        orientHelper.fjm.clearMirror()
        
    def mirror(self):
        orientHelper.fjm.setJntAttrLock(False)
        id = self.ui.buttonGroup_4.checkedId()
        if id ==0:
            orientHelper.fjm.mirror("xy")
        elif id ==1:
            orientHelper.fjm.mirror("yz")
        elif id ==2:
            orientHelper.fjm.mirror("xz")
            
    #Initial the Axis in advanced setting with default value        
    def initialAxis(self):
        for i in range(len(orientHelper.fjm.primaryAxis)):
            if orientHelper.fjm.primaryAxis[i] != 0:
               self.ui.buttonGroup.button(i).setChecked(True)
               self.ui.comboBox_1.setCurrentIndex(orientHelper.fjm.secondaryAxis[i]*0.5+1)
               break 
        for i in range(len(orientHelper.fjm.secondaryAxis)):
            if orientHelper.fjm.secondaryAxis[i] != 0:
               self.ui.buttonGroup_2.button(i).setChecked(True)
               self.ui.comboBox_2.setCurrentIndex(orientHelper.fjm.secondaryAxis[i]*0.5+1)
               break 
        for i in range(len(orientHelper.fjm.secondaryAxisOrient)):
            if orientHelper.fjm.secondaryAxisOrient[i] != 0:
               self.ui.buttonGroup_3.button(i).setChecked(True)
               self.ui.comboBox_3.setCurrentIndex(orientHelper.fjm.secondaryAxisOrient[i]*0.5+1)
               break        
    
    #Save the locked joint`s attribute when import a new template skeleton
    def saveJntLockedAttr(self):
        jointList = cmds.ls(type = "joint")
        attr = [".rotateX",".rotateY",".rotateZ",".translateX",".translateY",".translateZ"]
        for jnt in jointList:
            lockedAttr = []
            for a in attr:    
                if cmds.getAttr(jnt+a,lock = True):
                    lockedAttr.append(a)
            orientHelper.fjm.lockedAttrDict[jnt] = lockedAttr
        print "Locked Joint Attribute : ",orientHelper.fjm.lockedAttrDict
   
        
    def OpenCreateRigUI(self):        
        CreateRigUI.openMayaWindow()
        