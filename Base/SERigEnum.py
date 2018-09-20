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
    RT_Ankle                = 10,
    RT_Foot                 = 11,
    RT_Clavicle           = 12,
    RT_Hand               = 13,
    RT_LegPV              = 14,
    RT_ArmPV              = 15,
    RT_Neck               = 16,
    RT_Head               = 17,
    RT_Global             = 18,
    RT_Component          = 19,
    RT_LegComponent       = 20,
    RT_ArmComponent       = 21,
    RT_SpineComponent     = 22,
    RT_NeckComponent      = 23,
    RT_HandComponent      = 24,
    RT_Max                = 25
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
    'RT_Ankle',
    'RT_Foot',
    'RT_Clavicle',
    'RT_Hand',
    'RT_LegPV',
    'RT_ArmPV',
    'RT_Neck',
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