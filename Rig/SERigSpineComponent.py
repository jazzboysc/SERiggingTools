import maya.cmds as cmds
from ..Base import SERigComponent
from ..Base import SERigControl
from ..Base import SERigEnum
from ..Base import SERigNaming

class SERigSimpleIKSpine(SERigComponent):
    def __init__(
                 self, 
                 prefix = 'new',
                 baseRig = None
                 ):
        pass

    def build(
            baseRig = None,
            spineJoints = [],
            rootJoint = '',
            spineCurve = '',
            bodyLocator = '',
            chestLocator = '',
            pelvisLocator = '',
            prefix = 'spine',
            rigScale = 1.0,
            spineIKTwist = 0.0
            ):
        # Create rig component.
        rigComp = SERigComponent.SERigComponent(prefix = prefix, baseRig = baseRig)

        # Create spine curve clusters.
        spineCurveCVs = cmds.ls(spineCurve + '.cv[*]', fl = 1)
        numSpineCVs = len(spineCurveCVs)
        middleCVIndex = numSpineCVs / 2
        spineCurveClusters = []

        for i in range(numSpineCVs):
            cluster = cmds.cluster(spineCurveCVs[i], n = prefix + 'Cluster%d' % (i + 1))[1]
            spineCurveClusters.append(cluster)

        cmds.hide(spineCurveClusters)

        # Create controls.
        bodyCtrl = SERigControl.SERigControl(
                                             rigSide = SERigEnum.eRigSide.RS_Center,
                                             rigType = SERigEnum.eRigType.RT_Spine,
                                             prefix = prefix + 'Body', 
                                             translateTo = bodyLocator,
                                             scale = rigScale*3,
                                             parent = rigComp.ControlsGrp
                                             )

        chestCtrl = SERigControl.SERigControl(
                                             rigSide = SERigEnum.eRigSide.RS_Center,
                                             rigType = SERigEnum.eRigType.RT_Spine,
                                             prefix = prefix + 'Chest', 
                                             translateTo = chestLocator,
                                             scale = rigScale*18,
                                             parent = bodyCtrl.ControlObject,
                                             shape = 'circleY'
                                             )

        pelvisCtrl = SERigControl.SERigControl(
                                             rigSide = SERigEnum.eRigSide.RS_Center,
                                             rigType = SERigEnum.eRigType.RT_Spine,
                                             prefix = prefix + 'Pelvis', 
                                             translateTo = pelvisLocator,
                                             scale = rigScale*18,
                                             parent = bodyCtrl.ControlObject,
                                             shape = 'circleY'
                                             )

        middleCtrl = SERigControl.SERigControl(
                                             rigSide = SERigEnum.eRigSide.RS_Center,
                                             rigType = SERigEnum.eRigType.RT_Spine,
                                             prefix = prefix + 'Middle', 
                                             translateTo = spineCurveClusters[middleCVIndex],
                                             scale = rigScale*18,
                                             parent = bodyCtrl.ControlObject,
                                             shape = 'circleY'
                                             )

        _adjustBodyCtrlShape(bodyCtrl, spineJoints, rigScale)

        # Attach controls.
        cmds.parentConstraint(chestCtrl.ControlObject, pelvisCtrl.ControlObject, middleCtrl.ControlGroup, sr = ['x', 'y', 'z'], mo = 1)

        # Attach clusters.
        cmds.parent(spineCurveClusters[(middleCVIndex + 1):], chestCtrl.ControlObject)
        cmds.parent(spineCurveClusters[middleCVIndex], middleCtrl.ControlObject)
        cmds.parent(spineCurveClusters[:middleCVIndex], pelvisCtrl.ControlObject)

        # Create IK handle.
        spineIK = cmds.ikHandle(n = prefix + '_ikh', sol = 'ikSplineSolver', sj = spineJoints[0], ee = spineJoints[-1], 
                                c = spineCurve, ccv = 0, parentCurve = 0)[0]

        cmds.hide(spineIK)
        cmds.parent(spineIK, rigComp.RigPartsFixedGrp)

        cmds.setAttr(spineIK + '.dTwistControlEnable', 1)
        cmds.setAttr(spineIK + '.dWorldUpType', 4)
        cmds.connectAttr(chestCtrl.ControlObject + '.worldMatrix[0]', spineIK + '.dWorldUpMatrixEnd')
        cmds.connectAttr(pelvisCtrl.ControlObject + '.worldMatrix[0]', spineIK + '.dWorldUpMatrix')

        cmds.setAttr(spineIK + '.twist', spineIKTwist)

        # Attach root joint.
        cmds.parentConstraint(pelvisCtrl.ControlObject, rootJoint, mo = 1)

        cmds.parent(spineCurve, rigComp.RigPartsFixedGrp)

        return {'RigComponent':rigComp}

    def _adjustBodyCtrlShape(bodyCtrl, spineJoints, rigScale):
        offsetGrp = cmds.group(em = 1, p = bodyCtrl.ControlObject)
        cmds.parent(offsetGrp, spineJoints[2])
        cluster = cmds.cluster(cmds.listRelatives(bodyCtrl.ControlObject, s = 1))[1]
        cmds.parent(cluster, offsetGrp)
        cmds.move(-40*rigScale, offsetGrp, moveZ = 1, relative = 1, objectSpace = 1)
        cmds.delete(bodyCtrl.ControlObject, ch = 1)