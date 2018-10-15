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
from ..Rig import SERigBipedLimbComponent

import UIConfig
#"E:/Users/admin/Documents/GitHub/SERiggingTools/UI/LoadRiggingUI.ui"

uiRootFile = os.path.dirname(UIConfig.__file__)
uifile_path = uiRootFile + "/Control2Rig.ui"

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

    uiWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    setControlToButtonMap(uiWindow)
    setSelectorCallBack(uiWindow)
    setButtonCallback(uiWindow)
    setMutiSelectedButtonCallback(uiWindow)
    setResetToModelBasePose(uiWindow)
    setIKFKShow(uiWindow)

    uiWindow.BodyBG.setPixmap(QtGui.QPixmap((uiRootFile +"/ControllUIBG.png")))
    uiWindow.RHandBG.setPixmap(QtGui.QPixmap((uiRootFile +"/ControllUIRHandBG.png")))
    uiWindow.LHandBG.setPixmap(QtGui.QPixmap((uiRootFile +"/ControllUILHandBG.png")))
    refreshCharacterInSelector(uiWindow)
    return uiWindow

def setSelectorCallBack(uiWindow):
    def selecterChangeCallback(index):
        name = uiWindow.characterSelector.currentText()
        getAllControllRigByName(name)
    uiWindow.characterSelector.currentIndexChanged.connect(selecterChangeCallback) 

def refreshCharacterInSelector(uiWindow):
    CharacterArray = getCurrentHaveCharacter();
    uiWindow.characterSelector.addItem("None")
    for x in range(len(CharacterArray)):
        uiWindow.characterSelector.addItem(CharacterArray[x])
    index = uiWindow.characterSelector.currentText()

def getCurrentHaveCharacter():
    cha = RigObjectHelper.listRigCharacters()
    return cha

def getAllControllRigByName(charName):
    if charName != "None":
        characterControls = RigObjectHelper.listRigCharacterControls(charName)
        return characterControls
    return None

