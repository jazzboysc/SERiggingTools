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
    RT_SpineFK              = 7,
    RT_Hip                  = 8,
    RT_Knee                 = 9,
    RT_AnkleIKRotation      = 10,
    RT_FootIKMain           = 11,
    RT_FootBaseSwive        = 12, 
    RT_FootToeSwive         = 13,
    RT_FootRotation         = 14,
    RT_LegFK                = 15,
    RT_Clavicle             = 16,
    RT_Hand                 = 17,
    RT_ThumbFK              = 18,
    RT_IndexFK              = 19,
    RT_MiddleFK             = 20,
    RT_RingFK               = 21,
    RT_PinkyFK              = 22,
    RT_LegPV                = 23,
    RT_ArmPV                = 24,
    RT_ArmIKMain            = 25,
    RT_NeckFK               = 26,
    RT_HeadFK               = 27,
    RT_Global               = 28,
    RT_Component            = 29,
    RT_LegComponent         = 30,
    RT_ArmComponent         = 31,
    RT_SpineComponent       = 32,
    RT_NeckComponent        = 33,
    RT_HandComponent        = 34,
    RT_Max                  = 35
    )

eRigTypeStringTable = [
    'RT_Unknown',
    'RT_ShoulderFK',
    'RT_ElbowFK',
    'RT_WristFK',
    'RT_SpineUpperBody',
    'RT_SpineChest',
    'RT_SpinePelvis',
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
    'RT_Global',
    'RT_Component',
    'RT_LegComponent',
    'RT_ArmComponent',
    'RT_SpineComponent',
    'RT_NeckComponent',
    'RT_HandComponent'
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