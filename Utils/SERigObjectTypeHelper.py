import maya.cmds as cmds

def createRigObjectTypeAttr(rigObjectTopGroup, rigObjectTypeNodeStr):
    rigObjectTypeNode = cmds.createNode(rigObjectTypeNodeStr)
    cmds.addAttr(rigObjectTopGroup, ln = 'RigObjectType', at = 'message')
    cmds.connectAttr(rigObjectTypeNode + '.message', rigObjectTopGroup + '.RigObjectType')

def linkRigObjects(ownerObject, linkedObject, linkAttrStr):
    if ownerObject and linkedObject and linkAttrStr != '':
        cmds.addAttr(ownerObject, ln = linkAttrStr, at = 'message')
        linkedAttrStr = linkAttrStr + 'Owner'
        cmds.addAttr(linkedObject, ln = linkedAttrStr, at = 'message')
        cmds.connectAttr(ownerObject + '.' + linkAttrStr, linkedObject + '.' + linkedAttrStr)
    else:
        cmds.error('Cannot create link attribute.')