import maya.cmds as cmds
import pymel.core as pm
from ..Base import SERigNaming

def createRigObjectTypeAttr(rigObjectTopGroup, rigObjectTypeNodeStr):
    rigObjectTypeNode = cmds.createNode(rigObjectTypeNodeStr)
    cmds.addAttr(rigObjectTopGroup, ln = 'RigObjectType', at = 'message')
    cmds.connectAttr(rigObjectTypeNode + '.message', rigObjectTopGroup + '.RigObjectType')

def linkRigObjects(ownerObject, linkedObject, linkAttrStr, linkedAttrStr = ''):
    if ownerObject and linkedObject and linkAttrStr != '':
        cmds.addAttr(ownerObject, ln = linkAttrStr, at = 'message')

        if linkedAttrStr == '':
            linkedAttrStr = linkAttrStr + 'Owner'
        cmds.addAttr(linkedObject, ln = linkedAttrStr, at = 'message')

        cmds.connectAttr(ownerObject + '.' + linkAttrStr, linkedObject + '.' + linkedAttrStr)
    else:
        cmds.error('Cannot create link attribute.') 


def getRigType(rigObject):
    if cmds.objExists(rigObject):
        rt = cmds.getAttr(rigObject + '.RigType')
        return rt
    else:
        return 'RT_Unknown'
        
def getRigSide(rigObject):
    if cmds.objExists(rigObject):
        rs = cmds.getAttr(rigObject + '.RigSide')
        return rs
    else:
        return 'RS_Unknown'
        
def getRigControlIndex(rigControl):
    if cmds.objExists(rigControl):
        index = cmds.getAttr(rigControl + '.RigControlIndex')
        return int(index)
    else:
        return -1
        
def getRigCharacterName(rigCharacter):
    if cmds.objExists(rigCharacter):
        name = cmds.getAttr(rigCharacter + '.characterName')
        return name
    else:
        return None            

# Return the actual rig control of current rig control group.
def getRigControlObjectFromGroup(rigControl):
    if cmds.objExists(rigControl):
        controlObjectLink = cmds.listConnections(rigControl + '.ControlObject')
        if controlObjectLink:
            return controlObjectLink[0]
        else:
            return None
    else:
        return None 

# Return the owner rig component group of current rig control group.
def getControlOwner(rigControl):
    if cmds.objExists(rigControl):
        ControlOwner = cmds.listConnections(rigControl + '.ControlOwner')
        if ControlOwner:
            return ControlOwner[0]
        else:
            return None

    else:
        return None

def getGlobalControlOwner(rigControl):
    if cmds.objExists(rigControl):
        ControlOwner = cmds.listConnections(rigControl + '.GlobalControlOwner')
        if ControlOwner:
            return ControlOwner[0]
        else:
            return None

    else:
        return None

def getComponentOwner(rigComponent):
    if cmds.objExists(rigComponent):
        ComponentOwner = cmds.listConnections(rigComponent + '.ComponentOwner')
        if ComponentOwner:
            return ComponentOwner[0]
        else:
            return None

    else:
        return None

def getRigControlObject(characterName, rigSideStr, rigTypeStr, rigControlIndex):
    links = cmds.ls(type = 'RigControlType')
    for link in links:
        control = cmds.listConnections(link + '.message')
        if control:

            rs = getRigSide(control[0])
            rt = getRigType(control[0])
            index = getRigControlIndex(control[0])

            if rs == rigSideStr and rt == rigTypeStr and index == rigControlIndex:
                controlObject = getRigControlObjectFromGroup(control[0])
                controlComponent = getControlOwner(control[0])
                
                controlCharacter = None
                if controlComponent:
                    controlCharacter = getComponentOwner(controlComponent)
                
                if controlObject and controlCharacter:
                    name = getRigCharacterName(controlCharacter)
                    
                    if name == characterName:
                        return controlObject
    
    return None

def getRigGlobalControlObject(characterName, rigSideStr, rigTypeStr, rigControlIndex):
    links = cmds.ls(type = 'RigControlType')
    for link in links:
        control = cmds.listConnections(link + '.message')
        if control:

            rs = getRigSide(control[0])
            rt = getRigType(control[0])
            index = getRigControlIndex(control[0])

            if rs == rigSideStr and rt == rigTypeStr and index == rigControlIndex:
                controlObject = getRigControlObjectFromGroup(control[0])                
                controlCharacter = getGlobalControlOwner(control[0])
                if controlObject and controlCharacter:
                    name = getRigCharacterName(controlCharacter)
                    if name == characterName:
                        return controlObject
    
    return None

def listRigCharacters(includeNamespace = False):
    characterNames = []
    links = cmds.ls(type = 'RigCharacterType')
    for link in links:
        character = cmds.listConnections(link + '.message')
        if character:
            characterName = cmds.getAttr(character[0] +'.characterName')
            characterNames.append(characterName)

    return characterNames

