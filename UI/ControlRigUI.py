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

def openControlRigWindow():
    ''' todo: stop open more than one window'''
    global ui
    ui = loadUI(uifile_path)
    ui.show()

def loadUI(uifile_path):
    #QtCore.QResource.addSearchPath("E:/Users/admin/Documents/GitHub/SERiggingTools/UI")
    uifile = QtCore.QFile(uifile_path)
    print(uifile)
    uifile.open(QtCore.QFile.ReadOnly)
    #QtCore.QResource.registerResource("E:/Users/admin/Documents/GitHub/SERiggingTools/UI/UIResource.qrc")
    uiWindow = QtUiTools.QUiLoader().load(uifile)
    uifile.close()

    rrr = QtCore.QResource.searchPaths()
    print(rrr)

    #uiWindow.label.setPixmap(QtGui.QPixmap(("E:/Users/admin/Documents/GitHub/SERiggingTools/UI/equipment_11_1.png")))
    refreshCharacterInSelector(uiWindow)
    
    return uiWindow

def refreshCharacterInSelector(uiWindow):
    CharacterArray = getCurrentHaveCharacter();
    uiWindow.characterSelector.addItem("djashdjkahskdhask")
    uiWindow.characterSelector.addItem("djashdjkahskdhask")
    uiWindow.characterSelector.addItem("djashdjkahskdhask")


def getCurrentHaveCharacter():
    pass