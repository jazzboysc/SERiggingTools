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
    RT_Shoulder             = 1,
    RT_Elbow                = 2,
    RT_Wrist                = 3,
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
    RT_LegPV                = 18,
    RT_ArmPV                = 19,
    RT_NeckFK               = 20,
    RT_Head                 = 21,
    RT_Global               = 22,
    RT_Component            = 23,
    RT_LegComponent         = 24,
    RT_ArmComponent         = 25,
    RT_SpineComponent       = 26,
    RT_NeckComponent        = 27,
    RT_HandComponent        = 28,
    RT_Max                  = 29
    )

eRigTypeStringTable = [
    'RT_Unknown',
    'RT_Shoulder',
    'RT_Elbow',
    'RT_Wrist',
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
    'RT_LegPV',
    'RT_ArmPV',
    'RT_NeckFK',
    'RT_Head',
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