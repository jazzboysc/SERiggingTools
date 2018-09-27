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
        super(mainPoseBrowseWindow, self).__init__(parent)
        self.setWindowTitle('Pose Library')
        self.descLabel = QtWidgets.QLabel("Click Icon to use the pose", parent = self)

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.descLabel)
        
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        #self.listWidget.setGridSize(QtCore.QSize(80 , 80))
        self.listWidget.setIconSize(QtCore.QSize(80 , 80));
        mainLayout.addWidget(self.listWidget)

        item = QtWidgets.QListWidgetItem()
        item.setIcon( QtGui.QIcon(PoseFilePath + "1111.bmp") )
        item.setText("1111")
        #item.setSizeHint(QtCore.QSize(80 , 80))
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        item.setIcon( QtGui.QIcon(PoseFilePath + "Input a vaild pose name!!!.bmp") )
        item.setText("2222")
        #item.setSizeHint(QtCore.QSize(80 , 80))
        self.listWidget.addItem(item)

        confirmLayout = QtWidgets.QHBoxLayout()
        self.ConfirmButton = QtWidgets.QPushButton("Use Pose")
        self.CancelButton = QtWidgets.QPushButton("Cancel")
        confirmLayout.addWidget(self.ConfirmButton)
        confirmLayout.addWidget(self.CancelButton)
        mainLayout.addLayout(confirmLayout)