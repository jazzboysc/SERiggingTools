sMainControlPrefix  = 'Main'
sControl            = '_Ctrl'
sControlGroup       = '_CtrlGrp'
sDriverGroup        = '_DrvGrp'
sOffsetGroup        = '_OffsetGrp'
sRigGroup           = 'RigGrp'
sJointsGroup        = 'JointsGrp'
sModelGroup         = 'ModelGrp'
sBuilderGroup       = 'BuilderGrp'
sRigCompsGroup      = 'RigComponentsGrp'
sRigPartsGroup      = 'RigPartsGrp'
sRigPartsFixedGroup = 'RigPartsFixedGrp'
sIKPrefix           = 'IK_'
sFKPrefix           = 'FK_'
sExpressionPrefix   = 'Expr_'
sSlavePrefix        = 'Slave_'
sControlsGroup      = 'ControlsGrp'
sTwistJointsGroup   = 'TwistJointsGrp'
sTwistBegin         = 'TwistBegin'
sTwistEnd           = 'TwistEnd'
sTwistKnob          = 'TwistKnob'
sTwistIKHandle      = 'Twist_ikHandle'
sProxy              = 'Proxy'
sCurve              = 'Curve'
sSplineIKHandle     = 'Spline_ikHandle'
sIKHandle           = 'ikHandle'
sPoleVector         = 'PV'
sSync               = 'Sync'
sDeformationGroup   = 'DeformationGrp'

sDeformationGroupAttr      = 'DeformationGroup'
sDeformationGroupOwnerAttr = 'DeformationGroupOwner'
sModelGroupAttr            = 'ModelGroup'
sModelGroupOwnerAttr       = 'ModelGroupOwner'

sModelVisibilityAttr           = 'modelVisibility'
sMasterJointsVisibilityAttr    = 'masterJointsVisibility'
sSlaveJointsVisibilityAttr     = 'slaveJointsVisibility'
sBodyControlsVisibilityAttr    = 'bodyControlsVisibility'
sFacialControlsVisibilityAttr  = 'facialControlsVisibility'
sFKNeckJoint0FollowHeadAttr    = 'neckJoint0FollowHead'
sIKHeadAimLocalToWorldAttr     = 'headAimControlLocalToWorld'

sJawForwardAttr = 'jawForward'
sJawForwardFactorAttr = 'jawForwardFactor'

sFootToeSwiveAttr         = 'toeSwive'
sFootHeelSwiveAttr        = 'heelSwive'
sFootRotateXAttr          = 'footRotateX'
sFootRotateZAttr          = 'footRotateZ'
sFootToeStartRotAngleAttr = 'toeStartRotAngle'
sFootToeRotAngleRangeAttr  = 'toeRotAngleRange'

sAU_01_L_Attr = 'AU01L'
sAU_01_R_Attr = 'AU01R'
sAU_02_L_Attr = 'AU02L'
sAU_02_R_Attr = 'AU02R'
sAU_05_L_Attr = 'AU05L'
sAU_05_R_Attr = 'AU05R'
sAU_06_L_Attr = 'AU06L'
sAU_06_R_Attr = 'AU06R'
sAU_07_L_Attr = 'AU07L'
sAU_07_R_Attr = 'AU07R'
sAU_Blink_L_Attr  = 'BlinkL'
sAU_Blink_R_Attr  = 'BlinkR'
sAU_LipClose_Attr = 'LipClose'
sAU_Eye_L_LookLeft_Attr  = 'Eye_L_LookLeft'
sAU_Eye_L_LookRight_Attr = 'Eye_L_LookRight'
sAU_Eye_L_LookUp_Attr    = 'Eye_L_LookUp'
sAU_Eye_L_LookDown_Attr  = 'Eye_L_LookDown'
sAU_Eye_R_LookLeft_Attr  = 'Eye_R_LookLeft'
sAU_Eye_R_LookRight_Attr = 'Eye_R_LookRight'
sAU_Eye_R_LookUp_Attr    = 'Eye_R_LookUp'
sAU_Eye_R_LookDown_Attr  = 'Eye_R_LookDown'

sWM01_browsRaiseInner_R_Attr = 'WM01_browsRaiseInner_R'
sWM01_browsRaiseInner_L_Attr = 'WM01_browsRaiseInner_L'
sWM01_browsRaiseOuter_R_Attr = 'WM01_browsRaiseOuter_R'
sWM01_browsRaiseOuter_L_Attr = 'WM01_browsRaiseOuter_L'
sWM02_browsDown_L_Attr = 'WM02_browsDown_L'
sWM02_browsDown_R_Attr = 'WM02_browsDown_R'
sWM02_browsLateral_L_Attr = 'WM02_browsLateral_L'
sWM02_browsLateral_R_Attr = 'WM02_browsLateral_R'
sWM02_noseWrinkler_L_Attr = 'WM02_noseWrinkler_L'
sWM02_noseWrinkler_R_Attr = 'WM02_noseWrinkler_R'

