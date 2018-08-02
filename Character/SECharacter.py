from ..Base import SERigControl
from ..Base import SERigComponent
from ..Base import SERigBase
from ..Base import SERigNaming
from . import SECharacterDeform

import maya.cmds as cmds

sceneScale = 1.0

modelFilePath = '%s/%s/Model/%s_Model.ma'
builderFilePath = '%s/%s/Builder/%s_Builder.ma'

rootJnt = 'Root'

def build(
          characterName, 
          mainProjectPath = '', 
          upperBodyUpperLimbKnobCount = 2, 
          upperBodyLowerLimbKnobCount = 2,
          lowerBodyUpperLimbKnobCount = 2,
          lowerBodyLowerLimbKnobCount = 1,
          ):
    # Create new scene
    #cmds.file(new = True, f = True)

    # Create base.
    baseRig = SERigBase.SERigBase(characterName = characterName, scale = sceneScale)

    # Import model.
    modelFile = modelFilePath % (mainProjectPath, characterName, characterName)
    cmds.file(modelFile, i = 1)

    # Import builder scene
    builderFile = builderFilePath % (mainProjectPath, characterName, characterName)
    cmds.file(builderFile, i = 1)

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
                            upperBodyUpperLimbKnobCount, 
                            upperBodyLowerLimbKnobCount, 
                            lowerBodyUpperLimbKnobCount, 
                            lowerBodyLowerLimbKnobCount, 
                            upperBodyUpperLimbJoints, 
                            upperBodyLowerLimbJoints, 
                            lowerBodyUpperLimbJoints, 
                            lowerBodyLowerLimbJoints)

    cmds.select(cl=1)