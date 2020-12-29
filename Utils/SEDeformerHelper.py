import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma
import re
import cPickle

from . import SEStringHelper
from . import SEFacsHelper
from . import SERigObjectTypeHelper
from . import SEJointHelper
from ..Base import SERigNaming
from ..Base import SERigEnum

#-----------------------------------------------------------------------------
# 1 Import AUBase and AUs frome AUs.ma maya scene file.

# 2 Check AUs naming, possibly remove namespace or prefix.
# Batch removing AUs prefix, first select AUBase and all the AUs, then run this tool:
# DeformerHelper.batchRemovePrefix()

# 3 Match the imported AUBase and AUs to our current character's face,
# first select AUBase and FacialBase, then run this tool:
# DeformerHelper.matchSourceBlendshapesToTarget()

# 4 Connetc AUBase to our rig's facial control system. Select AUBase mesh and FacialBase mesh, then run this tool:
# DeformerHelper.connectFACSDataBufferToAUBlendshape()

# 5 Add a blendshape target for our FacialBase mesh. Select AUBase and FacialBase mesh, then run maya command: Deform->BlendShape->Add->Specify node

# 6 Add a blendshape target for our FacialBaseTri mesh. Select FacialBase and FacialBaseTri, then run maya command: Deform-BlendShape->Create node

# 7 Create facial skin proxy joints and controls. First select our cage guide mesh(eg. FaceCage_V99) and our head LOD1 mesh, then run this tool:
# RigHumanFacialComponent.createFacialSkinProxyJointsAndControlsFromSelection(4, False, 0.2)

# 8 Create drivers for facial skin proxy controls.
# RigHumanFacialComponent.createFacialProxyControlRivetConstraints('FacialBaseTri', 'Kimono_Girl_RigGrp')

# 9 Remove some proxy controls and joints to fit the facial joint budget (75 joints per material)
#RigHumanFacialComponent.removeFaceProxyControlInfluence()

# 10 Add slave neck 1, slave head, slave jaw offset joints to the skincluster.
#-----------------------------------------------------------------------------

facialActionUnitTypeList = [
    SERigEnum.eRigFacialActionUnitType.AU_01_L,
    SERigEnum.eRigFacialActionUnitType.AU_01_R,
    SERigEnum.eRigFacialActionUnitType.AU_02_L,
    SERigEnum.eRigFacialActionUnitType.AU_02_R,
    SERigEnum.eRigFacialActionUnitType.AU_04_L,
    SERigEnum.eRigFacialActionUnitType.AU_04_R,
    SERigEnum.eRigFacialActionUnitType.AU_05_L,
    SERigEnum.eRigFacialActionUnitType.AU_05_R,
    SERigEnum.eRigFacialActionUnitType.AU_06_L,
    SERigEnum.eRigFacialActionUnitType.AU_06_R,
    SERigEnum.eRigFacialActionUnitType.AU_07_L,
    SERigEnum.eRigFacialActionUnitType.AU_07_R,
    SERigEnum.eRigFacialActionUnitType.AU_09_L,
    SERigEnum.eRigFacialActionUnitType.AU_09_R,
    SERigEnum.eRigFacialActionUnitType.AU_10_L,
    SERigEnum.eRigFacialActionUnitType.AU_10_R,
    SERigEnum.eRigFacialActionUnitType.AU_11_L,
    SERigEnum.eRigFacialActionUnitType.AU_11_R,
    SERigEnum.eRigFacialActionUnitType.AU_12_L,
    SERigEnum.eRigFacialActionUnitType.AU_12_R,
    SERigEnum.eRigFacialActionUnitType.AU_12_OL,
    SERigEnum.eRigFacialActionUnitType.AU_12_OR,
    SERigEnum.eRigFacialActionUnitType.AU_12_Blink_L,
    SERigEnum.eRigFacialActionUnitType.AU_12_Blink_R,
    SERigEnum.eRigFacialActionUnitType.AU_13_L,
    SERigEnum.eRigFacialActionUnitType.AU_13_R,
    SERigEnum.eRigFacialActionUnitType.AU_14_L,
    SERigEnum.eRigFacialActionUnitType.AU_14_R,
    SERigEnum.eRigFacialActionUnitType.AU_15_L,
    SERigEnum.eRigFacialActionUnitType.AU_15_R,
    SERigEnum.eRigFacialActionUnitType.AU_16_L,
    SERigEnum.eRigFacialActionUnitType.AU_16_R,
    SERigEnum.eRigFacialActionUnitType.AU_17_D,
    SERigEnum.eRigFacialActionUnitType.AU_17_U,
    SERigEnum.eRigFacialActionUnitType.AU_18_L,
    SERigEnum.eRigFacialActionUnitType.AU_18_R,
    SERigEnum.eRigFacialActionUnitType.AU_20_L,
    SERigEnum.eRigFacialActionUnitType.AU_20_R,
    SERigEnum.eRigFacialActionUnitType.AU_20_NL,
    SERigEnum.eRigFacialActionUnitType.AU_20_NR,
    SERigEnum.eRigFacialActionUnitType.AU_22_D,
    SERigEnum.eRigFacialActionUnitType.AU_22_U,
    SERigEnum.eRigFacialActionUnitType.AU_23_D,
    SERigEnum.eRigFacialActionUnitType.AU_23_U,
    SERigEnum.eRigFacialActionUnitType.AU_24,
    SERigEnum.eRigFacialActionUnitType.AU_25_D,
    SERigEnum.eRigFacialActionUnitType.AU_25_U,
    SERigEnum.eRigFacialActionUnitType.AU_26_Fix,
    SERigEnum.eRigFacialActionUnitType.AU_26_CloseFix,
    SERigEnum.eRigFacialActionUnitType.AU_28_D,
    SERigEnum.eRigFacialActionUnitType.AU_28_U,
    SERigEnum.eRigFacialActionUnitType.AU_Puff_L,
    SERigEnum.eRigFacialActionUnitType.AU_Puff_R,
    SERigEnum.eRigFacialActionUnitType.AU_Shrink_L,
    SERigEnum.eRigFacialActionUnitType.AU_Shrink_R,
    SERigEnum.eRigFacialActionUnitType.AU_Blink_L,
    SERigEnum.eRigFacialActionUnitType.AU_Blink_R,
    SERigEnum.eRigFacialActionUnitType.AU_Throat,
    SERigEnum.eRigFacialActionUnitType.AU_JawForward,
    SERigEnum.eRigFacialActionUnitType.AU_LipClose,
    SERigEnum.eRigFacialActionUnitType.AU_LowLipCompress,
    SERigEnum.eRigFacialActionUnitType.AU_UpLipCompress,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookLeft,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookRight,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookUp,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookDown,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookLeft,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookRight,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookUp,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookDown,
    SERigEnum.eRigFacialActionUnitType.AU_10_OL,
    SERigEnum.eRigFacialActionUnitType.AU_10_OR,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookLeft_Blink,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookRight_Blink,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookUp_Blink,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_L_LookDown_Blink,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookLeft_Blink,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookRight_Blink,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookUp_Blink,
    SERigEnum.eRigFacialActionUnitType.AU_Eye_R_LookDown_Blink
]

