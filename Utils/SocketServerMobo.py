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
    def __init__(self, data):    
        self.SocketData = data

    def processCommand(self):
        if self.SocketData.commandType == 1:
            print('Start Importing File.')
            impRes =self.importFbxFile(self.SocketData.importFBXPath, self.SocketData.importNamespace, self.SocketData.importModeMerge)
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
           print('Import file from %s successfully.' %self.SocketData.importFBXPath)
        else:
           print('Failed to import file from %s.' %self.SocketData.importFBXPath)

        return importRes

    def autoCharacterize(self):
        if self.SocketData.characterName == '':
            print('Character Name is None, which is invalid.')
            return False
        
        newCharName = self.SocketData.importNamespace.encode('ascii', 'ignore') + ":" + self.SocketData.characterName.encode('ascii', 'ignore')
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
            chracterName = self.SocketData.characterName.encode('ascii', 'ignore')
            myChar = FBCharacter(chracterName)
            #myChar.ProcessObjectNamespace(FBNamespaceAction.kFBRemoveAllNamespace, "")
            myChar.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.SocketData.importNamespace.encode('ascii', 'ignore'))
            for slotName in self.SocketData.skDefineSlotList:
                jtName = self.SocketData.skDefineMapList[slotName].encode('ascii', 'ignore')
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
                rig.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.SocketData.importNamespace.encode('ascii', 'ignore'))

            # Create Extension
            self.createCharacterExtension(myChar)

        return True


    def mapJointToCharacterDefinition(self, characterObject, slot, jointName):
        namespace = self.SocketData.importNamespace.encode('ascii', 'ignore') + ':'
        myJoint = FBFindModelByLabelName(namespace + jointName)
          
        property = characterObject.PropertyList.Find(slot + "Link")
        property.append(myJoint)

    def constrainCustomRigWithEffectors(self):
        for effectorName in self.SocketData.MoboEffectorList:
            mayaCtrlName = self.SocketData.importNamespace.encode() + ':' + self.SocketData.customRigMapTable[effectorName].encode()
            effectorName = self.SocketData.characterName.encode() + '_Ctrl:' + effectorName
            mayaCtrlModel = FBFindModelByLabelName(mayaCtrlName)
            effectorModel = FBFindModelByLabelName(effectorName)
            if mayaCtrlModel!= None and effectorModel != None:
                self.createParentChildConstrain(mayaCtrlModel, effectorModel)
    
    def createParentChildConstrain(self, child, parent):
        cons = FBConstraintManager().TypeCreateConstraint('Parent/Child')
        if self.SocketData.importNamespace.encode() != '':
            cons.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.SocketData.importNamespace.encode())
        else:
            cons.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.SocketData.importNamespace.encode())
            #cons.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.characterName.encode())
        cons.Name = 'P/C_' + child.Name
        cons.ReferenceAdd(0, child)
        cons.ReferenceAdd(1, parent)
        cons.Snap()

    def createCharacterExtension(self, character):
        customRigExt = FBCharacterExtension("CustomRig Extension")
        customRigExt.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, self.SocketData.importNamespace.encode())
        character.AddCharacterExtension(customRigExt)

        for effectorName in self.SocketData.MoboEffectorList:
            mayaCtrlName = self.SocketData.importNamespace.encode() + ':' + self.SocketData.customRigMapTable[effectorName].encode()
            mayaCtrlModel = FBFindModelByLabelName(mayaCtrlName)
            if mayaCtrlModel != None:
                FBConnect(mayaCtrlModel, customRigExt)
                customRigExt.AddObjectProperties(mayaCtrlModel)
                customRigExt.UpdateStancePose()