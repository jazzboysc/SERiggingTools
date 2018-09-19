import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
import maya.mel
import sys
import maya.cmds as cmds
import maya.OpenMayaUI as mui
from PySide2 import QtCore, QtGui, QtWidgets , QtUiTools
import shiboken2
import os
import time

import cPickle

from ..Character import SECharacter

import UIConfig
#"E:/Users/admin/Documents/GitHub/SERiggingTools/UI/LoadRiggingUI.ui"

uiRootFile = os.path.dirname(UIConfig.__file__)
uifile_path = uiRootFile + "/ControlRig.ui"

def openMayaWindow():
    ''' todo: stop open more than one window'''
    # global ui
    # ui = loadUI(uifile_path)
    # ui.show()

    global mainWin
    mainWin = mainRigWindow()
    mainWin.show()
    pass

def loadUI(uifile_path):
    QtCore.QResource.addSearchPath("E:/Users/admin/Documents/GitHub/SERiggingTools/UI")
    uifile = QtCore.QFile(uifile_path)
    print(uifile)
    uifile.open(QtCore.QFile.ReadOnly)
    #QtCore.QResource.registerResource("E:/Users/admin/Documents/GitHub/SERiggingTools/UI/UIResource.qrc")
    uiWindow = QtUiTools.QUiLoader().load(uifile)
    uifile.close()

    rrr = QtCore.QResource.searchPaths()
    print(rrr)

    #uiWindow.label.setPixmap(QtGui.QPixmap(("E:/Users/admin/Documents/GitHub/SERiggingTools/UI/equipment_11_1.png")))
    return uiWindow

def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)

