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

mainWin = None

def openMayaWindow():
    ''' todo: stop open more than one window'''
    # global ui
    # ui = loadUI(uifile_path)
    # ui.show()

    global mainWin
    if mainWin != None:
        mainWin.close()
    mainWin = mainRigWindow()
    mainWin.show()


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
        # Get project path and extract character name.
        mainProjectPath = self.MainProjectPathLine.text()
        res = os.path.split(mainProjectPath)
        mainProjectPath = res[0]
        characterName = res[1]

        # Get building parameters.
        upperBodyUpperLimbKnobCount = int(self.upperBodyUpperLine.text())
        upperBodyLowerLimbKnobCount = int(self.upperBodyLowerLine.text())
        lowerBodyUpperLimbKnobCount = int(self.lowerBodyUpperLine.text())
        lowerBodyLowerLimbKnobCount = int(self.lowerBodyLowerLine.text())
        mainCtrlOffset = int(self.mainBodyCtrlOffsetLine.text())
        fkLegControlScaleYZ = int(self.fkLegBodyControlScaleYZLine.text())
        fkLegControlScaleYZMultiplier = float(self.fkLegBodyControlScaleYZMultiplierLine.text())
        fkLegControlTransparency = float(self.fkLegControlTransparencyLine.text())
        ballIKTwistLeft = int(self.ballBodyIKTwistLeftLine.text())
        ballIKTwistRight = int(self.ballBodyIKTwistRightLine.text())
        toeIKTwistLeft = int(self.toeBodyIKTwistLeftLine.text())
        toeIKTwistRight = int(self.toeBodyIKTwistRightLine.text())
        fkArmControlScaleYZ = int(self.fkBodyArmControlScaleYZLine.text())
        fkArmControlScaleYZMultiplier = float(self.fkBodyArmControlScaleYZMultiplierLine.text())
        fkArmControlTransparency = float(self.fkBodyArmControlTransparencyLine.text())

        # Build character rig.
        character = SECharacter.RigBipedCharacter(characterName = characterName)
        character.build(  
                        mainProjectPath = mainProjectPath, 
                        upperBodyUpperLimbKnobCount = upperBodyUpperLimbKnobCount, 
                        upperBodyLowerLimbKnobCount = upperBodyLowerLimbKnobCount, 
                        lowerBodyUpperLimbKnobCount = lowerBodyUpperLimbKnobCount, 
                        lowerBodyLowerLimbKnobCount = lowerBodyLowerLimbKnobCount, 
                        mainCtrlOffset = mainCtrlOffset,
                        fkLegControlScaleYZ = fkLegControlScaleYZ,
                        fkLegControlScaleYZMultiplier = fkLegControlScaleYZMultiplier,
                        fkLegControlTransparency = fkLegControlTransparency,
                        ballIKTwistLeft = ballIKTwistLeft,
                        ballIKTwistRight = ballIKTwistRight,
                        toeIKTwistLeft = toeIKTwistLeft,
                        toeIKTwistRight = toeIKTwistRight,
                        fkArmControlScaleYZ = fkArmControlScaleYZ,
                        fkArmControlScaleYZMultiplier = fkArmControlScaleYZMultiplier,
                        fkArmControlTransparency = fkArmControlTransparency


                        )
        
        # Close the create rig window.
        self.close()

    def SetBuilderConfigWeight(self , mainLayout ):
        groupBox = QtWidgets.QVBoxLayout()
        upperBodyUpperLayout = QtWidgets.QHBoxLayout()
        upperBodyUpperLayout.addWidget(QtWidgets.QLabel("UpperArmTwist :"))
        self.upperBodyUpperLine = QtWidgets.QLineEdit()
        self.upperBodyUpperLine.setValidator(QtGui.QIntValidator(1,5))
        upperBodyUpperLayout.addWidget(self.upperBodyUpperLine)
        self.upperBodyUpperLine.setText('2')
        upperBodyUpperLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
        upperBodyUpperLayout.addSpacing(220)
        groupBox.addLayout(upperBodyUpperLayout)

        upperBodyLowerLayout = QtWidgets.QHBoxLayout()
        upperBodyLowerLayout.addWidget(QtWidgets.QLabel("LowerArmTwist :"))
        self.upperBodyLowerLine = QtWidgets.QLineEdit()
        self.upperBodyLowerLine.setValidator(QtGui.QIntValidator(1,5))
        upperBodyLowerLayout.addWidget(self.upperBodyLowerLine)
        self.upperBodyLowerLine.setText('2')
        upperBodyLowerLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
        upperBodyLowerLayout.addSpacing(220)
        groupBox.addLayout(upperBodyLowerLayout)

        lowerBodyUpperLayout = QtWidgets.QHBoxLayout()
        lowerBodyUpperLayout.addWidget(QtWidgets.QLabel("UpperLegTwist :"))
        self.lowerBodyUpperLine = QtWidgets.QLineEdit()
        self.lowerBodyUpperLine.setValidator(QtGui.QIntValidator(1,5))
        lowerBodyUpperLayout.addWidget(self.lowerBodyUpperLine)
        self.lowerBodyUpperLine.setText('2')
        lowerBodyUpperLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
        lowerBodyUpperLayout.addSpacing(220)
        groupBox.addLayout(lowerBodyUpperLayout)

        lowerBodyLowerLayout = QtWidgets.QHBoxLayout()
        lowerBodyLowerLayout.addWidget(QtWidgets.QLabel("LowerLegTwist :"))
        self.lowerBodyLowerLine = QtWidgets.QLineEdit()
        self.lowerBodyUpperLine.setValidator(QtGui.QIntValidator(1,5))
        lowerBodyLowerLayout.addWidget(self.lowerBodyLowerLine)
        self.lowerBodyLowerLine.setText('1')
        lowerBodyLowerLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
        lowerBodyLowerLayout.addSpacing(220)
        groupBox.addLayout(lowerBodyLowerLayout)
        mainLayout.addLayout(groupBox)

        
        mainBodyCtrlOffsetLayout = QtWidgets.QHBoxLayout()
        mainBodyCtrlOffsetLayout.addWidget(QtWidgets.QLabel("MainCtrlOffset :"))
        self.mainBodyCtrlOffsetLine = QtWidgets.QLineEdit()
        self.mainBodyCtrlOffsetLine.setValidator(QtGui.QIntValidator(0,50))
        mainBodyCtrlOffsetLayout.addWidget(self.mainBodyCtrlOffsetLine)
        self.mainBodyCtrlOffsetLine.setText('30')
        mainBodyCtrlOffsetLayout.addWidget(QtWidgets.QLabel("( 0 - 50)"))
        mainBodyCtrlOffsetLayout.addSpacing(215)
        groupBox.addLayout(mainBodyCtrlOffsetLayout)
        mainLayout.addLayout(groupBox)
        
        fkLegBodyControlScaleYZLayout = QtWidgets.QHBoxLayout()
        fkLegBodyControlScaleYZLayout.addWidget(QtWidgets.QLabel("FKLegControlScaleYZ :"))
        self.fkLegBodyControlScaleYZLine = QtWidgets.QLineEdit()
        self.fkLegBodyControlScaleYZLine.setValidator(QtGui.QIntValidator(0,30))
        fkLegBodyControlScaleYZLayout.addWidget(self.fkLegBodyControlScaleYZLine)
        self.fkLegBodyControlScaleYZLine.setText('19')
        fkLegBodyControlScaleYZLayout.addWidget(QtWidgets.QLabel("( 0 - 30)"))
        fkLegBodyControlScaleYZLayout.addSpacing(215)
        groupBox.addLayout(fkLegBodyControlScaleYZLayout)
        mainLayout.addLayout(groupBox)

        fkLegBodyControlScaleYZMultiplierLayout = QtWidgets.QHBoxLayout()
        fkLegBodyControlScaleYZMultiplierLayout.addWidget(QtWidgets.QLabel("FKLegControlScaleYZMultiplier :"))
        self.fkLegBodyControlScaleYZMultiplierLine = QtWidgets.QLineEdit()
        self.fkLegBodyControlScaleYZMultiplierLine.setValidator(QtGui.QDoubleValidator(0.0, 1.0, 4))
        fkLegBodyControlScaleYZMultiplierLayout.addWidget(self.fkLegBodyControlScaleYZMultiplierLine)
        self.fkLegBodyControlScaleYZMultiplierLine.setText('0.75')
        fkLegBodyControlScaleYZMultiplierLayout.addWidget(QtWidgets.QLabel("(0 - 1)"))
        fkLegBodyControlScaleYZMultiplierLayout.addSpacing(215)
        groupBox.addLayout(fkLegBodyControlScaleYZMultiplierLayout)
        mainLayout.addLayout(groupBox)

        fkLegControlTransparencyLayout = QtWidgets.QHBoxLayout()
        fkLegControlTransparencyLayout.addWidget(QtWidgets.QLabel("FKLegControlTransparency :"))
        self.fkLegControlTransparencyLine = QtWidgets.QLineEdit()
        self.fkLegControlTransparencyLine.setValidator(QtGui.QDoubleValidator(0.0, 1.0, 4))
        fkLegControlTransparencyLayout.addWidget(self.fkLegControlTransparencyLine)
        self.fkLegControlTransparencyLine.setText('0.85')
        fkLegControlTransparencyLayout.addWidget(QtWidgets.QLabel("(0 - 1)"))
        fkLegControlTransparencyLayout.addSpacing(215)
        groupBox.addLayout(fkLegControlTransparencyLayout)
        mainLayout.addLayout(groupBox)
                                                                                                                                                     
        ballBodyIKTwistLeftLayout = QtWidgets.QHBoxLayout()
        ballBodyIKTwistLeftLayout.addWidget(QtWidgets.QLabel("BallIKTwistLeft :"))
        self.ballBodyIKTwistLeftLine = QtWidgets.QLineEdit()
        self.ballBodyIKTwistLeftLine.setValidator(QtGui.QIntValidator(0,100))
        ballBodyIKTwistLeftLayout.addWidget(self.ballBodyIKTwistLeftLine)
        self.ballBodyIKTwistLeftLine.setText('90')
        ballBodyIKTwistLeftLayout.addWidget(QtWidgets.QLabel("(0 - 100)"))
        ballBodyIKTwistLeftLayout.addSpacing(215)
        groupBox.addLayout(ballBodyIKTwistLeftLayout)
        mainLayout.addLayout(groupBox)

        ballBodyIKTwistRightLayout = QtWidgets.QHBoxLayout()
        ballBodyIKTwistRightLayout.addWidget(QtWidgets.QLabel("BallIKTwistRightLayout :"))
        self.ballBodyIKTwistRightLine = QtWidgets.QLineEdit()
        self.ballBodyIKTwistRightLine.setValidator(QtGui.QIntValidator(0,270))
        ballBodyIKTwistRightLayout.addWidget(self.ballBodyIKTwistRightLine)
        self.ballBodyIKTwistRightLine.setText('270')
        ballBodyIKTwistRightLayout.addWidget(QtWidgets.QLabel("(0 - 270)"))
        ballBodyIKTwistRightLayout.addSpacing(215)
        groupBox.addLayout(ballBodyIKTwistRightLayout)
        mainLayout.addLayout(groupBox)

        toeBodyIKTwistLeftLayout = QtWidgets.QHBoxLayout()
        toeBodyIKTwistLeftLayout.addWidget(QtWidgets.QLabel("ToeIKTwistLeftLayout :"))
        self.toeBodyIKTwistLeftLine = QtWidgets.QLineEdit()
        self.toeBodyIKTwistLeftLine.setValidator(QtGui.QIntValidator(0,90))
        toeBodyIKTwistLeftLayout.addWidget(self.toeBodyIKTwistLeftLine)
        self.toeBodyIKTwistLeftLine.setText('90')
        toeBodyIKTwistLeftLayout.addWidget(QtWidgets.QLabel("(0 - 90)"))
        toeBodyIKTwistLeftLayout.addSpacing(215)
        groupBox.addLayout(toeBodyIKTwistLeftLayout)
        mainLayout.addLayout(groupBox)

        toeBodyIKTwistRightLayout = QtWidgets.QHBoxLayout()
        toeBodyIKTwistRightLayout.addWidget(QtWidgets.QLabel("ToeIKTwistRightLayout :"))
        self.toeBodyIKTwistRightLine = QtWidgets.QLineEdit()
        self.toeBodyIKTwistRightLine.setValidator(QtGui.QIntValidator(0,0))
        toeBodyIKTwistRightLayout.addWidget(self.toeBodyIKTwistRightLine)
        self.toeBodyIKTwistRightLine.setText('0')
        toeBodyIKTwistRightLayout.addWidget(QtWidgets.QLabel("(0 - 0)"))
        toeBodyIKTwistRightLayout.addSpacing(215)
        groupBox.addLayout(toeBodyIKTwistRightLayout)
        mainLayout.addLayout(groupBox)

        fkBodyArmControlScaleYZLayout = QtWidgets.QHBoxLayout()
        fkBodyArmControlScaleYZLayout.addWidget(QtWidgets.QLabel("FKArmControlScaleYZ :"))
        self.fkBodyArmControlScaleYZLine = QtWidgets.QLineEdit()
        self.fkBodyArmControlScaleYZLine.setValidator(QtGui.QIntValidator(0,10))
        fkBodyArmControlScaleYZLayout.addWidget(self.fkBodyArmControlScaleYZLine)
        self.fkBodyArmControlScaleYZLine.setText('10')
        fkBodyArmControlScaleYZLayout.addWidget(QtWidgets.QLabel("(0 - 10)"))
        fkBodyArmControlScaleYZLayout.addSpacing(215)
        groupBox.addLayout(fkBodyArmControlScaleYZLayout)
        mainLayout.addLayout(groupBox)

        fkBodyArmControlScaleYZMultiplierLayout = QtWidgets.QHBoxLayout()
        fkBodyArmControlScaleYZMultiplierLayout.addWidget(QtWidgets.QLabel("FKArmControlScaleYZMultiplierLayout :"))
        self.fkBodyArmControlScaleYZMultiplierLine = QtWidgets.QLineEdit()
        self.fkBodyArmControlScaleYZMultiplierLine.setValidator(QtGui.QDoubleValidator(0.0,1.0,4.0))
        fkBodyArmControlScaleYZMultiplierLayout.addWidget(self.fkBodyArmControlScaleYZMultiplierLine)
        self.fkBodyArmControlScaleYZMultiplierLine.setText('0.9')
        fkBodyArmControlScaleYZMultiplierLayout.addWidget(QtWidgets.QLabel("(0 - 1)"))
        fkBodyArmControlScaleYZMultiplierLayout.addSpacing(215)
        mainLayout.addLayout(groupBox)

        fkBodyArmControlTransparencyLayout = QtWidgets.QHBoxLayout()
        fkBodyArmControlTransparencyLayout.addWidget(QtWidgets.QLabel("FKArmControlTransparency :"))
        self.fkBodyArmControlTransparencyLine = QtWidgets.QLineEdit()
        self.fkBodyArmControlTransparencyLine.setValidator(QtGui.QDoubleValidator(0.0,1.0,4))
        fkBodyArmControlTransparencyLayout.addWidget(self.fkBodyArmControlTransparencyLine)
        self.fkBodyArmControlTransparencyLine.setText('0.85')
        fkBodyArmControlTransparencyLayout.addWidget(QtWidgets.QLabel("(0 - 1)"))
        fkBodyArmControlTransparencyLayout.addSpacing(215)
        mainLayout.addLayout(groupBox)














