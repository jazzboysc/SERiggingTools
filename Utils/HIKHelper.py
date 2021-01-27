import maya.cmds as cmds

# HIKSkeletonMapList = [
#     'root',            #0
#     'pelvis',          #1
#     'leftUpLeg',       #2
#     'leftLeg',         #3
#     'leftFoot',        #4
#     'rightUpLeg',      #5
#     'rightLeg',        #6
#     'rightFoot',       #7
#     'spine',           #8
#     'leftArm',         #9
#     'leftForeArm',     #10
#     'leftHand',        #11
#     'rightArm',        #12
#     'rightForeArm',    #13
#     'rightHand',       #14
#     'head',            #15
#     'leftToeBase',     #16
#     'rightToeBase',    #17
#     'leftShoulder',    #18
#     'rightShoulder',   #19
#     'neck',            #20
# ]

MobuEffectorList = [
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

HIKCustomRigMobu2MayaMapTable = {}
HIKCustomRigMobu2MayaMapTable['HipsEffector'] = 'HipsGX'
HIKCustomRigMobu2MayaMapTable['LeftAnkleEffector'] = 'LeftFootGX'
HIKCustomRigMobu2MayaMapTable['RightAnkleEffector'] = 'RightFootGX'
HIKCustomRigMobu2MayaMapTable['LeftWristEffector'] = 'LeftHandGX'
HIKCustomRigMobu2MayaMapTable['RightWristEffector'] = 'RightHandGX'
HIKCustomRigMobu2MayaMapTable['LeftKneeEffector'] = 'LeftLegGX'
HIKCustomRigMobu2MayaMapTable['RightKneeEffector'] = 'RightLegGX'
HIKCustomRigMobu2MayaMapTable['LeftElbowEffector'] = 'LeftForeArmGX'
HIKCustomRigMobu2MayaMapTable['RightElbowEffector'] = 'RightForeArmGX'
HIKCustomRigMobu2MayaMapTable['LeftShoulder'] = 'LeftShoulderGX'
HIKCustomRigMobu2MayaMapTable['RightShoulder'] = 'RightShoulderGX'
HIKCustomRigMobu2MayaMapTable['HeadEffector'] = 'HeadGX'
HIKCustomRigMobu2MayaMapTable['ChestOriginEffector'] = 'SpineGX'
HIKCustomRigMobu2MayaMapTable['ChestEndEffector'] = 'Spine3GX'

# CharacterList
def characterDefinitionList():
    charList = cmds.ls(type = 'HIKCharacterNode')
    return charList

# GetHIKState
def getCharacterHIKState(char):
    if not isCharacterDefinition(char):
        raise Exception('%s is not a valid HIKCharacterNode!'%char)
    HIKSolverNode = cmds.listConnections('{}.{}'.format(char, 'OutputCharacterDefinition'), d=True, t = 'HIKState2GlobalSK')
    return HIKSolverNode

# Check is the given name is valid HIK character Definition
def isCharacterDefinition(charName):
    if not cmds.objExists(charName):
        return False
    
    if cmds.objectType(charName) != 'HIKCharacterNode':
        return False
    
    return True

# Create HIK Definition
def createCharacterDefinition(characterName = ''):
    if characterName and isCharacterDefinition(characterName):
        raise Exception('CharacterDefinition:%s already exists!'%characterName)
    if not characterName: characterName = 'CharacterName1'
    
    # create HIK definition
    MAYA_LOCATION = os.environ['MAYA_LOCATION']
    mel.eval('source "'+MAYA_LOCATION+'/scripts/others/hikGlobalUtils.mel"')
    mel.eval('source "'+MAYA_LOCATION+'/scripts/others/hikCharacterControlsUI.mel"')
    mel.eval('source "'+MAYA_LOCATION+'/scripts/others/hikDefinitionOperations.mel"')
    mel.eval('hikCreateDefinition()')
    #charName = mel.eval('newCharacterWithName("'+characterName+'")')
    renameCharacterDefinition(characterName)


# Rename HIK character
def renameCharacterDefinition(newName = ''):
    curName = getCurrentCharacter()
    name = newName
    for char in cmds.ls(type = "HIKCharacterNode"):
        if curName == char:
            #rename HIKCharacterNode
            new_name = cmds.rename(char, name)
            print new_name
            #rename Character
            mel.eval('hikSetCurrentCharacter("{}");'.format(new_name)) 
            mel.eval('hikRenameConnectedNodes("{}","{}");'.format(new_name, char))

# Get Current Character
def getCurrentCharacter():
    char = mel.eval('hikGetCurrentCharacter();')
    return char

# Set Current Character
def setCurrentCharacter(char):
    if not isCharacterDefinition(char):
        raise Exception('%s is not a valid HIKCharacterNode!'%char)

    cmds.optionMenuGrp("hikCharacterList", e = True, v = char)
    mel.eval('hikUpdateCurrentCharacterFromUI()')
    mel.eval('hikUpdateContextualUI()')
    
    current_char = getCurrentCharacter()
    return current_char

# Set Character Source
def setCharacterSource(char, source):
    if not isCharacterDefinition(char):
        raise Exception('%s is not a valid HIKCharacterNode!'%char)
        
    # mel.eval('hikSetCurrentSource("'+source+'");')
    # mel.eval('hikUpdateSourceList()')
    # mel.eval('hikUpdateSkeletonUI()')
    allSourceChar = cmds.optionMenuGrp("hikSourceList", query=True, itemListLong=True)
    i=1
    for item in allSourceChar:
        optMenu = 'hikSourceList|OptionMenu'
        sourceChar = cmds.menuItem(item, query = True, label = True)
        print sourceChar.strip()
        if sourceChar.strip() == source:
            print 'Retarget Source Found.'
            cmds.optionMenu(optMenu, edit=True, select=i)
            mel.eval('hikUpdateCurrentSourceFromUI()')
            mel.eval('hikUpdateContextualUI()')
            mel.eval('hikControlRigSelectionChangedCallback')
            
            break
        i+=1

# Auto Define Skeleton Definition According to names        
#def defineCharacterSkeleton(char):
    #mel.eval('setCharacterObject("Slave_Root", "'+char+'", 8, 0);')
    #mel.eval('hikUpdateContextualUI()')
    #for i in range(len(HIKSkeletonMapList)):
    #    print i

# SelectCustomRigs
def addSelectCustomRigs(char, selectMesh = True):
    if not isCharacterDefinition(char):
        raise Exception('%s is not a valid HIKCharacterNode!'%char)
    
    HIKState = getCharacterHIKState(char)
    if HIKState == None:
        raise Exception('Found no custom rig for character %s.' %char)
    
    cmds.select(clear = True)
    for effector in MobuEffectorList:
        attr = HIKCustomRigMobu2MayaMapTable[effector]
        GXAttr = '{}.{}'.format(HIKState[0], attr)
        mappingNode = cmds.listConnections(GXAttr ,d = True, t = 'CustomRigDefaultMappingNode')
        if mappingNode != None:
            rigNode = cmds.listConnections('{}.{}'.format(mappingNode[0], 'destinationRig'), s = True)
            skNode = cmds.listConnections('{}.{}'.format(mappingNode[0], 'destinationSkeleton'), s = True)
            cmds.select(rigNode[0], add= True)
            if selectMesh:
                addSelectMeshBySkeleton(skNode[0])

# SelectMeshes
def addSelectMeshBySkeleton(skt): 
    if not cmds.objExists(skt):
        raise Exception('%s does not exist!' %skt)

    skinClusters = cmds.listConnections(skt, d=True, t = 'skinCluster')
    if skinClusters== None:
        return
        
    for skinC in skinClusters:
        skinSets = cmds.listConnections(skinC, d=True, t = 'objectSet')
        if skinSets != None:
            meshes = cmds.listConnections(skinSets[0], d=True, t = 'mesh')
            cmds.select(meshes, add = True)

# Get Custom Rig Map in Maya
def matchCustomRigWithEffector(char, effector):
    HIKState = getCharacterHIKState(char)
    attr = HIKCustomRigMobu2MayaMapTable[effector]
    GXAttr = '{}.{}'.format(HIKState[0], attr)
    mappingNode = cmds.listConnections(GXAttr ,d = True, t = 'CustomRigDefaultMappingNode')
    if mappingNode != None:
        rigNode = cmds.listConnections('{}.{}'.format(mappingNode[0], 'destinationRig'), s = True)
        if len(rigNode) > 0:
            return rigNode[0]
    return 0

def matchSkeletonDefineWithSlot(char, slot):
    if not isCharacterDefinition(char):
        raise Exception('%s is not a valid HIKCharacterNode!'%char)

    jointNode = cmds.listConnections('{}.{}'.format(char, slot) ,s = True, t = 'joint')
    if jointNode and len(jointNode) > 0:
        return jointNode[0]
    else:
        return 0


#addSelectCustomRigs('LittleTraveller')

# mel.eval('setCharacterObject("root", "Character1",0,0);')
# mel.eval('setCharacterObject("pelvis", "Character1",1,0);')
# mel.eval('setCharacterObject("thigh_l", "Character1",2,0);')
# mel.eval('setCharacterObject("calf_l", "Character1",3,0);')
# mel.eval('setCharacterObject("foot_l", "Character1",4,0);')
# mel.eval('setCharacterObject("thigh_r", "Character1",5,0);')
# mel.eval('setCharacterObject("calf_r", "Character1",6,0);')
# mel.eval('setCharacterObject("foot_r", "Character1",7,0);')
# mel.eval('setCharacterObject("spine_01", "Character1",8,0);')
# mel.eval('setCharacterObject("upperarm_l", "Character1",9,0);')
# mel.eval('setCharacterObject("lowerarm_l", "Character1",10,0);')
# mel.eval('setCharacterObject("hand_l", "Character1",11,0);')
# mel.eval('setCharacterObject("upperarm_r", "Character1",12,0);')
# mel.eval('setCharacterObject("lowerarm_r", "Character1",13,0);')
# mel.eval('setCharacterObject("hand_r", "Character1",14,0);')
# mel.eval('setCharacterObject("head", "Character1",15,0);')
# mel.eval('setCharacterObject("ball_l", "Character1",16,0);')
# mel.eval('setCharacterObject("ball_r", "Character1",17,0);')
# mel.eval('setCharacterObject("clavicle_l", "Character1",18,0);')
# mel.eval('setCharacterObject("clavicle_r", "Character1",19,0);')
# mel.eval('setCharacterObject("neck_01", "Character1",20,0);')
# #21 and 22 are extra wrists
# mel.eval('setCharacterObject("spine_02", "Character1",23,0);')
# mel.eval('setCharacterObject("spine_03", "Character1",24,0);')
# #25-32 are additional spines
# #33-42 are additional necks
# mel.eval('setCharacterObject("thumb_01_l", "Character1",50,0);')
# mel.eval('setCharacterObject("thumb_02_l", "Character1",51,0);')
# mel.eval('setCharacterObject("thumb_03_l", "Character1",52,0);')
# mel.eval('setCharacterObject("thumb_04_l_Jx", "Character1",53,0);')
# mel.eval('setCharacterObject("index_01_l", "Character1",54,0);')
# mel.eval('setCharacterObject("index_02_l", "Character1",55,0);')
# mel.eval('setCharacterObject("index_03_l", "Character1",56,0);')
# mel.eval('setCharacterObject("index_04_l_Jx", "Character1",57,0);')
# mel.eval('setCharacterObject("middle_01_l", "Character1",58,0);')
# mel.eval('setCharacterObject("middle_02_l", "Character1",59,0);')
# mel.eval('setCharacterObject("middle_03_l", "Character1",60,0);')
# mel.eval('setCharacterObject("middle_04_l_Jx", "Character1",61,0);')
# mel.eval('setCharacterObject("ring_01_l", "Character1",62,0);')
# mel.eval('setCharacterObject("ring_02_l", "Character1",63,0);')
# mel.eval('setCharacterObject("ring_03_l", "Character1",64,0);')
# mel.eval('setCharacterObject("ring_04_l_Jx", "Character1",65,0);')
# mel.eval('setCharacterObject("pinky_01_l", "Character1",66,0);')
# mel.eval('setCharacterObject("pinky_02_l", "Character1",67,0);')
# mel.eval('setCharacterObject("pinky_03_l", "Character1",68,0);')
# mel.eval('setCharacterObject("pinky_04_l_Jx", "Character1",69,0);')
# #70-73 is left hand 6th finger
# mel.eval('setCharacterObject("thumb_01_r", "Character1",74,0);')
# mel.eval('setCharacterObject("thumb_02_r", "Character1",75,0);')
# mel.eval('setCharacterObject("thumb_03_r", "Character1",76,0);')
# mel.eval('setCharacterObject("thumb_04_r_Jx", "Character1",77,0);')
# mel.eval('setCharacterObject("index_01_r", "Character1",78,0);')
# mel.eval('setCharacterObject("index_02_r", "Character1",79,0);')
# mel.eval('setCharacterObject("index_03_r", "Character1",80,0);')
# mel.eval('setCharacterObject("index_04_r_Jx", "Character1",81,0);')
# mel.eval('setCharacterObject("middle_01_r", "Character1",82,0);')
# mel.eval('setCharacterObject("middle_02_r", "Character1",83,0);')
# mel.eval('setCharacterObject("middle_03_r", "Character1",84,0);')
# mel.eval('setCharacterObject("middle_04_r_Jx", "Character1",85,0);')
# mel.eval('setCharacterObject("ring_01_r", "Character1",86,0);')
# mel.eval('setCharacterObject("ring_02_r", "Character1",87,0);')
# mel.eval('setCharacterObject("ring_03_r", "Character1",88,0);')
# mel.eval('setCharacterObject("ring_04_r_Jx", "Character1",89,0);')
# mel.eval('setCharacterObject("pinky_01_r", "Character1",90,0);')
# mel.eval('setCharacterObject("pinky_02_r", "Character1",91,0);')
# mel.eval('setCharacterObject("pinky_03_r", "Character1",92,0);')
# mel.eval('setCharacterObject("pinky_04_r_Jx", "Character1",93,0);')
# #94-97 is 6th right hand finger
# #98-101 is 6th left foot toe
# #102-121 are left foot toes
# #122-125 is 6th right foot toe
# #126-145 are right foot toes
# #146 is left hand thumb 0

# mel.eval('hikUpdateDefinitionUI;')
# mel.eval('LockSkeletonDefinition();')

# mel.eval('hikCreateControlRig;')
# cmds.parent('Character1_Ctrl_Reference', 'Character1_Root_CNT')