def listRigCharacterGroups():
    characterGroups = []
    links = cmds.ls(type = 'RigCharacterType')
    for link in links:
        character = cmds.listConnections(link + '.message')
        if character:
            characterGroups.append(character[0])

    return characterGroups

def listRigCharacterControls(characterName):
    characterControls = [{}, {}]
    links = cmds.ls(type = 'RigControlType')
    for link in links:
        controlGroup = cmds.listConnections(link + '.message')[0]

        try:
            # Local controls have component owner.
            componentsGroup = cmds.listConnections(controlGroup + '.ControlOwner')[0]
            rigGroup = cmds.listConnections(componentsGroup + '.ComponentOwner')[0]
            curCharacterName = cmds.getAttr(rigGroup + '.characterName')

            if characterName == curCharacterName:
                control = cmds.listConnections(controlGroup + '.ControlObject')[0]
                rigSide = getRigSide(controlGroup)
                rigType = getRigType(controlGroup)
                rigControlIndex = getRigControlIndex(controlGroup)

                curKey = (rigSide, rigType, rigControlIndex)
                characterControls[0][curKey] = control
        except:
            # Gloabl controls do not have component owner.
            rigGroup = cmds.listConnections(controlGroup + '.GlobalControlOwner')[0]
            curCharacterName = cmds.getAttr(rigGroup + '.characterName')
            
            if characterName == curCharacterName:
                control = cmds.listConnections(controlGroup + '.ControlObject')[0]
                rigSide = getRigSide(controlGroup)
                rigType = getRigType(controlGroup)
                rigControlIndex = getRigControlIndex(controlGroup)

                curKey = (rigSide, rigType, rigControlIndex)
                characterControls[1][curKey] = control

    return characterControls

def genRigCharacterData(characterName):
    characterControls = [{}, {}]
    links = cmds.ls(type = 'RigControlType')
    for link in links:
        controlGroup = cmds.listConnections(link + '.message')[0]

        try:
            # Local controls have component owner.
            componentsGroup = cmds.listConnections(controlGroup + '.ControlOwner')[0]
            rigGroup = cmds.listConnections(componentsGroup + '.ComponentOwner')[0]
            curCharacterName = cmds.getAttr(rigGroup + '.characterName')

            if characterName == curCharacterName:
                control = cmds.listConnections(controlGroup + '.ControlObject')[0]
                rigSide = getRigSide(controlGroup)
                rigType = getRigType(controlGroup)
                rigControlIndex = getRigControlIndex(controlGroup)

                curKey = (rigSide, rigType, rigControlIndex)
                characterControls[0][curKey] = getRigCtrlTransByCtrlName(control)
        except:
            # Gloabl controls do not have component owner.
            rigGroup = cmds.listConnections(controlGroup + '.GlobalControlOwner')[0]
            curCharacterName = cmds.getAttr(rigGroup + '.characterName')
            
            if characterName == curCharacterName:
                control = cmds.listConnections(controlGroup + '.ControlObject')[0]
                rigSide = getRigSide(controlGroup)
                rigType = getRigType(controlGroup)
                rigControlIndex = getRigControlIndex(controlGroup)

                curKey = (rigSide, rigType, rigControlIndex)
                characterControls[1][curKey] = getRigCtrlTransByCtrlName(control)

    return characterControls

def getRigCtrlTransByCtrlName(control):
    if cmds.objExists(control):
        translateX = cmds.getAttr(control +'.translateX')
        translateY = cmds.getAttr(control +'.translateY')
        translateZ = cmds.getAttr(control +'.translateZ')
        rotateX = cmds.getAttr(control + '.rotateX')
        rotateY = cmds.getAttr(control + '.rotateY')
        rotateZ = cmds.getAttr(control + '.rotateZ')

        return (translateX, translateY, translateZ, rotateX, rotateY, rotateZ)      
    else:
        return None

def getRigControlTransform(characterName, rigSideStr, rigTypeStr, rigControlIndex):
    '''
    @param characterName: str, input a character name
    @param rigSideStr: str, Proprietary attributes of the controller
    @param rigTypeStr: str, Proprietary attributes of the controller
    @param rigControlIndex: str, Proprietary attributes of the controller
    '''

    control = getRigControlObject(characterName, rigSideStr, rigTypeStr, rigControlIndex)
    if control == None: return None;
    return getRigCtrlTransByCtrlName(control)

