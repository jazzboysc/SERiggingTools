import socket
import threading

import HIKHelper
import maya.cmds as cmds

class MayaMoboCommands():
    def __init__(self):    
        self.MoboEffectorList = [
            'HipsEffector',
            'ChestOriginEffector',
            'ChestEndEffector',
            'HeadEffector',
            'LeftShoulder',
            'RightShoulder',
            'LeftElbowEffector',
            'RightElbowEffector',
            'LeftWristEffector',
            'RightWristEffector',
            'LeftKneeEffector',
            'RightKneeEffector',
            'LeftAnkleEffector',
            'RightAnkleEffector',
        ]
        self.customRigMapTable = {}
        self.customRigMapTable['HipsEffector'] = 0
        self.customRigMapTable['LeftAnkleEffector'] = 0
        self.customRigMapTable['RightAnkleEffector'] = 0
        self.customRigMapTable['LeftWristEffector'] = 0
        self.customRigMapTable['RightWristEffector'] = 0
        self.customRigMapTable['LeftKneeEffector'] = 0
        self.customRigMapTable['RightKneeEffector'] = 0
        self.customRigMapTable['LeftElbowEffector'] = 0
        self.customRigMapTable['RightElbowEffector'] = 0
        self.customRigMapTable['LeftShoulder'] = 0
        self.customRigMapTable['RightShoulder'] = 0
        self.customRigMapTable['HeadEffector'] = 0
        self.customRigMapTable['ChestOriginEffector'] = 0
        self.customRigMapTable['ChestEndEffector'] = 0

        # Skeleton Definition Slot List and Map List
        self.skDefineSlotList = [
            'Hips',
            'LeftUpLeg',
            'LeftLeg',
            'LeftFoot',
            'RightUpLeg',
            'RightLeg',
            'RightFoot',
            'Spine',
            'LeftArm',
            'LeftForeArm',
            'LeftHand',
            'RightArm',
            'RightForeArm',
            'RightHand',
            'Head',
            'LeftShoulder',
            'RightShoulder',
            'LeftHandIndex1',
            'LeftHandIndex2',
            'LeftHandIndex3',
            'LeftHandIndex4',
            'LeftHandMiddle1',
            'LeftHandMiddle2',
            'LeftHandMiddle3',
            'LeftHandMiddle4',
            'LeftHandPinky1',
            'LeftHandPinky2',
            'LeftHandPinky3',
            'LeftHandPinky4',
            'LeftHandRing1',
            'LeftHandRing2',
            'LeftHandRing3',
            'LeftHandRing4',
            'LeftHandThumb1',
            'LeftHandThumb2',
            'LeftHandThumb3',
            'LeftHandThumb4',
            'LeftInHandIndex',
            'LeftInHandMiddle',
            'LeftInHandPinky',
            'LeftInHandRing',
            'RightHandIndex1',
            'RightHandIndex2',
            'RightHandIndex3',
            'RightHandIndex4',
            'RightHandMiddle1',
            'RightHandMiddle2',
            'RightHandMiddle3',
            'RightHandMiddle4',
            'RightHandPinky1',
            'RightHandPinky2',
            'RightHandPinky3',
            'RightHandPinky4',
            'RightHandRing1',
            'RightHandRing2',
            'RightHandRing3',
            'RightHandRing4',
            'RightHandThumb1',
            'RightHandThumb2',
            'RightHandThumb3',
            'RightHandThumb4',
            'RightInHandIndex',
            'RightInHandMiddle',
            'RightInHandPinky',
            'RightInHandRing',
        ]

        self.skDefineMapList = {}
        self.skDefineMapList['Hips'] = 0
        self.skDefineMapList['LeftUpLeg'] = 0
        self.skDefineMapList['LeftLeg'] = 0
        self.skDefineMapList['LeftFoot'] = 0
        self.skDefineMapList['RightUpLeg'] = 0
        self.skDefineMapList['RightLeg'] = 0
        self.skDefineMapList['RightFoot'] = 0
        self.skDefineMapList['Spine'] = 0
        self.skDefineMapList['LeftArm'] = 0
        self.skDefineMapList['LeftForeArm'] = 0
        self.skDefineMapList['LeftHand'] = 0
        self.skDefineMapList['RightArm'] = 0
        self.skDefineMapList['RightForeArm'] = 0
        self.skDefineMapList['RightHand'] = 0
        self.skDefineMapList['Head'] = 0
        self.skDefineMapList['LeftShoulder'] = 0
        self.skDefineMapList['RightShoulder'] = 0
        self.skDefineMapList['LeftHandIndex1'] = 0
        self.skDefineMapList['LeftHandIndex2'] = 0
        self.skDefineMapList['LeftHandIndex3'] = 0
        self.skDefineMapList['LeftHandIndex4'] = 0
        self.skDefineMapList['LeftHandMiddle1'] = 0
        self.skDefineMapList['LeftHandMiddle2'] = 0
        self.skDefineMapList['LeftHandMiddle3'] = 0
        self.skDefineMapList['LeftHandMiddle4'] = 0
        self.skDefineMapList['LeftHandPinky1'] = 0
        self.skDefineMapList['LeftHandPinky2'] = 0
        self.skDefineMapList['LeftHandPinky3'] = 0
        self.skDefineMapList['LeftHandPinky4'] = 0
        self.skDefineMapList['LeftHandRing1'] = 0
        self.skDefineMapList['LeftHandRing2'] = 0
        self.skDefineMapList['LeftHandRing3'] = 0
        self.skDefineMapList['LeftHandRing4'] = 0
        self.skDefineMapList['LeftHandThumb1'] = 0
        self.skDefineMapList['LeftHandThumb2'] = 0
        self.skDefineMapList['LeftHandThumb3'] = 0
        self.skDefineMapList['LeftHandThumb4'] = 0
        self.skDefineMapList['LeftInHandIndex'] = 0
        self.skDefineMapList['LeftInHandMiddle'] = 0
        self.skDefineMapList['LeftInHandPinky'] = 0
        self.skDefineMapList['LeftInHandRing'] = 0
        self.skDefineMapList['RightHandIndex1'] = 0
        self.skDefineMapList['RightHandIndex2'] = 0
        self.skDefineMapList['RightHandIndex3'] = 0
        self.skDefineMapList['RightHandIndex4'] = 0
        self.skDefineMapList['RightHandMiddle1'] = 0
        self.skDefineMapList['RightHandMiddle2'] = 0
        self.skDefineMapList['RightHandMiddle3'] = 0
        self.skDefineMapList['RightHandMiddle4'] = 0
        self.skDefineMapList['RightHandPinky1'] = 0
        self.skDefineMapList['RightHandPinky2'] = 0
        self.skDefineMapList['RightHandPinky3'] = 0
        self.skDefineMapList['RightHandPinky4'] = 0
        self.skDefineMapList['RightHandRing1'] = 0
        self.skDefineMapList['RightHandRing2'] = 0
        self.skDefineMapList['RightHandRing3'] = 0
        self.skDefineMapList['RightHandRing4'] = 0
        self.skDefineMapList['RightHandThumb1'] = 0
        self.skDefineMapList['RightHandThumb2'] = 0
        self.skDefineMapList['RightHandThumb3'] = 0
        self.skDefineMapList['RightHandThumb4'] = 0
        self.skDefineMapList['RightInHandIndex'] = 0
        self.skDefineMapList['RightInHandMiddle'] = 0
        self.skDefineMapList['RightInHandPinky'] = 0
        self.skDefineMapList['RightInHandRing'] = 0

        self.moboTransform = {}
        self.moboTransform['HipsEffector'] = []
        self.moboTransform['LeftAnkleEffector'] = []
        self.moboTransform['RightAnkleEffector'] = []
        self.moboTransform['LeftWristEffector'] = []
        self.moboTransform['RightWristEffector'] = []
        self.moboTransform['LeftKneeEffector'] = []
        self.moboTransform['RightKneeEffector'] = []
        self.moboTransform['LeftElbowEffector'] = []
        self.moboTransform['RightElbowEffector'] = []
        self.moboTransform['LeftShoulder'] = []
        self.moboTransform['RightShoulder'] = []
        self.moboTransform['HeadEffector'] = []
        self.moboTransform['ChestOriginEffector'] = []
        self.moboTransform['ChestEndEffector'] = []

        # parameters
        self.importFBXPath = ''
        self.importNamespace = ''
        self.importModeMerge = True
        self.skeletonDefinePath = ''
        self.commandType = 0  # 0 represents no command; 1 represents get Maya valid characters; 2 represents set keyframes to the custom rigs
        self.characterName = ''  
        self.targetCharacter = ''        
        
    def processCommand(self):
        if self.commandType == 1:
            print('Start Getting Valid Characters.')
            charRes = self.getValidCharacterListWithCustomRig()
            return charRes
        elif self.commandType == 2:
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
        char = self.targetCharacter
        if not HIKHelper.isCharacterDefinition(char):
            cmds.warning('%s is not a valid HIKCharacterNode!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'%char)
            return('Failed to retarget to Maya.')

        for effector in self.MoboEffectorList:
            if self.moboTransform[effector] == []:
                continue

            # set to 30 fps mode  \\ delete key frames between retarget frame zones.
            cmds.currentUnit(t = 'ntsc' )
            #cmds.playbackOptions(minTime = newMinTime)
            tarRig = HIKHelper.matchCustomRigWithEffector(char, effector)
            if tarRig == 0:
                return('Failed to retarget to Maya.2')

            parentDrivenNode = self.getDrivenParent(tarRig)
            if parentDrivenNode != None:
                print('This controller:%s might need to be set to world space.'%parentDrivenNode)
            
            # set key values
            self.setKeyOfEffector(effector, tarRig)


        return('Reraget to %s completed.' %char)

    def getDrivenParent(self, nodeName):
        attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz']
        parent = cmds.listRelatives(nodeName, ap = True)
        if len(parent) > 0:
            par = parent[0]
            for attr in attrList:
                res = cmds.connectionInfo('{}.{}'.format(par, attr), id=True)
                if res == True:
                    return par
        else:
            return None

    def setKeyOfEffectorlegacy(self, effector, tarRig):
        keyStartTime = self.moboTransform[effector][0]
        # set key values
        for i in range(1, len(self.moboTransform[effector])):
            kTime = keyStartTime + i - 1
            kValue = self.moboTransform[effector][i]
            kTrans = [kValue[0], kValue[1], kValue[2]]
            kRot = [kValue[3], kValue[4], kValue[5]]
            if len(kValue) == 6:
                cmds.setKeyframe(tarRig, at = 'tx', time = kTime, v = kValue[0])
                cmds.setKeyframe(tarRig, at = 'ty', time = kTime, v = kValue[1])
                cmds.setKeyframe(tarRig, at = 'tz', time = kTime, v = kValue[2])
                cmds.setKeyframe(tarRig, at = 'rx', time = kTime, v = kValue[3])
                cmds.setKeyframe(tarRig, at = 'ry', time = kTime, v = kValue[4])
                cmds.setKeyframe(tarRig, at = 'rz', time = kTime, v = kValue[5])

    def setKeyOfEffector(self, effector, tarRig):
        if len(self.moboTransform[effector]) != 6:
            return

        for i in range(len(self.moboTransform[effector])):
            keysGrp = self.moboTransform[effector][i]
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