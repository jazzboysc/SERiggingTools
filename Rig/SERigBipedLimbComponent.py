import maya.cmds as cmds
from ..Base.SERigComponent import RigComponent
from ..Base import SERigControl
from ..Base import SERigEnum
from ..Base import SERigNaming

#-----------------------------------------------------------------------------
# Rig Human Leg Class
# Sun Che
#-----------------------------------------------------------------------------
class RigHumanLeg(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 abc = ''
                 ):
        RigComponent.__init__(self, prefix, baseRig)

    def build(
            self,
            legJoints = [],
            rootJoint = '',
            footExtLocator = '',
            footIntLocator = '',
            footBaseLocator = '',
            footBaseSwiveLocator = '',
            footToeSwiveLocator = '',
            rigScale = 1.0
            ):
        pass
