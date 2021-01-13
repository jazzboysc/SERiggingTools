from PySide2 import QtCore, QtUiTools, QtWidgets
from pyfbsdk import *
from pyfbsdk_additions import *

import pythonidelib
import os
import socket
import cPickle
import time

#from ...Utils import  SocketServerMobo
from ...Utils.SocketDataHelper import MayaMoboSocketData

filePath = os.path.dirname(os.path.abspath(__file__))
uifile_path = os.path.join(filePath, "MotionbuilderToMaya.ui")
print("uifile_path is: %s" %uifile_path)
splitSymbol = '>>>'

def mobo_print(string):
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
        mobo_main_window = self.get_dialog_parent()
        CloseTool(mobo_main_window)

    def refreshBtnCallback(self):
        self.refreshMotionbuilderCharacterList()
        self.refreshMayaCharacterList()
        self.ui.mapListWidget.clear()
        mobo_print('refresh')

    def addToQueueBtnCallback(self):
        moboChar = self.ui.MoboListWidget.selectedItems()
        mayaChar = self.ui.MayaListWidget.selectedItems()
        if len(moboChar) == 0:
            mobo_print('Motionbuilder Character has not been selected!!!')
            return
        if len(mayaChar) == 0:
            mobo_print('Maya Character has not been selected!!!')
            return

        addedText = str(moboChar[0].text()) + splitSymbol + str(mayaChar[0].text())
        if self.isMappingExistingInQueue(addedText):
            mobo_print('The Mapping has already been added to the Queue.')
            return
        item = QtWidgets.QListWidgetItem(addedText)
        self.ui.mapListWidget.addItem(item)
        mobo_print('addToQueue')
    
    # Send Mobo Animations to Maya
    def sendBtnCallback(self):
        # Get MappingList
        mappingList = []
        rowCount = self.ui.mapListWidget.count()
        for i in range(rowCount):
            item = self.ui.mapListWidget.item(i).text()
            sp = item.split(splitSymbol)
            if len(sp) > 0:
                moboChar = sp[0]
                mayaChar = sp[1]
                mappingList.append([moboChar, mayaChar])
        mobo_print(mappingList)
        mobo_print('sendToMaya Clicked.')

        # Send to Maya
        if len(mappingList) == 0:
            mobo_print('No retarget mapping was added to queue.')
            return
        for mapItem in mappingList:
            # Get Mobo Effectors' data
            sendCommand = MayaMoboSocketData()#SocketServerMobo.MayaMoboCommands()
            sendCommand.commandType = 2
            moboChar = mapItem[0].encode()
            mayaChar = mapItem[1].encode()
            sendCommand.targetCharacter = mayaChar
            setDataRes = self.setCharacterDataToCommand(moboChar, sendCommand)
            if not setDataRes:
                mobo_print('Cannot find constraints or controls.')
                return
            mobo_print('Begin To Send')
            sendCommand = setDataRes
            #mobo_print(sendCommand.moboTransform['RightShoulder'][1]) #HeadEffector
            
            # Socket
            commandPort = 6001
            mSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                mSocket.connect(('localhost', commandPort))
                serialized_obj = cPickle.dumps(sendCommand)
                mobo_print('DataSize:' + str(len(serialized_obj)).encode())
                mSocket.send(serialized_obj)
                data = mSocket.recv(1024)
                recvData = cPickle.loads(data)
                mobo_print(recvData)
            except Exception as e:
                mobo_print('Send to Maya Fail:', e)
            
            mSocket.close()
            mobo_print('Socket Connection closed.')

    def get_dialog_parent(self):
        if FBToolList.has_key("MoboToMaya Tool"):
            my_tool = FBToolList["MoboToMaya Tool"]
            return my_tool

    def refreshMotionbuilderCharacterList(self):
        characterList = FBSystem().Scene.Characters
        charNameList = []
        for char in characterList:
            if char.GetCurrentControlSet() != None:
                charNameList.append(char.LongName)

        self.ui.MoboListWidget.clear()
        for charName in charNameList:
            item = QtWidgets.QListWidgetItem(charName)
            self.ui.MoboListWidget.addItem(item)

    def refreshMayaCharacterList(self):
        self.ui.MayaListWidget.clear()
        
        sendCommand = MayaMoboSocketData()#SocketServerMobo.MayaMoboCommands()
        sendCommand.commandType = 1
        recvHIKList = []
        # Socket Setting
        commandPort = 6001
        mSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mSocket.connect(('localhost', commandPort))
            serialized_obj = cPickle.dumps(sendCommand)
            mSocket.send(serialized_obj)
            data = mSocket.recv(1024)
            recvHIKList = cPickle.loads(data)
            mobo_print(recvHIKList)
        except Exception as e:
            mobo_print('Connect to Maya failed.')
        
        mSocket.close()
        mobo_print('Socket Connection closed.')

        if len(recvHIKList) > 0:
            for mayaChar in recvHIKList:
                item = QtWidgets.QListWidgetItem(mayaChar.encode())
                self.ui.MayaListWidget.addItem(item)

    # check if the added mapping already exists in the queque
    def isMappingExistingInQueue(self, itemText):
        out = self.ui.mapListWidget.findItems(itemText, QtCore.Qt.MatchExactly)
        res = len(out) > 0
        mobo_print(res)
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
        mobo_print("Namespace of character is:%s" %nameSpace)
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
            moboEffector = comp.ReferenceGet(1)
            if mayaCtrl != None and moboEffector != None:
                mayaCtrlCVs = self.getObjTransformCurves(mayaCtrl)
                #minFrame, maxFrame = self.getCurvesMaxFrameRange(mayaCtrlCVs)
                effectorName = moboEffector.Name
                #thisCommand.moboTransform[effectorName].append(minFrame)
                
                if len(mayaCtrlCVs) != 6:
                    mobo_print('Warning: The animation curve number may not be correct.')
                    return
                
                keysGroupList = [cv.Keys for cv in mayaCtrlCVs]
                for keys in keysGroupList: # 6 keysgroup: tx ty tz rx ry rz
                    valueList = [[k.Time.GetFrame(), k.Value] for k in keys]
                    thisCommand.moboTransform[effectorName].append(valueList)
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
