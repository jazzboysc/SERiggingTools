import maya.cmds as cmds
import pymel.core as pm
import math

from ..Base import SERigNaming

#-----------------------------------------------------------------------------
def loadPlugin(plugin):
    loaded = cmds.pluginInfo(plugin, q = True, loaded = True)
    if not loaded:
        cmds.loadPlugin(plugin)
#-----------------------------------------------------------------------------
def isPluginLoaded(plugin):
    loaded = cmds.pluginInfo(plugin, q = True, loaded = True)
    return loaded
#-----------------------------------------------------------------------------
def createRigObjectTypeAttr(rigObjectTopGroup, rigObjectTypeNodeStr):
    rigObjectTypeNode = cmds.createNode(rigObjectTypeNodeStr)
    cmds.addAttr(rigObjectTopGroup, ln = 'RigObjectType', at = 'message')
    cmds.connectAttr(rigObjectTypeNode + '.message', rigObjectTopGroup + '.RigObjectType')
#-----------------------------------------------------------------------------
def linkRigObjects(ownerObject, linkedObject, linkAttrStr, linkedAttrStr = ''):
    if ownerObject and linkedObject and linkAttrStr != '':
        if not cmds.objExists(ownerObject + '.' + linkAttrStr):
            cmds.addAttr(ownerObject, ln = linkAttrStr, at = 'message')

        if linkedAttrStr == '':
            linkedAttrStr = linkAttrStr + SERigNaming.sOwnerSuffix
        if not cmds.objExists(linkedObject + '.' + linkedAttrStr):
            cmds.addAttr(linkedObject, ln = linkedAttrStr, at = 'message')

        cmds.connectAttr(ownerObject + '.' + linkAttrStr, linkedObject + '.' + linkedAttrStr, f = True)
    else:
        cmds.error('Cannot create link attribute.') 
#-----------------------------------------------------------------------------
def getRigType(rigObject):
    if cmds.objExists(rigObject):
        rt = cmds.getAttr(rigObject + '.RigType')
        return rt
    else:
        return 'RT_Unknown'
#-----------------------------------------------------------------------------
def getRigSide(rigObject):
    if cmds.objExists(rigObject):
        rs = cmds.getAttr(rigObject + '.RigSide')
        return rs
    else:
        return 'RS_Unknown'
#-----------------------------------------------------------------------------
def getRigControlIndex(rigControl):
    if cmds.objExists(rigControl):
        index = cmds.getAttr(rigControl + '.RigControlIndex')
        return int(index)
    else:
        return -1
#-----------------------------------------------------------------------------
def getRigCharacterName(rigCharacter):
    if cmds.objExists(rigCharacter):
        name = cmds.getAttr(rigCharacter + '.characterName')
        return name
    else:
        return None            
#-----------------------------------------------------------------------------
def getControlObjectOwner(rigControlObject):
    if cmds.objExists(rigControlObject):
        controlObjectOwner = cmds.listConnections(rigControlObject + '.' + SERigNaming.sControlObject + SERigNaming.sOwnerSuffix)
        if controlObjectOwner:
            return controlObjectOwner[0]
        else:
            return None

    else:
        return None
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
def getGlobalControlOwner(rigControl):
    if cmds.objExists(rigControl):
        ControlOwner = cmds.listConnections(rigControl + '.GlobalControlOwner')
        if ControlOwner:
            return ControlOwner[0]
        else:
            return None

    else:
        return None
#-----------------------------------------------------------------------------
def getComponentOwner(rigComponent):
    if cmds.objExists(rigComponent):
        ComponentOwner = cmds.listConnections(rigComponent + '.ComponentOwner')
        if ComponentOwner:
            return ComponentOwner[0]
        else:
            return None

    else:
        return None
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
def listRigCharacters(includeNamespace = False):
    characterNames = []
    links = cmds.ls(type = 'RigCharacterType')
    for link in links:
        character = cmds.listConnections(link + '.message')
        if character:
            characterName = cmds.getAttr(character[0] +'.characterName')
            characterNames.append(characterName)

    return characterNames
#-----------------------------------------------------------------------------
def listRigCharacterGroups():
    characterGroups = []
    links = cmds.ls(type = 'RigCharacterType')
    for link in links:
        character = cmds.listConnections(link + '.message')
        if character:
            characterGroups.append(character[0])

    return characterGroups
#-----------------------------------------------------------------------------
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
            try:
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
            except:
                # TODO:
                # Face proxy controls.
                #print(controlGroup)
                pass

    return characterControls
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
def isRigControlTransModified(control):
    trans = getRigCtrlTransByCtrlName(control)

    if trans == None:
        return False

    for transChannel in trans:
        if math.fabs(transChannel) > 0.00001:
            return True

    return False
#-----------------------------------------------------------------------------
def getRigControlTransform(characterName, rigSideStr, rigTypeStr, rigControlIndex):
    '''
    @param characterName: str, input a character name
    @param rigSideStr: str, Proprietary attributes of the controller
    @param rigTypeStr: str, Proprietary attributes of the controller
    @param rigControlIndex: str, Proprietary attributes of the controller
    '''

    control = getRigControlObject(characterName, rigSideStr, rigTypeStr, rigControlIndex)
    if control == None: return None
    return getRigCtrlTransByCtrlName(control)
