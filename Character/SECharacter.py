from ..Base.SERigControl import RigControl
from ..Base.SERigComponent import RigComponent
from ..Base.SERigBase import RigBase
from ..Base import SERigNaming
from ..Base import SERigEnum
from ..Rig import SERigSpineComponent
from ..Rig import SERigBipedLimbComponent
from ..Rig import SERigBipedNeckComponent
from . import SECharacterDeform

import maya.cmds as cmds

sceneScale = 1.0

modelFilePath = '%s/%s/Model/%s_Model.ma'
builderFilePath = '%s/%s/Builder/%s_Builder.ma'

rootJnt = 'Root'
headJnt = 'C_Head'
gLeftArm = None
gRightArm = None
gLeftLeg = None
gRightLeg = None

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

def leftArmSyncIKToFK():

    global gLeftArm
    if gLeftArm != None:
        gLeftArm.syncIKToFK()
    else:
        print('gLeftArm is None')

def rightArmSyncIKToFK():

    global gRightArm
    if gRightArm != None:
        gRightArm.syncIKToFK()
    else:
        print('gRightArm is None')

def leftArmSyncFKToIK():

    global gLeftArm
    if gLeftArm != None:
        gLeftArm.syncFKToIK()
    else:
        print('gLeftArm is None')

def rightArmSyncFKToIK():

    global gRightArm
    if gRightArm != None:
        gRightArm.syncFKToIK()
    else:
        print('gRightArm is None')

def leftLegSyncIKToFK():

    global gLeftLeg
    if gLeftLeg != None:
        gLeftLeg.syncIKToFK()
    else:
        print('gLeftLeg is None')

def leftLegSyncFKToIK():

    global gLeftLeg
    if gLeftLeg != None:
        gLeftLeg.syncFKToIK()
    else:
        print('gLeftLeg is None')

def rightLegSyncIKToFK():

    global gRightLeg
    if gRightLeg != None:
        gRightLeg.syncIKToFK()
    else:
        print('gRightLeg is None')

def rightLegSyncFKToIK():

    global gRightLeg
    if gRightLeg != None:
        gRightLeg.syncFKToIK()
    else:
        print('gRightLeg is None')

def createRigComponents(baseRig, spineIKTwist):

    # Prepare joints.
    spineJnts = ['C_Pelvis', 'C_Spine_0', 'C_Spine_1', 'C_Spine_2', 'C_Spine_3', 'C_ChestBegin']

    leftLegJnts = ['L_Hip', 'L_Knee', 'L_Ankle', 'L_Ball', 'L_Toe']

    rightLegJnts = ['R_Hip', 'R_Knee', 'R_Ankle', 'R_Ball', 'R_Toe']

    leftFootHelperJoints = SERigBipedLimbComponent.RigHumanLeg.buildFootHelperJointsMapForLeftSide(legJoints = leftLegJnts,
        footExtLocator = 'locator_L_Foot_Ext', footIntLocator = 'locator_L_Foot_Int', footBaseLocator = 'locator_L_Foot_Base',
        footBaseSwiveLocator = 'locator_L_Foot_BaseSwive', footToeSwiveLocator = 'locator_L_Foot_ToeSwive')

    rightFootHelperJoints = SERigBipedLimbComponent.RigHumanLeg.mirrorFootHelperJointsMapForRightSide(leftFootHelperJoints)

    leftArmJnts = ['L_Shoulder', 'L_Elbow', 'L_Wrist']

    rightArmJnts = ['R_Shoulder', 'R_Elbow', 'R_Wrist']

    leftHandJnts = ['L_Thumb_0', 'L_Index_0', 'L_Middle_0', 'L_Ring_0', 'L_Pinky_0']

    rightHandJnts = ['R_Thumb_0', 'R_Index_0', 'R_Middle_0', 'R_Ring_0', 'R_Pinky_0']

    neckJnts = ['C_Neck_0', 'C_Neck_1', 'C_Head', 'C_FacialRoot']

    # Spine.
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

    # Left Leg.
    global gLeftLeg
    gLeftLeg = SERigBipedLimbComponent.RigHumanLeg(prefix = 'L_Leg', baseRig = baseRig,
                                                  rigSide = SERigEnum.eRigSide.RS_Left, 
                                                  rigType = SERigEnum.eRigType.RT_Component)
    gLeftLeg.build(
            legJoints = leftLegJnts,
            footHelperJoints = leftFootHelperJoints,
            legPVLocator = 'locator_L_LegPV',
            rigScale = sceneScale
            )

    # Right Leg.
    global gRightLeg
    gRightLeg = SERigBipedLimbComponent.RigHumanLeg(prefix = 'R_Leg', baseRig = baseRig,
                                                   rigSide = SERigEnum.eRigSide.RS_Right, 
                                                   rigType = SERigEnum.eRigType.RT_Component)
    gRightLeg.build(
            legJoints = rightLegJnts,
            footHelperJoints = rightFootHelperJoints,
            legPVLocator = 'locator_R_LegPV',
            rigScale = sceneScale
            )

    # Left arm.
    global gLeftArm
    gLeftArm = SERigBipedLimbComponent.RigHumanArm(prefix = 'L_Arm', baseRig = baseRig,
                                                  rigSide = SERigEnum.eRigSide.RS_Left, 
                                                  rigType = SERigEnum.eRigType.RT_Component)
    gLeftArm.build(
            armJoints = leftArmJnts,
            armPVLocator = 'locator_L_ArmPV',
            chestEndJoint = 'C_ChestEnd',
            rigScale = sceneScale
            )

    # Right arm.
    global gRightArm
    gRightArm = SERigBipedLimbComponent.RigHumanArm(prefix = 'R_Arm', baseRig = baseRig,
                                                  rigSide = SERigEnum.eRigSide.RS_Right, 
                                                  rigType = SERigEnum.eRigType.RT_Component)
    gRightArm.build(
            armJoints = rightArmJnts,
            armPVLocator = 'locator_R_ArmPV',
            chestEndJoint = 'C_ChestEnd',
            rigScale = sceneScale
            )

    # Left hand.
    leftHand = SERigBipedLimbComponent.RigHumanHand(prefix = 'L_Hand', baseRig = baseRig,
                                                  rigSide = SERigEnum.eRigSide.RS_Left, 
                                                  rigType = SERigEnum.eRigType.RT_Component)
    leftHand.build(
            fingers = leftHandJnts,
            armFKFingerAttachPoint = 'L_Wrist',
            rigScale = sceneScale
            )

    # Right hand.
    rightHand = SERigBipedLimbComponent.RigHumanHand(prefix = 'R_Hand', baseRig = baseRig,
                                                  rigSide = SERigEnum.eRigSide.RS_Right, 
                                                  rigType = SERigEnum.eRigType.RT_Component)
    rightHand.build(
            fingers = rightHandJnts,
            armFKFingerAttachPoint = 'R_Wrist',
            rigScale = sceneScale
            )

    # Neck.
    neck = SERigBipedNeckComponent.RigHumanNeck(prefix = 'C_Neck', baseRig = baseRig,
                                                  rigSide = SERigEnum.eRigSide.RS_Center, 
                                                  rigType = SERigEnum.eRigType.RT_Neck)
    neck.build(
            neckJoints = neckJnts,
            fkNeckAttachPoint = 'C_ChestEnd',
            rigScale = sceneScale
            )