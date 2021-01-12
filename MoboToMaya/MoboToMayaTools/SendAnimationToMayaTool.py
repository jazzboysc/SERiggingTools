from PySide2 import QtWidgets
from pyfbsdk import *
from pyfbsdk_additions import *

import shiboken2
import MoboToMaya.MoboToMayaTools.SendToMayaUI as SendToMayaUI; reload(SendToMayaUI)

class nativeWidgetHolder(FBWidgetHolder):
    def WidgetCreate(self, pWidgetParent):
        self.moboMain = SendToMayaUI.MainUI(shiboken2.wrapInstance(pWidgetParent, QtWidgets.QWidget))
        return shiboken2.getCppPointer(self.moboMain)[0]


class FileReferenceTool(FBTool):
    def __init__(self, name):
        FBTool.__init__(self, name)
        self.mNativeWidgetHolder = nativeWidgetHolder();
        self.BuildLayout()
        self.StartSizeX = 900
        self.StartSizeY = 325
        self.MinSizeX = 900
        self.MinSizeY = 325

    def BuildLayout(self):
        x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"")
        self.AddRegion("main","main", x, y, w, h)
        self.SetControl("main", self.mNativeWidgetHolder)

def showSendToMayaUI():
    gToolName = "MoboToMaya Tool"
    #Development? - need to recreate each time!!
    gDEVELOPMENT = True

    if gDEVELOPMENT:
        FBDestroyToolByName(gToolName)

    if gToolName in FBToolList:
        tool = FBToolList[gToolName]
        ShowTool(tool)
    else:
        tool=FileReferenceTool(gToolName)
        FBAddTool(tool)
        if gDEVELOPMENT:
            ShowTool(tool)