dataBufferAUsToBlendshapeAUsTable = {}
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_01_L_Attr]         = 'AU_01_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_01_R_Attr]         = 'AU_01_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_02_L_Attr]         = 'AU_02_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_02_R_Attr]         = 'AU_02_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_04_L_Attr]         = 'AU_04_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_04_R_Attr]         = 'AU_04_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_05_L_Attr]         = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_05_R_Attr]         = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_06_L_Attr]         = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_06_R_Attr]         = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_07_L_Attr]         = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_07_R_Attr]         = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_09_L_Attr]         = 'AU_09_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_09_R_Attr]         = 'AU_09_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_10_L_Attr]         = 'AU_10_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_10_R_Attr]         = 'AU_10_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_11_L_Attr]         = 'AU_11_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_11_R_Attr]         = 'AU_11_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_12_L_Attr]         = 'AU_12_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_12_R_Attr]         = 'AU_12_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_12_OL_Attr]        = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_12_OR_Attr]        = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_12_Blink_L_Attr]   = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_12_Blink_R_Attr]   = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_13_L_Attr]         = 'AU_13_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_13_R_Attr]         = 'AU_13_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_14_L_Attr]         = 'AU_14_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_14_R_Attr]         = 'AU_14_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_15_L_Attr]         = 'AU_15_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_15_R_Attr]         = 'AU_15_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_16_L_Attr]         = 'AU_16_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_16_R_Attr]         = 'AU_16_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_17_D_Attr]         = 'AU_17_D'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_17_U_Attr]         = 'AU_17_U'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_18_L_Attr]         = 'AU_18_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_18_R_Attr]         = 'AU_18_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_20_L_Attr]         = 'AU_20_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_20_R_Attr]         = 'AU_20_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_20_NL_Attr]        = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_20_NR_Attr]        = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_22_D_Attr]         = 'AU_22_D'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_22_U_Attr]         = 'AU_22_U'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_23_D_Attr]         = 'AU_23_D'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_23_U_Attr]         = 'AU_23_U'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_24_Attr]           = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_25_D_Attr]         = 'AU_25_D'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_25_U_Attr]         = 'AU_25_U'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_26_Fix_Attr]       = 'AU_26_Fix'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_26_CloseFix_Attr]  = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_28_D_Attr]         = 'AU_28_D'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_28_U_Attr]         = 'AU_28_U'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Puff_L_Attr]       = 'AU_Puff_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Puff_R_Attr]       = 'AU_Puff_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Shrink_L_Attr]     = 'AU_Shrink_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Shrink_R_Attr]     = 'AU_Shrink_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Blink_L_Attr]      = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Blink_R_Attr]      = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Throat_Attr]       = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_JawForward_Attr]   = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_LipClose_Attr]         = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_LowLipCompress_Attr]   = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_UpLipCompress_Attr]    = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_L_LookLeft_Attr]   = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_L_LookRight_Attr]  = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_L_LookUp_Attr]     = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_L_LookDown_Attr]   = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_R_LookLeft_Attr]   = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_R_LookRight_Attr]  = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_R_LookUp_Attr]     = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_R_LookDown_Attr]   = ''
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_10_OL_Attr]            = 'AU_10_OL'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_10_OR_Attr]            = 'AU_10_OR'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_L_LookLeft_Blink_Attr]    = 'AU_EyeLookLeftBlink_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_L_LookRight_Blink_Attr]   = 'AU_EyeLookRightBlink_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_L_LookUp_Blink_Attr]      = 'AU_EyeLookUpBlink_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_L_LookDown_Blink_Attr]    = 'AU_EyeLookDownBlink_L'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_R_LookLeft_Blink_Attr]    = 'AU_EyeLookLeftBlink_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_R_LookRight_Blink_Attr]   = 'AU_EyeLookRightBlink_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_R_LookUp_Blink_Attr]      = 'AU_EyeLookUpBlink_R'
dataBufferAUsToBlendshapeAUsTable[SERigNaming.sAU_Eye_R_LookDown_Blink_Attr]    = 'AU_EyeLookDownBlink_R'


