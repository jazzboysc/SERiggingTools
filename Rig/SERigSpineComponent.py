import maya.cmds as cmds
from ..Base.SERigComponent import RigComponent
from ..Base import SERigControl
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

        # Create upper body control.
        upperBodyCtrl = SERigControl.RigCubeControl(
                                rigSide = SERigEnum.eRigSide.RS_Center,
                                rigType = SERigEnum.eRigType.RT_Spine,
                                prefix = self.Prefix + 'UpperBody', 
                                translateTo = spineJoints[0],
                                rotateTo = spineJoints[0],
                                scale = rigScale*20,
                                parent = self.ControlsGrp,
                                cubeScaleX = 2.0,
                                cubeScaleY = 40.0,
                                cubeScaleZ = 40.0,
                                transparency = 0.8
                                )

        # Create pelvis and chest proxy joints.
        pelvisProxyJoint = cmds.duplicate(spineJoints[0], n = spineJoints[0] + SERigNaming.s_Proxy, parentOnly = True)[0]
        chestBeginProxyJoint = cmds.duplicate(spineJoints[-1], n = spineJoints[-1] + SERigNaming.s_Proxy, parentOnly = True)[0]

        # Create IK controls.
        chestBeginCtrl = SERigControl.RigCircleControl(
                                    rigSide = SERigEnum.eRigSide.RS_Center,
                                    rigType = SERigEnum.eRigType.RT_Spine,
                                    prefix = self.Prefix + 'Chest', 
                                    translateTo = chestBeginProxyJoint,
                                    rotateTo = chestBeginProxyJoint,
                                    scale = rigScale*20,
                                    parent = upperBodyCtrl.ControlObject
                                    )

        pelvisCtrl = SERigControl.RigCircleControl(
                                rigSide = SERigEnum.eRigSide.RS_Center,
                                rigType = SERigEnum.eRigType.RT_Spine,
                                prefix = self.Prefix + 'Pelvis', 
                                translateTo = pelvisProxyJoint,
                                rotateTo = pelvisProxyJoint,
                                scale = rigScale*25,
                                parent = upperBodyCtrl.ControlObject
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

        # Create FK joints.
        resCurve = cmds.rebuildCurve(spineCurveNewName, ch = 0, rpo = 0, rt = 0, end = 1, kr = 0, kcp = 0, kep = 1, kt = 0, s = 3, d = 1, tol = 0.00393701)[0]

        cmds.select(cl=1)
        jnt0 = cmds.joint(n = SERigNaming.sFKPrefix + spineJoints[0])
        cmds.delete(cmds.pointConstraint(spineJoints[0], jnt0))

        cmds.select(cl=1)
        jnt1 = cmds.joint(n = SERigNaming.sFKPrefix + 'C_Spine_0')
        cmds.select(resCurve + '.cv[1]')
        res = cmds.pointPosition()
        cmds.move(res[0], res[1], res[2], jnt1, rpr = 1)

        cmds.select(cl=1)
        jnt2 = cmds.joint(n = SERigNaming.sFKPrefix + 'C_Spine_1')
        cmds.select(resCurve + '.cv[2]')
        res = cmds.pointPosition()
        cmds.move(res[0], res[1], res[2], jnt2, rpr = 1)

        cmds.select(cl=1)
        jnt3 = cmds.joint(n = SERigNaming.sFKPrefix + spineJoints[-1])
        cmds.delete(cmds.pointConstraint(spineJoints[-1], jnt3))

        RefJnt = cmds.duplicate(jnt2, n =  'Ref_jnt', parentOnly = True)[0]
        cmds.move(0, 0, -10, RefJnt, r = 1, os = 1)

        cmds.delete(cmds.aimConstraint(jnt1, jnt0, offset = [0, 0, 0], w = 1, aim = [1, 0, 0], u = [0, 1, 0], worldUpType = 'object', worldUpObject = RefJnt))
        cmds.delete(cmds.aimConstraint(jnt2, jnt1, offset = [0, 0, 0], w = 1, aim = [1, 0, 0], u = [0, 1, 0], worldUpType = 'object', worldUpObject = RefJnt))
        cmds.delete(cmds.aimConstraint(jnt3, jnt2, offset = [0, 0, 0], w = 1, aim = [1, 0, 0], u = [0, 1, 0], worldUpType = 'object', worldUpObject = RefJnt))

        cmds.delete(cmds.orientConstraint(spineJoints[-1], jnt3))

        cmds.parent(jnt3, jnt2)
        cmds.parent(jnt2, jnt1)
        cmds.parent(jnt1, jnt0)
        cmds.parent(jnt0, self.JointsGrp)

        cmds.makeIdentity(jnt0, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        cmds.delete(RefJnt)
        cmds.delete(resCurve)

        # Attach FK root joint to upper body control.
        cmds.parentConstraint(upperBodyCtrl.ControlObject, jnt0, mo = 1)

        # Create FK spine_0 control.
        FKSpine0Ctrl = SERigControl.RigCubeControl(
                                rigSide = SERigEnum.eRigSide.RS_Center,
                                rigType = SERigEnum.eRigType.RT_Spine,
                                prefix = SERigNaming.sFKPrefix + self.Prefix + '_0', 
                                translateTo = jnt1,
                                rotateTo = jnt1,
                                scale = rigScale*20,
                                parent = upperBodyCtrl.ControlObject,
                                lockChannels = ['t', 's', 'v'],
                                cubeScaleX = 4.0,
                                cubeScaleY = 35.0,
                                cubeScaleZ = 35.0,
                                transparency = 0.75
                                )
        cmds.orientConstraint(FKSpine0Ctrl.ControlObject, jnt1)

        # Create FK spine_1 control.
        FKSpine1Ctrl = SERigControl.RigCubeControl(
                                rigSide = SERigEnum.eRigSide.RS_Center,
                                rigType = SERigEnum.eRigType.RT_Spine,
                                prefix = SERigNaming.sFKPrefix + self.Prefix + '_1', 
                                translateTo = jnt2,
                                rotateTo = jnt2,
                                scale = rigScale*20,
                                parent = FKSpine0Ctrl.ControlObject,
                                lockChannels = ['t', 's', 'v'],
                                cubeScaleX = 4.0,
                                cubeScaleY = 28.0,
                                cubeScaleZ = 28.0,
                                transparency = 0.75
                                )
        cmds.orientConstraint(FKSpine1Ctrl.ControlObject, jnt2)

        # Attach IK_ChestBegin control to FK spine_1 control.
        cmds.parent(chestBeginCtrl.ControlGroup, FKSpine1Ctrl.ControlObject)

        cmds.hide(jnt0, pelvisProxyJoint, chestBeginProxyJoint)

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