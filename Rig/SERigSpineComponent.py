import maya.cmds as cmds
from ..Base.SERigComponent import RigComponent
from ..Base.SERigControl import RigControl
from ..Base import SERigEnum
from ..Base import SERigNaming

class RigSimpleIKSpine(RigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None
                 ):
        RigComponent.__init__(self, prefix, baseRig)

    def build(
            self,
            spineJoints = [],
            rootJoint = '',
            bodyLocator = '',
            chestLocator = '',
            pelvisLocator = '',
            rigScale = 1.0
            ):

        # Create pelvis and chest proxy joints.
        pelvisProxyJoint = cmds.duplicate(spineJoints[0], n = spineJoints[0] + SERigNaming.s_Proxy, parentOnly = True)[0]
        chestBeginProxyJoint = cmds.duplicate(spineJoints[-1], n = spineJoints[-1] + SERigNaming.s_Proxy, parentOnly = True)[0]

        # Create IK controls.
        chestBeginCtrl = RigControl(
                                    rigSide = SERigEnum.eRigSide.RS_Center,
                                    rigType = SERigEnum.eRigType.RT_Spine,
                                    prefix = self.Prefix + 'Chest', 
                                    translateTo = chestBeginProxyJoint,
                                    rotateTo = chestBeginProxyJoint,
                                    scale = rigScale*20,
                                    parent = self.ControlsGrp
                                    )

        pelvisCtrl = RigControl(
                                rigSide = SERigEnum.eRigSide.RS_Center,
                                rigType = SERigEnum.eRigType.RT_Spine,
                                prefix = self.Prefix + 'Pelvis', 
                                translateTo = pelvisProxyJoint,
                                rotateTo = pelvisProxyJoint,
                                scale = rigScale*20,
                                parent = self.ControlsGrp
                                )

        cmds.parent(pelvisProxyJoint, chestBeginProxyJoint, self.JointsGrp)

        cmds.parentConstraint(chestBeginCtrl.ControlObject, chestBeginProxyJoint)
        cmds.parentConstraint(pelvisCtrl.ControlObject, pelvisProxyJoint)

        # Create IK handle.
        resList = cmds.ikHandle(n = self.Prefix + SERigNaming.s_SplineIKHandle, 
                                sol = 'ikSplineSolver', sj = spineJoints[0], ee = spineJoints[-1], ccv = 1, parentCurve = 0, numSpans = 4)
        spineIK = resList[0]
        spineCurve = resList[2]
        spineCurveNewName = self.Prefix + SERigNaming.s_Curve
        cmds.rename(spineCurve, spineCurveNewName)
                                                
        cmds.hide(spineIK)
        cmds.hide(spineCurveNewName)
        cmds.parent(spineIK, spineCurveNewName, self.RigPartsFixedGrp)

        cmds.select(pelvisProxyJoint, chestBeginProxyJoint, spineCurveNewName)
        cmds.skinCluster(toSelectedBones = 1, bindMethod = 0, nw = 1, wd = 0, mi = 5, omi = True, dr = 4, rui = True)

        # Make the spine twistable.
        cmds.setAttr(spineIK + '.dTwistControlEnable', 1)
        cmds.setAttr(spineIK + '.dWorldUpType', 4)
        cmds.connectAttr(pelvisCtrl.ControlObject + '.worldMatrix[0]', spineIK + '.dWorldUpMatrix')
        cmds.connectAttr(chestBeginCtrl.ControlObject + '.worldMatrix[0]', spineIK + '.dWorldUpMatrixEnd')

    #def build(
    #        baseRig = None,
    #        spineJoints = [],
    #        rootJoint = '',
    #        spineCurve = '',
    #        bodyLocator = '',
    #        chestLocator = '',
    #        pelvisLocator = '',
    #        prefix = 'spine',
    #        rigScale = 1.0,
    #        spineIKTwist = 0.0
    #        ):
    #    # Create rig component.
    #    rigComp = SERigComponent.SERigComponent(prefix = prefix, baseRig = baseRig)

    #    # Create spine curve clusters.
    #    spineCurveCVs = cmds.ls(spineCurve + '.cv[*]', fl = 1)
    #    numSpineCVs = len(spineCurveCVs)
    #    middleCVIndex = numSpineCVs / 2
    #    spineCurveClusters = []

    #    for i in range(numSpineCVs):
    #        cluster = cmds.cluster(spineCurveCVs[i], n = prefix + 'Cluster%d' % (i + 1))[1]
    #        spineCurveClusters.append(cluster)

    #    cmds.hide(spineCurveClusters)


    #    # Create IK handle.
    #    spineIK = cmds.ikHandle(n = prefix + '_ikh', sol = 'ikSplineSolver', sj = spineJoints[0], ee = spineJoints[-1], 
    #                            c = spineCurve, ccv = 0, parentCurve = 0)[0]

    #    cmds.hide(spineIK)
    #    cmds.parent(spineIK, rigComp.RigPartsFixedGrp)

    #    cmds.setAttr(spineIK + '.dTwistControlEnable', 1)
    #    cmds.setAttr(spineIK + '.dWorldUpType', 4)
    #    cmds.connectAttr(chestCtrl.ControlObject + '.worldMatrix[0]', spineIK + '.dWorldUpMatrixEnd')
    #    cmds.connectAttr(pelvisCtrl.ControlObject + '.worldMatrix[0]', spineIK + '.dWorldUpMatrix')

    #    cmds.setAttr(spineIK + '.twist', spineIKTwist)

    #    # Attach root joint.
    #    cmds.parentConstraint(pelvisCtrl.ControlObject, rootJoint, mo = 1)

    #    cmds.parent(spineCurve, rigComp.RigPartsFixedGrp)

    #    return {'RigComponent':rigComp}

    #def _adjustBodyCtrlShape(bodyCtrl, spineJoints, rigScale):
    #    offsetGrp = cmds.group(em = 1, p = bodyCtrl.ControlObject)
    #    cmds.parent(offsetGrp, spineJoints[2])
    #    cluster = cmds.cluster(cmds.listRelatives(bodyCtrl.ControlObject, s = 1))[1]
    #    cmds.parent(cluster, offsetGrp)
    #    cmds.move(-40*rigScale, offsetGrp, moveZ = 1, relative = 1, objectSpace = 1)
    #    cmds.delete(bodyCtrl.ControlObject, ch = 1)