#-----------------------------------------------------------------------------
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
    if control == None: return
    if cmds.objExists(control):
        setOneRigTrans(control, translateX, translateY, translateZ)
    else:
        pass
#-----------------------------------------------------------------------------
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
    if control == None: return
    if cmds.objExists(control):
        setOneRigRot(control, rotateX, rotateY, rotateZ)
    else:
        pass
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
def setOneRigRotAndTrans(control, translateX, translateY, translateZ, rotateX, rotateY, rotateZ):
    if control == None: return
    if cmds.objExists(control):
        setOneRigRot(control, rotateX, rotateY, rotateZ)
        setOneRigTrans(control, translateX, translateY, translateZ)
    else:
        pass
#-----------------------------------------------------------------------------
def setOneRigRot(control, rotateX, rotateY, rotateZ):
    try:
        cmds.setAttr(control + '.rotateX', rotateX)
        cmds.setAttr(control + '.rotateY', rotateY)
        cmds.setAttr(control + '.rotateZ', rotateZ)
    except:
        if 0:
            cmds.warning('Rotation channel is locked on control: ' + control)
#-----------------------------------------------------------------------------
def setOneRigTrans(control, translateX, translateY, translateZ):
    try:
        cmds.setAttr(control + '.translateX', translateX)
        cmds.setAttr(control + '.translateY', translateY)
        cmds.setAttr(control + '.translateZ', translateZ)
    except:
        if 0:
            cmds.warning('Translation channel is locked on control: ' + control)
#-----------------------------------------------------------------------------
def hideCharacterIKFKByName(characterName , bIsHide , attrName):
    print characterName , bIsHide
    if characterName == None: return
    mainCtrl = getRigGlobalControlObject(characterName , u'RS_Center', u'RT_Global', 0)
    print mainCtrl  
    if mainCtrl:
        cmds.setAttr(mainCtrl + '.'+ attrName, bIsHide)
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
def getCharacterMasterJointsGroup(characterGroup):
    if cmds.objExists(characterGroup):
        try:
            res = cmds.listConnections(characterGroup + '.' + SERigNaming.sMasterJointsGroupAttr)[0]
            return res
        except:
            cmds.warning('Cannot find character group: ' + characterGroup + ' master joints group')
            return None
    else:
        cmds.warning('Cannot find character group: ' + characterGroup)
        return None
#-----------------------------------------------------------------------------
def getCharacterModelGroup(characterGroup):
    if cmds.objExists(characterGroup):
        try:
            res = cmds.listConnections(characterGroup + '.' + SERigNaming.sModelGroupAttr)[0]
            return res
        except:
            cmds.warning('Cannot find character group: ' + characterGroup + ' model group')
            return None
    else:
        cmds.warning('Cannot find character group: ' + characterGroup)
        return None
#-----------------------------------------------------------------------------
def getCharacterFacialControlUIGroup(characterGroup):
    facialComponent = getCharacterFacialComponentGroup(characterGroup)
    if facialComponent:
        controlsGrp = getCharacterComponentControlsGroup(facialComponent)

        if controlsGrp:
            try:
                res = cmds.listConnections(controlsGrp + '.' + SERigNaming.sFaceControlUIAttr)[0]
                return res
            except:
                cmds.warning('Cannot find character : ' + characterGroup + ' face control UI')
                return None
#-----------------------------------------------------------------------------
def getCharacterFacialComponentGroup(characterGroup):
    if cmds.objExists(characterGroup):
        try:
            res = cmds.listConnections(characterGroup + '.' + SERigNaming.sFacialComponentAttr)[0]
            return res
        except:
            cmds.warning('Cannot find character : ' + characterGroup + ' facial component')
            return None
    else:
        cmds.warning('Cannot find character group: ' + characterGroup)
        return None
#-----------------------------------------------------------------------------
def getFaceProxyJointControlsGroup(facialComponentGroup):
    if cmds.objExists(facialComponentGroup):
        try:
            res = cmds.listConnections(facialComponentGroup + '.' + SERigNaming.sFaceProxyControlGroupAttr)[0]
            return res
        except:
            cmds.warning('Cannot find facial component : ' + facialComponentGroup + ' face proxy joint controls group')
            return None
    else:
        cmds.warning('Cannot find facial component group: ' + facialComponentGroup)
        return None
#-----------------------------------------------------------------------------
def getFaceProxyControlRivetsGroup(facialComponentGroup):
    if cmds.objExists(facialComponentGroup):
        try:
            res = cmds.listConnections(facialComponentGroup + '.' + SERigNaming.sFaceProxyControlRivetGroupAttr)[0]
            return res
        except:
            cmds.warning('Cannot find facial component : ' + facialComponentGroup + ' face proxy control rivets group')
            return None
    else:
        cmds.warning('Cannot find facial component group: ' + facialComponentGroup)
        return None