class mainRigWindow(QtWidgets.QDialog):
    """docstring for mainWindow"""
    def __init__(self, parent = getMayaWindow()):
        super(mainRigWindow, self).__init__(parent)
        self.setWindowTitle('Create Character Rig')
        self.descLabel = QtWidgets.QLabel("Please choose the main project path", parent = self)

        TextLayoutMainProjectPath = QtWidgets.QHBoxLayout()
        self.MainProjectPathLine = QtWidgets.QLineEdit()
        TextLayoutMainProjectPath.addWidget(QtWidgets.QLabel("Main Project Path :"))
        TextLayoutMainProjectPath.addWidget(self.MainProjectPathLine)
        self.SetMainProjectPathButton = QtWidgets.QPushButton("Set Path")
        TextLayoutMainProjectPath.addWidget(self.SetMainProjectPathButton)

        #TextLayoutCharacterName = QtWidgets.QHBoxLayout()
        #self.CharacterNameLine = QtWidgets.QLineEdit()
        #TextLayoutCharacterName.addWidget(QtWidgets.QLabel("Character Name :"))
        #TextLayoutCharacterName.addWidget(self.CharacterNameLine)
        #TextLayoutCharacterName.addSpacing(220)

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.descLabel)
        mainLayout.addLayout(TextLayoutMainProjectPath)
        self.SetBuilderConfigWeight(mainLayout)

        self.connect(self.SetMainProjectPathButton, QtCore.SIGNAL("clicked()"), self.selectMainProjectPath)

        confirmLayout = QtWidgets.QHBoxLayout()
        self.ConfirmButton = QtWidgets.QPushButton("Create Rig")
        self.CancelButton = QtWidgets.QPushButton("Cancel")
        confirmLayout.addWidget(self.ConfirmButton)
        confirmLayout.addWidget(self.CancelButton)
        mainLayout.addLayout(confirmLayout)

        self.connect(self.ConfirmButton, QtCore.SIGNAL("clicked()"), self.createRig)
        self.connect(self.CancelButton, QtCore.SIGNAL("clicked()"), self.close)
        #mainLayout.addLayout(ButtonHLayout)
        #self.addLayout(ButtonHLayout)
        #self.setLayout(ButtonHLayout)
        self.resize(400, 10)


    #############################################################################################################################	

    def addLayoutOne(self):
        ButtonOne = QtWidgets.QPushButton("Button1")
        ButtonTwo = QtWidgets.QPushButton("Button2")

        ButtonHLayout = QtWidgets.QHBoxLayout()
        ButtonHLayout.addWidget(ButtonOne)
        ButtonHLayout.addWidget(ButtonTwo)
        return ButtonHLayout

    def selectMainProjectPath(self):
        fileResult = cmds.fileDialog2(fm = 3)
        if fileResult != None:
            print(fileResult[0])
            self.MainProjectPathLine.setText(fileResult[0])
            mainWin.update()

    def createRig(self):
        mainProjectPath = self.MainProjectPathLine.text()
        res = os.path.split(mainProjectPath)
        mainProjectPath = res[0]
        characterName = res[1]

        character = SECharacter.RigBipedCharacter(characterName = characterName)
        character.build(  
                        mainProjectPath = mainProjectPath, 
                        upperBodyUpperLimbKnobCount = 2, 
                        upperBodyLowerLimbKnobCount = 2, 
                        lowerBodyUpperLimbKnobCount = 2, 
                        lowerBodyLowerLimbKnobCount = 1, 
                        mainCtrlOffset = 30
                        )
        
        self.close()

    def SetBuilderConfigWeight(self , mainLayout ):
        groupBox = QtWidgets.QVBoxLayout()
        upperBodyUpperLayout = QtWidgets.QHBoxLayout()
        upperBodyUpperLayout.addWidget(QtWidgets.QLabel("upperArmTwist :"))
        self.upperBodyUpperLine = QtWidgets.QLineEdit()
        self.upperBodyUpperLine.setValidator(QtGui.QIntValidator(1,5))
        upperBodyUpperLayout.addWidget(self.upperBodyUpperLine)
        self.upperBodyUpperLine.setText(str(1))
        upperBodyUpperLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
        upperBodyUpperLayout.addSpacing(220)
        groupBox.addLayout(upperBodyUpperLayout)

        upperBodyLowerLayout = QtWidgets.QHBoxLayout()
        upperBodyLowerLayout.addWidget(QtWidgets.QLabel("lowerArmTwist :"))
        self.upperBodyLowerLine = QtWidgets.QLineEdit()
        self.upperBodyLowerLine.setValidator(QtGui.QIntValidator(1,5))
        upperBodyLowerLayout.addWidget(self.upperBodyLowerLine)
        self.upperBodyLowerLine.setText(str(1))
        upperBodyLowerLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
        upperBodyLowerLayout.addSpacing(220)
        groupBox.addLayout(upperBodyLowerLayout)

        lowerBodyUpperLayout = QtWidgets.QHBoxLayout()
        lowerBodyUpperLayout.addWidget(QtWidgets.QLabel("upperLegTwist :"))
        self.lowerBodyUpperLine = QtWidgets.QLineEdit()
        self.lowerBodyUpperLine.setValidator(QtGui.QIntValidator(1,5))
        lowerBodyUpperLayout.addWidget(self.lowerBodyUpperLine)
        self.lowerBodyUpperLine.setText(str(1))
        lowerBodyUpperLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
        lowerBodyUpperLayout.addSpacing(220)
        groupBox.addLayout(lowerBodyUpperLayout)

        lowerBodyLowerLayout = QtWidgets.QHBoxLayout()
        lowerBodyLowerLayout.addWidget(QtWidgets.QLabel("lowerLegTwist :"))
        self.lowerBodyLowerLine = QtWidgets.QLineEdit()
        self.lowerBodyUpperLine.setValidator(QtGui.QIntValidator(1,5))
        lowerBodyLowerLayout.addWidget(self.lowerBodyLowerLine)
        self.lowerBodyLowerLine.setText(str(1))
        lowerBodyLowerLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
        lowerBodyLowerLayout.addSpacing(220)
        groupBox.addLayout(lowerBodyLowerLayout)
        mainLayout.addLayout(groupBox)