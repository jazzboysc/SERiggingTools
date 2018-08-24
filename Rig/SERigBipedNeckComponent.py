import maya.cmds as cmds
from ..Base.SERigComponent import RigComponent
from ..Base import SERigControl
from ..Base import SERigEnum
from ..Base import SERigNaming
from ..Utils import SEStringHelper
from ..Utils import SEMathHelper
from ..Utils import SEJointHelper

#-----------------------------------------------------------------------------
# Rig Human Neck Class
# Sun Che
#-----------------------------------------------------------------------------
class RigHumanNeck(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Center,
                 rigType = SERigEnum.eRigType.RT_Neck
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.
        self.FKNeckControls = []

    def build(
            self,
            neckJoints = [],
            rootJoint = '',
            fkNeckAttachPoint = '',
            rigScale = 1.0
            ):
        
        fkNeckControlGroup = cmds.group(n = self.Prefix + SERigNaming.s_FKPrefix + 'Neck' + SERigNaming.sControlGroup, em = 1, 
                                        p = self.FKControlGroup)

        # Attach fk neck to the spine.
        if cmds.objExists(fkNeckAttachPoint):
            cmds.parentConstraint(fkNeckAttachPoint, fkNeckControlGroup)

        # Create FK neck controls.
        preParent = fkNeckControlGroup
        curFKJnt = None
        nextFKJnt = None
        fkJoints = neckJoints
        for i in range(len(fkJoints) - 1):
            curFKJnt = fkJoints[i]
            nextFKJnt = fkJoints[i + 1]
            curFKJntLoc = SEMathHelper.getWorldPosition(curFKJnt)
            nextFKJntLoc = SEMathHelper.getWorldPosition(nextFKJnt)
            distance = SEMathHelper.getDistance3(curFKJntLoc, nextFKJntLoc)
            if i != (len(fkJoints) - 2):
                distance *= 0.618
                curScaleYZ = 14
            else:
                distance *= 3
                curScaleYZ = 18

            curFKControl = SERigControl.RigCubeControl(
                                    rigSide = self.RigSide,
                                    rigType = self.RigType,
                                    prefix = SERigNaming.sFKPrefix + fkJoints[i], 
                                    translateTo = curFKJnt,
                                    rotateTo = curFKJnt,
                                    scale = rigScale,
                                    parent = preParent,
                                    lockChannels = ['t', 's', 'v'],
                                    cubeScaleX = distance,
                                    cubeScaleY = curScaleYZ,
                                    cubeScaleZ = curScaleYZ,
                                    transparency = 0.75
                                    )
            self.FKNeckControls.append(curFKControl)

            cmds.orientConstraint(curFKControl.ControlObject, curFKJnt)
            cmds.pointConstraint(curFKControl.ControlObject, curFKJnt)

            preParent = curFKControl.ControlObject
