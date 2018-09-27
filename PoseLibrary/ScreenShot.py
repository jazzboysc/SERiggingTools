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

import PoseConfig
import SavePose

reload(SavePose)

PoseRootPath = os.path.dirname(PoseConfig.__file__)
PoseFilePath = PoseRootPath + "\\PoseFile\\"
#ScreenShotPoseIns = None

def createSnapShotWindow():
    SnapShotWindow()
    #cmds.showWindow( ScreenShotPoseWindow )

class SnapShotWindow():
    """docstring for SnapShotWindow"""
    def __init__(self):
        #self.arg = arg
        if cmds.window("ScreenShotPoseWindow", exists = True):
            cmds.deleteUI("ScreenShotPoseWindow")
        self.ScreenShotPoseWindow = cmds.window('ScreenShotPoseWindow' , cc = self.windowCloseCallBack )
        '''from minmum size'''
        mainLayout = cmds.rowColumnLayout( numberOfColumns = 1)
        cmds.separator( height=10, style='out' )
        cmds.text( label='  before you press save button , please make sure this window is selected!!!  ' , backgroundColor = [0.8 , 0.2 , 0.1] )
        cmds.separator( height=10, style='in' )
        cmds.setParent( mainLayout )
        # todo add a name inpput text widget
        self.CreateViewWindow()

        cmds.setParent( mainLayout ) 
        nameLayout = cmds.rowColumnLayout( numberOfColumns = 2 , w = 200)
        cmds.text( label=' pose name : ' )
        self.NameInput = cmds.textField(tx = "Input a vaild pose name!!!" , w = 150 )
        cmds.setParent( ".." )
        cmds.text( label='A vaild name has no space , same name will override the name already exit!!!' , backgroundColor = [0.8 , 0.2 , 0.1] )
        cmds.setParent( mainLayout )
        cmds.separator( height=10, style='in' )
        cmds.text( label=' save pose ' )
        cmds.separator( height=10, style='out' )
        cmds.button(label='Save' , command = functools.partial(self.savePoseButtonCallback, self))

        # todo a listview show all poses include the new one we just created by clicked the save button

        cmds.showWindow( self.ScreenShotPoseWindow )

    def CreateViewWindow(self):
        self.camera = None
        form = cmds.formLayout(w = 300, h = 300)
        self.editorShot = cmds.modelEditor()
        column = cmds.columnLayout('true' , bgc = [0,0,0])
        cmds.formLayout( form, edit=True, attachForm=[ (column, 'top', 10), (column, 'left', 10),
            (self.editorShot, 'top', 10), (self.editorShot, 'bottom', 10), (self.editorShot, 'right', 10),(self.editorShot, 'left', 10)] ,
            attachNone=[(column, 'bottom'), (column, 'right')], 
            attachControl=(self.editorShot, 'left', 0, column))
        self.camera = cmds.camera(centerOfInterest=2.450351,position = (1.535314, 1.135712, 1.535314),rotation = (0, 0, 0),worldUp = (0, 0, 1))
        cmds.setAttr(self.camera[1] + ".focalLength", 70)
        cmds.modelEditor( self.editorShot, edit=True, camera=self.camera[0] )
        cmds.viewFit(self.camera[0])
        cmds.modelEditor(self.editorShot, edit = True, nurbsCurves = False, displayAppearance = "smoothShaded", 
            displayTextures = True, headsUpDisplay = False, cameras = False, grid = False, joints = False, textures = True )

    def windowCloseCallBack(self):
        cmds.delete(self.camera[0])
        print "Snapshot window close"

    def savePoseButtonCallback(self , *args ):
        if self.canSavePose() == True:
            self.savePoseMain()
        print "save button is clicked"

    def canSavePose(self):
        name = cmds.textField(self.NameInput , q = True , tx = True)
        # todo check this name is valid
        return True

    def savePoseMain(self):
        # todo have a valid name 
        # 1. chose path
        # 2. create pose data
        # 3. snap shot pose
        self.snapShotFunc()
        # todo close this window???
        print "savePose function"

    def snapShotFunc(self):
        if cmds.playblast(activeEditor = True) != self.editorShot:
            cmds.modelEditor(self.editorShot, edit = True, activeView = True)
        
        try:
            name = cmds.textField(self.NameInput , q = True , tx = True)
            fullNamePath = PoseFilePath + name +  ".bmp"
            f = open(fullNamePath, 'w')
            f.close()               
            success = True
        except:
            cmds.confirmDialog(title = "Save Pose", icon = "critical", message = "Perforce operation unsucessful. Could not save file. Aborting operation.")
            return 
        currentTime = cmds.currentTime( query=True )
        cmds.playblast(frame = currentTime, format = "image", cf = fullNamePath , v = False, wh = [100, 100], p = 100 , compression ="bmp" )
        savePoseDataToFile(name , fullNamePath)
        # todo save this icon to a config file

    def savePoseDataToFile(name , fullNamePath ):
        poseData = dict(poseName = name , icon = fullNamePath , rigData = dict( root = [1,1,1] ) , characterName = "Elisa")
        SavePose.savePose(poseData)
        print "save pose from screen shot succeed"