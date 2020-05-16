import maya.cmds as cmds

from . import SEStringHelper
from ..Base import SERigNaming
from ..Base import SERigEnum

#-----------------------------------------------------------------------------
def getFACS_DataBuffer(facialComponentGroup):
    if cmds.objExists(facialComponentGroup):
        try:
            res = cmds.listConnections(facialComponentGroup + '.' + SERigNaming.sFACS_DataBufferAttr)[0]
            return res
        except:
            cmds.warning('Cannot find facial component: ' + facialComponentGroup + ' FACS data buffer')
            return None
    else:
        cmds.warning('Cannot find facial component: ' + facialComponentGroup)
        return None
#-----------------------------------------------------------------------------
def getFacialActionUnitAttrName(bufferObject, actionUnitType):
    res = None
    if cmds.objExists(bufferObject):
        res = bufferObject + '.' + SERigNaming.auAttrList[actionUnitType]
    else:
        cmds.warning('Buffer object does not exist: ' + bufferObject)

    return res
#-----------------------------------------------------------------------------