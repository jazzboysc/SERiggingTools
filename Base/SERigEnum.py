def SE_RigEnum(**namedValues):
    return type('SERigEnum', (), namedValues)

eRigSide = SE_RigEnum(
    RS_Left = 1,
    RS_Right = 2,
    RS_Center = 3,
    RS_Unknown = 4
    )

eRigType = SE_RigEnum(
    RT_Shoulder = 1,
    RT_Elbow    = 2,
    RT_Wrist    = 3,
    RT_Spine    = 4,
    RT_Hip      = 5,
    RT_Knee     = 6,
    RT_Ankle    = 7,
    RT_Foot     = 8,
    RT_Global   = 9,
    RT_Unknown  = 10
    )

eRigColor = SE_RigEnum(
    RC_Red = 13,
    RC_Blue = 6,
    RC_Yellow = 22
    )

eRigFacing = SE_RigEnum(
    RF_X = 1,
    RF_Y = 2,
    RF_Z = 3
    )