def setControlToButtonMap(uiWindow):
    '''{(u'RS_Center', u'RT_Global', 1): u'Global_01_Ctrl', (u'RS_Center', u'RT_Global', 0): u'Main_Ctrl', (u'RS_Center', u'RT_Global', 2): u'Global_02_Ctrl'}'''
    # global MainControllToButton 
    # MainControllToButton = {(u'RS_Center', u'RT_Global', 1): uiWindow.Global_01_Ctrl, (u'RS_Center', u'RT_Global', 0): uiWindow.Main_Ctrl, (u'RS_Center', u'RT_Global', 2): uiWindow.Global_02_Ctrl}
    # global ButtonToMainControll 
    # ButtonToMainControll = {uiWindow.Global_01_Ctrl:(u'RS_Center', u'RT_Global', 1), 
    #                         uiWindow.Main_Ctrl:(u'RS_Center', u'RT_Global', 0), 
    #                         uiWindow.Global_02_Ctrl:(u'RS_Center', u'RT_Global', 2)}
    global ControlToButton
    ControlToButton = {
                    (u'RS_Center', u'RT_SpineFK', 0): uiWindow.FK_C_Spine_0_Ctrl,
                    (u'RS_Right', u'RT_WristFK', 0): uiWindow.FK_R_Arm2_Ctrl, 
                    (u'RS_Center', u'RT_SpineFK', 1): uiWindow.FK_C_Spine_1_Ctrl,
                    (u'RS_Right', u'RT_Clavicle', 0): uiWindow.R_Arm_Clav_Rotation_Ctrl,
                    (u'RS_Center', u'RT_NeckFK', 0): uiWindow.FK_C_Neck_0_Ctrl,
                    (u'RS_Left', u'RT_ShoulderFK', 0): uiWindow.FK_L_Arm0_Ctrl,
                    (u'RS_Left', u'RT_LegFK', 1): uiWindow.FK_L_Leg1_Ctrl,
                    (u'RS_Left', u'RT_LegFK', 0): uiWindow.FK_L_Leg0_Ctrl,
                    (u'RS_Left', u'RT_LegFK', 3): uiWindow.FK_L_Leg3_Ctrl, 
                    (u'RS_Left', u'RT_LegFK', 2): uiWindow.FK_L_Leg2_Ctrl, 
                    (u'RS_Right', u'RT_LegFK', 3): uiWindow.FK_R_Leg3_Ctrl,
                    (u'RS_Right', u'RT_LegFK', 2): uiWindow.FK_R_Leg2_Ctrl,
                    (u'RS_Right', u'RT_LegFK', 1): uiWindow.FK_R_Leg1_Ctrl,
                    (u'RS_Right', u'RT_LegFK', 0): uiWindow.FK_R_Leg0_Ctrl,
                    (u'RS_Right', u'RT_ShoulderFK', 0): uiWindow.FK_R_Arm0_Ctrl, 
                    (u'RS_Center', u'RT_SpineUpperBody', 0): uiWindow.C_SpineUpperBody_Ctrl,
                    (u'RS_Center', u'RT_HeadFK', 0): uiWindow.FK_C_Head_Ctrl, 
                    (u'RS_Center', u'RT_NeckFK', 1): uiWindow.FK_C_Neck_1_Ctrl, 
                    (u'RS_Left', u'RT_ElbowFK', 0): uiWindow.FK_L_Arm1_Ctrl,
                    (u'RS_Left', u'RT_Clavicle', 0): uiWindow.L_Arm_Clav_Rotation_Ctrl,
                    (u'RS_Left', u'RT_WristFK', 0): uiWindow.FK_L_Arm2_Ctrl,
                    (u'RS_Right', u'RT_ElbowFK', 0): uiWindow.FK_R_Arm1_Ctrl,                    
                    (u'RS_Left', u'RT_MiddleFK', 2): uiWindow.FK_L_Middle_02_Ctrl,
                    (u'RS_Right', u'RT_PinkyFK', 2): uiWindow.FK_R_Pinky_02_Ctrl, 
                    (u'RS_Right', u'RT_ThumbFK', 2): uiWindow.FK_R_Thumb_02_Ctrl,
                    (u'RS_Left', u'RT_PinkyFK', 2): uiWindow.FK_L_Pinky_02_Ctrl,                   
                    (u'RS_Left', u'RT_MiddleFK', 1): uiWindow.FK_L_Middle_01_Ctrl, 
                    (u'RS_Right', u'RT_PinkyFK', 3): uiWindow.FK_R_Pinky_03_Ctrl,
                    (u'RS_Left', u'RT_PinkyFK', 3): uiWindow.FK_L_Pinky_03_Ctrl, 
                    (u'RS_Left', u'RT_MiddleFK', 0): uiWindow.FK_L_Middle_00_Ctrl,                    
                    (u'RS_Left', u'RT_ThumbFK', 2): uiWindow.FK_L_Thumb_02_Ctrl,                    
                    (u'RS_Left', u'RT_PinkyFK', 1): uiWindow.FK_L_Pinky_01_Ctrl,
                    (u'RS_Right', u'RT_PinkyFK', 1): uiWindow.FK_R_Pinky_01_Ctrl,                                        
                    (u'RS_Left', u'RT_ThumbFK', 1): uiWindow.FK_L_Thumb_01_Ctrl,                     
                    (u'RS_Left', u'RT_IndexFK', 3): uiWindow.FK_L_Index_03_Ctrl,                                                            
                    (u'RS_Left', u'RT_ThumbFK', 0): uiWindow.FK_L_Thumb_00_Ctrl,
                    (u'RS_Left', u'RT_RingFK', 0): uiWindow.FK_L_Ring_00_Ctrl, 
                    (u'RS_Left', u'RT_IndexFK', 2): uiWindow.FK_L_Index_02_Ctrl,                    
                    (u'RS_Right', u'RT_MiddleFK', 0): uiWindow.FK_R_Middle_00_Ctrl,
                    (u'RS_Left', u'RT_RingFK', 1): uiWindow.FK_L_Ring_01_Ctrl,
                    (u'RS_Left', u'RT_IndexFK', 1): uiWindow.FK_L_Index_01_Ctrl,                     
                    (u'RS_Left', u'RT_RingFK', 3): uiWindow.FK_L_Ring_03_Ctrl,
                    (u'RS_Right', u'RT_MiddleFK', 3): uiWindow.FK_R_Middle_03_Ctrl, 
                    (u'RS_Left', u'RT_IndexFK', 0): uiWindow.FK_L_Index_00_Ctrl,                    
                    (u'RS_Right', u'RT_MiddleFK', 2): uiWindow.FK_R_Middle_02_Ctrl,                                       
                    (u'RS_Right', u'RT_ThumbFK', 0): uiWindow.FK_R_Thumb_00_Ctrl,                                          
                    (u'RS_Left', u'RT_PinkyFK', 0): uiWindow.FK_L_Pinky_00_Ctrl,                                       
                    (u'RS_Right', u'RT_IndexFK', 3): uiWindow.FK_R_Index_03_Ctrl,                                       
                    (u'RS_Left', u'RT_RingFK', 2): uiWindow.FK_L_Ring_02_Ctrl,                      
                    (u'RS_Right', u'RT_ThumbFK', 1): uiWindow.FK_R_Thumb_01_Ctrl,                    
                    (u'RS_Right', u'RT_MiddleFK', 1): uiWindow.FK_R_Middle_01_Ctrl, 
                    (u'RS_Right', u'RT_PinkyFK', 0): uiWindow.FK_R_Pinky_00_Ctrl,
                    (u'RS_Right', u'RT_RingFK', 0): uiWindow.FK_R_Ring_00_Ctrl,                                           
                    (u'RS_Right', u'RT_RingFK', 2): uiWindow.FK_R_Ring_02_Ctrl,
                    (u'RS_Right', u'RT_RingFK', 1): uiWindow.FK_R_Ring_01_Ctrl,                                                          
                    (u'RS_Right', u'RT_IndexFK', 2): uiWindow.FK_R_Index_02_Ctrl,                                          
                    (u'RS_Right', u'RT_RingFK', 3): uiWindow.FK_R_Ring_03_Ctrl,                                       
                    (u'RS_Left', u'RT_MiddleFK', 3): uiWindow.FK_L_Middle_03_Ctrl,
                    (u'RS_Right', u'RT_IndexFK', 0): uiWindow.FK_R_Index_00_Ctrl, 
                    (u'RS_Right', u'RT_IndexFK', 1): uiWindow.FK_R_Index_01_Ctrl,
                    (u'RS_Right', u'RT_FootToeSwive', 0): u'R_Leg_ToeSwive_Ctrl', 
                    (u'RS_Center', u'RT_SpinePelvis', 0): u'C_SpinePelvis_Ctrl',
                    (u'RS_Right', u'RT_FootRotation', 0): u'R_Leg_Rotation_Ctrl',
                    (u'RS_Right', u'RT_FootBaseSwive', 0): u'R_Leg_FootBaseSwive_Ctrl',
                    (u'RS_Left', u'RT_FootBaseSwive', 0): u'L_Leg_FootBaseSwive_Ctrl', 
                    (u'RS_Right', u'RT_FootIKMain', 0): u'R_Leg_IK_Main_Ctrl',
                    (u'RS_Left', u'RT_LegPV', 0): u'L_Leg_PV_Ctrl',
                    (u'RS_Left', u'RT_FootRotation', 0): u'L_Leg_Rotation_Ctrl', 
                    (u'RS_Center', u'RT_SpineChest', 0): u'C_SpineChest_Ctrl',
                    (u'RS_Left', u'RT_ArmIKMain', 0): u'L_Arm_IK_Main_Ctrl',
                    (u'RS_Left', u'RT_FootToeSwive', 0): u'L_Leg_ToeSwive_Ctrl',
                    (u'RS_Right', u'RT_LegPV', 0): u'R_Leg_PV_Ctrl',
                    (u'RS_Right', u'RT_ArmPV', 0): u'R_Arm_PV_Ctrl', 
                    (u'RS_Right', u'RT_AnkleIKRotation', 0): u'R_Leg_IK_Rotation_Ctrl',
                    (u'RS_Left', u'RT_AnkleIKRotation', 0): u'L_Leg_IK_Rotation_Ctrl',
                    (u'RS_Right', u'RT_ArmIKMain', 0): u'R_Arm_IK_Main_Ctrl',
                    (u'RS_Left', u'RT_ArmPV', 0): u'L_Arm_PV_Ctrl',
                    (u'RS_Left', u'RT_FootIKMain', 0): u'L_Leg_IK_Main_Ctrl',
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
        uiWindow.FK_L_Thumb_00_Ctrl:(u'RS_Left', u'RT_ThumbFK', 0),
        uiWindow.FK_L_Thumb_01_Ctrl:(u'RS_Left', u'RT_ThumbFK', 1),
        uiWindow.FK_L_Thumb_02_Ctrl:(u'RS_Left', u'RT_ThumbFK', 2),
        uiWindow.FK_L_Index_03_Ctrl:(u'RS_Left', u'RT_IndexFK', 3),
        uiWindow.FK_L_Index_02_Ctrl:(u'RS_Left', u'RT_IndexFK', 2),
        uiWindow.FK_L_Index_01_Ctrl:(u'RS_Left', u'RT_IndexFK', 1),                     
        uiWindow.FK_L_Index_00_Ctrl:(u'RS_Left', u'RT_IndexFK', 0),
        uiWindow.FK_L_Middle_02_Ctrl:(u'RS_Left', u'RT_MiddleFK', 2),
        uiWindow.FK_L_Middle_01_Ctrl:(u'RS_Left', u'RT_MiddleFK', 1), 
        uiWindow.FK_L_Middle_00_Ctrl:(u'RS_Left', u'RT_MiddleFK', 0),                    
        uiWindow.FK_L_Middle_03_Ctrl:(u'RS_Left', u'RT_MiddleFK', 3),
        uiWindow.FK_L_Ring_00_Ctrl:(u'RS_Left', u'RT_RingFK', 0), 
        uiWindow.FK_L_Ring_01_Ctrl:(u'RS_Left', u'RT_RingFK', 1),
        uiWindow.FK_L_Ring_03_Ctrl:(u'RS_Left', u'RT_RingFK', 3),
        uiWindow.FK_L_Ring_02_Ctrl:(u'RS_Left', u'RT_RingFK', 2), 
        uiWindow.FK_R_Thumb_02_Ctrl:(u'RS_Right', u'RT_ThumbFK', 2),
        uiWindow.FK_R_Thumb_00_Ctrl:(u'RS_Right', u'RT_ThumbFK', 0), 
        uiWindow.FK_R_Thumb_01_Ctrl:(u'RS_Right', u'RT_ThumbFK', 1),
        uiWindow.FK_R_Index_03_Ctrl:(u'RS_Right', u'RT_IndexFK', 3),
        uiWindow.FK_R_Index_02_Ctrl:(u'RS_Right', u'RT_IndexFK', 2), 
        uiWindow.FK_R_Index_00_Ctrl:(u'RS_Right', u'RT_IndexFK', 0), 
        uiWindow.FK_R_Index_01_Ctrl:(u'RS_Right', u'RT_IndexFK', 1),
        uiWindow.FK_R_Middle_00_Ctrl:(u'RS_Right', u'RT_MiddleFK', 0),
        uiWindow.FK_R_Middle_03_Ctrl:(u'RS_Right', u'RT_MiddleFK', 3), 
        uiWindow.FK_R_Middle_02_Ctrl:(u'RS_Right', u'RT_MiddleFK', 2), 
        uiWindow.FK_R_Middle_01_Ctrl:(u'RS_Right', u'RT_MiddleFK', 1),
        uiWindow.FK_R_Ring_00_Ctrl:(u'RS_Right', u'RT_RingFK', 0),                      
        uiWindow.FK_R_Ring_02_Ctrl:(u'RS_Right', u'RT_RingFK', 2),
        uiWindow.FK_R_Ring_01_Ctrl:(u'RS_Right', u'RT_RingFK', 1),                     
        uiWindow.FK_R_Ring_03_Ctrl:(u'RS_Right', u'RT_RingFK', 3),                    
        uiWindow.FK_R_Pinky_02_Ctrl:(u'RS_Right', u'RT_PinkyFK', 2), 
        uiWindow.FK_R_Pinky_03_Ctrl:(u'RS_Right', u'RT_PinkyFK', 3),
        uiWindow.FK_R_Pinky_01_Ctrl:(u'RS_Right', u'RT_PinkyFK', 1),                    
        uiWindow.FK_R_Pinky_00_Ctrl:(u'RS_Right', u'RT_PinkyFK', 0),
        uiWindow.FK_L_Pinky_02_Ctrl:(u'RS_Left', u'RT_PinkyFK', 2),
        uiWindow.FK_L_Pinky_03_Ctrl:(u'RS_Left', u'RT_PinkyFK', 3), 
        uiWindow.FK_L_Pinky_01_Ctrl:(u'RS_Left', u'RT_PinkyFK', 1),
        uiWindow.FK_L_Pinky_00_Ctrl:(u'RS_Left', u'RT_PinkyFK', 0),                            
    }
    global MultiVerticalButtonToControl
    MultiVerticalButtonToControl = {
    uiWindow.FK_L_Pinky_Ctrl:[(u'RS_Left', u'RT_PinkyFK', 0),(u'RS_Left', u'RT_PinkyFK', 1),(u'RS_Left', u'RT_PinkyFK', 2),(u'RS_Left', u'RT_PinkyFK', 3)],
    uiWindow.FK_R_Pinky_Ctrl:[(u'RS_Right', u'RT_PinkyFK', 0),(u'RS_Right', u'RT_PinkyFK', 1),(u'RS_Right', u'RT_PinkyFK', 2),(u'RS_Right', u'RT_PinkyFK', 3)],
    uiWindow.FK_R_Ring_Ctrl:[(u'RS_Right', u'RT_RingFK', 0),(u'RS_Right', u'RT_RingFK', 1),(u'RS_Right', u'RT_RingFK', 2),(u'RS_Right', u'RT_RingFK', 3)],
    uiWindow.FK_L_Ring_Ctrl:[(u'RS_Left', u'RT_RingFK', 0),(u'RS_Left', u'RT_RingFK', 1),(u'RS_Left', u'RT_RingFK', 2),(u'RS_Left', u'RT_RingFK', 3)],
    uiWindow.FK_R_Index_Ctrl:[(u'RS_Right', u'RT_IndexFK', 0),(u'RS_Right', u'RT_IndexFK', 1),(u'RS_Right', u'RT_IndexFK', 2),(u'RS_Right', u'RT_IndexFK', 3)],
    uiWindow.FK_L_Index_Ctrl:[(u'RS_Left', u'RT_IndexFK', 0),(u'RS_Left', u'RT_IndexFK', 1),(u'RS_Left', u'RT_IndexFK', 2),(u'RS_Left', u'RT_IndexFK', 3)],
    uiWindow.FK_R_Middle_Ctrl:[(u'RS_Right', u'RT_MiddleFK', 0),(u'RS_Right', u'RT_MiddleFK', 1),(u'RS_Right', u'RT_MiddleFK', 2),(u'RS_Right', u'RT_MiddleFK', 3)],
    uiWindow.FK_L_Middle_Ctrl:[(u'RS_Left', u'RT_MiddleFK', 0),(u'RS_Left', u'RT_MiddleFK', 1),(u'RS_Left', u'RT_MiddleFK', 2),(u'RS_Left', u'RT_MiddleFK', 3)],
    uiWindow.FK_L_Finger_00_Ctrl:[(u'RS_Left', u'RT_IndexFK', 0),(u'RS_Left', u'RT_MiddleFK', 0),(u'RS_Left', u'RT_RingFK', 0),(u'RS_Left', u'RT_PinkyFK', 0)],
    uiWindow.FK_L_Finger_01_Ctrl:[(u'RS_Left', u'RT_IndexFK', 1),(u'RS_Left', u'RT_MiddleFK', 1),(u'RS_Left', u'RT_RingFK', 1),(u'RS_Left', u'RT_PinkyFK', 1)],
    uiWindow.FK_L_Finger_02_Ctrl:[(u'RS_Left', u'RT_IndexFK', 2),(u'RS_Left', u'RT_MiddleFK', 2),(u'RS_Left', u'RT_RingFK', 2),(u'RS_Left', u'RT_PinkyFK', 2)],
    uiWindow.FK_L_Finger_03_Ctrl:[(u'RS_Left', u'RT_IndexFK', 3),(u'RS_Left', u'RT_MiddleFK', 3),(u'RS_Left', u'RT_RingFK', 3),(u'RS_Left', u'RT_PinkyFK', 3)],
    uiWindow.FK_R_Finger_00_Ctrl:[(u'RS_Right', u'RT_IndexFK', 0),(u'RS_Right', u'RT_MiddleFK', 0),(u'RS_Right', u'RT_RingFK', 0),(u'RS_Right', u'RT_PinkyFK', 0)],
    uiWindow.FK_R_Finger_01_Ctrl:[(u'RS_Right', u'RT_IndexFK', 1),(u'RS_Right', u'RT_MiddleFK', 1),(u'RS_Right', u'RT_RingFK', 1),(u'RS_Right', u'RT_PinkyFK', 1)],
    uiWindow.FK_R_Finger_02_Ctrl:[(u'RS_Right', u'RT_IndexFK', 2),(u'RS_Right', u'RT_MiddleFK', 2),(u'RS_Right', u'RT_RingFK', 2),(u'RS_Right', u'RT_PinkyFK', 2)],
    uiWindow.FK_R_Finger_03_Ctrl:[(u'RS_Right', u'RT_IndexFK', 3),(u'RS_Right', u'RT_MiddleFK', 3),(u'RS_Right', u'RT_RingFK', 3),(u'RS_Right', u'RT_PinkyFK', 3)],

    uiWindow.FK_R_FourFinger_Ctrl:[(u'RS_Right', u'RT_IndexFK', 0),(u'RS_Right', u'RT_MiddleFK', 0),(u'RS_Right', u'RT_RingFK', 0),(u'RS_Right', u'RT_PinkyFK', 0),
    (u'RS_Right', u'RT_IndexFK', 1),(u'RS_Right', u'RT_MiddleFK', 1),(u'RS_Right', u'RT_RingFK', 1),(u'RS_Right', u'RT_PinkyFK', 1),
    (u'RS_Right', u'RT_IndexFK', 2),(u'RS_Right', u'RT_MiddleFK', 2),(u'RS_Right', u'RT_RingFK', 2),(u'RS_Right', u'RT_PinkyFK', 2),
    (u'RS_Right', u'RT_IndexFK', 3),(u'RS_Right', u'RT_MiddleFK', 3),(u'RS_Right', u'RT_RingFK', 3),(u'RS_Right', u'RT_PinkyFK', 3)],

    uiWindow.FK_L_FourFinger_Ctrl:[(u'RS_Left', u'RT_IndexFK', 0),(u'RS_Left', u'RT_MiddleFK', 0),(u'RS_Left', u'RT_RingFK', 0),(u'RS_Left', u'RT_PinkyFK', 0),
    (u'RS_Left', u'RT_IndexFK', 1),(u'RS_Left', u'RT_MiddleFK', 1),(u'RS_Left', u'RT_RingFK', 1),(u'RS_Left', u'RT_PinkyFK', 1),
    (u'RS_Left', u'RT_IndexFK', 2),(u'RS_Left', u'RT_MiddleFK', 2),(u'RS_Left', u'RT_RingFK', 2),(u'RS_Left', u'RT_PinkyFK', 2),
    (u'RS_Left', u'RT_IndexFK', 3),(u'RS_Left', u'RT_MiddleFK', 3),(u'RS_Left', u'RT_RingFK', 3),(u'RS_Left', u'RT_PinkyFK', 3)],
    }

