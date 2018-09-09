import maya.cmds as cmds
from . import SERigEnum
from . import SERigNaming
from . import SERigControl

sceneObjectType = 'rig'

characterNameAttr = 'characterName'
sceneObjectTypeAttr = 'sceneObjectType'

#-----------------------------------------------------------------------------
# Rig Base Class
# Sun Che
#-----------------------------------------------------------------------------
class RigBase():
    def __init__(
                 self, 
                 characterName = 'new',
                 scale = 1.0,
                 mainCtrlAttachObject = '',
                 mainCtrlOffset = 35.0
                 ):
        # Add public members.
        self.RigComponents = []

        self.TopGrp = cmds.group(n = characterName + SERigNaming.s_RigGroup, em = 1)
        self.RigGrp = cmds.group(n = SERigNaming.sRigGroup, em = 1, p = self.TopGrp)
        self.ModelGrp = cmds.group(n = SERigNaming.sModelGroup, em = 1, p = self.TopGrp)
        self.DeformationGrp = cmds.group(n = SERigNaming.sDeformationGroup, em = 1, p = self.RigGrp)

        # Add custom attributes for the TopGrp object.
        for attr in [characterNameAttr, sceneObjectTypeAttr]:
            cmds.addAttr(self.TopGrp, ln = attr, dt = 'string')

        cmds.setAttr(self.TopGrp + '.' + characterNameAttr, characterName, type = 'string', l = 1)
        cmds.setAttr(self.TopGrp + '.' + sceneObjectTypeAttr, sceneObjectType, type = 'string', l = 1)

        # Create global controls.
        global1Ctrl = SERigControl.RigCircleControl(
                                rigSide = SERigEnum.eRigSide.RS_Center,
                                rigType = SERigEnum.eRigType.RT_Global,
                                prefix = 'Global_01', 
                                scale = scale * 40, 
                                parent = self.RigGrp, 
                                lockChannels = ['v'])

        global2Ctrl = SERigControl.RigSpikeCrossControl(
                                rigSide = SERigEnum.eRigSide.RS_Center,
                                rigType = SERigEnum.eRigType.RT_Global,
                                prefix = 'Global_02', 
                                scale = scale * 30, 
                                parent = global1Ctrl.ControlObject, 
                                lockChannels = ['s', 'v'])

        self._flattenGlobalCtrlShape(global1Ctrl.ControlObject)

        # Only allow uniform scaling.
        for axis in ['y', 'z']:
            cmds.connectAttr(global1Ctrl.ControlObject + '.sx', global1Ctrl.ControlObject + '.s' + axis)
            cmds.setAttr(global1Ctrl.ControlObject + '.s' + axis, k = 0)
        
        # Create more groups.
        self.JointsGrp = cmds.group(n = SERigNaming.sJointsGroup, em = 1, p = global2Ctrl.ControlObject)
        self.RigCompsGrp = cmds.group(n = SERigNaming.sRigCompsGroup, em = 1, p = global2Ctrl.ControlObject)

        self.RigPartsGrp = cmds.group(n = SERigNaming.sRigPartsGroup, em = 1, p = self.RigGrp)
        cmds.setAttr(self.RigPartsGrp + '.it', 0, l = 1) # Not inheriting transform

        # Create main control.
        mainCtrl = SERigControl.RigCircleControl(
                            rigSide = SERigEnum.eRigSide.RS_Center,
                            rigType = SERigEnum.eRigType.RT_Global,
                            prefix = 'Main', 
                            scale = scale * 4, 
                            parent = global2Ctrl.ControlObject, 
                            translateTo = mainCtrlAttachObject,
                            lockChannels = ['t', 'r', 's', 'v'])
        self.MainControl = mainCtrl

        # Adjust main control position and orientation.
        self._adjustMainCtrlShape(mainCtrl, scale, mainCtrlOffset)

        if cmds.objExists(mainCtrlAttachObject):
            cmds.parentConstraint(mainCtrlAttachObject, mainCtrl.ControlGroup, mo = 1)

        mainVisAts = ['modelVisibility', 'masterJointsVisibility', 'slaveJointsVisibility']
        mainVisAtsDV = [1, 0, 0]
        mainDispAts = ['modelDisplay', 'masterJointsDisplay', 'slaveJointsDisplay']
        mainObjList = [self.ModelGrp, self.JointsGrp, self.DeformationGrp]

        # Add rig visibility connections.
        for at, obj, dv in zip(mainVisAts, mainObjList, mainVisAtsDV):
            cmds.addAttr(mainCtrl.ControlObject, ln = at, at = 'enum', enumName = 'off:on', k = 1, dv = dv)
            cmds.setAttr(mainCtrl.ControlObject + '.' + at, cb = 1)
            cmds.connectAttr(mainCtrl.ControlObject + '.' + at, obj + '.v')

        # Add rig display type connections.
        for at, obj in zip(mainDispAts, mainObjList):
            cmds.addAttr(mainCtrl.ControlObject, ln = at, at = 'enum', enumName = 'normal:template:reference', k = 1, dv = 2)
            cmds.setAttr(mainCtrl.ControlObject + '.' + at, cb = 1)
            cmds.setAttr(obj + '.ove', 1)
            cmds.connectAttr(mainCtrl.ControlObject + '.' + at, obj + '.ovdt')

        # Add IK/FK switches.
        mainIKFKSwitchAts = [SERigNaming.sLeftLegIKFKSwitch, SERigNaming.sRightLegIKFKSwitch, 
                             SERigNaming.sLeftArmIKFKSwitch, SERigNaming.sRightArmIKFKSwitch]
        for at in mainIKFKSwitchAts:
            cmds.addAttr(mainCtrl.ControlObject, ln = at, at = 'float', k = 1, dv = 0.0, hasMinValue = True, min = 0.0, hasMaxValue = True, max = 1.0)
            cmds.setAttr(mainCtrl.ControlObject + '.' + at, cb = 1)
        self.MainIKFKSwitchAts = mainIKFKSwitchAts

        # Add IK/FK auto hide options.
        mainIKFKAutoHideAts = [SERigNaming.sLeftLegIKFKAutoHide, SERigNaming.sRightLegIKFKAutoHide, 
                             SERigNaming.sLeftArmIKFKAutoHide, SERigNaming.sRightArmIKFKAutoHide]
        for at in mainIKFKAutoHideAts:
            cmds.addAttr(mainCtrl.ControlObject, ln = at, at = 'enum', enumName = 'off:on', k = 1, dv = 1)
            cmds.setAttr(mainCtrl.ControlObject + '.' + at, cb = 1)
        self.MainIKFKAutoHideAts = mainIKFKAutoHideAts

        
    def getLegIKFKSwitch(self, rigSide = SERigEnum.eRigSide.RS_Unknown):

        if rigSide == SERigEnum.eRigSide.RS_Left:
            return self.MainControl.ControlObject + '.' + self.MainIKFKSwitchAts[0]
        elif rigSide == SERigEnum.eRigSide.RS_Right:
            return self.MainControl.ControlObject + '.' + self.MainIKFKSwitchAts[1]
        else:
            return None

    def getArmIKFKSwitch(self, rigSide = SERigEnum.eRigSide.RS_Unknown):

        if rigSide == SERigEnum.eRigSide.RS_Left:
            return self.MainControl.ControlObject + '.' + self.MainIKFKSwitchAts[2]
        elif rigSide == SERigEnum.eRigSide.RS_Right:
            return self.MainControl.ControlObject + '.' + self.MainIKFKSwitchAts[3]
        else:
            return None

    def getCharacterName(self):
        res = cmds.getAttr(self.TopGrp + '.' + characterNameAttr)
        return res

    # Helper functions
    def _adjustMainCtrlShape(self, ctrl, scale, offset):
        ctrlShapes = cmds.listRelatives(ctrl.ControlObject, s = 1, type = 'nurbsCurve')
        cluster = cmds.cluster(ctrlShapes)[1] # Get cluster handle, [0]: cluster name
        cmds.setAttr(cluster + '.ry', 90)
        cmds.delete(ctrlShapes, ch = 1)
        cmds.move(scale*offset, ctrl.ControlGroup, moveY = True, relative = True)

    def _flattenGlobalCtrlShape(self, ctrlObject):
        ctrlShapes = cmds.listRelatives(ctrlObject, s = 1, type = 'nurbsCurve')
        cluster = cmds.cluster(ctrlShapes)[1] # Get cluster handle, [0]: cluster name
        cmds.setAttr(cluster + '.rz', 90)
        cmds.delete(ctrlShapes, ch = 1)
        