import maya.cmds as cmds
from . import SERigEnum
from . import SERigNaming

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
        
        # Parent this component to the rig base.
        if baseRig:
            cmds.parent(self.TopGrp, baseRig.RigCompsGrp)
            baseRig.RigComponents.append(self)