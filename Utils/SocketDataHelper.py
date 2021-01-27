class MayaMobuSocketData():
    def __init__(self):    
        self.MobuEffectorList = [
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

        self.MobuTransform = {}
        self.MobuTransform['HipsEffector'] = []
        self.MobuTransform['LeftAnkleEffector'] = []
        self.MobuTransform['RightAnkleEffector'] = []
        self.MobuTransform['LeftWristEffector'] = []
        self.MobuTransform['RightWristEffector'] = []
        self.MobuTransform['LeftKneeEffector'] = []
        self.MobuTransform['RightKneeEffector'] = []
        self.MobuTransform['LeftElbowEffector'] = []
        self.MobuTransform['RightElbowEffector'] = []
        self.MobuTransform['LeftShoulder'] = []
        self.MobuTransform['RightShoulder'] = []
        self.MobuTransform['HeadEffector'] = []
        self.MobuTransform['ChestOriginEffector'] = []
        self.MobuTransform['ChestEndEffector'] = []
        
        # parameters
        self.importFBXPath = ''
        self.importNamespace = ''
        self.importModeMerge = True
        self.skeletonDefinePath = ''
        self.commandType = 0  # 0 represents no command; 1 represents import; 
        self.characterName = '' 
        self.targetCharacter = ''