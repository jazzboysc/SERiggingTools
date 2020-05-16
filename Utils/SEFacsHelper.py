import maya.cmds as cmds

from . import SEStringHelper
from ..Base import SERigNaming
from ..Base import SERigEnum

#-----------------------------------------------------------------------------
def getFacialActionUnitAttrName(bufferObject, actionUnitType):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.auAttrList[actionUnitType]
    else:
        cmds.warning('Buffer object does not exist: ' + bufferObject)

    return res
#-----------------------------------------------------------------------------