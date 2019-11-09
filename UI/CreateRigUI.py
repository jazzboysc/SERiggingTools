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

#http://doc.qt.io/qt-5/qtwidgets-dialogs-tabdialog-example.html

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


# def loadUI(uifile_path):
#     #QtCore.QResource.addSearchPath("E:/Users/admin/Documents/GitHub/SERiggingTools/UI")
#     uifile = QtCore.QFile(uifile_path)
#     print(uifile)
#     uifile.open(QtCore.QFile.ReadOnly)
#     #QtCore.QResource.registerResource("E:/Users/admin/Documents/GitHub/SERiggingTools/UI/UIResource.qrc")
#     uiWindow = QtUiTools.QUiLoader().load(uifile)
#     uifile.close()

#     rrr = QtCore.QResource.searchPaths()
#     print(rrr)

#     #uiWindow.label.setPixmap(QtGui.QPixmap(("E:/Users/admin/Documents/GitHub/SERiggingTools/UI/equipment_11_1.png")))
#     return uiWindow

def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)

#class BodyConfigTab(QtWidgets.QWidget):
#    def __init__(self, parent = getMayaWindow()):

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

        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)

        mainLayout.addWidget(separator)

        self.createBuilderConfigLayout(mainLayout)

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
        fkArmControlScaleYZ = int(self.fkBodyArmControlScaleYZLine.text())
        fkArmControlScaleYZMultiplier = float(self.fkBodyArmControlScaleYZMultiplierLine.text())
        fkArmControlTransparency = float(self.fkBodyArmControlTransparencyLine.text())
        createCircleFkFingerControl = self.circleFkFingerControlCheckBox.isChecked()
        circleFkFingerControlScaleFactor = 1.7
        createSimpleSpine = self.fixedEndsSpineOptionCheckBox.isChecked()
        createSpineFKSystem = self.createSpineFKSystemCheckBox.isChecked()
        createSimpleFKNeck = not self.ikDrivenNeckOptionCheckBox.isChecked()
        createCompactFootControl = self.compactFootControlCheckBox.isChecked()
        createNeckMuscleSplineSystem = self.NeckMuscleSplineOptionCheckBox.isChecked()
        neckMuscleSplineJointCount = int(self.neckMuscleSplineJointCountLine.text())
        usePortraitCameraFocalLength = self.PortraitCameraOptionCheckBox.isChecked()
        portraitCameraFocalLength = float(self.PortraitCameraFocalLengthLine.text())
        createFacialSystem = self.facialSystemOptionCheckBox.isChecked()
        createSpineNeckCircleFkControl = self.circleFkSpineNeckControlCheckBox.isChecked()
        createLimbCircleFkControl = self.circleFkLimbControlCheckBox.isChecked()
        createArmCircleIkControl = not self.cubeIkArmControlCheckBox.isChecked()
        createSpineCircleIkControl = not self.cubeIkSpineControlCheckBox.isChecked()

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
                        fkArmControlScaleYZ = fkArmControlScaleYZ,
                        fkArmControlScaleYZMultiplier = fkArmControlScaleYZMultiplier,
                        fkArmControlTransparency = fkArmControlTransparency,
                        createCircleFkFingerControl = createCircleFkFingerControl,
                        circleFkFingerControlScaleFactor = circleFkFingerControlScaleFactor,
                        createCompactFootControl = createCompactFootControl,
                        createSimpleSpine = createSimpleSpine,
                        createSpineFKSystem = createSpineFKSystem,
                        createSimpleFKNeck = createSimpleFKNeck,
                        createNeckMuscleSplineSystem = createNeckMuscleSplineSystem,
                        neckMuscleSplineJointCount = neckMuscleSplineJointCount,
                        usePortraitCameraFocalLength = usePortraitCameraFocalLength,
                        portraitCameraFocalLength = portraitCameraFocalLength,
                        createFacialSystem = createFacialSystem,
                        createArmCircleFkControl = createLimbCircleFkControl,
                        createArmCircleIkControl = createArmCircleIkControl,
                        createSpineCircleFkControl = createSpineNeckCircleFkControl,
                        createSpineCircleIkControl = createSpineCircleIkControl,
                        createNeckCircleFkControl = createSpineNeckCircleFkControl,
                        createLegCircleFkControl = createLimbCircleFkControl
                        )
        
        # Close the create rig window.
        self.close()

    def createBuilderConfigLayout(self, mainLayout):

        tabs = QtWidgets.QTabWidget()

        # Body config tab page.
        pageBodyConfig = QtWidgets.QWidget()
        bodyConfigTabPageLayout = QtWidgets.QVBoxLayout()
        pageBodyConfig.setLayout(bodyConfigTabPageLayout)
        tabs.addTab(pageBodyConfig, "Body Configuration")

        # Head config tab page.
        pageHeadConfig = QtWidgets.QWidget()
        headConfigTabPageLayout = QtWidgets.QVBoxLayout()
        pageHeadConfig.setLayout(headConfigTabPageLayout)
        tabs.addTab(pageHeadConfig, "Head Configuration")

        # Weapon config tab page.
        pageWeaponConfig = QtWidgets.QWidget()
        weaponConfigTabPageLayout = QtWidgets.QVBoxLayout()
        pageWeaponConfig.setLayout(weaponConfigTabPageLayout)
        tabs.addTab(pageWeaponConfig, "Weapon Configuration")

        # Body config tab page layout.
        upperBodyUpperLayout = QtWidgets.QHBoxLayout()
        upperBodyUpperLayout.addWidget(QtWidgets.QLabel("Upper Arm Twist :"))
        self.upperBodyUpperLine = QtWidgets.QLineEdit()
        self.upperBodyUpperLine.setValidator(QtGui.QIntValidator(1, 5))
        upperBodyUpperLayout.addWidget(self.upperBodyUpperLine)
        self.upperBodyUpperLine.setText('2')
        upperBodyUpperLayout.addWidget(QtWidgets.QLabel("(1 - 5)"))
        upperBodyUpperLayout.addSpacing(220)
        bodyConfigTabPageLayout.addLayout(upperBodyUpperLayout)

        upperBodyLowerLayout = QtWidgets.QHBoxLayout()
        upperBodyLowerLayout.addWidget(QtWidgets.QLabel("Lower Arm Twist :"))
        self.upperBodyLowerLine = QtWidgets.QLineEdit()
        self.upperBodyLowerLine.setValidator(QtGui.QIntValidator(1, 5))
        upperBodyLowerLayout.addWidget(self.upperBodyLowerLine)
        self.upperBodyLowerLine.setText('2')
        upperBodyLowerLayout.addWidget(QtWidgets.QLabel("(1 - 5)"))
        upperBodyLowerLayout.addSpacing(220)
        bodyConfigTabPageLayout.addLayout(upperBodyLowerLayout)

        lowerBodyUpperLayout = QtWidgets.QHBoxLayout()
        lowerBodyUpperLayout.addWidget(QtWidgets.QLabel("Upper Leg Twist :"))
        self.lowerBodyUpperLine = QtWidgets.QLineEdit()
        self.lowerBodyUpperLine.setValidator(QtGui.QIntValidator(1, 5))
        lowerBodyUpperLayout.addWidget(self.lowerBodyUpperLine)
        self.lowerBodyUpperLine.setText('2')
        lowerBodyUpperLayout.addWidget(QtWidgets.QLabel("(1 - 5)"))
        lowerBodyUpperLayout.addSpacing(220)
        bodyConfigTabPageLayout.addLayout(lowerBodyUpperLayout)

        lowerBodyLowerLayout = QtWidgets.QHBoxLayout()
        lowerBodyLowerLayout.addWidget(QtWidgets.QLabel("Lower Leg Twist :"))
        self.lowerBodyLowerLine = QtWidgets.QLineEdit()
        self.lowerBodyUpperLine.setValidator(QtGui.QIntValidator(1, 5))
        lowerBodyLowerLayout.addWidget(self.lowerBodyLowerLine)
        self.lowerBodyLowerLine.setText('1')
        lowerBodyLowerLayout.addWidget(QtWidgets.QLabel("(1 - 5)"))
        lowerBodyLowerLayout.addSpacing(220)
        bodyConfigTabPageLayout.addLayout(lowerBodyLowerLayout)

        spineOptionLayout = QtWidgets.QHBoxLayout()
        spineOptionLayout.addWidget(QtWidgets.QLabel("Create Simple Spine:"))
        self.fixedEndsSpineOptionCheckBox = QtWidgets.QCheckBox()
        self.fixedEndsSpineOptionCheckBox.setChecked(False)
        spineOptionLayout.addWidget(self.fixedEndsSpineOptionCheckBox)
        spineOptionLayout.addSpacing(25)
        spineOptionLayout.addWidget(QtWidgets.QLabel("Create Spine FK System:"))
        self.createSpineFKSystemCheckBox = QtWidgets.QCheckBox()
        self.createSpineFKSystemCheckBox.setChecked(True)
        spineOptionLayout.addWidget(self.createSpineFKSystemCheckBox)
        spineOptionLayout.addSpacing(270)
        bodyConfigTabPageLayout.addLayout(spineOptionLayout)

        mainBodyCtrlOffsetLayout = QtWidgets.QHBoxLayout()
        mainBodyCtrlOffsetLayout.addWidget(QtWidgets.QLabel("Main Control Offset :"))
        self.mainBodyCtrlOffsetLine = QtWidgets.QLineEdit()
        self.mainBodyCtrlOffsetLine.setValidator(QtGui.QIntValidator(0, 50))
        mainBodyCtrlOffsetLayout.addWidget(self.mainBodyCtrlOffsetLine)
        self.mainBodyCtrlOffsetLine.setText('30')
        mainBodyCtrlOffsetLayout.addWidget(QtWidgets.QLabel("(0 - 50)"))
        mainBodyCtrlOffsetLayout.addSpacing(215)
        bodyConfigTabPageLayout.addLayout(mainBodyCtrlOffsetLayout)
        
        fkLegBodyControlScaleYZLayout = QtWidgets.QHBoxLayout()
        fkLegBodyControlScaleYZLayout.addWidget(QtWidgets.QLabel("FK Leg Control Scale YZ :"))
        self.fkLegBodyControlScaleYZLine = QtWidgets.QLineEdit()
        self.fkLegBodyControlScaleYZLine.setValidator(QtGui.QIntValidator(0, 30))
        fkLegBodyControlScaleYZLayout.addWidget(self.fkLegBodyControlScaleYZLine)
        self.fkLegBodyControlScaleYZLine.setText('19')
        fkLegBodyControlScaleYZLayout.addWidget(QtWidgets.QLabel("(0 - 30)"))
        fkLegBodyControlScaleYZLayout.addSpacing(215)
        bodyConfigTabPageLayout.addLayout(fkLegBodyControlScaleYZLayout)

        fkLegBodyControlScaleYZMultiplierLayout = QtWidgets.QHBoxLayout()
        fkLegBodyControlScaleYZMultiplierLayout.addWidget(QtWidgets.QLabel("FK Leg Control Scale YZ Multiplier :"))
        self.fkLegBodyControlScaleYZMultiplierLine = QtWidgets.QLineEdit()
        self.fkLegBodyControlScaleYZMultiplierLine.setValidator(QtGui.QDoubleValidator(0.0, 1.0, 4))
        fkLegBodyControlScaleYZMultiplierLayout.addWidget(self.fkLegBodyControlScaleYZMultiplierLine)
        self.fkLegBodyControlScaleYZMultiplierLine.setText('0.75')
        fkLegBodyControlScaleYZMultiplierLayout.addWidget(QtWidgets.QLabel("(0 - 1)"))
        fkLegBodyControlScaleYZMultiplierLayout.addSpacing(215)
        bodyConfigTabPageLayout.addLayout(fkLegBodyControlScaleYZMultiplierLayout)

        fkLegControlTransparencyLayout = QtWidgets.QHBoxLayout()
        fkLegControlTransparencyLayout.addWidget(QtWidgets.QLabel("FK Leg Control Transparency :"))
        self.fkLegControlTransparencyLine = QtWidgets.QLineEdit()
        self.fkLegControlTransparencyLine.setValidator(QtGui.QDoubleValidator(0.0, 1.0, 4))
        fkLegControlTransparencyLayout.addWidget(self.fkLegControlTransparencyLine)
        self.fkLegControlTransparencyLine.setText('0.85')
        fkLegControlTransparencyLayout.addWidget(QtWidgets.QLabel("(0 - 1)"))
        fkLegControlTransparencyLayout.addSpacing(215)
        bodyConfigTabPageLayout.addLayout(fkLegControlTransparencyLayout)
                                                                                                                                                             
        fkBodyArmControlScaleYZLayout = QtWidgets.QHBoxLayout()
        fkBodyArmControlScaleYZLayout.addWidget(QtWidgets.QLabel("FK Arm Control Scale YZ :"))
        self.fkBodyArmControlScaleYZLine = QtWidgets.QLineEdit()
        self.fkBodyArmControlScaleYZLine.setValidator(QtGui.QIntValidator(0, 10))
        fkBodyArmControlScaleYZLayout.addWidget(self.fkBodyArmControlScaleYZLine)
        self.fkBodyArmControlScaleYZLine.setText('10')
        fkBodyArmControlScaleYZLayout.addWidget(QtWidgets.QLabel("(0 - 10)"))
        fkBodyArmControlScaleYZLayout.addSpacing(215)
        bodyConfigTabPageLayout.addLayout(fkBodyArmControlScaleYZLayout)

        fkCircleFkControlOptionLayout = QtWidgets.QHBoxLayout()
        fkCircleFkControlOptionLayout.addWidget(QtWidgets.QLabel("Create Circle FK Finger Control :"))
        self.circleFkFingerControlCheckBox = QtWidgets.QCheckBox()
        self.circleFkFingerControlCheckBox.setChecked(True)
        fkCircleFkControlOptionLayout.addWidget(self.circleFkFingerControlCheckBox)

        fkCircleFkControlOptionLayout.addWidget(QtWidgets.QLabel("Create Circle FK Limb Control :"))
        self.circleFkLimbControlCheckBox = QtWidgets.QCheckBox()
        self.circleFkLimbControlCheckBox.setChecked(True)
        fkCircleFkControlOptionLayout.addWidget(self.circleFkLimbControlCheckBox)

        fkCircleFkControlOptionLayout.addWidget(QtWidgets.QLabel("Create Circle FK Spine and Neck Control :"))
        self.circleFkSpineNeckControlCheckBox = QtWidgets.QCheckBox()
        self.circleFkSpineNeckControlCheckBox.setChecked(True)
        fkCircleFkControlOptionLayout.addWidget(self.circleFkSpineNeckControlCheckBox)

        fkCircleFkControlOptionLayout.addSpacing(215)
        bodyConfigTabPageLayout.addLayout(fkCircleFkControlOptionLayout)

        limbControlOptionLayout = QtWidgets.QHBoxLayout()
        limbControlOptionLayout.addWidget(QtWidgets.QLabel("Create Compact Foot Control :"))
        self.compactFootControlCheckBox = QtWidgets.QCheckBox()
        self.compactFootControlCheckBox.setChecked(False)
        limbControlOptionLayout.addWidget(self.compactFootControlCheckBox)

        limbControlOptionLayout.addWidget(QtWidgets.QLabel("Create Cube Arm IK Control :"))
        self.cubeIkArmControlCheckBox = QtWidgets.QCheckBox()
        self.cubeIkArmControlCheckBox.setChecked(True)
        limbControlOptionLayout.addWidget(self.cubeIkArmControlCheckBox)

        limbControlOptionLayout.addWidget(QtWidgets.QLabel("Create Cube Spine IK Control :"))
        self.cubeIkSpineControlCheckBox = QtWidgets.QCheckBox()
        self.cubeIkSpineControlCheckBox.setChecked(True)
        limbControlOptionLayout.addWidget(self.cubeIkSpineControlCheckBox)

        limbControlOptionLayout.addSpacing(270)
        bodyConfigTabPageLayout.addLayout(limbControlOptionLayout)

        fkBodyArmControlScaleYZMultiplierLayout = QtWidgets.QHBoxLayout()
        fkBodyArmControlScaleYZMultiplierLayout.addWidget(QtWidgets.QLabel("FK Arm Control Scale YZ Multiplier :"))
        self.fkBodyArmControlScaleYZMultiplierLine = QtWidgets.QLineEdit()
        self.fkBodyArmControlScaleYZMultiplierLine.setValidator(QtGui.QDoubleValidator(0.0, 1.0, 4.0))
        fkBodyArmControlScaleYZMultiplierLayout.addWidget(self.fkBodyArmControlScaleYZMultiplierLine)
        self.fkBodyArmControlScaleYZMultiplierLine.setText('0.9')
        fkBodyArmControlScaleYZMultiplierLayout.addWidget(QtWidgets.QLabel("(0 - 1)"))
        fkBodyArmControlScaleYZMultiplierLayout.addSpacing(215)
        bodyConfigTabPageLayout.addLayout(fkBodyArmControlScaleYZMultiplierLayout)

        fkBodyArmControlTransparencyLayout = QtWidgets.QHBoxLayout()
        fkBodyArmControlTransparencyLayout.addWidget(QtWidgets.QLabel("FK Arm Control Transparency :"))
        self.fkBodyArmControlTransparencyLine = QtWidgets.QLineEdit()
        self.fkBodyArmControlTransparencyLine.setValidator(QtGui.QDoubleValidator(0.0, 1.0, 4.0))
        fkBodyArmControlTransparencyLayout.addWidget(self.fkBodyArmControlTransparencyLine)
        self.fkBodyArmControlTransparencyLine.setText('0.85')
        fkBodyArmControlTransparencyLayout.addWidget(QtWidgets.QLabel("(0 - 1)"))
        fkBodyArmControlTransparencyLayout.addSpacing(215)
        bodyConfigTabPageLayout.addLayout(fkBodyArmControlTransparencyLayout)

        # Head config tab page layout.
        neckOptionLayout = QtWidgets.QHBoxLayout()
        neckOptionLayout.addWidget(QtWidgets.QLabel("Create IK Driven Neck:"))
        self.ikDrivenNeckOptionCheckBox = QtWidgets.QCheckBox()
        self.ikDrivenNeckOptionCheckBox.setChecked(False)
        neckOptionLayout.addWidget(self.ikDrivenNeckOptionCheckBox)
        neckOptionLayout.addSpacing(25)
        neckOptionLayout.addWidget(QtWidgets.QLabel("Create Neck Muscle Spline System:"))
        self.NeckMuscleSplineOptionCheckBox = QtWidgets.QCheckBox()
        self.NeckMuscleSplineOptionCheckBox.setChecked(False)
        neckOptionLayout.addWidget(self.NeckMuscleSplineOptionCheckBox)
        neckOptionLayout.addSpacing(25)
        neckOptionLayout.addWidget(QtWidgets.QLabel("Muscle Spline Joint Count:"))
        self.neckMuscleSplineJointCountLine = QtWidgets.QLineEdit()
        self.neckMuscleSplineJointCountLine.setValidator(QtGui.QIntValidator(3, 7))
        neckOptionLayout.addWidget(self.neckMuscleSplineJointCountLine)
        self.neckMuscleSplineJointCountLine.setText('3')
        neckOptionLayout.addWidget(QtWidgets.QLabel("(3 - 7)"))
        neckOptionLayout.addSpacing(270)
        headConfigTabPageLayout.addLayout(neckOptionLayout)

        separator01 = QtWidgets.QFrame()
        separator01.setFrameShape(QtWidgets.QFrame.HLine)
        separator01.setFrameShadow(QtWidgets.QFrame.Sunken)
        headConfigTabPageLayout.addWidget(separator01)

        portraitCameraOptionLayout = QtWidgets.QHBoxLayout()
        portraitCameraOptionLayout.addWidget(QtWidgets.QLabel("Use Portrait Camera Focal Length:"))
        self.PortraitCameraOptionCheckBox = QtWidgets.QCheckBox()
        self.PortraitCameraOptionCheckBox.setChecked(True)
        portraitCameraOptionLayout.addWidget(self.PortraitCameraOptionCheckBox)
        portraitCameraOptionLayout.addSpacing(25)
        portraitCameraOptionLayout.addWidget(QtWidgets.QLabel("Portrait Camera Focal Length:"))
        self.PortraitCameraFocalLengthLine = QtWidgets.QLineEdit()
        self.PortraitCameraFocalLengthLine.setValidator(QtGui.QDoubleValidator(35.0, 135.0, 2))
        portraitCameraOptionLayout.addWidget(self.PortraitCameraFocalLengthLine)
        self.PortraitCameraFocalLengthLine.setText('85')
        portraitCameraOptionLayout.addWidget(QtWidgets.QLabel("(35 - 135)"))
        portraitCameraOptionLayout.addSpacing(400)
        headConfigTabPageLayout.addLayout(portraitCameraOptionLayout)

        separator02 = QtWidgets.QFrame()
        separator02.setFrameShape(QtWidgets.QFrame.HLine)
        separator02.setFrameShadow(QtWidgets.QFrame.Sunken)
        headConfigTabPageLayout.addWidget(separator02)

        # Facial system layout.
        facialSystemOptionLayout = QtWidgets.QHBoxLayout()
        facialSystemOptionLayout.addWidget(QtWidgets.QLabel("Create F.A.C.S facial system:"))
        self.facialSystemOptionCheckBox = QtWidgets.QCheckBox()
        self.facialSystemOptionCheckBox.setChecked(False)
        self.facialSystemOptionCheckBox.setEnabled(False)
        self.facialSystemOptionCheckBox.setStyleSheet("QCheckBox { background-color: grey }")
        facialSystemOptionLayout.addWidget(self.facialSystemOptionCheckBox)
        facialSystemOptionLayout.addSpacing(800)
        headConfigTabPageLayout.addLayout(facialSystemOptionLayout)

        headConfigTabPageLayout.addSpacing(300)

        mainLayout.addWidget(tabs)

        self.connect(self.ikDrivenNeckOptionCheckBox, QtCore.SIGNAL("clicked()"), self.validateFacialSystemDependency)

    def validateFacialSystemDependency(self):
        ikDrivenNeckChecked = self.ikDrivenNeckOptionCheckBox.isChecked()
        self.ikDrivenNeckOptionCheckBox.checkState 
        if ikDrivenNeckChecked:
            self.facialSystemOptionCheckBox.setEnabled(True)
            self.facialSystemOptionCheckBox.setStyleSheet("QCheckBox { background-color: dark grey }")
        else:
            self.facialSystemOptionCheckBox.setChecked(False)
            self.facialSystemOptionCheckBox.setEnabled(False)
            self.facialSystemOptionCheckBox.setStyleSheet("QCheckBox { background-color: grey }")