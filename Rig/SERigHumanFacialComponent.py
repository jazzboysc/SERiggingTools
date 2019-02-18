import maya.cmds as cmds

from ..Base.SERigComponent import RigComponent
from ..Base import SERigControl
from ..Base import SERigEnum
from ..Base import SERigNaming
from ..Utils import SEStringHelper
from ..Utils import SEMathHelper
from ..Utils import SEJointHelper
from ..Utils import SERigObjectTypeHelper

#-----------------------------------------------------------------------------
# Rig Human Facial System Class
# Sun Che
#-----------------------------------------------------------------------------
class RigHumanFacialSystem(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Center,
                 rigType = SERigEnum.eRigType.RT_NeckComponent
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.EyesAimIKControl = None
        self.IKJointsGroup = None

    def build(
            self,
            facialJoints = [],  # []
            rootJoint = '',
            facialAttachPoint = '',
            rigScale = 1.0
            ):
        print('Building facial system...')