#-----------------------------------------------------------------------------
def getFaceProxyControlRivetDriverGroup(FaceProxyControlGroup):
    if cmds.objExists(FaceProxyControlGroup):
        try:
            res = cmds.listConnections(FaceProxyControlGroup + '.' + SERigNaming.sFaceProxyControlRivetDriverGroupAttr)[0]
            return res
        except:
            cmds.warning('Cannot find face proxy control group : ' + FaceProxyControlGroup + ' rivet driver group')
            return None
    else:
        cmds.warning('Cannot find face proxy control group: ' + FaceProxyControlGroup)
        return None
#-----------------------------------------------------------------------------
def getCharacterComponentControlsGroup(characterComponentGroup):
    if cmds.objExists(characterComponentGroup):
        try:
            res = cmds.listConnections(characterComponentGroup + '.' + SERigNaming.sControlsGroupAttr)[0]
            return res
        except:
            cmds.warning('Cannot find character component: ' + characterComponentGroup + ' controls group')
            return None
    else:
        cmds.warning('Cannot find character component: ' + characterComponentGroup)
        return None
#-----------------------------------------------------------------------------
def getCharacterComponentRigPartsGroup(characterComponentGroup):
    if cmds.objExists(characterComponentGroup):
        try:
            res = cmds.listConnections(characterComponentGroup + '.' + SERigNaming.sRigPartsGroupAttr)[0]
            return res
        except:
            cmds.warning('Cannot find character component: ' + characterComponentGroup + ' rig parts group')
            return None                 
    else:
        cmds.warning('Cannot find character component: ' + characterComponentGroup)
        return None
#-----------------------------------------------------------------------------
def getCharacterComponentPrefix(characterComponentGroup):
    if cmds.objExists(characterComponentGroup):
        try:
            res = cmds.getAttr(characterComponentGroup + '.' + SERigNaming.sRigComponentPrefix)
            return res
        except:
            cmds.warning('Cannot find character component prefix : ' + characterComponentGroup)
            return None                 
    else:
        cmds.warning('Cannot find character component: ' + characterComponentGroup)
        return None
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
def isRigControlGroup(inputObject):
    if cmds.objExists(inputObject):
        try:
            rigObjectTypeNode = cmds.listConnections(inputObject + '.RigObjectType')[0]
            if cmds.nodeType(rigObjectTypeNode) == 'RigControlType':
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
#-----------------------------------------------------------------------------
def findRelatedRigCharacterGroup(inputObject):
    if not cmds.objExists(inputObject):
        return None

    curParent = cmds.listRelatives(inputObject, p = True)
    while curParent:
        curParent = curParent[0]
        if isRigCharacterGroup(curParent):
            return curParent
        
        curParent = cmds.listRelatives(curParent, p = True)
    
    return None
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
def getDefaultCameras():
    # Get all cameras first.
    cameras = cmds.ls(type = ('camera'), l = True)

    # Let's filter all startup / default cameras.
    startupCameras = [camera for camera in cameras if cmds.camera(cmds.listRelatives(camera, parent = True)[0], startupCamera = True, q = True)]

    return startupCameras
#-----------------------------------------------------------------------------
def getNonDefaultCameras():
    # Get all cameras first.
    cameras = cmds.ls(type = ('camera'), l = True)

    startupCameras = getDefaultCameras()

    # non-default cameras are easy to find now.
    nonStartupCameras = list(set(cameras) - set(startupCameras))

    # Let's get their respective transform names, just in-case
    nonStartupCamerasTransforms = map(lambda x: cmds.listRelatives(x, parent = True)[0], nonStartupCameras)

    return [nonStartupCameras, nonStartupCamerasTransforms]
#-----------------------------------------------------------------------------
def getDefaultPerspectiveCamera():
    startupCameras = getDefaultCameras()
    for camera in startupCameras:
        index = camera.find('persp')
        if index != -1:
            return camera

    return None
#-----------------------------------------------------------------------------
def hideTransObjectChannels(transObject, hideChannels = []):
    singleAttributeList = []
    for hc in hideChannels:
        if hc in ['t', 'r', 's']:
            for axis in ['x', 'y', 'z']:
                attr = hc + axis
                singleAttributeList.append(attr)
        else:
            singleAttributeList.append(hc)

    for attr in singleAttributeList:
        cmds.setAttr(transObject + '.' + attr, cb = 0, k = 0)
#-----------------------------------------------------------------------------
def getFaceProxyJointControls(rigCharacterGroup):
    proxyJointControls = []
    
    facialComponentGroup = getCharacterFacialComponentGroup(rigCharacterGroup)
    if facialComponentGroup:
        faceProxyJointControlsGroup = getFaceProxyJointControlsGroup(facialComponentGroup)

        if faceProxyJointControlsGroup:
            proxyGroupChildren = cmds.listRelatives(faceProxyJointControlsGroup, c = True, type = 'transform')
            for child in proxyGroupChildren:
                if isRigControlGroup(child):
                    proxyJointControl = getRigControlObjectFromGroup(child)
                    if proxyJointControl:
                        proxyJointControls.append(proxyJointControl)
    
    return proxyJointControls
#-----------------------------------------------------------------------------