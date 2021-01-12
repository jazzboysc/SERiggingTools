import sys
import socket
import threading
import tempfile

from pyfbsdk import *
from pyfbsdk_additions import *

class SocketServer():
    def __init__(self, host = '', port = 6000):
        self.HOST = host
        self.PORT = port
        self.SIZE = 2**20
        self.BACKLOG = 5
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

    def get_socket(self):
        try:
            self.s.bind((self.HOST, self.PORT))
            self.s.listen(self.BACKLOG)
            print('Socket Bind successfully. %s' %self.PORT)
            return True
        except socket.error, msg:
            print("Tried to open port %s, but failed: It is probably already open. \n" %self.PORT)
            return False

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
        self.commandType = 0  # 0 represents no command; 1 represents import; 
        self.characterName = '' 
        self.targetCharacter = ''

    def processCommand(self):
        if self.commandType == 1:
            print('Start Importing File.')
            impRes =self.importFbxFile(self.importFBXPath, self.importNamespace, self.importModeMerge)
            if not impRes:
                return
            print('Continue To Characterize.')
            chaRes = self.autoCharacterize()
            if not chaRes:
                return
            print('Continue To Constrain Custom Rigs.')
            self.constrainCustomRigWithEffectors()
            print("Finished Constraining Custom Rigs.")
        else:
            print('There is no valid command need to be implemented.')

    def importFbxFile(self, filePath, namespace = '', mergeOrAppend = True):    
        app = FBApplication()
        lFilePath = filePath
        lOptions = FBFbxOptions(True, lFilePath)
        
        ## Enable merging of only the first import file take
        #for lTakeIndex in range( 0, lOptions.GetTakeCount() ):
        #    lOptions.SetTakeSelect( lTakeIndex, False )
        #lOptions.SetTakeSelect( 0, True )
        
        lOptions.BaseCameras = False
        lOptions.CameraSwitcherSettings = False
        lOptions.GlobalLightingSettings = False
        lOptions.CurrentCameraSettings = False
        
        lOptions.TransportSetting = False
        lOptions.ShowOptionsDialog = False
        #lOptions.ShowFileDialog = False
        
        # Enable Namespace
        lOptions.NamespaceList = namespace.encode('ascii', 'ignore')
        print("Namespace is: %s" %lOptions.NamespaceList)
        
        # Merge Option
        if mergeOrAppend:
            lOptions.SetAll(FBElementAction.kFBElementActionMerge, False)
        else:
            lOptions.SetAll(FBElementAction.kFBElementActionAppend, False)
        
        ## Finish import
        importRes = app.FileMerge( lFilePath , False, lOptions )
        if importRes:
           print('Import file from %s successfully.' %self.importFBXPath)
        else:
           print('Failed to import file from %s.' %self.importFBXPath)

        return importRes

    def autoCharacterize(self):
        if self.characterName == '':
            print('Character Name is None, which is invalid.')
            return False
        
        newCharName = self.importNamespace.encode('ascii', 'ignore') + ":" + self.characterName.encode('ascii', 'ignore')
        characterList = FBSystem().Scene.Characters
        NotCharYet = True
        for char in characterList:
            charName = char.LongName
            # Check the character exists or not in the scene
            if charName == newCharName:
                # Check characterized?
                if char.GetCharacterize():
                    NotCharYet = False
                    if not char.GetCurrentControlSet():
                        char.CreateControlRig(True)
                    char.ActiveInput = True
                    break
                else:
                    # Try to characterize it
                    if char.SetCharacterizeOn(True):
                        NotCharYet = False
                        char.CreateControlRig(True)
                        char.ActiveInput = True
                        break
                    else:
                        print('Current Skeleton Definition is not completed or invalid, need to be redefined.')
                        print(char.GetCharacterizeError())
                        # Delete it
                        char.FBDelete()
                        break

        if NotCharYet:
            # Define Skeleton
            chracterName = self.characterName.encode('ascii', 'ignore')
            myChar = FBCharacter(chracterName)
            #myChar.ProcessObjectNamespace(FBNamespaceAction.kFBRemoveAllNamespace, "")
            myChar.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.importNamespace.encode('ascii', 'ignore'))
            for slotName in self.skDefineSlotList:
                jtName = self.skDefineMapList[slotName].encode('ascii', 'ignore')
                if jtName != 0:
                    self.mapJointToCharacterDefinition(myChar, slotName, jtName)

            # Characterize
            chaRes = myChar.SetCharacterizeOn(True)
            if not chaRes:
                print('Error: Characterize failed.')
                print(myChar.GetCharacterizeError())
                return False

            # CreateRig
            myChar.CreateControlRig(True)
            myChar.ActiveInput = True
            rig = myChar.GetCurrentControlSet()
            if rig:
                rig.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.importNamespace.encode('ascii', 'ignore'))

            # Create Extension
            self.createCharacterExtension(myChar)

        return True


    def mapJointToCharacterDefinition(self, characterObject, slot, jointName):
        namespace = self.importNamespace.encode('ascii', 'ignore') + ':'
        myJoint = FBFindModelByLabelName(namespace + jointName)
          
        property = characterObject.PropertyList.Find(slot + "Link")
        property.append(myJoint)

    def constrainCustomRigWithEffectors(self):
        for effectorName in self.MoboEffectorList:
            mayaCtrlName = self.importNamespace.encode() + ':' + self.customRigMapTable[effectorName].encode()
            effectorName = self.characterName.encode() + '_Ctrl:' + effectorName
            mayaCtrlModel = FBFindModelByLabelName(mayaCtrlName)
            effectorModel = FBFindModelByLabelName(effectorName)
            if mayaCtrlModel!= None and effectorModel != None:
                self.createParentChildConstrain(mayaCtrlModel, effectorModel)
    
    def createParentChildConstrain(self, child, parent):
        cons = FBConstraintManager().TypeCreateConstraint('Parent/Child')
        if self.importNamespace.encode() != '':
            cons.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.importNamespace.encode())
        else:
            cons.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.importNamespace.encode())
            #cons.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.characterName.encode())
        cons.Name = 'P/C_' + child.Name
        cons.ReferenceAdd(0, child)
        cons.ReferenceAdd(1, parent)
        cons.Snap()

    def createCharacterExtension(self, character):
        customRigExt = FBCharacterExtension("CustomRig Extension")
        customRigExt.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.importNamespace.encode())
        character.AddCharacterExtension(customRigExt)

        for effectorName in self.MoboEffectorList:
            mayaCtrlName = self.importNamespace.encode() + ':' + self.customRigMapTable[effectorName].encode()
            mayaCtrlModel = FBFindModelByLabelName(mayaCtrlName)
            if mayaCtrlModel != None:
                FBConnect(mayaCtrlModel, customRigExt)
                customRigExt.AddObjectProperties(mayaCtrlModel)
                customRigExt.UpdateStancePose()