import maya.cmds as cmds
from . import SERigEnum
from . import SERigNaming

#-----------------------------------------------------------------------------
# Rig Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigControl():
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_X,
                 prefix = 'new', 
                 scale = 1.0, 
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v']
                 ):
        
        # Create control object and control group.

        ctrlObj = None
        ctrlGrp = None

        ctrlObj = self._createControlShape(rigSide, rigType, rigFacing, prefix, scale)
        if ctrlObj:
            # Parent to control group.
            ctrlGrp = cmds.group(n = prefix + SERigNaming.sControlGroup, em = 1)
            cmds.parent(ctrlObj, ctrlGrp)

            # Translate control group to target translation object.
            if cmds.objExists(translateTo):
                cmds.delete(cmds.pointConstraint(translateTo, ctrlGrp))

            # Rotate control group to target rotation object.
            if cmds.objExists(rotateTo):
                cmds.delete(cmds.orientConstraint(rotateTo, ctrlGrp))

            # Parent the control group to the given parent.
            if cmds.objExists(parent):
                cmds.parent(ctrlGrp, parent)

            # Lock control channels.
            singleAttributeLockList = []
            for lc in lockChannels:
                if lc in ['t', 'r', 's']:
                    for axis in ['x', 'y', 'z']:
                        attr = lc + axis
                        singleAttributeLockList.append(attr)
                else:
                    singleAttributeLockList.append(lc)

            for attr in singleAttributeLockList:
                cmds.setAttr(ctrlObj + '.' + attr, l = 1, k = 0)

        # Add public members.
        self.ControlObject = ctrlObj
        self.ControlGroup = ctrlGrp
        self.RigSide = rigSide
        self.RigType = rigType

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale):
        return None

#-----------------------------------------------------------------------------
# Rig Circle Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigCircleControl(RigControl):
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_X,
                 prefix = 'new', 
                 scale = 1.0, 
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v']
                 ):

        RigControl.__init__(self, rigSide, rigType, rigFacing, prefix, 
                            scale, translateTo, rotateTo, parent, lockChannels)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale):
        
        circleNormal = [1, 0, 0]
        if rigFacing == SERigEnum.eRigFacing.RF_X:
            circleNormal = [1, 0, 0]
        elif rigFacing == SERigEnum.eRigFacing.RF_Y:
            circleNormal = [0, 1, 0]
        elif rigFacing == SERigEnum.eRigFacing.RF_Z:
            circleNormal = [0, 0, 1]
        else:
            pass

        ctrlObj = cmds.circle(n = prefix + SERigNaming.sControl, ch = False, normal = circleNormal, radius = scale)[0]

        # Set control color.
        ctrlShape = cmds.listRelatives(ctrlObj, s = 1)[0]
        cmds.setAttr(ctrlShape + '.ove', 1)

        if rigSide == SERigEnum.eRigSide.RS_Left:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Blue)
        elif rigSide == SERigEnum.eRigSide.RS_Right:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Red)
        elif rigSide == SERigEnum.eRigSide.RS_Center:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Yellow)
        else:
            # TODO:
            pass

        return ctrlObj