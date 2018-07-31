import maya.cmds as cmds
import os
from ..ThirdParty import bSkinSaver

skinWeightsDir = 'Weights/SkinCluster'
skinWeightsExt = '.swt'

def build(baseRig, mainProjectPath, sceneScale):
    pass

def saveSkinWeights(characterName, mainProjectPath, geoList = []):
    for obj in geoList:
        # Weights file path.
        weightFilePath = os.path.join(mainProjectPath, characterName, skinWeightsDir, obj + skinWeightsExt)

        # Save skin weights.
        cmds.select(obj)
        bSkinSaver.bSaveSkinValues(weightFilePath)