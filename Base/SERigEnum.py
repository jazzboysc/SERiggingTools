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
    RT_SpineChestLocal      = 6,
    RT_SpinePelvis          = 7,
    RT_SpinePelvisLocal     = 8,
    RT_SpineFK              = 9,
    RT_Hip                  = 10,
    RT_Knee                 = 11,
    RT_AnkleIKRotation      = 12,
    RT_FootIKMain           = 13,
    RT_FootBaseSwive        = 14, 
    RT_FootToeSwive         = 15,
    RT_FootRotation         = 16,
    RT_LegFK                = 17,
    RT_Clavicle             = 18,
    RT_Hand                 = 19,
    RT_ThumbFK              = 20,
    RT_IndexFK              = 21,
    RT_MiddleFK             = 22,
    RT_RingFK               = 23,
    RT_PinkyFK              = 24,
    RT_LegPV                = 25,
    RT_ArmPV                = 26,
    RT_ArmIKMain            = 27,
    RT_NeckFK               = 28,
    RT_HeadFK               = 29,
    RT_HeadAimIK            = 30,
    RT_OnFaceIK             = 31,
    RT_OnFaceFK             = 32,
    RT_Global               = 33,
    RT_Component            = 34,
    RT_LegComponent         = 35,
    RT_ArmComponent         = 36,
    RT_SpineComponent       = 37,
    RT_NeckComponent        = 38,
    RT_HandComponent        = 39,
    RT_FacialComponent      = 40,
    RT_Max                  = 41
    )

eRigTypeStringTable = [
    'RT_Unknown',
    'RT_ShoulderFK',
    'RT_ElbowFK',
    'RT_WristFK',
    'RT_SpineUpperBody',
    'RT_SpineChest',
    'RT_SpineChestLocal',
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