import maya.cmds as cmds
from ..Base import SERigComponent
from ..Base import SERigControl
from ..Base import SERigEnum
from ..Base import SERigNaming

def build(
    baseRig = None,
    spineJoints = [],
    rootJoint = '',
    spineCurve = '',
    bodyLocator = '',
    chestLocator = '',
    pelvisLocator = '',
    prefix = 'spine',
    rigScale = 1.0
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
                                         scale = rigScale*4,
                                         parent = rigComp.ControlsGrp
                                         )

    chestCtrl = SERigControl.SERigControl(
                                         rigSide = SERigEnum.eRigSide.RS_Center,
                                         rigType = SERigEnum.eRigType.RT_Spine,
                                         prefix = prefix + 'Chest', 
                                         translateTo = chestLocator,
                                         scale = rigScale*6,
                                         parent = bodyCtrl.ControlObject
                                         )

    pelvisCtrl = SERigControl.SERigControl(
                                         rigSide = SERigEnum.eRigSide.RS_Center,
                                         rigType = SERigEnum.eRigType.RT_Spine,
                                         prefix = prefix + 'Pelvis', 
                                         translateTo = pelvisLocator,
                                         scale = rigScale*6,
                                         parent = bodyCtrl.ControlObject
                                         )

    middleCtrl = SERigControl.SERigControl(
                                         rigSide = SERigEnum.eRigSide.RS_Center,
                                         rigType = SERigEnum.eRigType.RT_Spine,
                                         prefix = prefix + 'Middle', 
                                         translateTo = spineCurveClusters[middleCVIndex],
                                         scale = rigScale*6,
                                         parent = bodyCtrl.ControlObject
                                         )

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

    # Attach root joint.
    cmds.parentConstraint(pelvisCtrl.ControlObject, rootJoint, mo = 1)

    return {'RigComponent':rigComp}