AUsAliasTable = {}
AUsAliasTable[SERigNaming.sAU_01_L_Attr]         = 'Inner Brow Raise_L'
AUsAliasTable[SERigNaming.sAU_01_R_Attr]         = 'Inner Brow Raise_L'
AUsAliasTable[SERigNaming.sAU_02_L_Attr]         = 'Outer Brow Raiser_L'
AUsAliasTable[SERigNaming.sAU_02_R_Attr]         = 'Outer Brow Raiser_R'
AUsAliasTable[SERigNaming.sAU_04_L_Attr]         = 'Brow Lowerer_L'
AUsAliasTable[SERigNaming.sAU_04_R_Attr]         = 'Brow Lowerer_R'
AUsAliasTable[SERigNaming.sAU_05_L_Attr]         = 'Upper Lid Raiser_L'
AUsAliasTable[SERigNaming.sAU_05_R_Attr]         = 'Upper Lid Raiser_R'
AUsAliasTable[SERigNaming.sAU_06_L_Attr]         = 'Cheek Raiser_L'
AUsAliasTable[SERigNaming.sAU_06_R_Attr]         = 'Cheek Raiser_R'
AUsAliasTable[SERigNaming.sAU_07_L_Attr]         = 'Lid Tightener_L'
AUsAliasTable[SERigNaming.sAU_07_R_Attr]         = 'Lid Tightener_R'
AUsAliasTable[SERigNaming.sAU_09_L_Attr]         = 'Nose Wrinkler_L'
AUsAliasTable[SERigNaming.sAU_09_R_Attr]         = 'Nose Wrinkler_R'
AUsAliasTable[SERigNaming.sAU_10_L_Attr]         = 'Upper Lip Raiser_L'
AUsAliasTable[SERigNaming.sAU_10_R_Attr]         = 'Upper Lip Raiser_R'
AUsAliasTable[SERigNaming.sAU_11_L_Attr]         = 'Nasolabial Deepener_L'
AUsAliasTable[SERigNaming.sAU_11_R_Attr]         = 'Nasolabial Deepener_R'
AUsAliasTable[SERigNaming.sAU_12_L_Attr]         = 'Lip Corner Puller_L'
AUsAliasTable[SERigNaming.sAU_12_R_Attr]         = 'Lip Corner Puller_R'
AUsAliasTable[SERigNaming.sAU_12_OL_Attr]        = ''
AUsAliasTable[SERigNaming.sAU_12_OR_Attr]        = ''
AUsAliasTable[SERigNaming.sAU_12_Blink_L_Attr]   = ''
AUsAliasTable[SERigNaming.sAU_12_Blink_R_Attr]   = ''
AUsAliasTable[SERigNaming.sAU_13_L_Attr]         = 'Cheek Puffer_L'
AUsAliasTable[SERigNaming.sAU_13_R_Attr]         = 'Cheek Puffer_R'
AUsAliasTable[SERigNaming.sAU_14_L_Attr]         = 'Dimpler_L'
AUsAliasTable[SERigNaming.sAU_14_R_Attr]         = 'Dimpler_R'
AUsAliasTable[SERigNaming.sAU_15_L_Attr]         = 'Lip Corner Depressor_L'
AUsAliasTable[SERigNaming.sAU_15_R_Attr]         = 'Lip Corner Depressor_R'
AUsAliasTable[SERigNaming.sAU_16_L_Attr]         = 'Lower Lip Depressor_L'
AUsAliasTable[SERigNaming.sAU_16_R_Attr]         = 'Lower Lip Depressor_R'
AUsAliasTable[SERigNaming.sAU_17_D_Attr]         = 'Chin Raiser_D'
AUsAliasTable[SERigNaming.sAU_17_U_Attr]         = 'Chin Raiser_U'
AUsAliasTable[SERigNaming.sAU_18_L_Attr]         = 'Lip Pucker_L'
AUsAliasTable[SERigNaming.sAU_18_R_Attr]         = 'Lip Pucker_R'
AUsAliasTable[SERigNaming.sAU_20_L_Attr]         = 'Lip Stretcher_L'
AUsAliasTable[SERigNaming.sAU_20_R_Attr]         = 'Lip Stretcher_R'
AUsAliasTable[SERigNaming.sAU_20_NL_Attr]        = ''
AUsAliasTable[SERigNaming.sAU_20_NR_Attr]        = ''
AUsAliasTable[SERigNaming.sAU_22_D_Attr]         = ''
AUsAliasTable[SERigNaming.sAU_22_U_Attr]         = ''
AUsAliasTable[SERigNaming.sAU_23_D_Attr]         = 'Lip Tightener_D'
AUsAliasTable[SERigNaming.sAU_23_U_Attr]         = 'Lip Tightener_U'
AUsAliasTable[SERigNaming.sAU_24_Attr]           = 'Lip Pressor'
AUsAliasTable[SERigNaming.sAU_25_D_Attr]         = 'Lips Part_D'
AUsAliasTable[SERigNaming.sAU_25_U_Attr]         = 'Lips Part_U'
AUsAliasTable[SERigNaming.sAU_26_Fix_Attr]       = 'Jaw drop_Fix'
AUsAliasTable[SERigNaming.sAU_26_CloseFix_Attr]  = 'Jaw drop_CloseFix'
AUsAliasTable[SERigNaming.sAU_28_D_Attr]         = ''
AUsAliasTable[SERigNaming.sAU_28_U_Attr]         = ''
AUsAliasTable[SERigNaming.sAU_Puff_L_Attr]       = 'Puff_L'
AUsAliasTable[SERigNaming.sAU_Puff_R_Attr]       = 'Puff_R'
AUsAliasTable[SERigNaming.sAU_Shrink_L_Attr]     = 'Shrink_L'
AUsAliasTable[SERigNaming.sAU_Shrink_R_Attr]     = 'Shrink_R'
AUsAliasTable[SERigNaming.sAU_Blink_L_Attr]      = 'Blink_L'
AUsAliasTable[SERigNaming.sAU_Blink_R_Attr]      = 'Blink_R'
AUsAliasTable[SERigNaming.sAU_Throat_Attr]       = 'Throat'
AUsAliasTable[SERigNaming.sAU_JawForward_Attr]   = 'JawForward'
AUsAliasTable[SERigNaming.sAU_LipClose_Attr]         = 'LipClose'
AUsAliasTable[SERigNaming.sAU_LowLipCompress_Attr]   = 'LowLipCompress'
AUsAliasTable[SERigNaming.sAU_UpLipCompress_Attr]    = 'UpLipCompress'
AUsAliasTable[SERigNaming.sAU_Eye_L_LookLeft_Attr]   = 'Eye LookLeft_L'
AUsAliasTable[SERigNaming.sAU_Eye_L_LookRight_Attr]  = 'Eye LookRight_L'
AUsAliasTable[SERigNaming.sAU_Eye_L_LookUp_Attr]     = 'Eye LookUp_L'
AUsAliasTable[SERigNaming.sAU_Eye_L_LookDown_Attr]   = 'Eye LookDown_L'
AUsAliasTable[SERigNaming.sAU_Eye_R_LookLeft_Attr]   = 'Eye LookLeft_R'
AUsAliasTable[SERigNaming.sAU_Eye_R_LookRight_Attr]  = 'Eye LookRight_R'
AUsAliasTable[SERigNaming.sAU_Eye_R_LookUp_Attr]     = 'Eye LookUp_R'
AUsAliasTable[SERigNaming.sAU_Eye_R_LookDown_Attr]   = 'Eye LookDown_R'
AUsAliasTable[SERigNaming.sAU_10_OL_Attr]            = ''
AUsAliasTable[SERigNaming.sAU_10_OR_Attr]            = ''
AUsAliasTable[SERigNaming.sAU_Eye_L_LookLeft_Blink_Attr]    = 'Eye LookLeftBlink_L'
AUsAliasTable[SERigNaming.sAU_Eye_L_LookRight_Blink_Attr]   = 'Eye LookRightBlink_L'
AUsAliasTable[SERigNaming.sAU_Eye_L_LookUp_Blink_Attr]      = 'Eye LookUpBlink_L'
AUsAliasTable[SERigNaming.sAU_Eye_L_LookDown_Blink_Attr]    = 'Eye LookDownBlink_L'
AUsAliasTable[SERigNaming.sAU_Eye_R_LookLeft_Blink_Attr]    = 'Eye LookLeftBlink_R'
AUsAliasTable[SERigNaming.sAU_Eye_R_LookRight_Blink_Attr]   = 'Eye LookRightBlink_R'
AUsAliasTable[SERigNaming.sAU_Eye_R_LookUp_Blink_Attr]      = 'Eye LookUpBlink_R'
AUsAliasTable[SERigNaming.sAU_Eye_R_LookDown_Blink_Attr]    = 'Eye LookDownBlink_R'
#-----------------------------------------------------------------------------
def getMeshVertexPosition(vtxName):
    # Get vertex number and object having that vertex
    testVtx = re.search('(?<=\[)(?P<vtxNum>[\d]+)(?=\])', str(vtxName))
    if testVtx:
        vtxNum = int(testVtx.group('vtxNum'))
        vtxObj = vtxName.split('.')[0]
    else:
        return

    # Get Api MDagPath for object
    activList = om.MSelectionList()
    activList.add(vtxObj)
    pathDg = om.MDagPath()
    activList.getDagPath(0, pathDg)

    # Iterate over all the mesh vertices and get position of required vtx
    mItVtx = om.MItMeshVertex(pathDg)
    vtxPos = []
    while not mItVtx.isDone():
        if mItVtx.index() == vtxNum:
            point = om.MPoint()
            point = mItVtx.position(om.MSpace.kWorld)
            vtxPos = [round(point.x, 5), round(point.y, 5), round(point.z, 5)]
            break
        mItVtx.next()

    return vtxPos