def getCurrentSelecterName(uiWindow):
    name = uiWindow.characterSelector.currentText()
    if name == "None":
        #cmds.confirmDialog(title = "Wrong Character", icon = "critical", message = "Please select a vaild Character name in comboBox" )
        return name
    return name




    # def selectControl(CurrWidget):
    #     data = ButtonToControl[CurrWidget]
    #     name = getCurrentSelecterName(uiWindow)
    #     currentRig = RigObjectHelper.getRigControlObject(name, data[0], data[1], data[2])
    #     cmds.select(currentRig)
        
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

def setMutiSelectedButtonCallback(uiWindow):
    for key in MultiVerticalButtonToControl:
        callback = multiCallbackobj(key , uiWindow)
        key.clicked.connect(functools.partial(callback.functor, callback))

def setButtonCallback(uiWindow):
    for key in ButtonToControl:
        callback = callbackobj(key , uiWindow)
        key.clicked.connect(functools.partial(callback.functor, callback))

def setResetToModelBasePose(uiWindow):
    print "setResetToModelBasePose"
    def resetToBasePoseCallback():
        print resetToBasePoseCallback
        name = uiWindow.characterSelector.currentText()
        controllrigs = getAllControllRigByName(name)
        for key , rig in controllrigs[0].items():
            RigObjectHelper.setOneRigRotAndTrans(rig ,0,0,0,0,0,0)
    uiWindow.ResetPoseButton.clicked.connect(resetToBasePoseCallback)

