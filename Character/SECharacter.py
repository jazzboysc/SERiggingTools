from ..Base.SERigControl import RigControl
from ..Base.SERigComponent import RigComponent
from ..Base.SERigBase import RigBase
from ..Base import SERigNaming
from ..Base import SERigEnum
from ..Rig import SERigSpineComponent
from ..Rig import SERigBipedLimbComponent
from ..Rig import SERigBipedNeckComponent
from ..Rig import SERigHumanFacialComponent
from ..Utils import SERigObjectTypeHelper
from ..Utils import SEMathHelper
from ..Utils import SEJointHelper
from . import SECharacterDeform

import maya.cmds as cmds
import pymel.core as pm
import os

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
        self.FacialSystem = None

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
              createLegCircleFkControl = True,
              ballIKTwistLeft = 90,
              ballIKTwistRight = 270,
              toeIKTwistLeft = 90,
              toeIKTwistRight = 0,
              fkArmControlScaleYZ = 10,
              fkArmControlScaleYZMultiplier = 0.9,
              fkArmControlTransparency = 0.85,
              createArmCircleFkControl = True,
              createArmCircleIkControl = False,
              createCircleFkFingerControl = True,
              circleFkFingerControlScaleFactor = 1.7,
              createCompactFootControl = True,
              createSimpleSpine = False,
              createSpineFKSystem = True,
              createSpineCircleFkControl = True,
              createSpineCircleIkControl = False,
              createSimpleFKNeck = True,
              createNeckMuscleSplineSystem = False,
              neckMuscleSplineJointCount = 5,
              createNeckCircleFkControl = True,
              createFacialSystem = True,
              usePortraitCameraFocalLength = True,
              portraitCameraFocalLength = 85.0
              ):

        # Check if SERiggingTools plugin is loaded.
        pluginLoaded = SERigObjectTypeHelper.isPluginLoaded('SERiggingToolsPlugin.py')
        if not pluginLoaded:
            cmds.error('Cannot build rig. SERiggingToolsPlugin.py is not loaded.')
            return

        # Import model scene.
        modelFile = modelFilePath % (mainProjectPath, self.CharacterName, self.CharacterName)
        if os.path.isfile(modelFile):
            print('Importing model file: ' + modelFile)
            try:
                cmds.file(modelFile, i = 1)
            except:
                print('Invalid model file: ' + modelFile)
                return
        else:
            print(modelFile + ' does not exist.')
            return

        # Import builder scene.
        builderFile = builderFilePath % (mainProjectPath, self.CharacterName, self.CharacterName)
        if os.path.isfile(builderFile):
            print('Importing builder file: ' + builderFile)
            try:
                cmds.file(builderFile, i = 1)
            except:
                print('Invalid builder file: ' + builderFile)
                return
        else:
            print(builderFile + ' does not exist.')
            return

        # Adjust default perspective camera's focal length and orientation to fit the character.
        if usePortraitCameraFocalLength:
            portraitCamera = SERigObjectTypeHelper.getDefaultPerspectiveCamera()
            if portraitCamera:
                cmds.setAttr(portraitCamera + '.focalLength', portraitCameraFocalLength)
                cmds.setAttr(portraitCamera + '.nearClipPlane', 0.5)

                portraitCameraTrans = cmds.listRelatives(portraitCamera, parent = True)[0]
                cmds.setAttr(portraitCameraTrans + '.rotateX', -10.0)
                cmds.setAttr(portraitCameraTrans + '.rotateY', 25.0)
                cmds.setAttr(portraitCameraTrans + '.rotateZ', 0.0)
                cmds.delete(cmds.pointConstraint('C_ChestBegin', portraitCameraTrans))
                pm.viewFit(all = True)

        # Create rig base.
        baseRig = RigBase(characterName = self.CharacterName, 
                          scale = sceneScale, mainCtrlAttachObject = headJnt, 
                          mainCtrlOffset = mainCtrlOffset)
        self.BaseRig = baseRig

        # Create character type node.
        SERigObjectTypeHelper.createRigObjectTypeAttr(self.BaseRig.TopGrp, 'RigCharacterType')

        # Parent the imported model to the rig base.
        modelGrp = ('%s' + SERigNaming.s_ModelGroup) % self.CharacterName
        if cmds.objExists(modelGrp):
            cmds.parent(modelGrp, baseRig.ModelGrp)
        else:
            cmds.error('Cannot find model group.')

        # Get surrounding meshes from model group.
        surroundingMeshes = cmds.listRelatives(cmds.ls(type = 'mesh'), type ='transform', p = True)

        # Parent the imported skeleton to the rig base.
        cmds.parent(rootJnt, baseRig.JointsGrp)

        # Prepare joints.
        spineJnts = SEJointHelper.getBuilderSpineJoints()

        upperChestJnts = SEJointHelper.getBuilderUpperChestJoints()

        leftLegJnts = SEJointHelper.getBuilderLeftLegJoints()

        rightLegJnts = SEJointHelper.getBuilderRightLegJoints()

        leftFootHelperJoints = SERigBipedLimbComponent.RigHumanLeg.buildFootHelperJointsMapForLeftSide(legJoints = leftLegJnts,
            footExtLocator = 'locator_L_Foot_Ext', footIntLocator = 'locator_L_Foot_Int', footBaseLocator = 'locator_L_Foot_Base',
            footBaseSwiveLocator = 'locator_L_Foot_BaseSwive', footToeSwiveLocator = 'locator_L_Foot_ToeSwive')

        rightFootHelperJoints = SERigBipedLimbComponent.RigHumanLeg.mirrorFootHelperJointsMapForRightSide(leftFootHelperJoints)

        leftArmJnts = SEJointHelper.getBuilderLeftArmJoints()

        rightArmJnts = SEJointHelper.getBuilderRightArmJoints()

        leftHandJnts = SEJointHelper.getBuilderLeftHandJoints()

        rightHandJnts = SEJointHelper.getBuilderRightHandJoints()

        neckJnts = SEJointHelper.getBuilderNeckJoints()

        facialJnts = SEJointHelper.getFacialJoints()

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
                                createLegCircleFkControl,
                                fkArmControlScaleYZ,
                                fkArmControlScaleYZMultiplier,
                                fkArmControlTransparency,
                                createArmCircleFkControl,
                                createArmCircleIkControl,
                                createCircleFkFingerControl,
                                circleFkFingerControlScaleFactor,
                                createCompactFootControl,
                                createSimpleSpine,
                                createSpineFKSystem,
                                createSpineCircleFkControl,
                                createSpineCircleIkControl,
                                createSimpleFKNeck,
                                createNeckMuscleSplineSystem,
                                neckMuscleSplineJointCount,
                                createNeckCircleFkControl,
                                createFacialSystem,
                                facialJnts,
                                surroundingMeshes
                                )

        # Setup model deformation.

        upperBodyUpperLimbJoints = SEJointHelper.getBuilderUpperBodyUpperLimbJoints()
        upperBodyLowerLimbJoints = SEJointHelper.getBuilderUpperBodyLowerLimbJoints()
        lowerBodyUpperLimbJoints = SEJointHelper.getBuilderLowerBodyUpperLimbJoints()
        lowerBodyLowerLimbJoints = SEJointHelper.getBuilderLowerBodyLowerLimbJoints()

        if self.RigDeform:

            leftNeckMuscleMasterJnts = []
            rightNeckMuscleMasterJnts = []

            # Get neck muscle master joints.
            if not createSimpleFKNeck and createNeckMuscleSplineSystem:
                leftNeckMuscleDrivenJnts = self.Neck.getLeftNeckKeepOutDrivenJoints()
                rightNeckMuscleDrivenJnts = self.Neck.getRightNeckKeepOutDrivenJoints()
                leftNeckMuscleDriverJnts = self.Neck.getLeftNeckKeepOutDriverJoints()
                rightNeckMuscleDriverJnts = self.Neck.getRightNeckKeepOutDriverJoints()

                leftNeckMuscleMasterJnts = leftNeckMuscleDrivenJnts[1:-1]
                leftNeckMuscleMasterJnts.insert(0, leftNeckMuscleDriverJnts[0])
                leftNeckMuscleMasterJnts.append(leftNeckMuscleDriverJnts[1])

                rightNeckMuscleMasterJnts = rightNeckMuscleDrivenJnts[1:-1]
                rightNeckMuscleMasterJnts.insert(0, rightNeckMuscleDriverJnts[0])
                rightNeckMuscleMasterJnts.append(rightNeckMuscleDriverJnts[1])

            # Build deformation system.
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
                                createNeckMuscleSplineSystem,
                                leftNeckMuscleMasterJnts,
                                rightNeckMuscleMasterJnts,
                                facialJnts,
                                rootJnt
                                )

        # Delete imported builder group.
        builderGrp = ('%s' + SERigNaming.s_BuilderGroup) % self.CharacterName
        if cmds.objExists(builderGrp):
            print('Deleting builder group: ' + builderGrp)
            cmds.delete(builderGrp)
        else:
            cmds.warning('Cannot delete builder group:'  + builderGrp)

        cmds.select(cl = 1)


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
                            createLegCircleFkControl,
                            fkArmControlScaleYZ,
                            fkArmControlScaleYZMultiplier,
                            fkArmControlTransparency,
                            createArmCircleFkControl,
                            createArmCircleIkControl,
                            createCircleFkFingerControl,
                            circleFkFingerControlScaleFactor,
                            createCompactFootControl,
                            createSimpleSpine,
                            createSpineFKSystem,
                            createSpineCircleFkControl,
                            createSpineCircleIkControl,
                            createSimpleFKNeck,
                            createNeckMuscleSplineSystem,
                            neckMuscleSplineJointCount,
                            createNeckCircleFkControl,
                            createFacialSystem,
                            facialJnts,
                            surroundingMeshes
                            ):

        # Spine.
        spine = None
        if createSimpleSpine:
            spine = SERigSpineComponent.RigSimpleIKSpine(prefix = 'C_Spine', baseRig = self.BaseRig, 
                                                         rigSide = SERigEnum.eRigSide.RS_Center, 
                                                         rigType = SERigEnum.eRigType.RT_SpineComponent)
        else:
            spine = SERigSpineComponent.RigFixedEndsIKSpine(prefix = 'C_Spine', baseRig = self.BaseRig, 
                                                         rigSide = SERigEnum.eRigSide.RS_Center, 
                                                         rigType = SERigEnum.eRigType.RT_SpineComponent)
        spine.build(
                    spineJoints = spineJnts,
                    rootJoint = rootJnt,
                    rigScale = sceneScale,
                    createFKSystem = createSpineFKSystem,
                    createCircleFkControl = createSpineCircleFkControl,
                    createCircleIkControl = createSpineCircleIkControl,
                    surroundingMeshes = surroundingMeshes
                    )
        self.Spine = spine
        SERigObjectTypeHelper.linkRigObjects(self.BaseRig.TopGrp, self.Spine.TopGrp, 'SpineComponent', 'ComponentOwner')

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
                createCircleFkControl = createLegCircleFkControl,
                createCompactFootControl = createCompactFootControl,
                surroundingMeshes = surroundingMeshes
                )
        self.LeftLeg = leftLeg
        SERigObjectTypeHelper.linkRigObjects(self.BaseRig.TopGrp, self.LeftLeg.TopGrp, 'LeftLegComponent', 'ComponentOwner')

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
                createCircleFkControl = createLegCircleFkControl,
                createCompactFootControl = createCompactFootControl,
                surroundingMeshes = surroundingMeshes
                )
        self.RightLeg = rightLeg
        SERigObjectTypeHelper.linkRigObjects(self.BaseRig.TopGrp, self.RightLeg.TopGrp, 'RightLegComponent', 'ComponentOwner')

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
                fkControlTransparency = fkArmControlTransparency,
                createCircleFkControl = createArmCircleFkControl,
                createCircleIkControl = createArmCircleIkControl,
                surroundingMeshes = surroundingMeshes
                )
        self.LeftArm = leftArm
        SERigObjectTypeHelper.linkRigObjects(self.BaseRig.TopGrp, self.LeftArm.TopGrp, 'LeftArmComponent', 'ComponentOwner')

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
                fkControlTransparency = fkArmControlTransparency,
                createCircleFkControl = createArmCircleFkControl,
                createCircleIkControl = createArmCircleIkControl,
                surroundingMeshes = surroundingMeshes
                )
        self.RightArm = rightArm
        SERigObjectTypeHelper.linkRigObjects(self.BaseRig.TopGrp, self.RightArm.TopGrp, 'RightArmComponent', 'ComponentOwner')

        # Left hand.
        leftHand = SERigBipedLimbComponent.RigHumanHand(prefix = 'L_Hand', baseRig = self.BaseRig,
                                                      rigSide = SERigEnum.eRigSide.RS_Left, 
                                                      rigType = SERigEnum.eRigType.RT_HandComponent)
        leftHand.build(
                fingers = leftHandJnts,
                armFKFingerAttachPoint = 'L_Wrist',
                palmThumbFingerRootPoint = 'L_Thumb_1',
                palmIndexFingerRootPoint = 'L_Index_1',
                palmPinkyFingerRootPoint = 'L_Pinky_1',
                rigScale = sceneScale,
                createCircleFkFingerControl = createCircleFkFingerControl,
                circleFkFingerControlScaleFactor = circleFkFingerControlScaleFactor,
                surroundingMeshes = surroundingMeshes
                )
        self.LeftHand = leftHand
        SERigObjectTypeHelper.linkRigObjects(self.BaseRig.TopGrp, self.LeftHand.TopGrp, 'LeftHandComponent', 'ComponentOwner')

        # Right hand.
        rightHand = SERigBipedLimbComponent.RigHumanHand(prefix = 'R_Hand', baseRig = self.BaseRig,
                                                      rigSide = SERigEnum.eRigSide.RS_Right, 
                                                      rigType = SERigEnum.eRigType.RT_HandComponent)
        rightHand.build(
                fingers = rightHandJnts,
                armFKFingerAttachPoint = 'R_Wrist',
                palmThumbFingerRootPoint = 'R_Thumb_1',
                palmIndexFingerRootPoint = 'R_Index_1',
                palmPinkyFingerRootPoint = 'R_Pinky_1',
                rigScale = sceneScale,
                createCircleFkFingerControl = createCircleFkFingerControl,
                circleFkFingerControlScaleFactor = circleFkFingerControlScaleFactor,
                surroundingMeshes = surroundingMeshes
                )
        self.RightHand = rightHand
        SERigObjectTypeHelper.linkRigObjects(self.BaseRig.TopGrp, self.RightHand.TopGrp, 'RightHandComponent', 'ComponentOwner')

        # Neck.
        neck = None
        if createSimpleFKNeck:
            neck = SERigBipedNeckComponent.RigSimpleHumanNeck(prefix = 'C_Neck', baseRig = self.BaseRig,
                                                          rigSide = SERigEnum.eRigSide.RS_Center, 
                                                          rigType = SERigEnum.eRigType.RT_NeckComponent)
            neck.build(
                    neckJoints = neckJnts,
                    neckAttachPoint = 'C_ChestEnd',
                    rigScale = sceneScale,
                    createCircleFkControl = createNeckCircleFkControl,
                    surroundingMeshes = surroundingMeshes
                    )
        else:
            spineRefLength = SEMathHelper.getDistanceBetweenObjects(spineJnts[0], spineJnts[-1])

            neck = SERigBipedNeckComponent.RigMuscleSplineHumanNeck(prefix = 'C_Neck', baseRig = self.BaseRig,
                                                          rigSide = SERigEnum.eRigSide.RS_Center, 
                                                          rigType = SERigEnum.eRigType.RT_NeckComponent)
            neck.build(
                    neckJoints = neckJnts,
                    neckAttachPoint = 'C_ChestEnd',
                    rigScale = sceneScale,
                    leftChestHeadBegin = 'locator_L_ChestHeadBegin',
                    leftChestHeadEnd = 'locator_L_ChestHeadEnd',
                    rightChestHeadBegin = 'locator_R_ChestHeadBegin',
                    rightChestHeadEnd = 'locator_R_ChestHeadEnd',
                    createMuscleSpline = createNeckMuscleSplineSystem,
                    keepOutJointCount = neckMuscleSplineJointCount,
                    spineReferenceLength = spineRefLength,
                    createCircleFkControl = createNeckCircleFkControl,
                    surroundingMeshes = surroundingMeshes
                    )

        if neck:
            self.Neck = neck
            SERigObjectTypeHelper.linkRigObjects(self.BaseRig.TopGrp, self.Neck.TopGrp, 'NeckComponent', 'ComponentOwner')

        if createFacialSystem and not createSimpleFKNeck:
            facialSystem = SERigHumanFacialComponent.RigHumanFacialSystem(prefix = 'C_Face', baseRig = self.BaseRig, 
                                                                          rigSide = SERigEnum.eRigSide.RS_Center, 
                                                                          rigType = SERigEnum.eRigType.RT_FacialComponent)
            facialSystem.build(
                facialJoints = facialJnts,
                jawEndJoint = 'C_JawEnd',
                throatJoint = 'C_Throat',
                rootJoint = '',
                facialAttachPoint = 'C_FacialRoot',
                rigScale = 1.0,
                createChinBulgeIKSystem = True,
                headAimIkControl = neck.HeadAimIKControl
                )
            self.FacialSystem = facialSystem
            SERigObjectTypeHelper.linkRigObjects(self.BaseRig.TopGrp, self.FacialSystem.TopGrp, 'FacialComponent', 'ComponentOwner')
