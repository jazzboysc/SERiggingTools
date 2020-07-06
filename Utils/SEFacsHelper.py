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

def getFACS_AUBuffer(facialComponentGroup):
    if cmds.objExists(facialComponentGroup):
        try:
            res = cmds.listConnections(facialComponentGroup + '.' + SERigNaming.sFACS_AUBufferAttr)[0]
            return res
        except:
            cmds.warning('Cannot find facial component: ' + facialComponentGroup + ' FACS AU buffer')
            return None
    else:
        cmds.warning('Cannot find facial component: ' + facialComponentGroup)
        return None

def getFACS_ControlMode(facialComponentGroup):
    if cmds.objExists(facialComponentGroup):
        try:
            res = cmds.listConnections(facialComponentGroup + '.' + SERigNaming.sFACS_ControlModeAttr)[0]
            return res
        except:
            cmds.warning('Cannot find facial component: ' + facialComponentGroup + ' FACS Control Mode')
            return None
    else:
        cmds.warning('Cannot find facial component: ' + facialComponentGroup)
        return None

def getFACS_CustomConnectionMapBuffer(facialComponentGroup):
    if cmds.objExists(facialComponentGroup):
        try:
            res = cmds.listConnections(facialComponentGroup + '.' + SERigNaming.sFACS_CustomConnectionMapAttr)[0]
            return res
        except:
            cmds.warning('Cannot find facial component: ' + facialComponentGroup + ' Custom Connection Map Buffer')
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