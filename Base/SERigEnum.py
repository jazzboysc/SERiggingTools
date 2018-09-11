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
    RT_Unknown   = 0,
    RT_Shoulder  = 1,
    RT_Elbow     = 2,
    RT_Wrist     = 3,
    RT_Spine     = 4,
    RT_Hip       = 5,
    RT_Knee      = 6,
    RT_Ankle     = 7,
    RT_Foot      = 8,
    RT_Clavicle  = 9,
    RT_Hand      = 10,
    RT_LegPV     = 11,
    RT_ArmPV     = 12,
    RT_Neck      = 13,
    RT_Head      = 14,
    RT_Global    = 15,
    RT_Component = 16,
    RT_LegComponent   = 17,
    RT_ArmComponent   = 18,
    RT_SpineComponent = 19,
    RT_NeckComponent  = 20,
    RT_HandComponent  = 21,
    RT_Max            = 22
    )

eRigTypeStringTable = [
    'RT_Unknown',
    'RT_Shoulder',
    'RT_Elbow',
    'RT_Wrist',
    'RT_Spine',
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