#-----------------------------------------------------------------------------
def batchRemovePrefix():
    selected = cmds.ls(sl = 1)
    for i in selected:
        newName = SEStringHelper.SE_RemovePrefix(i)
        cmds.rename(i, newName)
#-----------------------------------------------------------------------------
def connectFACSDataBufferToAUBlendshape(connectionMap = None):
    selected = cmds.ls(sl = 1)
    if len(selected) != 2:
        cmds.warning('Please select AUBase mesh and FacialBase mesh.')
        return
        
    source = selected[0] 
    target = selected[1]

    auBlendshapeNode = getConnectedInputBlendshapeNode(source)
    rigCharacterGroup = SERigObjectTypeHelper.findRelatedRigCharacterGroup(target)
    facialComponent = SERigObjectTypeHelper.getCharacterFacialComponentGroup(rigCharacterGroup)
    facsDataBuffer = SEFacsHelper.getFACS_DataBuffer(facialComponent)
    auDataBuffer = SEFacsHelper.getFACS_AUBuffer(facialComponent)
    controlModeSwitch = SEFacsHelper.getFACS_ControlMode(facialComponent)

    #_connectFACSDataBufferToAUBlendshape(facsDataBuffer, auBlendshapeNode, connectionMap)
    _connectFACSControlModeSwitchToAUBlendShape(facsDataBuffer, auDataBuffer, controlModeSwitch, auBlendshapeNode, connectionMap)
#-----------------------------------------------------------------------------
def _connectFACSDataBufferToAUBlendshape(facsDataBuffer, auBlendshapeNode, connectionMap = None):
    if connectionMap == None:
        connectionMap = dataBufferAUsToBlendshapeAUsTable

    for auType in facialActionUnitTypeList:
        key = SERigNaming.auAttrList[auType]
        value = connectionMap[key]

        src = SEFacsHelper.getFacialActionUnitAttrName(facsDataBuffer, auType)        
        dst = getBlendshapTargetNameByMatchName(auBlendshapeNode, value, True)

        if src and dst:
            cmds.connectAttr(src, dst, f = 1)

def _connectFACSControlModeSwitchToAUBlendShape(facsDataBuffer, faceAUBuffer, controlModeSwitch, auBlendshapeNode, connectionMap = None):
    useDefault = False
    if connectionMap == None:
        connectionMap = dataBufferAUsToBlendshapeAUsTable
        useDefault = True
    
    if controlModeSwitch == None:
        cmds.warning('Fail to connect AU. Cannot find FACS Control Mode')
        return

    for auType in facialActionUnitTypeList:
        key = SERigNaming.auAttrList[auType]
        value = connectionMap[key]

        srcCtrlData = SEFacsHelper.getFacialActionUnitAttrName(facsDataBuffer, auType)   
        srcAUData =  SEFacsHelper.getFacialActionUnitAttrName(faceAUBuffer, auType)
        dst = getBlendshapTargetNameByMatchName(auBlendshapeNode, value, True)

        if srcCtrlData and srcAUData and dst:
            condition = cmds.createNode('condition', n = key + '_Condition')
            cmds.setAttr(condition + '.operation', 0)
            cmds.connectAttr(srcAUData, condition + '.colorIfTrueR', f = 1)
            cmds.connectAttr(srcCtrlData, condition + '.colorIfFalseR', f = 1)
            cmds.connectAttr(controlModeSwitch + '.' + SERigNaming.sFACS_ControlModeAttr, condition + '.firstTerm', f = 1)

            clampNode = cmds.createNode('clamp', n = key + '_Clamp')
            cmds.setAttr( clampNode + '.max', 1, 1, 1)
            cmds.setAttr( clampNode + '.min', 0, 0, 0)
            cmds.connectAttr(condition + '.outColorR', clampNode + '.inputR', f = 1)
            cmds.connectAttr(clampNode + '.outputR', dst, f = 1)
    
    if useDefault == True:
        cmds.setAttr(controlModeSwitch + '.' + SERigNaming.sFACS_IsUsingCustomMapAttr, False)
    else:
        cmds.setAttr(controlModeSwitch + '.' + SERigNaming.sFACS_IsUsingCustomMapAttr, True)
    
    SERigObjectTypeHelper.linkRigObjects(controlModeSwitch, auBlendshapeNode, SERigNaming.sFACS_AUConnectedAttr)    
