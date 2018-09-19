from ..Base.SERigControl import RigControl
from ..Base.SERigComponent import RigComponent
from ..Base.SERigBase import RigBase
from ..Base import SERigNaming
from ..Base import SERigEnum
from ..Rig import SERigSpineComponent
from ..Rig import SERigBipedLimbComponent
from ..Rig import SERigBipedNeckComponent
from ..Utils import SERigObjectTypeHelper
from . import SECharacterDeform

import maya.cmds as cmds

sceneScale = 1.0

modelFilePath = '%s/%s/Model/%s_Model.ma'
builderFilePath = '%s/%s/Builder/%s_Builder.ma'

rootJnt = 'Root'
headJnt = 'C_Head'


#-----------------------------------------------------------------------------
# Rig Biped Character Base Class
# Sun Che
#-----------------------------------------------------------------------------
class RigBipedCharacter():
    def __init__(
                 self,
                 characterName
                 ):
        # Rig info.
        self.CharacterName = characterName

        # Rig components.
        self.BaseRig = None
        self.Spine = None
        self.LeftLeg = None
        self.RightLeg = None
        self.LeftArm = None
        self.RightArm = None
        self.LeftHand = None
        self.RightHand = None
        self.Neck = None

        # Rig deformation system.
        self.RigDeform = SECharacterDeform.RigBipedCharacterDeform(self)

    def build(
              self,
              mainProjectPath = '', 
              upperBodyUpperLimbKnobCount = 2, 
              upperBodyLowerLimbKnobCount = 2,
              lowerBodyUpperLimbKnobCount = 2,
              lowerBodyLowerLimbKnobCount = 1,
              mainCtrlOffset = 30,
              fkLegControlScaleYZ = 19,
              fkLegControlScaleYZMultiplier = 0.75,
              fkLegControlTransparency = 0.85,
              ballIKTwistLeft = 90,
              ballIKTwistRight = 270,
              toeIKTwistLeft = 90,
              toeIKTwistRight = 0,
              fkArmControlScaleYZ = 10,
              fkArmControlScaleYZMultiplier = 0.9,
              fkArmControlTransparency = 0.85
              ):

        # Import model.
        modelFile = modelFilePath % (mainProjectPath, self.CharacterName, self.CharacterName)
        print('Importing model file: ' + modelFile)
        cmds.file(modelFile, i = 1)

        # Import builder scene.
        builderFile = builderFilePath % (mainProjectPath, self.CharacterName, self.CharacterName)
        print('Importing builder file: ' + builderFile)
        cmds.file(builderFile, i = 1)

        # Create rig base.
        baseRig = RigBase(characterName = self.CharacterName, 
                          scale = sceneScale, mainCtrlAttachObject = headJnt, 
                          mainCtrlOffset = mainCtrlOffset)
        self.BaseRig = baseRig

        # Create character type node.
        SERigObjectTypeHelper.createRigObjectTypeAttr(self.BaseRig.TopGrp, 'RigCharacterType')

        # Parent the imported model to the rig base.
        modelGrp = ('%s' + SERigNaming.s_ModelGroup) % self.CharacterName
        cmds.parent(modelGrp, baseRig.ModelGrp)

        # Parent the imported skeleton to the rig base.
        cmds.parent(rootJnt, baseRig.JointsGrp)

        # Prepare joints.
        spineJnts = ['C_Pelvis', 'C_Spine_0', 'C_Spine_1', 'C_Spine_2', 'C_Spine_3', 'C_ChestBegin']

        upperChestJnts = ['L_Clav', 'R_Clav', 'C_ChestEnd', 'L_Breast', 'R_Breast']

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

        facialJnts = ['L_Eye', 'R_Eye', 'C_UpperTeeth', 'L_EyelidUpper', 'L_EyelidLower', 'R_EyelidUpper', 
                      'R_EyelidLower', 'C_Jaw', 'C_JawEnd', 'C_LowerTeeth']

        # Create rig components.
        self._createRigComponents( 
                                spineJnts,
                                leftLegJnts,
                                rightLegJnts,
                                leftFootHelperJoints,
                                rightFootHelperJoints,
                                leftArmJnts,
                                rightArmJnts,
                                leftHandJnts,
                                rightHandJnts,
                                neckJnts,
                                fkLegControlScaleYZ,
                                fkLegControlScaleYZMultiplier,
                                fkLegControlTransparency,
                                ballIKTwistLeft,
                                ballIKTwistRight,
                                toeIKTwistLeft,
                                toeIKTwistRight,
                                fkArmControlScaleYZ,
                                fkArmControlScaleYZMultiplier,
                                fkArmControlTransparency
                                )

        # Setup model deformation.

        upperBodyUpperLimbJoints = ['L_Shoulder', 'R_Shoulder']
        upperBodyLowerLimbJoints = ['L_Elbow', 'R_Elbow']
        lowerBodyUpperLimbJoints = ['L_Hip', 'R_Hip']
        lowerBodyLowerLimbJoints = ['L_Knee', 'R_Knee']

        if self.RigDeform:
            self.RigDeform.build(
                                baseRig, mainProjectPath, sceneScale, 
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
                                lowerBodyLowerLimbJoints,
                                spineJnts,
                                upperChestJnts,
                                leftLegJnts,
                                rightLegJnts,
                                leftFootHelperJoints,
                                rightFootHelperJoints,
                                leftArmJnts,
                                rightArmJnts,
                                leftHandJnts,
                                rightHandJnts,
                                neckJnts,
                                facialJnts,
                                rootJnt
                                )

        cmds.select(cl=1)


    def _createRigComponents(
                            self,
                            spineJnts, 
                            leftLegJnts, 
                            rightLegJnts, 
                            leftFootHelperJoints, 
                            rightFootHelperJoints,
                            leftArmJnts,
                            rightArmJnts,
                            leftHandJnts,
                            rightHandJnts,
                            neckJnts,
                            fkLegControlScaleYZ,
                            fkLegControlScaleYZMultiplier,
                            fkLegControlTransparency,
                            ballIKTwistLeft,
                            ballIKTwistRight,
                            toeIKTwistLeft,
                            toeIKTwistRight,
                            fkArmControlScaleYZ,
                            fkArmControlScaleYZMultiplier,
                            fkArmControlTransparency
                            ):

        # Spine.
        spine = SERigSpineComponent.RigSimpleIKSpine(prefix = 'C_Spine', baseRig = self.BaseRig, 
                                                     rigSide = SERigEnum.eRigSide.RS_Center, 
                                                     rigType = SERigEnum.eRigType.RT_SpineComponent)
        spine.build(
                    spineJoints = spineJnts,
                    rootJoint = rootJnt,
                    bodyLocator = 'locator_Body',
                    chestLocator = 'locator_Chest',
                    pelvisLocator = 'locator_Pelvis',
                    rigScale = sceneScale
                    )
        self.Spine = spine

        # Left Leg.
        leftLeg = SERigBipedLimbComponent.RigHumanLeg(prefix = 'L_Leg', baseRig = self.BaseRig,
                                                      rigSide = SERigEnum.eRigSide.RS_Left, 
                                                      rigType = SERigEnum.eRigType.RT_LegComponent)
        leftLeg.build(
                legJoints = leftLegJnts,
                footHelperJoints = leftFootHelperJoints,
                legPVLocator = 'locator_L_LegPV',
                rigScale = sceneScale,
                fkControlScaleYZ = fkLegControlScaleYZ,
                fkControlScaleYZMultiplier = fkLegControlScaleYZMultiplier,
                fkControlTransparency = fkLegControlTransparency,
                ballIKTwistLeft = ballIKTwistLeft,
                ballIKTwistRight = ballIKTwistRight,
                toeIKTwistLeft = toeIKTwistLeft,
                toeIKTwistRight = toeIKTwistRight
                )
        self.LeftLeg = leftLeg

        # Right Leg.
        rightLeg = SERigBipedLimbComponent.RigHumanLeg(prefix = 'R_Leg', baseRig = self.BaseRig,
                                                       rigSide = SERigEnum.eRigSide.RS_Right, 
                                                       rigType = SERigEnum.eRigType.RT_LegComponent)
        rightLeg.build(
                legJoints = rightLegJnts,
                footHelperJoints = rightFootHelperJoints,
                legPVLocator = 'locator_R_LegPV',
                rigScale = sceneScale,
                fkControlScaleYZ = fkLegControlScaleYZ,
                fkControlScaleYZMultiplier = fkLegControlScaleYZMultiplier,
                fkControlTransparency = fkLegControlTransparency,
                ballIKTwistLeft = ballIKTwistLeft,
                ballIKTwistRight = ballIKTwistRight,
                toeIKTwistLeft = toeIKTwistLeft,
                toeIKTwistRight = toeIKTwistRight
                )
        self.RightLeg = rightLeg

        # Left arm.
        leftArm = SERigBipedLimbComponent.RigHumanArm(prefix = 'L_Arm', baseRig = self.BaseRig,
                                                      rigSide = SERigEnum.eRigSide.RS_Left, 
                                                      rigType = SERigEnum.eRigType.RT_ArmComponent)
        leftArm.build(
                armJoints = leftArmJnts,
                armPVLocator = 'locator_L_ArmPV',
                chestEndJoint = 'C_ChestEnd',
                rigScale = sceneScale,
                fkControlScaleYZ = fkArmControlScaleYZ,
                fkControlScaleYZMultiplier = fkArmControlScaleYZMultiplier,
                fkControlTransparency = fkArmControlTransparency
                )
        self.LeftArm = leftArm

        # Right arm.
        rightArm = SERigBipedLimbComponent.RigHumanArm(prefix = 'R_Arm', baseRig = self.BaseRig,
                                                      rigSide = SERigEnum.eRigSide.RS_Right, 
                                                      rigType = SERigEnum.eRigType.RT_ArmComponent)
        rightArm.build(
                armJoints = rightArmJnts,
                armPVLocator = 'locator_R_ArmPV',
                chestEndJoint = 'C_ChestEnd',
                rigScale = sceneScale,
                fkControlScaleYZ = fkArmControlScaleYZ,
                fkControlScaleYZMultiplier = fkArmControlScaleYZMultiplier,
                fkControlTransparency = fkArmControlTransparency
                )
        self.RightArm = rightArm

        # Left hand.
        leftHand = SERigBipedLimbComponent.RigHumanHand(prefix = 'L_Hand', baseRig = self.BaseRig,
                                                      rigSide = SERigEnum.eRigSide.RS_Left, 
                                                      rigType = SERigEnum.eRigType.RT_HandComponent)
        leftHand.build(
                fingers = leftHandJnts,
                armFKFingerAttachPoint = 'L_Wrist',
                rigScale = sceneScale
                )
        self.LeftHand = leftHand

        # Right hand.
        rightHand = SERigBipedLimbComponent.RigHumanHand(prefix = 'R_Hand', baseRig = self.BaseRig,
                                                      rigSide = SERigEnum.eRigSide.RS_Right, 
                                                      rigType = SERigEnum.eRigType.RT_HandComponent)
        rightHand.build(
                fingers = rightHandJnts,
                armFKFingerAttachPoint = 'R_Wrist',
                rigScale = sceneScale
                )
        self.RightHand = rightHand

        # Neck.
        neck = SERigBipedNeckComponent.RigHumanNeck(prefix = 'C_Neck', baseRig = self.BaseRig,
                                                      rigSide = SERigEnum.eRigSide.RS_Center, 
                                                      rigType = SERigEnum.eRigType.RT_NeckComponent)
        neck.build(
                neckJoints = neckJnts,
                fkNeckAttachPoint = 'C_ChestEnd',
                rigScale = sceneScale
                )
        self.Neck = neck

