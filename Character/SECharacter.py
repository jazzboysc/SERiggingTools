from ..Base import SERigControl
from ..Base import SERigComponent
from ..Base import SERigBase
from ..Base import SERigNaming
from ..Rig import SERigSpineComponent
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
          mainCtrlOffset = 30
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
    baseRig = SERigBase.SERigBase(characterName = characterName, 
                                  scale = sceneScale, mainCtrlAttachObject = headJnt, 
                                  mainCtrlOffset = mainCtrlOffset)

    # Parent the imported model to the rig base.
    modelGrp = ('%s' + SERigNaming.s_ModelGroup) % characterName
    cmds.parent(modelGrp, baseRig.ModelGrp)

    # Parent the imported skeleton to the rig base.
    cmds.parent(rootJnt, baseRig.JointsGrp)

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

    # Create rig components.
    createRigComponents(baseRig)


def createRigComponents(baseRig):
    # Spine
    spineJoints = ['C_Pelvis', 'C_Spine_0', 'C_Spine_1', 'C_Spine_2', 'C_Spine_3', 'C_ChestBegin']
    SERigSpineComponent.build(
                                baseRig = baseRig,
                                spineJoints = spineJoints,
                                rootJoint = rootJnt,
                                spineCurve = 'C_Spine_Curve',
                                bodyLocator = 'locator_Body',
                                chestLocator = 'locator_Chest',
                                pelvisLocator = 'locator_Pelvis',
                                prefix = 'Spine',
                                rigScale = sceneScale
                                )