#-----------------------------------------------------------------------------
def _matchSourceBlendshapesToTarget(source, target):
    if not cmds.objExists(source) or not cmds.objExists(target):
        return

    sourceInputTargets = []
    bs = getConnectedInputBlendshapeNode(source)
    if bs:
        sourceInputTargets = cmds.listConnections(bs + '.inputTarget')
    cmds.delete(source, ch = 1)

    # Reset source transformation.
    cmds.setAttr(source + '.tx', 0)
    cmds.setAttr(source + '.ty', 0)
    cmds.setAttr(source + '.tz', 0)

    # Temporally disable target deformation otherwise we cannot match the source and target correctly.
    for node in cmds.listHistory(target):
        if cmds.nodeType(node) == 'skinCluster' or cmds.nodeType(node) == 'blendShape':
            cmds.setAttr(node + '.envelope', 0.0)

    sourcePos = getMeshVertexPosition(source + '.vtx[0]')
    targetPos = getMeshVertexPosition(target + '.vtx[0]')
    dx = targetPos[0] - sourcePos[0]
    dy = targetPos[1] - sourcePos[1]
    dz = targetPos[2] - sourcePos[2]

    cmds.setAttr(source + '.tx', dx)
    cmds.setAttr(source + '.ty', dy)
    cmds.setAttr(source + '.tz', dz)
    cmds.makeIdentity(source, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

    # Update all the source input targets to match our target mesh and freeze them.
    for sourceInputTarget in sourceInputTargets:
        cmds.setAttr(sourceInputTarget + '.tx', dx)
        cmds.setAttr(sourceInputTarget + '.ty', dy)
        cmds.setAttr(sourceInputTarget + '.tz', dz)
        cmds.makeIdentity(sourceInputTarget, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

    # Recreate blendshape node.
    cmds.blendShape(sourceInputTargets, source)

    # Restore target deformation.
    for node in cmds.listHistory(target):
        if cmds.nodeType(node) == 'skinCluster' or cmds.nodeType(node) == 'blendShape':
            cmds.setAttr(node + '.envelope', 1.0)
    
    # Match the positions of vertices of source to target
    sourceVertsNum = cmds.polyEvaluate(source, v=True)
    targetVertsNum = cmds.polyEvaluate(target, v=True)
    pivotOffset = [0, 0, 0]
    if (sourceVertsNum == targetVertsNum):
        for i in range(sourceVertsNum):
            resTar = getMeshVertexPosition(target + '.vtx[%s]'%i)
            resSrc = getMeshVertexPosition(source + '.vtx[%s]'%i)
            srcPT = [round(resSrc[0], 5), round(resSrc[1], 5), round(resSrc[2], 5)]
            tarPT = [round(resTar[0], 5), round(resTar[1], 5), round(resTar[2], 5)]
            pivotOffset[0] = pivotOffset[0] + tarPT[0] - srcPT[0]
            pivotOffset[1] = pivotOffset[1] + tarPT[1] - srcPT[1]
            pivotOffset[2] = pivotOffset[2] + tarPT[2] - srcPT[2]
            cmds.xform(source + '.vtx[%s]'%i, t = tarPT , ws = True)  
        sourcePiv = cmds.xform (source, piv=True, q=True, ws=True)
        sourcePiv[0] = sourcePiv[0] + pivotOffset[0] / sourceVertsNum 
        sourcePiv[1] = sourcePiv[1] + pivotOffset[1] / sourceVertsNum 
        sourcePiv[2] = sourcePiv[2] + pivotOffset[2] / sourceVertsNum 
        cmds.xform( source, ws=True, piv=(sourcePiv[0], sourcePiv[1], sourcePiv[2]) )
#-----------------------------------------------------------------------------
def matchSourceBlendshapesToTarget():
    selected = cmds.ls(sl = 1)
    source = selected[0]
    target = selected[1]

    _matchSourceBlendshapesToTarget(source, target)
#-----------------------------------------------------------------------------
def createMirrorShapeAlongLocalAxis(sculptShape, baseShape, localAxis = 'x', newShape = ''):
    baseWrapped = cmds.duplicate(baseShape)[0]
    baseWrapper = cmds.duplicate(baseShape)[0]

    if localAxis == 'x' or localAxis == 'X':
        cmds.setAttr(baseWrapper + '.scaleX', -1)
    elif localAxis == 'y' or localAxis == 'Y':
        cmds.setAttr(baseWrapper + '.scaleY', -1)
    elif localAxis == 'z' or localAxis == 'Z':
        cmds.setAttr(baseWrapper + '.scaleZ', -1)
    else:
        cmds.error('Unknown mirror axis.')
        cmds.delete(baseWrapped, baseWrapper)
        return None

    tempBS = cmds.blendShape(sculptShape, baseWrapper)[0]

    cmds.select(cl = True)
    cmds.select(baseWrapped)
    cmds.select(baseWrapper, add = True)
    mel.eval('doWrapArgList "7" { "1", "0", "1", "2", "1", "1", "0", "0" }')
    cmds.select(cl = True)

    cmds.setAttr(tempBS + '.' + sculptShape, 1)

    res = cmds.duplicate(baseWrapped, name = newShape)[0]
    cmds.delete(baseWrapped, baseWrapper)

    # Delete junk shape orig data.
    junkName = res + 'ShapeOrig'
    if cmds.objExists(junkName):
        cmds.delete(junkName)

    return res
#-----------------------------------------------------------------------------
def findSymmetricalBlendshape(inputShape, pattern_R = 'R', pattern_r = 'r', pattern_L = 'L', pattern_l = 'l'):
    if not cmds.objExists(inputShape):
        cmds.warning('Input shape does not exist: ' + inputShape)
        return None

    shapeName = SEStringHelper.SE_RemoveSuffix(inputShape)
    suffix = SEStringHelper.getSuffix(inputShape)
    if suffix == None:
        cmds.warning('Suffix not found for input shape: ' + inputShape)
        return None

    if suffix == pattern_R or suffix == pattern_r:
        # Try to find left side shape and suffix pattern.
        shapeName_L = shapeName + '_' + pattern_L
        shapeName_l = shapeName + '_' + pattern_l

        symmetricalBS = None
        symmetricalPattern = None
        if cmds.objExists(shapeName_L):
            symmetricalBS = shapeName_L
            symmetricalPattern = pattern_L
        elif cmds.objExists(shapeName_l):
            symmetricalBS = shapeName_l
            symmetricalPattern = pattern_l
        else:
            cmds.warning('Symmetrical blend shape does not exist for input shape: ' + inputShape)

        return [symmetricalBS, symmetricalPattern, shapeName_L]

    elif suffix == pattern_L or suffix == pattern_l:
        # Try to find right side shape and suffix pattern.
        shapeName_R = shapeName + '_' + pattern_R
        shapeName_r = shapeName + '_' + pattern_r

        symmetricalBS = None
        symmetricalPattern = None
        if cmds.objExists(shapeName_R):
            symmetricalBS = shapeName_R
            symmetricalPattern = pattern_R
        elif cmds.objExists(shapeName_l):
            symmetricalBS = shapeName_r
            symmetricalPattern = pattern_r
        else:
            cmds.warning('Symmetrical blend shape does not exist for input shape: ' + inputShape)

        return [symmetricalBS, symmetricalPattern, shapeName_R]
    
    else:
        # Blendshape that matches symmetrical pattern not found.
        cmds.warning('Blendshape that matches symmetrical pattern not found for input shape: ' + inputShape)
        return None 
#-----------------------------------------------------------------------------
def getConnectedOutputBlendshapeNode(inputShape):
    # TODO:
    # Return the first connection that is blendshape.
    blsNode = cmds.listConnections(inputShape + '.worldMesh[0]')
    if blsNode:
        blsNode = blsNode[0]

    return blsNode
#-----------------------------------------------------------------------------
def getConnectedInputBlendshapeNode(inputShape):
    # TODO:
    # Return the first connection that is blendshape.
    blsNode = cmds.listConnections(inputShape + '.inMesh')
    if blsNode:
        blsNode = blsNode[0]

    return blsNode
#-----------------------------------------------------------------------------
def getConnectedBaseShape(inputShape):
    bsNode = getConnectedOutputBlendshapeNode(inputShape)
    res = cmds.listConnections(bsNode + '.outputGeometry[0]')[0]
    return res
#-----------------------------------------------------------------------------
def getBlendshapTargetIndexByName(blsNode, targetName, matchExactly = True, tokenSeparator = '_'):
    attr = blsNode + '.w[{}]'
    weightCount = cmds.blendShape(blsNode, q = True, wc = True)
    for index in xrange(weightCount):
        if cmds.aliasAttr(attr.format(index), q = True) == targetName:
            return index
        aliasName = cmds.aliasAttr(attr.format(index), q = True)
        if matchExactly:
            if aliasName == targetName:
                return index
        else:
            match = True
            aliasNameTokens = aliasName.split(tokenSeparator)

            for aliasNameToken in aliasNameTokens:
                if targetName.find(aliasNameToken) == -1:
                    match = False
                    break
            if match:
                return index

    return -1
#-----------------------------------------------------------------------------
def getBlendshapTargetNameByMatchName(blsNode, matchName, matchExactly = True, tokenSeparator = '_'):
    attr = blsNode + '.w[{}]'
    weightCount = cmds.blendShape(blsNode, q = True, wc = True)
    for index in xrange(weightCount):
        aliasName = cmds.aliasAttr(attr.format(index), q = True)
        if matchExactly:
            if aliasName == matchName:
                return blsNode + '.' + aliasName
        else:
            match = True
            aliasNameTokens = aliasName.split(tokenSeparator)

            for aliasNameToken in aliasNameTokens:
                if matchName.find(aliasNameToken) == -1:
                    match = False
                    break
            if match:
                return blsNode + '.' + aliasName

    return None
#-----------------------------------------------------------------------------
def getConnectedShapeInverter(inputShape):
    shapeInverterNode = cmds.listConnections(inputShape + '.outMesh')
    if shapeInverterNode:
        shapeInverterNode = shapeInverterNode[0]
        nodeType = cmds.nodeType(shapeInverterNode)
        if nodeType == 'cvShapeInverter':
            return shapeInverterNode
    
    return None
#-----------------------------------------------------------------------------
def updateSymmetricalBlendshape(cleanBaseMesh, createIfNotFound = True, pattern_R = 'R', pattern_r = 'r', pattern_L = 'L', pattern_l = 'l'):
    """Update symmetrical blendshape mesh for current selected mesh.

    @param[in] cleanBaseMesh A clean base mesh which has no inputs or outputs.
    @param[in] createIfNotFound Whether or not create a new mesh if symmetrical mesh is not found.
    @param[in] pattern_R Right side suffix pattern for the mesh name.
    @param[in] pattern_r Right side suffix pattern for the mesh name.
    @param[in] pattern_L Left side suffix pattern for the mesh name.
    @param[in] pattern_l Left side suffix pattern for the mesh name.
    @return Nothing.
    """

    selected = cmds.ls(sl = 1)
    if len(selected) != 1:
        cmds.warning('Please select one blendshape mesh.')
        return
    selected = selected[0]
    parentGrp = cmds.listRelatives(selected, p = True)
    if parentGrp:
        parentGrp = parentGrp[0]

    findRes = findSymmetricalBlendshape(selected, pattern_R, pattern_r, pattern_L, pattern_l)
    if findRes == None:
        cmds.warning('Unable to update symmetrical blendshape.')
        return
    symmetricalBS = findRes[0]

    if symmetricalBS:
        # Symmetrical blendshape exists, update shape.        
        selectedClean = cmds.duplicate(selected, rr = True)[0]
        newMirrorShape = createMirrorShapeAlongLocalAxis(selectedClean, cleanBaseMesh, newShape = symmetricalBS)
        cmds.showHidden(newMirrorShape)
        
        # If symmetrical shape is connected to a blendshape node, then update the connection.
        connectedBlendshapeNodeAttr = cmds.listConnections(symmetricalBS + '.worldMesh[0]', plugs = 1)
        if connectedBlendshapeNodeAttr:
            connectedBlendshapeNodeAttr = connectedBlendshapeNodeAttr[0]
            cmds.disconnectAttr(symmetricalBS + '.worldMesh[0]', connectedBlendshapeNodeAttr)
            cmds.connectAttr(newMirrorShape + '.worldMesh[0]', connectedBlendshapeNodeAttr)

        # If symmetrical shape is connected to a shape inverter node, then update the connection.
        shapeInverterNode = getConnectedShapeInverter(symmetricalBS)
        if shapeInverterNode:
            cmds.disconnectAttr(symmetricalBS + '.outMesh', shapeInverterNode + '.correctiveMesh')
            cmds.connectAttr(newMirrorShape + '.outMesh', shapeInverterNode + '.correctiveMesh')

        tx = cmds.getAttr(symmetricalBS + '.tx')
        ty = cmds.getAttr(symmetricalBS + '.ty')
        tz = cmds.getAttr(symmetricalBS + '.tz')
        cmds.setAttr(newMirrorShape + '.tx', tx)
        cmds.setAttr(newMirrorShape + '.ty', ty)
        cmds.setAttr(newMirrorShape + '.tz', tz)
        
        cmds.delete(symmetricalBS)
        cmds.delete(selectedClean)
        cmds.rename(newMirrorShape, symmetricalBS)

        if parentGrp:
            symmetricalBSParentGrp = cmds.listRelatives(symmetricalBS, p = True)
            if symmetricalBSParentGrp:
                symmetricalBSParentGrp = symmetricalBSParentGrp[0]

            if parentGrp != symmetricalBSParentGrp:
                cmds.parent(symmetricalBS, parentGrp)
    else:
        # Symmetrical blendshape does not exist, possibly create a new shape.
        if createIfNotFound:
            print('Creating new symmetrical blendshape for: ' + selected)
            
            # Create new mirror shape.
            selectedClean = cmds.duplicate(selected, rr = True)[0]
            newMirrorShape = createMirrorShapeAlongLocalAxis(selectedClean, cleanBaseMesh, newShape = findRes[2])
            cmds.showHidden(newMirrorShape)
            cmds.delete(selectedClean)

            if parentGrp:
                newMirrorShapeParentGrp = cmds.listRelatives(newMirrorShape, p = True)
                if newMirrorShapeParentGrp:
                    newMirrorShapeParentGrp = newMirrorShapeParentGrp[0]

                if parentGrp != newMirrorShapeParentGrp:
                    cmds.parent(newMirrorShape, parentGrp)

            baseShape = getConnectedBaseShape(selected)
            blsNode = getConnectedOutputBlendshapeNode(selected)

            # Possibly add new mirror shape to the blendshape node.
            if blsNode:
                newTargetIndex = cmds.blendShape(blsNode, q = True, wc = True) + 1
                cmds.blendShape(baseShape, e = True, t = (baseShape, newTargetIndex, newMirrorShape, 1.0))

        else:
            print('No new symmetrical blendshape created for: ' + selected)
#-----------------------------------------------------------------------------
# Skin weights functions based on Tyler Thornock's tutorial:
# https://www.charactersetup.com/tutorial_skinWeights.html
#-----------------------------------------------------------------------------
def getSkinClusterWeights(shapeName):
    # Return joints' DAG partial path names and vertices' skin weights.
    # The weights are stored in dictionary, the key is the vertex Id, the value is another dictionary whose key is the joint id and 
    # value is the weight for that joint    
    clusterName = SEJointHelper.findRelatedSkinCluster(shapeName)
    if clusterName == None:
        cmds.warning('Skincluster not found for: ' + shapeName)        
        return None

    # Get the MFnSkinCluster for clusterName
    selList = om.MSelectionList()
    selList.add(clusterName)
    clusterNode = om.MObject()
    selList.getDependNode(0, clusterNode)
    skinFn = oma.MFnSkinCluster(clusterNode)

    # Get the MDagPath for all influence
    infDags = om.MDagPathArray()
    skinFn.influenceObjects(infDags)

    # Create a dictionary whose key is the MPlug indice id and whose value is the influence list id
    # Notice that the MPlug indice id MAY or MAY NOT equal to the influence list id, 
    # due to the fact that some influences may have been removed by the rigger(ex. There were 80 joints, 5 were removed from the skincluster), 
    # which lead to incontinuous MPlug indices. 
    infIndicesToIds = {}
    infIdsToIndices = {}
    infPartialPathNames = []
    for i in range(infDags.length()):
        infPartialPathName = infDags[i].partialPathName()
        infIndex = int(skinFn.indexForInfluenceObject(infDags[i]))

        infIndicesToIds[infIndex] = i
        infIdsToIndices[i] = infIndex
        infPartialPathNames.append(infPartialPathName)

    # Get the MPlug for the weightList and weights attributes
    weightListPlug = skinFn.findPlug('weightList')
    weightsPlug = skinFn.findPlug('weights')
    wlAttr = weightListPlug.attribute()
    wAttr = weightsPlug.attribute()
    vertexInfIndices = om.MIntArray()

    weights = {}
    for vertexId in range(weightListPlug.numElements()):
        vertexWeights = {}

        # Tell the weights attribute which vertex id it represents
        weightsPlug.selectAncestorLogicalIndex(vertexId, wlAttr)
        
        # Get the indices of all non-zero weights for this vertex
        weightsPlug.getExistingArrayAttributeIndices(vertexInfIndices)

        # Create a copy of the current weightsPlug
        infPlug = om.MPlug(weightsPlug)
        for infIndex in vertexInfIndices:
            # Tell the infPlug it represents the current influence id
            infPlug.selectAncestorLogicalIndex(infIndex, wAttr)
            
            # Add this influence and its weight to this verts weights
            try:
                # Get continuous influence ID.
                infId = infIndicesToIds[infIndex]
                vertexWeights[infId] = infPlug.asDouble()
            except KeyError:
                # Assumes a removed influence
                pass
                
        weights[vertexId] = vertexWeights

    return [infPartialPathNames, weights, infIndicesToIds, infIdsToIndices]
#-----------------------------------------------------------------------------
def setSkinClusterWeights(shapeName, weights, infIdsToIndices = None):
    clusterName = SEJointHelper.findRelatedSkinCluster(shapeName)
    if clusterName == None:
        cmds.warning('Skincluster not found for: ' + shapeName)
        return

    infJoints = cmds.skinCluster(clusterName, q = 1, inf = 1)

    # Unlock influences used by skincluster
    for inf in infJoints:
        cmds.setAttr('%s.liw' % inf, 0)

    # Normalize needs turned off for the prune to work
    skinNorm = cmds.getAttr('%s.normalizeWeights' % clusterName)
    if skinNorm != 0:
        cmds.setAttr('%s.normalizeWeights' % clusterName, 0)
    cmds.skinPercent(clusterName, shapeName, nrm = False, prw = 100)

    # Restore normalize setting
    if skinNorm != 0:
        cmds.setAttr('%s.normalizeWeights' % clusterName, skinNorm)

    if infIdsToIndices:
        for vertId, weightData in weights.items():
            wlAttr = '%s.weightList[%s]' % (clusterName, vertId)

            for infId, infValue in weightData.items():
                infIndex = infIdsToIndices[infId]
                wAttr = '.weights[%s]' % infIndex
                cmds.setAttr(wlAttr + wAttr, infValue)
    else:
         for vertId, weightData in weights.items():
            wlAttr = '%s.weightList[%s]' % (clusterName, vertId)

            for infId, infValue in weightData.items():
                wAttr = '.weights[%s]' % infId
                cmds.setAttr(wlAttr + wAttr, infValue)
#-----------------------------------------------------------------------------
def exportSkinClusterWeights(fileFolderPath, shapeName, maximumInfluences = 4):
    sc = SEJointHelper.findRelatedSkinCluster(shapeName)
    if sc == None:
        return

    scWeights = getSkinClusterWeights(shapeName)
    infJoints = scWeights[0]
    weights = scWeights[1]
    saveData = [maximumInfluences, infJoints, weights]

    fileName = fileFolderPath + '/' + shapeName + '.sew'
    try:
        f = open(fileName, 'wb')
        cPickle.dump(saveData, f)
        f.close()
    except:
        cmds.warning('Failed exporting skin weights for: ' + shapeName)
#-----------------------------------------------------------------------------
def importSkinClusterWeights(fileFolderPath, shapeName):
    sc = SEJointHelper.findRelatedSkinCluster(shapeName)

    loadData = []
    fileName = fileFolderPath + '/' + shapeName + '.sew'
    try:
        f = open(fileName, 'rb')
        loadData = cPickle.load(f)
        f.close()
    except:
        print('Skipped importing skin weights for: ' + shapeName)
        return

    maxInfluences = loadData[0]
    infJoints = loadData[1]
    weights = loadData[2]

    if sc != None:
        cmds.skinCluster(shapeName, e = True, ub = True)

    newSC = cmds.skinCluster(infJoints, shapeName, toSelectedBones = True, skinMethod = 0, normalizeWeights = 1, obeyMaxInfluences = 1, maximumInfluences = maxInfluences)[0]
    setSkinClusterWeights(shapeName, weights)
#-----------------------------------------------------------------------------
def batchExportSkinClusterWeights():
    rigCharacterGroup = SEJointHelper.getSelectedRigCharacterGroup()
    if rigCharacterGroup == None:
        return

    fileResult = cmds.fileDialog2(fm = 3)
    if fileResult != None:
        modelGroup = SERigObjectTypeHelper.getCharacterModelGroup(rigCharacterGroup)
        if modelGroup:
            cmds.select(modelGroup)
            shapeNames = cmds.filterExpand(sm = [12])
            cmds.select(rigCharacterGroup)

            for shapeName in shapeNames:
                exportSkinClusterWeights(fileResult[0], shapeName)

            print('Batching export skincluster weighhts finished for: ' + rigCharacterGroup)
        else:
            cmds.warning('Model group not found. Batching export skincluster weighhts failed for:' + rigCharacterGroup)
#-----------------------------------------------------------------------------
def batchImportSkinClusterWeights():
    rigCharacterGroup = SEJointHelper.getSelectedRigCharacterGroup()
    if rigCharacterGroup == None:
        return

    fileResult = cmds.fileDialog2(fm = 3)
    if fileResult != None:
        modelGroup = SERigObjectTypeHelper.getCharacterModelGroup(rigCharacterGroup)
        if modelGroup:
            cmds.select(modelGroup)
            shapeNames = cmds.filterExpand(sm = [12])
            cmds.select(rigCharacterGroup)

            totalProgress = len(shapeNames)
            curProgress = 0
            cmds.progressWindow(title = 'Batching import skincluster weights', progress = 0,max = totalProgress, status = 'Importing skincluster weights for: ', isInterruptable = True)

            for shapeName in shapeNames:
                importSkinClusterWeights(fileResult[0], shapeName)
                cmds.progressWindow(edit = True, progress = curProgress, status = ('Importing skincluster weights for: %s' % shapeName))
                curProgress += 1

            cmds.progressWindow(endProgress = True)
            print('Batching import skincluster weighhts finished for: ' + rigCharacterGroup)
        else:
            cmds.warning('Model group not found. Batching import skincluster weighhts failed for:' + rigCharacterGroup)
#-----------------------------------------------------------------------------
def exportCustomConnectMap(fileNamePath, customMapTable):
    saveData = customMapTable
    fileName = fileNamePath + '.seccm'
        
    try:
        f = open(fileName, 'wb')
        cPickle.dump(saveData, f)
        f.close()
    except Exception as e:
        print e
        cmds.warning('Failed exporting custom connect map.')
#-----------------------------------------------------------------------------
def importCustomConnectMap(fileNamePath):
    loadData = []
    fileName = fileNamePath
    try:
        f = open(fileName, 'rb')
        loadData = cPickle.load(f)
        f.close()
    except:
        print('Skipped importing Custom Connect Map.')
        return

    return loadData