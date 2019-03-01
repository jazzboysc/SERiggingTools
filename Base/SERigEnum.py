def SE_RigEnum(**namedValues):
    return type('SERigEnum', (), namedValues)

eRigSide = SE_RigEnum(
    RS_Unknown = 0,
    RS_Left    = 1,
    RS_Right   = 2,
    RS_Center  = 3,
    RS_Max     = 4
    )

eRigSideStringTable = [
    'RS_Unknown',    
    'RS_Left',
    'RS_Right',
    'RS_Center'
    ]

eRigType = SE_RigEnum(
    RT_Unknown              = 0,
    RT_ShoulderFK           = 1,
    RT_ElbowFK              = 2,
    RT_WristFK              = 3,
    RT_SpineUpperBody       = 4,
    RT_SpineChest           = 5,
    RT_SpinePelvis          = 6,
    RT_SpinePelvisLocal     = 7,
    RT_SpineFK              = 8,
    RT_Hip                  = 9,
    RT_Knee                 = 10,
    RT_AnkleIKRotation      = 11,
    RT_FootIKMain           = 12,
    RT_FootBaseSwive        = 13, 
    RT_FootToeSwive         = 14,
    RT_FootRotation         = 15,
    RT_LegFK                = 16,
    RT_Clavicle             = 17,
    RT_Hand                 = 18,
    RT_ThumbFK              = 19,
    RT_IndexFK              = 20,
    RT_MiddleFK             = 21,
    RT_RingFK               = 22,
    RT_PinkyFK              = 23,
    RT_LegPV                = 24,
    RT_ArmPV                = 25,
    RT_ArmIKMain            = 26,
    RT_NeckFK               = 27,
    RT_HeadFK               = 28,
    RT_HeadAimIK            = 29,
    RT_OnFaceIK             = 30,
    RT_OnFaceFK             = 31,
    RT_Global               = 32,
    RT_Component            = 33,
    RT_LegComponent         = 34,
    RT_ArmComponent         = 35,
    RT_SpineComponent       = 36,
    RT_NeckComponent        = 37,
    RT_HandComponent        = 38,
    RT_FacialComponent      = 39,
    RT_Max                  = 40
    )

eRigTypeStringTable = [
    'RT_Unknown',
    'RT_ShoulderFK',
    'RT_ElbowFK',
    'RT_WristFK',
    'RT_SpineUpperBody',
    'RT_SpineChest',
    'RT_SpinePelvis',
    'RT_SpinePelvisLocal',
    'RT_SpineFK',
    'RT_Hip',
    'RT_Knee',
    'RT_AnkleIKRotation',
    'RT_FootIKMain',
    'RT_FootBaseSwive',
    'RT_FootToeSwive',
    'RT_FootRotation',
    'RT_LegFK',
    'RT_Clavicle',
    'RT_Hand',
    'RT_ThumbFK',
    'RT_IndexFK',
    'RT_MiddleFK',
    'RT_RingFK',
    'RT_PinkyFK',
    'RT_LegPV',
    'RT_ArmPV',
    'RT_ArmIKMain',
    'RT_NeckFK',
    'RT_HeadFK',
    'RT_HeadAimIK',
    'RT_OnFaceIK',
    'RT_OnFaceFK',
    'RT_Global',
    'RT_Component',
    'RT_LegComponent',
    'RT_ArmComponent',
    'RT_SpineComponent',
    'RT_NeckComponent',
    'RT_HandComponent',
    'RT_FacialComponent'
    ]

eRigColor = SE_RigEnum(
    RC_Red    = 13,
    RC_Blue   = 6,
    RC_Yellow = 22
    )

eRigFacing = SE_RigEnum(
    RF_X = 1,
    RF_Y = 2,
    RF_Z = 3
    )

eRigFacialControlID = SE_RigEnum(
    RFCID_JawPos         = 0,
    RFCID_JawMidPos      = 1,
    RFCID_JawIK          = 2,
    RFCID_LipCloseFK     = 3,
    RFCID_EyesAimIK      = 4,
    RFCID_LeftEyeAimIK   = 5,
    RFCID_RightEyeAimIK  = 6
    )