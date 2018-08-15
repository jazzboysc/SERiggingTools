import maya.cmds as cmds
from ..Base.SERigComponent import RigComponent
from ..Base import SERigControl
from ..Base import SERigEnum
from ..Base import SERigNaming
from ..Utils import SEStringHelper
from ..Utils import SEMathHelper

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

        self.FootHelperJoints = None

    def build(
            self,
            legJoints = [],  # 0: hip, -1: toe, -2: ball, -3: ankle
            legPVLocator = '',
            rootJoint = '',
            footExtLocator = '',
            footIntLocator = '',
            footBaseLocator = '',
            footBaseSwiveLocator = '',
            footToeSwiveLocator = '',
            rigScale = 1.0
            ):

        # Create a map.
        self.FootHelperJoints = self.buildFootHelperJoints(legJoints, footExtLocator, footIntLocator, 
                                                           footBaseLocator, footBaseSwiveLocator, footToeSwiveLocator)

        # Measure foot size.
        footBaseLocation = SEMathHelper.getWorldPosition(self.FootHelperJoints[SERigNaming.sFootBaseJnt])
        footToeLocation = SEMathHelper.getWorldPosition(self.FootHelperJoints[SERigNaming.sFootToeProxy])
        footSize = SEMathHelper.getDistance3(footBaseLocation, footToeLocation)

        # Create foot IK main control.
        footIKMainControl = SERigControl.RigFootControl(
                                rigSide = SERigEnum.eRigSide.RS_Left,
                                rigType = SERigEnum.eRigType.RT_Foot,
                                prefix = 'FootIKMain_', 
                                scale = rigScale * 30, 
                                matchBoundingBoxScale = True,
                                scaleX = footSize,
                                scaleZ = footSize,
                                translateTo = self.FootHelperJoints[SERigNaming.sFootBaseJnt],
                                rotateTo = self.FootHelperJoints[SERigNaming.sFootBaseJnt],
                                parent = self.ControlsGrp, 
                                lockChannels = ['s', 'v'])

        # Attach foot helper joints to the foot IK main control.
        cmds.parentConstraint(footIKMainControl.ControlObject, self.FootHelperJoints[SERigNaming.sFootExtJnt], mo = 1)

        # Create IK leg joints.
        cmds.duplicate(legJoints[0], n = SERigNaming.sIKPrefix + legJoints[0], parentOnly = False)[0]

    def buildFootHelperJoints(
            self,
            legJoints = [],  # 0: hip, -1: toe, -2: ball, -3: ankle
            footExtLocator = '',
            footIntLocator = '',
            footBaseLocator = '',
            footBaseSwiveLocator = '',
            footToeSwiveLocator = ''
            ):

        nameNoPrefix = SEStringHelper.SE_RemovePrefix(footExtLocator)
        cmds.select(cl=1)
        footExtJnt = cmds.joint(n = nameNoPrefix + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(footExtLocator, footExtJnt))

        nameNoPrefix = SEStringHelper.SE_RemovePrefix(footIntLocator)
        cmds.select(cl=1)
        footIntJnt = cmds.joint(n = nameNoPrefix + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(footIntLocator, footIntJnt))

        nameNoPrefix = SEStringHelper.SE_RemovePrefix(footBaseLocator)
        cmds.select(cl=1)
        footBaseJnt = cmds.joint(n = nameNoPrefix + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(footBaseLocator, footBaseJnt))

        nameNoPrefix = SEStringHelper.SE_RemovePrefix(footBaseSwiveLocator)
        cmds.select(cl=1)
        footBaseSwiveJnt = cmds.joint(n = nameNoPrefix + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(footBaseSwiveLocator, footBaseSwiveJnt))

        nameNoPrefix = SEStringHelper.SE_RemovePrefix(footToeSwiveLocator)
        cmds.select(cl=1)
        footToeSwiveJnt = cmds.joint(n = nameNoPrefix + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(footToeSwiveLocator, footToeSwiveJnt))

        cmds.select(cl=1)
        footToeProxy = cmds.joint(n = legJoints[-1] + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(legJoints[-1], footToeProxy))

        cmds.select(cl=1)
        footBallProxy = cmds.joint(n = legJoints[-2] + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(legJoints[-2], footBallProxy))

        cmds.select(cl=1)
        footAnkleProxy = cmds.joint(n = legJoints[-3] + SERigNaming.s_Proxy)
        cmds.delete(cmds.parentConstraint(legJoints[-3], footAnkleProxy))

        cmds.parent(footAnkleProxy, footBallProxy)
        cmds.parent(footBallProxy, footToeProxy)
        cmds.parent(footToeProxy, footToeSwiveJnt)
        cmds.parent(footToeSwiveJnt, footBaseSwiveJnt)
        cmds.parent(footBaseSwiveJnt, footBaseJnt)
        cmds.parent(footBaseJnt, footIntJnt)
        cmds.parent(footIntJnt, footExtJnt)

        # Attach foot helper joints to component's JointsGroup.
        cmds.parent(footExtJnt, self.JointsGrp)
        cmds.makeIdentity(footExtJnt, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        # Create foot PVs for foot IK handles.
        toeProxyPVlocator = cmds.spaceLocator(n = footToeProxy + SERigNaming.s_PoleVector)
        cmds.delete(cmds.parentConstraint(footToeProxy, toeProxyPVlocator))
        cmds.parent(toeProxyPVlocator, footToeProxy)
        cmds.move(0, 0, 5, toeProxyPVlocator, r = 1, os = 1)

        ballProxyPVlocator = cmds.spaceLocator(n = footBallProxy + SERigNaming.s_PoleVector)
        cmds.delete(cmds.parentConstraint(footBallProxy, ballProxyPVlocator))
        cmds.parent(ballProxyPVlocator, footBallProxy)
        cmds.move(0, 0, 5, ballProxyPVlocator, r = 1, os = 1)

        return {
                SERigNaming.sFootExtJnt:footExtJnt,
                SERigNaming.sFootIntJnt:footIntJnt,
                SERigNaming.sFootBaseJnt:footBaseJnt,
                SERigNaming.sFootBaseSwiveJnt:footBaseSwiveJnt,
                SERigNaming.sFootToeSwiveJnt:footToeSwiveJnt,
                SERigNaming.sFootToeProxy:footToeProxy,
                SERigNaming.sFootBallProxy:footBallProxy,
                SERigNaming.sFootAnkleProxy:footAnkleProxy,
                SERigNaming.sToeProxyPVlocator:toeProxyPVlocator,
                SERigNaming.sBallProxyPVlocator:ballProxyPVlocator
                }