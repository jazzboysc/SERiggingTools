import maya.cmds as cmds

from . import SEStringHelper

def SE_MakeOffsetGrp(object, prefix = ''):
    if not prefix:
        prefix = SEStringHelper.SE_RemoveSuffix(object)

    offsetGrp = cmds.group(n = prefix + 'OffsetGrp', em = 1)

    objectParents = cmds.listRelatives(object, p = 1)
    if objectParents:
        cmds.parent(offsetGrp, objectParents[0])

    # Match group's transform to object's transform.
    cmds.delete(cmds.parentConstraint(object, offsetGrp))
    cmds.delete(cmds.scaleConstraint(object, offsetGrp))
    
    # Parent the object under the offset group.
    cmds.parent(object, offsetGrp)

    return offsetGrp