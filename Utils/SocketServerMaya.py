import socket
import threading

import HIKHelper
import maya.cmds as cmds

class MayaMobuCommands():
    def __init__(self, data):      
        self.SocketData = data
        
    def processCommand(self):
        print self.SocketData.commandType

        if self.SocketData.commandType == 1:
            print('Start Getting Valid Characters.')
            charRes = self.getValidCharacterListWithCustomRig()
            return charRes

        elif self.SocketData.commandType == 2:
            print('Receving custom rig animation data.')
            tarRes = self.setKeyframesOfCustomRigs()
            return tarRes

        else:
            print('There is no valid command need to be implemented.')
            return 0

    def getValidCharacterListWithCustomRig(self):
        charList = HIKHelper.characterDefinitionList()
        nameList = []
        for char in charList:
            HIKState = HIKHelper.getCharacterHIKState(char)
            if HIKState == None:
                continue
            nameList.append(char)

        return nameList

    def setKeyframesOfCustomRigs(self):
        char = self.SocketData.targetCharacter
        if not HIKHelper.isCharacterDefinition(char):
            cmds.warning('%s is not a valid HIKCharacterNode!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'%char)
            return('Failed to retarget to Maya custom rig.')

        for effector in HIKHelper.MobuEffectorList:
            if self.SocketData.MobuTransform[effector] == []:
                continue

            # set to 30 fps mode  \\ delete key frames between retarget frame zones.
            cmds.currentUnit(t = 'ntsc' )
            #cmds.playbackOptions(minTime = newMinTime)
            tarRigControl = HIKHelper.matchCustomRigWithEffector(char, effector)
            if tarRigControl == 0:
                return('Failed to retarget to Maya.2')

            parentDrivenNode = self.getDrivenParent(tarRigControl)
            if parentDrivenNode != None:
                print('This controller:%s might need to be set to world space.'%parentDrivenNode)
            
            # set key values
            self.setKeyOfEffector(effector, tarRigControl)


        return('Reraget to %s completed.' %char)

    def getDrivenParent(self, nodeName):
        attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz']
        parent = cmds.listRelatives(nodeName, ap = True)
        if parent and len(parent) > 0:
            par = parent[0]
            for attr in attrList:
                res = cmds.connectionInfo('{}.{}'.format(par, attr), id=True)
                if res == True:
                    return par
        else:
            return None

    def setKeyOfEffectorlegacy(self, effector, tarRig):
        if not self.SocketData.MobuTransform[effector]:
            print('Effector is none:' + effector)
            return

        keyStartTime = self.SocketData.MobuTransform[effector][0]
        # set key values
        for i in range(1, len(self.SocketData.MobuTransform[effector])):
            kTime = keyStartTime + i - 1
            kValue = self.SocketData.MobuTransform[effector][i]
            kTrans = [kValue[0], kValue[1], kValue[2]]
            kRot = [kValue[3], kValue[4], kValue[5]]

            if not kValue:
                print('kValue is none:' + effector + str(i))
                continue

            if len(kValue) == 6:
                cmds.setKeyframe(tarRig, at = 'tx', time = kTime, v = kValue[0])
                cmds.setKeyframe(tarRig, at = 'ty', time = kTime, v = kValue[1])
                cmds.setKeyframe(tarRig, at = 'tz', time = kTime, v = kValue[2])
                cmds.setKeyframe(tarRig, at = 'rx', time = kTime, v = kValue[3])
                cmds.setKeyframe(tarRig, at = 'ry', time = kTime, v = kValue[4])
                cmds.setKeyframe(tarRig, at = 'rz', time = kTime, v = kValue[5])

    def setKeyOfEffector(self, effector, tarRig):
        if self.SocketData.MobuTransform[effector] and len(self.SocketData.MobuTransform[effector]) != 6:
            print('Animation channel number does not equal 6: ' + tarRig)
            return

        for i in range(len(self.SocketData.MobuTransform[effector])):
            keysGrp = self.SocketData.MobuTransform[effector][i]

            if not keysGrp:
                continue
            
            for j in range(len(keysGrp)):
                keyTime = keysGrp[j][0]
                keyValue = keysGrp[j][1]
                if i == 0:
                    cmds.setKeyframe(tarRig, at = 'tx', time = keyTime, v = keyValue)
                elif i == 1:
                    cmds.setKeyframe(tarRig, at = 'ty', time = keyTime, v = keyValue)
                elif i == 2:
                    cmds.setKeyframe(tarRig, at = 'tz', time = keyTime, v = keyValue)
                elif i == 3:
                    cmds.setKeyframe(tarRig, at = 'rx', time = keyTime, v = keyValue)
                elif i == 4:
                    cmds.setKeyframe(tarRig, at = 'ry', time = keyTime, v = keyValue)
                elif i == 5:
                    cmds.setKeyframe(tarRig, at = 'rz', time = keyTime, v = keyValue)
        
class SocketServerMaya():
    def __init__(self, host = '', port = 6000):
        self.HOST = host
        self.PORT = port
        self.SIZE = 2**20
        self.BACKLOG = 5
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)


    def get_socket(self):
        try:
            self.s.bind((self.HOST, self.PORT))
            self.s.listen(self.BACKLOG)
            print('Socket Bind successfully. %s' %self.PORT)
            return True
        except socket.error, msg:
            print("Tried to open port %s, but failed: It is probably already open. \n" %self.PORT)
            return False