import maya.cmds as cmds
from . import SERigEnum
from . import SERigNaming
from . import SERigControl

sceneObjectType = 'rig'

#-----------------------------------------------------------------------------
# Rig Base Class
# Sun Che
#-----------------------------------------------------------------------------
class SERigBase():
    def __init__(
                 self, 
                 characterName = 'new',
                 scale = 1.0
                 ):
        # Add public members.
        self.TopGrp = cmds.group(n = characterName + SERigNaming.s_RigGroup, em = 1)
        self.RigGrp = cmds.group(n = SERigNaming.sRigGroup, em = 1, p = self.TopGrp)
        self.ModelGrp = cmds.group(n = SERigNaming.sModelGroup, em = 1, p = self.TopGrp)

        # Add custom attributes for the TopGrp object.
        characterNameAttr = 'characterName'
        sceneObjectTypeAttr = 'sceneObjectType'

        for attr in [characterNameAttr, sceneObjectTypeAttr]:
            cmds.addAttr(self.TopGrp, ln = attr, dt = 'string')

        cmds.setAttr(self.TopGrp + '.' + characterNameAttr, characterName, type = 'string', l = 1)
        cmds.setAttr(self.TopGrp + '.' + sceneObjectTypeAttr, sceneObjectType, type = 'string', l = 1)

        # Create global controls.
        global1Ctrl = SERigControl.SERigControl(
                                                 rigSide = SERigEnum.eRigSide.RS_Center,
                                                 rigType = SERigEnum.eRigType.RT_Global,
                                                 prefix = 'global1', 
                                                 scale = scale * 20, 
                                                 parent = self.RigGrp, 
                                                 lockChannels = ['v'])

        global2Ctrl = SERigControl.SERigControl(
                                                 rigSide = SERigEnum.eRigSide.RS_Center,
                                                 rigType = SERigEnum.eRigType.RT_Global,
                                                 prefix = 'global2', 
                                                 scale = scale * 18, 
                                                 parent = global1Ctrl.ContrlObject, 
                                                 lockChannels = ['s', 'v'])

        self._flattenGlobalCtrlShape(global1Ctrl.ContrlObject)
        self._flattenGlobalCtrlShape(global2Ctrl.ContrlObject)

        # Only allow uniform scaling.
        for axis in ['y', 'z']:
            cmds.connectAttr(global1Ctrl.ContrlObject + '.sx', global1Ctrl.ContrlObject + '.s' + axis)
            cmds.setAttr(global1Ctrl.ContrlObject + '.s' + axis, k = 0)
        
        # Create more groups.
        self.JointsGrp = cmds.group(n = SERigNaming.sJointsGroup, em = 1, p = global2Ctrl.ContrlObject)
        self.RigCompsGrp = cmds.group(n = SERigNaming.sRigCompsGroup, em = 1, p = global2Ctrl.ContrlObject)

        self.RigPartsGrp = cmds.group(n = SERigNaming.sRigPartsGroup, em = 1, p = self.RigGrp)
        cmds.setAttr(self.RigPartsGrp + '.it', 0, l = 1) # Not inheriting transform

    # Helper functions
    def _flattenGlobalCtrlShape(self, ctrlObject):
        ctrlShapes = cmds.listRelatives(ctrlObject, s = 1, type = 'nurbsCurve')
        cluster = cmds.cluster(ctrlShapes)[1] # Get cluster handle, [0]: cluster name
        cmds.setAttr(cluster + '.rz', 90)
        cmds.delete(ctrlShapes, ch = 1)
        