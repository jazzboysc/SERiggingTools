from ..Base.SERigControl import RigControl
from ..Base.SERigComponent import RigComponent
from ..Base.SERigBase import RigBase
from ..Base import SERigNaming
from ..Base import SERigEnum
from ..Rig import SERigSpineComponent
from ..Rig import SERigBipedLimbComponent
from . import SECharacterDeform

import maya.cmds as cmds

sceneScale = 1.0

modelFilePath = '%s/%s/Model/%s_Model.ma'
builderFilePath = '%s/%s/Builder/%s_Builder.ma'

rootJnt = 'Root'
headJnt = 'C_Head'

def build(
          characterName, 
          mainProjectPath = '', 
          upperBodyUpperLimbKnobCount = 2, 
          upperBodyLowerLimbKnobCount = 2,
          lowerBodyUpperLimbKnobCount = 2,
          lowerBodyLowerLimbKnobCount = 1,
          mainCtrlOffset = 30,
          spineIKTwist = 180.0
          ):
    # Create new scene
    #cmds.file(new = True, f = True)

    # Import model.
    modelFile = modelFilePath % (mainProjectPath, characterName, characterName)
    cmds.file(modelFile, i = 1)

    # Import builder scene.
    builderFile = builderFilePath % (mainProjectPath, characterName, characterName)
    cmds.file(builderFile, i = 1)

    # Create rig base.
    baseRig = RigBase(characterName = characterName, 
                      scale = sceneScale, mainCtrlAttachObject = headJnt, 
                      mainCtrlOffset = mainCtrlOffset)

    # Parent the imported model to the rig base.
    modelGrp = ('%s' + SERigNaming.s_ModelGroup) % characterName
    cmds.parent(modelGrp, baseRig.ModelGrp)

    # Parent the imported skeleton to the rig base.
    cmds.parent(rootJnt, baseRig.JointsGrp)

    # Create rig components.
    createRigComponents(baseRig, spineIKTwist)

    # Setup model deformation.
    upperBodyUpperLimbJoints = ['L_Shoulder', 'R_Shoulder']
    upperBodyLowerLimbJoints = ['L_Elbow', 'R_Elbow']
    lowerBodyUpperLimbJoints = ['L_Hip', 'R_Hip']
    lowerBodyLowerLimbJoints = ['L_Knee', 'R_Knee']

    SECharacterDeform.build(baseRig, mainProjectPath, sceneScale, 
                            False,
                            False,
                            '',
                            False,
                            [],
                            '',
                            upperBodyUpperLimbKnobCount, 
                            upperBodyLowerLimbKnobCount, 
                            lowerBodyUpperLimbKnobCount, 
                            lowerBodyLowerLimbKnobCount, 
                            upperBodyUpperLimbJoints, 
                            upperBodyLowerLimbJoints, 
                            lowerBodyUpperLimbJoints, 
                            lowerBodyLowerLimbJoints)

    cmds.select(cl=1)

    return baseRig


def createRigComponents(baseRig, spineIKTwist):
    # Spine
    spineJnts = ['C_Pelvis', 'C_Spine_0', 'C_Spine_1', 'C_Spine_2', 'C_Spine_3', 'C_ChestBegin']
    spine = SERigSpineComponent.RigSimpleIKSpine(prefix = 'C_Spine', baseRig = baseRig, 
                                                 rigSide = SERigEnum.eRigSide.RS_Center, 
                                                 rigType = SERigEnum.eRigType.RT_Component)
    spine.build(
                spineJoints = spineJnts,
                rootJoint = rootJnt,
                bodyLocator = 'locator_Body',
                chestLocator = 'locator_Chest',
                pelvisLocator = 'locator_Pelvis',
                rigScale = sceneScale
                )

    # Left Leg
    leftLeg = SERigBipedLimbComponent.RigHumanLeg(prefix = 'L_Leg', baseRig = baseRig,
                                                  rigSide = SERigEnum.eRigSide.RS_Left, 
                                                  rigType = SERigEnum.eRigType.RT_Component)
    leftLegJnts = ['L_Hip', 'L_Knee', 'L_Ankle', 'L_Ball', 'L_Toe']
    leftFootHelperJoints = SERigBipedLimbComponent.RigHumanLeg.buildFootHelperJointsMapForLeftSide(
                                                                                                    legJoints = leftLegJnts,
                                                                                                    footExtLocator = 'locator_L_Foot_Ext',
                                                                                                    footIntLocator = 'locator_L_Foot_Int',
                                                                                                    footBaseLocator = 'locator_L_Foot_Base',
                                                                                                    footBaseSwiveLocator = 'locator_L_Foot_BaseSwive',
                                                                                                    footToeSwiveLocator = 'locator_L_Foot_ToeSwive',
                                                                                                    )
    leftLeg.build(
            legJoints = leftLegJnts,
            footHelperJoints = leftFootHelperJoints,
            legPVLocator = 'locator_L_LegPV',
            rigScale = sceneScale
            )

    # Right Leg
    rightLeg = SERigBipedLimbComponent.RigHumanLeg(prefix = 'R_Leg', baseRig = baseRig,
                                                   rigSide = SERigEnum.eRigSide.RS_Right, 
                                                   rigType = SERigEnum.eRigType.RT_Component)
    rightLegJnts = ['R_Hip', 'R_Knee', 'R_Ankle', 'R_Ball', 'R_Toe']
    rightFootHelperJoints = SERigBipedLimbComponent.RigHumanLeg.mirrorFootHelperJointsMapForRightSide(leftFootHelperJoints)
    rightLeg.build(
            legJoints = rightLegJnts,
            footHelperJoints = rightFootHelperJoints,
            legPVLocator = 'locator_R_LegPV',
            rigScale = sceneScale
            )