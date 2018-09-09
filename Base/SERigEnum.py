def SE_RigEnum(**namedValues):
    return type('SERigEnum', (), namedValues)

eRigSide = SE_RigEnum(
    RS_Left    = 1,
    RS_Right   = 2,
    RS_Center  = 3,
    RS_Unknown = 4
    )

eRigType = SE_RigEnum(
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
    RT_Unknown        = 22
    )

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