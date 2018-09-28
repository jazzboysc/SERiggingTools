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
import functools

import cPickle

from ..Character import SECharacter

from ..Utils import SERigObjectTypeHelper as RigObjectHelper

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

    setControlToButtonMap(uiWindow)
    setSelectorCallBack(uiWindow)
    setButtonCallback(uiWindow)

    #uiWindow.label.setPixmap(QtGui.QPixmap(("E:/Users/admin/Documents/GitHub/SERiggingTools/UI/equipment_11_1.png")))
    refreshCharacterInSelector(uiWindow)
    return uiWindow

def setSelectorCallBack(uiWindow):
    def selecterChangeCallback(index):
        name = uiWindow.characterSelector.currentText()
        getAllControllRigByName(name)
        print name
    uiWindow.characterSelector.currentIndexChanged.connect(selecterChangeCallback) 

def refreshCharacterInSelector(uiWindow):
    CharacterArray = getCurrentHaveCharacter();
    uiWindow.characterSelector.addItem("None")
    for x in range(len(CharacterArray)):
        uiWindow.characterSelector.addItem(CharacterArray[x])
    index = uiWindow.characterSelector.currentText()
    print index

def getCurrentHaveCharacter():
    cha = RigObjectHelper.listRigCharacters()
    return cha

def getAllControllRigByName(charName):
    if charName != "None":
        characterControls = RigObjectHelper.listRigCharacterControls(charName)
        print characterControls
        return characterControls
    return None