gWM_AttrList = [sWM01_browsRaiseInner_R_Attr,
                sWM01_browsRaiseInner_L_Attr,
                sWM01_browsRaiseOuter_R_Attr,
                sWM01_browsRaiseOuter_L_Attr,
                sWM02_browsDown_L_Attr,
                sWM02_browsDown_R_Attr,
                sWM02_browsLateral_L_Attr,
                sWM02_browsLateral_R_Attr,
                sWM02_noseWrinkler_L_Attr,
                sWM02_noseWrinkler_R_Attr]

s_JointsGroup        = '_' + sJointsGroup
s_ModelGroup         = '_' + sModelGroup
s_BuilderGroup       = '_' + sBuilderGroup
s_RigGroup           = '_' + sRigGroup
s_RigCompsGroup      = '_' + sRigCompsGroup
s_RigPartsGroup      = '_' + sRigPartsGroup
s_RigPartsFixedGroup = '_' + sRigPartsFixedGroup
s_IKPrefix           = '_' + sIKPrefix
s_FKPrefix           = '_' + sFKPrefix
s_ExpressionPrefix   = '_' + sExpressionPrefix
s_ControlsGroup      = '_' + sControlsGroup
s_TwistJointsGroup   = '_' + sTwistJointsGroup
s_TwistBegin         = '_' + sTwistBegin
s_TwistEnd           = '_' + sTwistEnd
s_TwistKnob          = '_' + sTwistKnob
s_TwistIKHandle      = '_' + sTwistIKHandle
s_Proxy              = '_' + sProxy
s_Curve              = '_' + sCurve
s_SplineIKHandle     = '_' + sSplineIKHandle
s_IKHandle           = '_' + sIKHandle
s_PoleVector         = '_' + sPoleVector
s_Sync               = '_' + sSync

sFootExtJnt         = 'footExtJnt'
sFootIntJnt         = 'footIntJnt'
sFootBaseJnt        = 'footBaseJnt'
sFootBaseSwiveJnt   = 'footBaseSwiveJnt'
sFootToeSwiveJnt    = 'footToeSwiveJnt'
sFootToeProxy       = 'footToeProxy'
sFootBallProxy      = 'footBallProxy'
sFootAnkleProxy     = 'footAnkleProxy'
sToeProxyPVlocator  = 'toeProxyPVlocator'
sBallProxyPVlocator = 'ballProxyPVlocator'

sLeftLegIKFKSwitch  = 'leftLegIkFkSwitch'
sRightLegIKFKSwitch = 'rightLegIkFkSwitch'
sLeftArmIKFKSwitch  = 'leftArmIkFkSwitch'
sRightArmIKFKSwitch = 'rightArmIkFkSwitch'

sLeftLegFKLocalToWorldSwitch  = 'leftLegFkLocalToWorldSwitch'
sRightLegFKLocalToWorldSwitch = 'rightLegFkLocalToWorldSwitch'
sLeftArmFKLocalToWorldSwitch  = 'leftArmFkLocalToWorldSwitch'
sRightArmFKLocalToWorldSwitch = 'rightArmFkLocalToWorldSwitch'

sLeftLegPVFollowSwitch = 'leftLegPvFollowSwitch'
sRightLegPVFollowSwitch = 'rightLegPvFollowSwitch'
sLeftArmPVFollowSwitch = 'leftArmPvFollowSwitch'
sRightArmPVFollowSwitch = 'rightArmPvFollowSwitch'

sHeadFkFollowWorldSwitch = 'headFkFollowWorldSwitch'

sLeftLegIKFKAutoHide  = 'leftLegIkFkAutoHide'
sRightLegIKFKAutoHide = 'rightLegIkFkAutoHide'
sLeftArmIKFKAutoHide  = 'leftArmIkFkAutoHide'
sRightArmIKFKAutoHide = 'rightArmIkFkAutoHide'

sPrefixAttr              = 'Prefix'
sFKSyncTargets           = 'FKSyncTargets'
sFKSyncTarget            = 'FKSyncTarget'
sFKSyncSources           = 'FKSyncSources'
sFKSyncSource            = 'FKSyncSource'
sIKMainControl           = 'IKMainControl'
sIKMainRotationControl   = 'IKMainRotationControl'
sPVControl               = 'PVControl'
sIKMainControlSyncTarget = 'IKMainControlSyncTarget'
sPVLocatorSyncTarget     = 'PVLocatorSyncTarget'

sJointTagSlaveFingerEnd   = 'SlaveFingerEnd'
sJointTagSlaveToeEnd      = 'SlaveToeEnd'
sJointTagSlaveBreast      = 'SlaveBreast'
sJointTagSlaveRoot        = 'SlaveRoot'
sJointTagSlaveNeckMuscle  = 'SlaveNeckMuscle'
sJointTagSlaveChestEnd    = 'SlaveChestEnd'
sJointTagSlaveFacial      = 'SlaveFacial'
sJointTagFacialBase       = 'FacialBase'
sJointTagFacialRoot       = 'FacialRoot'

