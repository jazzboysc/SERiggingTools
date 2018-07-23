import maya.cmds as cmds
from . import SERigEnum
from . import SERigNaming

#-----------------------------------------------------------------------------
# Rig Component Class
# Sun Che
#-----------------------------------------------------------------------------
class SERigComponent():
    def __init__(
                 self, 
                 prefix = 'new',
                 rigBase = None
                 ):
        # Add public members.
        self.TopGrp = cmds.group(n = prefix + SERigNaming.s_RigCompsGroup, em = 1)

        self.ControlsGrp = cmds.group(n = prefix + SERigNaming.s_ControlsGroup, em = 1, p = self.TopGrp)
        self.JointsGrp = cmds.group(n = prefix + SERigNaming.s_JointsGroup, em = 1, p = self.TopGrp)
        self.RigPartsGrp = cmds.group(n = prefix + SERigNaming.s_RigPartsGroup, em = 1, p = self.TopGrp)
        self.RigPartsFixedGrp = cmds.group(n = prefix + SERigNaming.s_RigPartsFixedGroup, em = 1, p = self.TopGrp)
        cmds.setAttr(self.RigPartsFixedGrp + '.it', 0, l = 1)
        
        # Parent this component to the rig base.
        if rigBase:
            cmds.parent(self.TopGrp, rigBase.RigCompsGrp)