def setControlToButtonMap(uiWindow):
    global ControlToButton
    ControlToButton = {(u'RS_Right', u'RT_LegPV', 0): u'R_Leg_PV_Ctrl',
                    (u'RS_Left', u'RT_MiddleFK', 2): u'FK_L_Middle_02_Ctrl',
                    (u'RS_Right', u'RT_PinkyFK', 2): u'FK_R_Pinky_02_Ctrl', 
                    (u'RS_Right', u'RT_ThumbFK', 2): u'FK_R_Thumb_02_Ctrl',
                    (u'RS_Left', u'RT_PinkyFK', 2): u'FK_L_Pinky_02_Ctrl',
                    (u'RS_Right', u'RT_ArmPV', 0): u'R_Arm_PV_Ctrl', 
                    (u'RS_Left', u'RT_MiddleFK', 1): u'FK_L_Middle_01_Ctrl', 
                    (u'RS_Right', u'RT_PinkyFK', 3): u'FK_R_Pinky_03_Ctrl',
                    (u'RS_Left', u'RT_PinkyFK', 3): u'FK_L_Pinky_03_Ctrl',
                    (u'RS_Center', u'RT_SpineFK', 0): uiWindow.FK_C_Spine_0_Ctrl, 
                    (u'RS_Left', u'RT_MiddleFK', 0): u'FK_L_Middle_00_Ctrl',
                    (u'RS_Right', u'RT_WristFK', 0): uiWindow.FK_R_Arm2_Ctrl, 
                    (u'RS_Center', u'RT_SpineFK', 1): uiWindow.FK_C_Spine_1_Ctrl,
                    (u'RS_Left', u'RT_ThumbFK', 2): u'FK_L_Thumb_02_Ctrl',
                    (u'RS_Right', u'RT_Clavicle', 0): uiWindow.R_Arm_Clav_Rotation_Ctrl,
                    (u'RS_Left', u'RT_PinkyFK', 1): u'FK_L_Pinky_01_Ctrl',
                    (u'RS_Right', u'RT_PinkyFK', 1): u'FK_R_Pinky_01_Ctrl',
                    (u'RS_Center', u'RT_NeckFK', 0): uiWindow.FK_C_Neck_0_Ctrl,
                    (u'RS_Right', u'RT_AnkleIKRotation', 0): u'R_Leg_IK_Rotation_Ctrl',
                    (u'RS_Left', u'RT_ThumbFK', 1): u'FK_L_Thumb_01_Ctrl', 
                    (u'RS_Left', u'RT_AnkleIKRotation', 0): u'L_Leg_IK_Rotation_Ctrl', 
                    (u'RS_Left', u'RT_IndexFK', 3): u'FK_L_Index_03_Ctrl',
                    (u'RS_Right', u'RT_ArmIKMain', 0): u'R_Arm_IK_Main_Ctrl', 
                    (u'RS_Left', u'RT_ArmPV', 0): u'L_Arm_PV_Ctrl', 
                    (u'RS_Left', u'RT_ShoulderFK', 0): uiWindow.FK_L_Arm0_Ctrl,
                    (u'RS_Left', u'RT_ThumbFK', 0): u'FK_L_Thumb_00_Ctrl',
                    (u'RS_Left', u'RT_RingFK', 0): u'FK_L_Ring_00_Ctrl', 
                    (u'RS_Left', u'RT_IndexFK', 2): u'FK_L_Index_02_Ctrl',
                    (u'RS_Left', u'RT_FootIKMain', 0): u'L_Leg_IK_Main_Ctrl', 
                    (u'RS_Right', u'RT_MiddleFK', 0): u'FK_R_Middle_00_Ctrl',
                    (u'RS_Left', u'RT_RingFK', 1): u'FK_L_Ring_01_Ctrl',
                    (u'RS_Left', u'RT_IndexFK', 1): u'FK_L_Index_01_Ctrl',
                    (u'RS_Left', u'RT_LegFK', 1): uiWindow.FK_L_Leg1_Ctrl, 
                    (u'RS_Left', u'RT_RingFK', 3): u'FK_L_Ring_03_Ctrl',
                    (u'RS_Right', u'RT_MiddleFK', 3): u'FK_R_Middle_03_Ctrl', 
                    (u'RS_Left', u'RT_IndexFK', 0): u'FK_L_Index_00_Ctrl',
                    (u'RS_Left', u'RT_LegFK', 0): uiWindow.FK_L_Leg0_Ctrl,
                    (u'RS_Right', u'RT_MiddleFK', 2): u'FK_R_Middle_02_Ctrl', 
                    (u'RS_Right', u'RT_FootToeSwive', 0): u'R_Leg_ToeSwive_Ctrl',
                    (u'RS_Left', u'RT_LegFK', 3): uiWindow.FK_L_Leg3_Ctrl, 
                    (u'RS_Right', u'RT_ThumbFK', 0): u'FK_R_Thumb_00_Ctrl', 
                    (u'RS_Center', u'RT_SpinePelvis', 0): u'C_SpinePelvis_Ctrl', 
                    (u'RS_Left', u'RT_LegFK', 2): uiWindow.FK_L_Leg2_Ctrl, 
                    (u'RS_Left', u'RT_PinkyFK', 0): u'FK_L_Pinky_00_Ctrl', 
                    (u'RS_Right', u'RT_FootRotation', 0): u'R_Leg_Rotation_Ctrl',
                    (u'RS_Right', u'RT_FootBaseSwive', 0): u'R_Leg_FootBaseSwive_Ctrl',
                    (u'RS_Right', u'RT_IndexFK', 3): u'FK_R_Index_03_Ctrl',
                    (u'RS_Left', u'RT_FootBaseSwive', 0): u'L_Leg_FootBaseSwive_Ctrl',
                    (u'RS_Right', u'RT_LegFK', 3): uiWindow.FK_R_Leg3_Ctrl,
                    (u'RS_Left', u'RT_RingFK', 2): u'FK_L_Ring_02_Ctrl',
                    (u'RS_Right', u'RT_LegFK', 2): uiWindow.FK_R_Leg2_Ctrl,
                    (u'RS_Right', u'RT_LegFK', 1): uiWindow.FK_R_Leg1_Ctrl,  
                    (u'RS_Right', u'RT_ThumbFK', 1): u'FK_R_Thumb_01_Ctrl',
                    (u'RS_Right', u'RT_FootIKMain', 0): u'R_Leg_IK_Main_Ctrl',
                    (u'RS_Right', u'RT_MiddleFK', 1): u'FK_R_Middle_01_Ctrl', 
                    (u'RS_Right', u'RT_PinkyFK', 0): u'FK_R_Pinky_00_Ctrl',
                    (u'RS_Right', u'RT_RingFK', 0): u'FK_R_Ring_00_Ctrl', 
                    (u'RS_Right', u'RT_LegFK', 0): uiWindow.FK_R_Leg0_Ctrl,
                    (u'RS_Right', u'RT_ShoulderFK', 0): uiWindow.FK_R_Arm0_Ctrl, 
                    (u'RS_Center', u'RT_SpineUpperBody', 0): uiWindow.C_SpineUpperBody_Ctrl, 
                    (u'RS_Left', u'RT_LegPV', 0): u'L_Leg_PV_Ctrl', 
                    (u'RS_Right', u'RT_RingFK', 2): u'FK_R_Ring_02_Ctrl',
                    (u'RS_Right', u'RT_RingFK', 1): u'FK_R_Ring_01_Ctrl',
                    (u'RS_Center', u'RT_HeadFK', 0): uiWindow.FK_C_Head_Ctrl, 
                    (u'RS_Center', u'RT_NeckFK', 1): uiWindow.FK_C_Neck_1_Ctrl, 
                    (u'RS_Left', u'RT_ElbowFK', 0): uiWindow.FK_L_Arm1_Ctrl, 
                    (u'RS_Left', u'RT_FootRotation', 0): u'L_Leg_Rotation_Ctrl',
                    (u'RS_Left', u'RT_Clavicle', 0): uiWindow.L_Arm_Clav_Rotation_Ctrl,
                    (u'RS_Right', u'RT_IndexFK', 2): u'FK_R_Index_02_Ctrl', 
                    (u'RS_Center', u'RT_SpineChest', 0): u'C_SpineChest_Ctrl', 
                    (u'RS_Left', u'RT_WristFK', 0): uiWindow.FK_L_Arm2_Ctrl,
                    (u'RS_Right', u'RT_RingFK', 3): u'FK_R_Ring_03_Ctrl', 
                    (u'RS_Right', u'RT_ElbowFK', 0): uiWindow.FK_R_Arm1_Ctrl, 
                    (u'RS_Left', u'RT_ArmIKMain', 0): u'L_Arm_IK_Main_Ctrl',
                    (u'RS_Left', u'RT_MiddleFK', 3): u'FK_L_Middle_03_Ctrl',
                    (u'RS_Right', u'RT_IndexFK', 0): u'FK_R_Index_00_Ctrl', 
                    (u'RS_Left', u'RT_FootToeSwive', 0): u'L_Leg_ToeSwive_Ctrl', 
                    (u'RS_Right', u'RT_IndexFK', 1): u'FK_R_Index_01_Ctrl'
    }

    global ButtonToControl
    ButtonToControl = {
        uiWindow.FK_C_Neck_0_Ctrl:(u'RS_Center', u'RT_NeckFK', 0),
        uiWindow.FK_C_Neck_1_Ctrl:(u'RS_Center', u'RT_NeckFK', 1),
        uiWindow.FK_C_Head_Ctrl:(u'RS_Center', u'RT_HeadFK', 0),
        uiWindow.FK_C_Spine_1_Ctrl:(u'RS_Center', u'RT_SpineFK', 1),
        uiWindow.FK_C_Spine_0_Ctrl:(u'RS_Center', u'RT_SpineFK', 0), 
        uiWindow.C_SpineUpperBody_Ctrl:(u'RS_Center', u'RT_SpineUpperBody', 0),
        uiWindow.FK_L_Leg0_Ctrl:(u'RS_Left', u'RT_LegFK', 0),
        uiWindow.FK_L_Leg1_Ctrl :(u'RS_Left', u'RT_LegFK', 1),
        uiWindow.FK_L_Leg2_Ctrl :(u'RS_Left', u'RT_LegFK', 2),
        uiWindow.FK_L_Leg3_Ctrl:(u'RS_Left', u'RT_LegFK', 3),
        uiWindow.FK_R_Leg0_Ctrl:(u'RS_Right', u'RT_LegFK', 0), 
        uiWindow.FK_R_Leg1_Ctrl:(u'RS_Right', u'RT_LegFK', 1),
        uiWindow.FK_R_Leg2_Ctrl:(u'RS_Right', u'RT_LegFK', 2),
        uiWindow.FK_R_Leg3_Ctrl:(u'RS_Right', u'RT_LegFK', 3), 
        uiWindow.FK_R_Arm1_Ctrl:(u'RS_Right', u'RT_ElbowFK', 0),
        uiWindow.FK_L_Arm2_Ctrl:(u'RS_Left', u'RT_WristFK', 0),
        uiWindow.FK_L_Arm1_Ctrl:(u'RS_Left', u'RT_ElbowFK', 0),
        uiWindow.FK_R_Arm2_Ctrl:(u'RS_Right', u'RT_WristFK', 0),
        uiWindow.FK_R_Arm0_Ctrl:(u'RS_Right', u'RT_ShoulderFK', 0),
        uiWindow.FK_L_Arm0_Ctrl:(u'RS_Left', u'RT_ShoulderFK', 0),
        uiWindow.L_Arm_Clav_Rotation_Ctrl:(u'RS_Left', u'RT_Clavicle', 0),
        uiWindow.R_Arm_Clav_Rotation_Ctrl:(u'RS_Right', u'RT_Clavicle', 0),
    }

