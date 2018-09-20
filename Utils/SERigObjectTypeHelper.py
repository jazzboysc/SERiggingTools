import maya.cmds as cmds

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
        
def getRigControlObjectFromGroup(rigControl):
    if cmds.objExists(rigControl):
        controlObjectLink = cmds.listConnections(rigControl + '.ControlObject')
        if controlObjectLink:
            return controlObjectLink[0]
        else:
            return None
    else:
        return None 
        
def getControlOwner(rigControl):
    if cmds.objExists(rigControl):
        ControlOwner = cmds.listConnections(rigControl + '.ControlOwner')
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