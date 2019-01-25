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
# Rig Simple Human Neck Class
# Sun Che
#-----------------------------------------------------------------------------
class RigSimpleHumanNeck(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Center,
                 rigType = SERigEnum.eRigType.RT_NeckComponent
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

        # Create FK neck and head controls.
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
            curRigType = 0
            curRigControlIndex = 0
            if i != (len(fkJoints) - 2):
                # Neck FK.
                distance *= 0.618
                curScaleYZ = 14
                curRigType = SERigEnum.eRigType.RT_NeckFK
                curRigControlIndex = i
            else:
                # Head FK.
                distance *= 3
                curScaleYZ = 18
                curRigType = SERigEnum.eRigType.RT_HeadFK
                curRigControlIndex = 0

            curFKControl = SERigControl.RigCubeControl(
                                    rigSide = self.RigSide,
                                    rigType = curRigType,
                                    rigControlIndex = curRigControlIndex,
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
            SERigObjectTypeHelper.linkRigObjects(self.TopGrp, curFKControl.ControlGroup, 'FKControl' + str(i), 'ControlOwner')

            cmds.orientConstraint(curFKControl.ControlObject, curFKJnt)
            cmds.pointConstraint(curFKControl.ControlObject, curFKJnt)

            preParent = curFKControl.ControlObject


#-----------------------------------------------------------------------------
# Rig Muscle Spline Human Neck Class
# Sun Che
#-----------------------------------------------------------------------------
class RigMuscleSplineHumanNeck(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None,
                 rigSide = SERigEnum.eRigSide.RS_Center,
                 rigType = SERigEnum.eRigType.RT_NeckComponent
                 ):

        RigComponent.__init__(self, prefix, baseRig, rigSide, rigType)

        # Add public members.

    def build(
            self,
            neckJoints = [],
            rootJoint = '',
            fkNeckAttachPoint = '',
            rigScale = 1.0
            ):
        pass
