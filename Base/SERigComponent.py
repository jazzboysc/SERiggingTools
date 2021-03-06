import maya.cmds as cmds
from . import SERigEnum
from . import SERigNaming
from ..Utils import SERigObjectTypeHelper

#-----------------------------------------------------------------------------
# Rig Component Class
# Sun Che
#-----------------------------------------------------------------------------
class RigComponent():
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 ):

        # Add public members.
        self.Prefix = prefix
        self.BaseRig = baseRig
        self.RigSide = rigSide
        self.RigType = rigType

        self.TopGrp = cmds.group(n = prefix + SERigNaming.s_RigCompsGroup, em = 1)
        self.ControlsGrp = cmds.group(n = prefix + SERigNaming.s_ControlsGroup, em = 1, p = self.TopGrp)
        self.JointsGrp = cmds.group(n = prefix + SERigNaming.s_JointsGroup, em = 1, p = self.TopGrp)
        self.RigPartsGrp = cmds.group(n = prefix + SERigNaming.s_RigPartsGroup, em = 1, p = self.TopGrp)
        self.RigPartsFixedGrp = cmds.group(n = prefix + SERigNaming.s_RigPartsFixedGroup, em = 1, p = self.TopGrp)
        cmds.setAttr(self.RigPartsFixedGrp + '.it', 0, l = 1)

        self.FKControlGroup = cmds.group(n = SERigNaming.sFKPrefix + prefix + SERigNaming.sControlGroup, p = self.ControlsGrp, em = 1)
        self.IKControlGroup = cmds.group(n = SERigNaming.sIKPrefix + prefix + SERigNaming.sControlGroup, p = self.ControlsGrp, em = 1)
        
        # Add component instance info to top group.
        cmds.addAttr(self.TopGrp, ln = 'RigSide', dt = 'string')
        cmds.addAttr(self.TopGrp, ln = 'RigType', dt = 'string')
        cmds.addAttr(self.TopGrp, ln = 'Prefix', dt = 'string')

        cmds.setAttr(self.TopGrp + '.' + 'RigSide', SERigEnum.eRigSideStringTable[self.RigSide], type = 'string', l = 1)
        cmds.setAttr(self.TopGrp + '.' + 'RigType', SERigEnum.eRigTypeStringTable[self.RigType], type = 'string', l = 1)
        cmds.setAttr(self.TopGrp + '.' + 'Prefix', self.Prefix, type = 'string', l = 1)

        # Link component's sub groups to the top group.
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.ControlsGrp, SERigNaming.sControlsGroupAttr)
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.JointsGrp, SERigNaming.sJointsGroupAttr)
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.RigPartsGrp, SERigNaming.sRigPartsGroupAttr)
        SERigObjectTypeHelper.linkRigObjects(self.TopGrp, self.RigPartsFixedGrp, SERigNaming.sRigPartsFixedGroupAttr)

        # Parent this component to the rig base.
        if baseRig:
            cmds.parent(self.TopGrp, baseRig.RigCompsGrp)
            baseRig.RigComponents.append(self)

        # Create component type node.
        SERigObjectTypeHelper.createRigObjectTypeAttr(self.TopGrp, 'RigComponentType')