def setRigControlTranslation(characterName, rigSideStr, rigTypeStr, rigControlIndex, 
                             translateX, translateY, translateZ):
    '''
    @param characterName: str, input a character name
    @param rigSideStr: str, Proprietary attributes of the controller
    @param rigTypeStr: str, Proprietary attributes of the controller
    @param rigControlIndex: str, Proprietary attributes of the controller
    @param translateX: str, reference object for control position
    @param translateY: str, reference object for control position
    @param translateZ: str, reference object for control position

    '''
    control = getRigControlObject(characterName, rigSideStr, rigTypeStr, rigControlIndex)
    if control == None: return;
    if cmds.objExists(control):
        setOneRigTrans(control, translateX, translateY, translateZ)
    else:
        pass

def setRigControlRotation(characterName, rigSideStr, rigTypeStr, rigControlIndex, 
                             rotateX, rotateY, rotateZ):
    '''
    @param characterName: str, input a character name
    @param rigSideStr: str, Proprietary attributes of the controller
    @param rigTypeStr: str, Proprietary attributes of the controller
    @param rigControlIndex: str, Proprietary attributes of the controller
    @param rotateX: str, reference object for control position
    @param rotateY: str, reference object for control position
    @param rotateZ: str, reference object for control position

    '''
    control = getRigControlObject(characterName, rigSideStr, rigTypeStr, rigControlIndex)   
    if control == None: return;
    if cmds.objExists(control):
        setOneRigRot(control, rotateX, rotateY, rotateZ)
    else:
        pass

def setRigControlTransform(characterName, rigSideStr, rigTypeStr, rigControlIndex, translateX, translateY, translateZ, rotateX, rotateY, rotateZ):
    '''
    @param characterName: str, input a character name
    @param rigSideStr: str, Proprietary attributes of the controller
    @param rigTypeStr: str, Proprietary attributes of the controller
    @param rigControlIndex: str, Proprietary attributes of the controller
    @param translateX: str, reference object for control position
    @param translateY: str, reference object for control position
    @param translateZ: str, reference object for control position
    @param rotateX: str, reference object for control position
    @param rotateY: str, reference object for control position
    @param rotateZ: str, reference object for control position
    '''
    control = getRigControlObject(characterName, rigSideStr, rigTypeStr, rigControlIndex) 
    setOneRigRotAndTrans(control,translateX, translateY, translateZ, rotateX, rotateY, rotateZ)  

def setOneRigRotAndTrans(control, translateX, translateY, translateZ, rotateX, rotateY, rotateZ):
    if control == None: return;
    if cmds.objExists(control):
        setOneRigRot(control, rotateX, rotateY, rotateZ)
        setOneRigTrans(control, translateX, translateY, translateZ)
    else:
        pass

def setOneRigRot(control, rotateX, rotateY, rotateZ):
    try:
        cmds.setAttr(control + '.rotateX', rotateX)
        cmds.setAttr(control + '.rotateY', rotateY)
        cmds.setAttr(control + '.rotateZ', rotateZ)
    except:
        if 0:
            cmds.warning('Rotation channel is locked on control: ' + control)

def setOneRigTrans(control, translateX, translateY, translateZ):
    try:
        cmds.setAttr(control + '.translateX', translateX)
        cmds.setAttr(control + '.translateY', translateY)
        cmds.setAttr(control + '.translateZ', translateZ)
    except:
        if 0:
            cmds.warning('Translation channel is locked on control: ' + control)

def hideCharacterIKFKByName(characterName , bIsHide , attrName):
    print characterName , bIsHide
    if characterName == None: return
    mainCtrl = getRigGlobalControlObject(characterName , u'RS_Center', u'RT_Global', 0)
    print mainCtrl  
    if mainCtrl:
        cmds.setAttr(mainCtrl + '.'+ attrName, bIsHide)

def getCharacterDeformationGroup(characterGroup):
    if cmds.objExists(characterGroup):
        try:
            res = cmds.listConnections(characterGroup + '.' + SERigNaming.sDeformationGroupAttr)[0]
            return res
        except:
            cmds.warning('Cannot find character group: ' + characterGroup + ' deformation group')
            return None
    else:
        cmds.warning('Cannot find character group: ' + characterGroup)
        return None
    
def isRigCharacterGroup(inputObject):
    if cmds.objExists(inputObject):
        try:
            rigObjectTypeNode = cmds.listConnections(inputObject + '.RigObjectType')[0]
            if cmds.nodeType(rigObjectTypeNode) == 'RigCharacterType':
                return True
            else:
                # This is not a rig character.
                return False
        except:
            # Attribute doesn't exist.
            return False
    else:
        # Object doesn't exist.
        return False

def getSpecificObjectsUnderNamespace(type = '', namespace = ''):
    res = []

    allObjects = cmds.ls(l = True)
    for obj in allObjects:
       if cmds.nodeType(obj) == type:
           cmds.select(obj)
           objNS = pm.selected()[0].namespace()

           if objNS == namespace:
               res.append(obj)

    cmds.select(cl = True)
    return res