def getCurrentSelecterName(uiWindow):
    name = uiWindow.characterSelector.currentText()
    if name == "None":
        #cmds.confirmDialog(title = "Wrong Character", icon = "critical", message = "Please select a vaild Character name in comboBox" )
        return name
    return name

def setButtonCallback(uiWindow):
    def selectControl(CurrWidget):
        data = ButtonToControl[CurrWidget]
        name = getCurrentSelecterName(uiWindow)
        currentRig = RigObjectHelper.getRigControlObject(name, data[0], data[1], data[2])
        cmds.select(currentRig)
        
    # uiWindow.FK_C_Neck_0_Ctrl.clicked.connect(lambda *arg:selectControl(uiWindow.FK_C_Neck_0_Ctrl))
    # uiWindow.FK_C_Neck_1_Ctrl.clicked.connect(lambda *arg:selectControl(uiWindow.FK_C_Neck_1_Ctrl))

    # for key in ButtonToControl:
    #     def function(*arg):
    #         print arg
    #         print key
    #         keyy = key 
    #         lambda *arg:selectControl(keyy)
    #         # selectControl(key)
    #     # key.clicked.connect(lambda *arg:selectControl(key))
    #     key.clicked.connect(function)
    #     print key
    
    # for key, value in ButtonToControl.items():
    #     print (key, ' value : ', value)
    #     valuee = value[2]
    #     aaa = callbackobj(key)
    #     print aaa.key
    #     def function(*arg):
    #         # print key , valuee
    #         print aaa.key
    #         lambda *arg:selectControl(aaa.key)
    #     key.clicked.connect(lambda *arg:selectControl(aaa.key))

    for key in ButtonToControl:
        callback = callbackobj(key , uiWindow)
        key.clicked.connect(functools.partial(callback.functor, callback))

class callbackobj():
    def __init__(self, key ,uiWindow):
        self.key = key
        self.uiWindow = uiWindow

    def functor(self , *arg):
        # print self.key
        self.selectControl()
    def selectControl(self):
        data = ButtonToControl[self.key]
        name = getCurrentSelecterName(self.uiWindow)
        currentRig = RigObjectHelper.getRigControlObject(name, data[0], data[1], data[2])
        cmds.select(currentRig)