import socket
import os
import tempfile
import shutil
import threading
import cPickle
import time

from ..Utils import SocketServerMaya
from ..Utils import HIKHelper
import UIConfig

import maya.mel as mel
import maya.OpenMayaUI as mui
from maya import cmds

import shiboken2
from PySide2 import QtCore, QtGui, QtWidgets , QtUiTools
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

# Global-----------------
mayaHIKs = []
sendToMoboCommand = SocketServerMaya.MayaMoboCommands() 


# UI------------------------------------------------------------
uiRootFile = os.path.dirname(UIConfig.__file__)
uifile_path = uiRootFile + "/MayaToMobo.ui"

tempFBXPath = 'C:/Users/claysun/Desktop/myTest3.fbx'

def maya_main_window():
    """
    Return the Maya Main Window Widget as a Python object
    """
    main_window = mui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(main_window), QtWidgets.QWidget)

class MayaToMoboUI(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent = maya_main_window()):
        super(MayaToMoboUI, self).__init__(parent)
        self.setWindowTitle("Send Custom Rig To Mobo")
        
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        uifile = QtCore.QFile(uifile_path)
        uifile.open(QtCore.QFile.ReadOnly)
        self.uiWindow = QtUiTools.QUiLoader().load(uifile, parentWidget = self)
        uifile.close()
        
        self.uiWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.initializeUI()
        self.setButtonsCallBack()

        self.sendToMoboCommand = SocketServerMaya.MayaMoboCommands()

    def initializeUI(self):
        charList = HIKHelper.characterDefinitionList()
        if len(charList) > 0:
            for char in charList:
                self.uiWindow.characterComboBox.addItem(char)
            self.uiWindow.namespacelineEdit.setText(self.uiWindow.characterComboBox.itemText(self.uiWindow.characterComboBox.currentIndex()))
        else:
            self.uiWindow.characterComboBox.addItem('Please define a Character and create custom rig Mapping.')


    def setButtonsCallBack(self):
        self.uiWindow.autoSelectBtn.clicked.connect(self.autoSelectBtnCallback)
        self.uiWindow.sendMergeBtn.clicked.connect(self.sendMergeBtnCallback)
        self.uiWindow.sendAddBtn.clicked.connect(self.sendMergeBtnCallback)

        self.uiWindow.characterComboBox.currentTextChanged.connect(self.onCharacterChangeCallback)
    
    def autoSelectBtnCallback(self):
        char = self.uiWindow.characterComboBox.itemText(self.uiWindow.characterComboBox.currentIndex())
        HIKHelper.addSelectCustomRigs(char)

    def sendMergeBtnCallback(self):
        char = self.uiWindow.characterComboBox.itemText(self.uiWindow.characterComboBox.currentIndex())
        if not HIKHelper.isCharacterDefinition(char):
            cmds.warning('Selection is not a valid character definition.')
            return

        dirpath = tempfile.gettempdir()
        filepath = tempFBXPath
        mel.eval('FBXResetExport;')
        mel.eval('FBXExportBakeComplexAnimation -v false;') #mel.eval("FBXExportInputConnections -v false;")
        res = cmds.file(filepath, force = True, type = "FBX export", exportSelected = True)#cmds.file(filepath, force = True, options = "v = 0", type = "FBX export", exportSelected = True)#shutil.rmtree(dirpath)
        
        charNameWithoutNamespace = char
        if len(char.split(':')) > 1:
        	charNameWithoutNamespace = char.split(':')[1]
        # command content setting
        self.sendToMoboCommand.commandType = 1
        self.sendToMoboCommand.importFBXPath = filepath
        self.sendToMoboCommand.importNamespace = self.uiWindow.namespacelineEdit.text()
        self.sendToMoboCommand.importModeMerge = True
        self.sendToMoboCommand.characterName = charNameWithoutNamespace

        for effector in self.sendToMoboCommand.MoboEffectorList:
            self.sendToMoboCommand.customRigMapTable[effector] = HIKHelper.matchCustomRigWithEffector(char, effector)
        for slot in self.sendToMoboCommand.skDefineSlotList:
            self.sendToMoboCommand.skDefineMapList[slot] = HIKHelper.matchSkeletonDefineWithSlot(char, slot)

        # Socket Setting
        commandPort = 6000
        mSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            mSocket.connect(('localhost', commandPort))
            serialized_obj = cPickle.dumps(self.sendToMoboCommand)
            mSocket.send(serialized_obj)#mSocket.send('ddddddd')
            recvData = mSocket.recv(1024)
            print recvData
        except Exception as e:
            print('Send to Mobo Fail:', e)
        
        mSocket.close()
        print('Socket Connection closed.')

    def onCharacterChangeCallback(self):
        charName = self.uiWindow.characterComboBox.itemText(self.uiWindow.characterComboBox.currentIndex())
        textName = charName
        spl = charName.split(':')
        if len(spl) > 1:
            charName = spl[1]
        self.uiWindow.namespacelineEdit.setText(charName)

    def run(self):
        self.resize(300, 230)
        self.show()

def openSendToMoboWindow():
    maya2Mobo = MayaToMoboUI()
    maya2Mobo.setMinimumSize( 270, 230 )
    maya2Mobo.run()
#-------------------------------------------------------------

def exportSelectionByHand():
    dirpath = tempfile.gettempdir()#tempfile.mkdtemp()  #
    filepath = tempFBXPath #os.path.join(dirpath, 'maya2Mobo.fbx')# #dirpath + '\maya2Mobu.fbx'#
    mel.eval('FBXResetExport;')
    mel.eval('FBXExportBakeComplexAnimation -v false;')
    #mel.eval("FBXExportInputConnections -v false;")
    res = cmds.file(filepath, force = True, type = "FBX export", exportSelected = True)#cmds.file(filepath, force = True, options = "v = 0", type = "FBX export", exportSelected = True)
    #shutil.rmtree(dirpath)
    print res
    return filepath

# def send_to_maya():
#     commandPort = 6004
#     mSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     sendToMoboCommand.commandType = 0
#     if sendToMoboCommand.commandType == 1:
#         sendToMoboCommand.importFBXPath = exportSelectionByHand()
#         sendToMoboCommand.importNamespace = ''
#         sendToMoboCommand.importModeMerge = True;   

#     try:
#         mSocket.connect(('localhost', commandPort))
#         for ct in range(3):
#             serialized_obj = cPickle.dumps(sendToMoboCommand)
#             mSocket.send(serialized_obj)#mSocket.send('ddddddd')
#             recvHIK = mSocket.recv(1024)
#             print recvHIK
#             time.sleep(0.5)
#     except Exception as e:
#         print('Send to Mobo Fail:', e)
    
#     mSocket.close()
#     print('Socket Connection closed.')

#----------------------------------------------------------------

#send_to_maya()
#exportSelectionByHand()


