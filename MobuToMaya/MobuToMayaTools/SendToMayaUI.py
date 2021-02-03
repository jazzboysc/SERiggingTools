from PySide2 import QtCore, QtUiTools, QtWidgets
from pyfbsdk import *
from pyfbsdk_additions import *

import pythonidelib
import os
import socket
import cPickle
import time

#from ...Utils import  SocketServerMobu
from ...Utils.SocketDataHelper import MayaMobuSocketData

filePath = os.path.dirname(os.path.abspath(__file__))
uifile_path = os.path.join(filePath, "MotionbuilderToMaya.ui")
print("uifile_path is: %s" %uifile_path)
splitSymbol = '>>>'

def Mobu_print(string):
    print(string)
    pythonidelib.FlushOutput()

class MainUI(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent )
        self.init_ui()
        self.createLayout()
        self.createConnections()

    def init_ui(self):
        f = QtCore.QFile(uifile_path)
        f.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(f, parentWidget=self)
        f.close()

        self.refreshBtnCallback()

    def createLayout(self):
        self.ui.layout().setContentsMargins(10, 10, 10, 10)

    def createConnections(self):
        self.ui.refreshBtn.clicked.connect(self.refreshBtnCallback)
        self.ui.addBtn.clicked.connect(self.addToQueueBtnCallback)
        self.ui.sendBtn.clicked.connect(self.sendBtnCallback)

    def quitBtnCallback(self):
        Mobu_main_window = self.get_dialog_parent()
        CloseTool(Mobu_main_window)

    def refreshBtnCallback(self):
        self.refreshMotionbuilderCharacterList()
        self.refreshMayaCharacterList()
        self.ui.mapListWidget.clear()
        Mobu_print('refresh')

    def addToQueueBtnCallback(self):
        MobuChar = self.ui.MobuListWidget.selectedItems()
        mayaChar = self.ui.MayaListWidget.selectedItems()
        if len(MobuChar) == 0:
            Mobu_print('Motionbuilder Character has not been selected!!!')
            return
        if len(mayaChar) == 0:
            Mobu_print('Maya Character has not been selected!!!')
            return

        addedText = str(MobuChar[0].text()) + splitSymbol + str(mayaChar[0].text())
        if self.isMappingExistingInQueue(addedText):
            Mobu_print('The Mapping has already been added to the Queue.')
            return
        item = QtWidgets.QListWidgetItem(addedText)
        self.ui.mapListWidget.addItem(item)
        Mobu_print('addToQueue')
    
    # Send Mobu Animations to Maya
    def sendBtnCallback(self):
        # Get MappingList
        mappingList = []
        rowCount = self.ui.mapListWidget.count()
        for i in range(rowCount):
            item = self.ui.mapListWidget.item(i).text()
            sp = item.split(splitSymbol)
            if len(sp) > 0:
                MobuChar = sp[0]
                mayaChar = sp[1]
                mappingList.append([MobuChar, mayaChar])
        Mobu_print(mappingList)
        Mobu_print('sendToMaya Clicked.')

        # Send to Maya
        if len(mappingList) == 0:
            Mobu_print('No retarget mapping was added to queue.')
            return

        for mapItem in mappingList:
            # Get Mobu Effectors' data
            sendCommand = MayaMobuSocketData()
            sendCommand.commandType = 2
            MobuChar = mapItem[0].encode()
            mayaChar = mapItem[1].encode()
            sendCommand.targetCharacter = mayaChar
            setDataRes = self.setCharacterDataToCommand(MobuChar, sendCommand)
            if not setDataRes:
                Mobu_print('Cannot find constraints or controls.')
                return
            Mobu_print('Begin To Send')
            sendCommand = setDataRes
            
            # Socket
            commandPort = 6001
            mSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                mSocket.connect(('localhost', commandPort))
                serialized_obj = cPickle.dumps(sendCommand)
                Mobu_print('DataSize:' + str(len(serialized_obj)).encode())
                mSocket.sendall(serialized_obj)

                res = cPickle.loads(serialized_obj)
                #res.debugDumpData() # DEBUG DUMP TO MOBU CONSOLE, TIME CONSUMING!!!

                pythonidelib.FlushOutput()

                #data = mSocket.recv(1024)
                #recvData = cPickle.loads(data)
                #Mobu_print(recvData)
            except Exception as e:
                Mobu_print('Send to Maya Fail:')
                Mobu_print(e)
            
            mSocket.close()
            Mobu_print('Socket Connection closed.')

    def get_dialog_parent(self):
        if FBToolList.has_key("MobuToMaya Tool"):
            my_tool = FBToolList["MobuToMaya Tool"]
            return my_tool

    def refreshMotionbuilderCharacterList(self):
        characterList = FBSystem().Scene.Characters
        charNameList = []
        for char in characterList:
            if char.GetCurrentControlSet() != None:
                charNameList.append(char.LongName)

        self.ui.MobuListWidget.clear()
        for charName in charNameList:
            item = QtWidgets.QListWidgetItem(charName)
            self.ui.MobuListWidget.addItem(item)

    def refreshMayaCharacterList(self):
        self.ui.MayaListWidget.clear()
        
        sendCommand = MayaMobuSocketData()#SocketServerMobu.MayaMobuCommands()
        sendCommand.commandType = 1
        recvHIKList = []
        # Socket Setting
        commandPort = 6001
        mSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mSocket.connect(('localhost', commandPort))
            serialized_obj = cPickle.dumps(sendCommand)
            mSocket.sendall(serialized_obj)
            data = mSocket.recv(1024)
            recvHIKList = cPickle.loads(data)
            Mobu_print(recvHIKList)
        except Exception as e:
            Mobu_print('Connect to Maya failed.')
        
        mSocket.close()
        Mobu_print('Socket Connection closed.')

        if len(recvHIKList) > 0:
            for mayaChar in recvHIKList:
                item = QtWidgets.QListWidgetItem(mayaChar.encode())
                self.ui.MayaListWidget.addItem(item)

    # check if the added mapping already exists in the queque
    def isMappingExistingInQueue(self, itemText):
        out = self.ui.mapListWidget.findItems(itemText, QtCore.Qt.MatchExactly)
        res = len(out) > 0
        Mobu_print(res)
        return res

    def setCharacterDataToCommand(self, charName, command):
        thisCommand = command
        splitList = charName.split(":")[:-1]
        nameSpace = ''
        if len(splitList) > 1:
            nameSpace = reduce(lambda x,y: x + ':' + y, splitList)
        elif len(splitList) == 1:
            nameSpace = splitList[0]
        else:
            nameSpace = ''
        Mobu_print("Namespace of character is:%s" %nameSpace)
        findConstrainName = nameSpace + ':P/C_*'
        includeNamespace = True
        modelsOnly = False
        foundComponents = FBComponentList()
        parent = FBFindObjectsByName(findConstrainName, foundComponents, includeNamespace, modelsOnly) #C_SpinUpperBody_Ctrl
        if len(foundComponents) == 0:
            return False

        FBPlayerControl().SetTransportFps(FBTimeMode().kFBTimeMode30Frames)
        for comp in foundComponents:
            mayaCtrl = comp.ReferenceGet(0)
            MobuEffector = comp.ReferenceGet(1)
            if mayaCtrl != None and MobuEffector != None:
                mayaCtrlCVs = self.getObjTransformCurves(mayaCtrl)
                #minFrame, maxFrame = self.getCurvesMaxFrameRange(mayaCtrlCVs)
                effectorName = MobuEffector.Name
                #thisCommand.MobuTransform[effectorName].append(minFrame)
                
                if len(mayaCtrlCVs) != 6:
                    Mobu_print('Warning: The animation curve number may not be correct.')
                    return
                
                keysGroupList = [cv.Keys for cv in mayaCtrlCVs]
                for keys in keysGroupList: # 6 keysgroup: tx ty tz rx ry rz
                    keyValueList = [(k.Time.GetFrame(), k.Value) for k in keys]
                    thisCommand.MobuTransform[effectorName].append(keyValueList)
            else:
                return False
        return thisCommand

    def getObjTransformCurves(self, obj):
        transProp = obj.PropertyList.Find("Lcl Translation")
        rotProp = obj.PropertyList.Find("Lcl Rotation")
        if not transProp:
            transProp.SetAnimated(True)
            transProp = obj.PropertyList.Find("Lcl Translation")
        if not rotProp:
            rotProp.SetAnimated(True)
            rotProp = obj.PropertyList.Find("Lcl Rotation")
        transNodes = transProp.GetAnimationNode().Nodes
        rotNodes = rotProp.GetAnimationNode().Nodes
        nodesList = list(transNodes) + list(rotNodes)
        if len(nodesList) == 0:
            return [None]
        return [node.FCurve for node in nodesList]

    def getCurvesMaxFrameRange(self, CVList):
        keysList = [cv.Keys for cv in CVList if len(cv.Keys)>0]
        if len(keysList) == 0:
            return [0,1]
        
        firstFrameList = [keys[0].Time.GetFrame() for keys in keysList]
        finalFrameList = [keys[len(keys)-1].Time.GetFrame() for keys in keysList]
        # def getMin(a , b):
        #     if a < b:
        #         return a
        #     else:
        #         return b
        # def getMax(a , b):
        #     if a > b:
        #         return a
        #     else:
        #         return b
        #minFrame = reduce(getMin, fFrameList, 0)
        #maxFrame = reduce(getMax, fFrameList, 0)
        minFrame = min(firstFrameList)
        maxFrame = max(finalFrameList, minFrame + 1)
        return [minFrame, maxFrame]
