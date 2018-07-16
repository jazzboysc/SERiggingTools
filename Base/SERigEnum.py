def SE_RigEnum(**namedValues):
    return type('SERigEnum', (), namedValues)

eRigSide = SE_RigEnum(
    RS_Left = 1,
    RS_Right = 2,
    RS_Center = 3,
    RS_Unkown = 4
    )

eRigType = SE_RigEnum(
    RT_Shoulder = 1,
    RT_Elbow = 2,
    RT_Wrist = 3,
    RT_Unkown = 4
    )
