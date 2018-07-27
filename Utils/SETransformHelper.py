import maya.cmds as cmds

from . import SEStringHelper

def SE_MakeOffsetGrp(object, prefix = ''):
    if not prefix:
        prefix = SEStringHelper.SE_RemoveSuffix(object)

    offsetGrp = cmds.group(n = prefix + 'OffsetGrp', em = 1)

    
