import maya.cmds as cmds
from ..Base import SERigComponent
from ..Base import SERigControl

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
                                         translateTo = spineCurveClusters[numSpineCVs / 2],
                                         scale = rigScale*6,
                                         parent = bodyCtrl.ControlObject
                                         )
