from Base import SERigControl
from Base import SERigComponent
from Base import SERigBase

import maya.cmds as cmds

sceneScale = 1.0

mainProjectPath = ''
modelFilePath = '%s/%s/model/%s_model.mb'
builderFilePath = '%s/%s/builder/%s_builder.mb'

def build(characterName):
    # Create new scene
    cmds.file(new = True, f = True)

    # Create base.
    baseRig = SERigBase.SERigBase(characterName = characterName, scale = sceneScale)

    # Import model.
    modelFile = modelFilePath % (mainProjectPath, characterName, characterName)
    cmds.file(modelFile, i = 1)

    # Import builder scene
    builderFile = builderFilePath % (mainProjectPath, characterName, characterName)
    cmds.file(builderFile, i = 1)
