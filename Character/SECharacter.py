from ..Base import SERigControl
from ..Base import SERigComponent
from ..Base import SERigBase

import maya.cmds as cmds

sceneScale = 1.0

modelFilePath = '%s/%s/Model/%s_Model.ma'
builderFilePath = '%s/%s/Builder/%s_Builder.ma'

def build(characterName, mainProjectPath = ''):
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