def setIKFKShow(uiWindow):
    def modifyValue(SliderValue):
        return SliderValue / 10.0
    def setLeftLegIKFK(SliderValue):
        RigObjectHelper.hideCharacterIKFKByName(uiWindow.characterSelector.currentText() , modifyValue(SliderValue) , 'leftLegIKFKSwitch')
    def setLeftArmIKFK(SliderValue):
        RigObjectHelper.hideCharacterIKFKByName(uiWindow.characterSelector.currentText() , modifyValue(SliderValue) , 'leftArmIKFKSwitch')
    def setRightLegIKFK(SliderValue):
        RigObjectHelper.hideCharacterIKFKByName(uiWindow.characterSelector.currentText() , modifyValue(SliderValue) , 'rightLegIKFKSwitch')
    def setRightArmIKFK(SliderValue):
        RigObjectHelper.hideCharacterIKFKByName(uiWindow.characterSelector.currentText() , modifyValue(SliderValue) , 'rightArmIKFKSwitch')
    uiWindow.IKFKLLeg.valueChanged.connect(setLeftLegIKFK)        
    uiWindow.IKFKLHand.valueChanged.connect(setLeftArmIKFK)
    uiWindow.IKFKRLeg.valueChanged.connect(setRightLegIKFK)
    uiWindow.IKFKRHand.valueChanged.connect(setRightArmIKFK)
    
    uiWindow.IKToFKRHandBtn.clicked.connect(lambda *arg:SERigBipedLimbComponent.RigHumanLimb.syncIKToFK('R_Arm_RigComponentsGrp'))
    uiWindow.FKToIKRHandBtn.clicked.connect(lambda *arg:SERigBipedLimbComponent.RigHumanLimb.syncFKToIK('R_Arm_RigComponentsGrp')) 

    uiWindow.IKToFKLHandBtn.clicked.connect(lambda *arg:SERigBipedLimbComponent.RigHumanLimb.syncIKToFK('L_Arm_RigComponentsGrp'))
    uiWindow.FKToIKLHandBtn.clicked.connect(lambda *arg:SERigBipedLimbComponent.RigHumanLimb.syncFKToIK('L_Arm_RigComponentsGrp'))

    uiWindow.IKToFKRLegBtn.clicked.connect(lambda *arg:SERigBipedLimbComponent.RigHumanLimb.syncIKToFK('R_Leg_RigComponentsGrp'))
    uiWindow.FKToIKRLegBtn.clicked.connect(lambda *arg:SERigBipedLimbComponent.RigHumanLimb.syncFKToIK('R_Leg_RigComponentsGrp')) 

    uiWindow.IKToFKLLegBtn.clicked.connect(lambda *arg:SERigBipedLimbComponent.RigHumanLimb.syncIKToFK('L_Leg_RigComponentsGrp'))
    uiWindow.FKToIKLLegBtn.clicked.connect(lambda *arg:SERigBipedLimbComponent.RigHumanLimb.syncFKToIK('L_Leg_RigComponentsGrp'))    

class callbackobj():
    def __init__(self, key ,uiWindow):
        self.key = key
        self.uiWindow = uiWindow

    def functor(self , *arg):
        print self.key
        self.selectControl()
    def selectControl(self):
        data = ButtonToControl[self.key]
        name = getCurrentSelecterName(self.uiWindow)
        currentRig = RigObjectHelper.getRigControlObject(name, data[0], data[1], data[2])
        print currentRig
        cmds.select(currentRig)

class multiCallbackobj():
    def __init__(self, key , uiWindow):
        self.key = key
        self.uiWindow = uiWindow

    def functor(self , *arg):
        # print self.key
        self.selectControl()
    def selectControl(self):
        dataArray = MultiVerticalButtonToControl[self.key]
        name = getCurrentSelecterName(self.uiWindow)
        cmds.select( clear=True )
        for data in dataArray:
            currentRig = RigObjectHelper.getRigControlObject(name, data[0], data[1], data[2])
            cmds.select(currentRig , add=True)
