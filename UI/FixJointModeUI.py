#TODO:
#doc order to select ik locator
#python parent child
#tip to close  orientHelper
#tip to export with select
import maya.cmds as cmds
from ..Utils import SEJointOrientHelper as orientHelper
import os
import SERiggingTools.UI.CreateRigUI as CreateRigUI
import UIConfig
import maya.OpenMayaUI as MayaUi
import shiboken2

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
    
class FixJointModeWindow(QtWidgets.QDialog):
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
        self.resize(677, 673)
        self.minSize = QtCore.QSize(677, 673)
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
        self.ui.tool_Btn.clicked.connect(self.seRiggingTool)
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
         orientHelperfjm.switchMode(True)
        
    def closeEvent(self, event):
         orientHelperfjm.switchMode(False)

    def resizeEvent(self,event):
        self.ui.resize(self.size().expandedTo(self.minSize))
        self.resize(self.size().expandedTo(self.minSize))
               
    def helpWindow(self):
        self.helpUi.show()
        
    def modeChanged(self):
        if self.ui.mode_Chk.isChecked():
             orientHelperfjm.switchMode(True)
            self.ui.modeTip_Label.setText("""<html><head/><body><p align="justify"><span style=" color:#00ff00;">FixJointMode already switch on.
            </span></p><p align="justify"><span style=" color:#00ff00;">You can rotate and move the Joint</span></p></body></html>""")
        else:
             orientHelperfjm.switchMode(False)
            self.ui.modeTip_Label.setText("""<html><head/><body><p align="justify"><span style=" color:#ff0000;">FixJointMode already switch off.
            </span></p><p align="justify"><span style=" color:#ff0000;">Don`t rotate and move any Joint </span></p></body></html>""")

    def debugMode(self):
        if self.ui.debug_Chk.isChecked():
             orientHelperfjm.switchDebugPlane(True)        
        else:
             orientHelperfjm.switchDebugPlane(False)
    
    def addIK(self):
         orientHelperfjm.addIKGroups()

    def showIK(self):
         orientHelperfjm.displayIKGroups() 
        
    def defaultIK(self):
         orientHelperfjm.defaultIKGroup()
        
    def clearIK(self):
         orientHelperfjm.clearIKGroups()
        
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
        if exportPath !="":
            cmds.file(exportPath,exportSelected = True,type = "mayaAscii")
            print "Export To "+exportPath
        else:
            print "Export Fail, The export path is not indicated"
        
    def pAxisBG(self):
        id = self.ui.buttonGroup.checkedId()
         orientHelperfjm.primaryAxis = [0,0,0]
         orientHelperfjm.primaryAxis[id] = self.ui.comboBox_1.currentIndex()*2-1
   
    def sAxisBG(self):
        id = self.ui.buttonGroup_2.checkedId()
         orientHelperfjm.secondaryAxis = [0,0,0]
         orientHelperfjm.secondaryAxis[id] = self.ui.comboBox_2.currentIndex()*2-1
               
    def sAxisOrientBG(self):
        id = self.ui.buttonGroup_3.checkedId()
         orientHelperfjm.secondaryAxisOrient = [0,0,0]
         orientHelperfjm.secondaryAxisOrient[id] = self.ui.comboBox_3.currentIndex()*2-1
            
    def addMirror(self):
         orientHelperfjm.addMirror()

    def showMirror(self):
         orientHelperfjm.displayMirror() 
        
    def defaultMirror(self):
         orientHelperfjm.defaultMirror()
        
    def clearMirror(self):
         orientHelperfjm.clearMirror()
        
    def mirror(self):
         orientHelperfjm.setJntAttrLock(False)
        id = self.ui.buttonGroup_4.checkedId()
        if id ==0:
             orientHelperfjm.mirror("xy")
        elif id ==1:
             orientHelperfjm.mirror("yz")
        elif id ==2:
             orientHelperfjm.mirror("xz")
            
    def initialAxis(self):
        for i in range(len( orientHelperfjm.primaryAxis)):
            if  orientHelperfjm.primaryAxis[i] != 0:
               self.ui.buttonGroup.button(i).setChecked(True)
               self.ui.comboBox_1.setCurrentIndex( orientHelperfjm.secondaryAxis[i]*0.5+1)
               break 
        for i in range(len( orientHelperfjm.secondaryAxis)):
            if  orientHelperfjm.secondaryAxis[i] != 0:
               self.ui.buttonGroup_2.button(i).setChecked(True)
               self.ui.comboBox_2.setCurrentIndex( orientHelperfjm.secondaryAxis[i]*0.5+1)
               break 
        for i in range(len( orientHelperfjm.secondaryAxisOrient)):
            if  orientHelperfjm.secondaryAxisOrient[i] != 0:
               self.ui.buttonGroup_3.button(i).setChecked(True)
               self.ui.comboBox_3.setCurrentIndex( orientHelperfjm.secondaryAxisOrient[i]*0.5+1)
               break        
    
    def saveJntLockedAttr(self):
        jointList = cmds.ls(type = "joint")
        attr = [".rotateX",".rotateY",".rotateZ",".translateX",".translateY",".translateZ"]
        for jnt in jointList:
            lockedAttr = []
            for a in attr:    
                if cmds.getAttr(jnt+a,lock = True):
                    lockedAttr.append(a)
             orientHelperfjm.lockedAttrDict[jnt] = lockedAttr
        print  orientHelperfjm.lockedAttrDict
        
    def seRiggingTool(self):        
        CreateRigUI.openMayaWindow()
        