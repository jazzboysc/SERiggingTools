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

from ..Utils import SERigObjectTypeHelper as RigObjectHelper
#reload(RigObjectHelper)

import PoseConfig
import SavePose

PoseRootPath = os.path.dirname(PoseConfig.__file__)
PoseFilePath = PoseRootPath + "\\PoseFile\\"

mainPoseWin = None

def openMayaWindow():
    global mainPoseWin
    if mainPoseWin != None:
        mainPoseWin.close()
    mainPoseWin = mainPoseBrowseWindow()
    mainPoseWin.show()

def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)

class mainPoseBrowseWindow(QtWidgets.QDialog):
    """docstring for ClassName"""
    def __init__(self, parent = getMayaWindow()):
        super(mainPoseBrowseWindow, self).__init__(parent , QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle('Pose Library')
        self.descLabel = QtWidgets.QLabel("Click Icon to use the pose", parent = self)

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.descLabel)
        self.addAndSetList(mainLayout)
        self.addPoseDataToList()
        self.addAndSetComboBox(mainLayout)
        self.addConfirmLayout(mainLayout)
        

    def addPoseDataToList(self):
        allPoseData = SavePose.openPoseLibraryFile()
        print allPoseData
        self.poseDataMap = dict()
        for oneData in allPoseData:
            # print "oneData"
            # print oneData
            item = QtWidgets.QListWidgetItem()
            for key, value in oneData.items():
                # print "value"
                # print value
                item.setIcon( QtGui.QIcon(value["icon"]))
                item.setText(value["poseName"])
                #item.setSizeHint(QtCore.QSize(80 , 80))
                self.listWidget.addItem(item)
                self.poseDataMap[value["poseName"]] = oneData[value["poseName"]]

    def addConfirmLayout(self , parent):
        confirmLayout = QtWidgets.QHBoxLayout()
        self.ConfirmButton = QtWidgets.QPushButton("Use Pose")
        self.CancelButton = QtWidgets.QPushButton("Cancel")
        #self.CancelButton.setFlat(True)
        confirmLayout.addWidget(self.ConfirmButton)
        confirmLayout.addWidget(self.CancelButton)
        self.connect(self.ConfirmButton, QtCore.SIGNAL("clicked()"), self.usePoseDataToCharacter)
        self.connect(self.CancelButton, QtCore.SIGNAL("clicked()"), self.close)
        parent.addLayout(confirmLayout)

    def addAndSetList(self , parent):
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        #self.listWidget.setGridSize(QtCore.QSize(80 , 80))
        self.listWidget.setIconSize(QtCore.QSize(80 , 80));
        parent.addWidget(self.listWidget)

    def getCurrentHaveCharacter(self):
        cha = RigObjectHelper.listRigCharacters()
        return cha

    def addAndSetComboBox(self , parent):
        self.characterSelector = QtWidgets.QComboBox()
        CharacterArray = self.getCurrentHaveCharacter();
        for cha in CharacterArray:
            self.characterSelector.addItem(cha)
        descLabel = QtWidgets.QLabel("Please choose a character to use pose !", parent = self)
        parent.addWidget(descLabel)
        parent.addWidget(self.characterSelector)

    def usePoseDataToCharacter(self):
        chooseCha =  self.characterSelector.currentText()
        choosePose = self.listWidget.currentItem().text()
        poseData =  self.poseDataMap[choosePose]["rigData"]
        for ctrl, ctrlData in poseData[0].items():
            RigObjectHelper.setRigControlTransform(chooseCha , ctrl[0] , ctrl[1] , ctrl[2] , ctrlData[0] ,ctrlData[1] ,ctrlData[2] ,ctrlData[3] ,ctrlData[4] ,ctrlData[5] )