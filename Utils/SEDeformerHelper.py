import maya.cmds as cmds

#-----------------------------------------------------------------------------
# This function doesn't work, do not use.
def createSingleWrap(wrapped, wrapper):    
    wrapperBase = cmds.duplicate(wrapper, n = wrapper + 'Base')
    cmds.hide(wrapperBase)
    
    wrappedShape = cmds.listRelatives(wrapped, s = True)[0]
    wrapperShape = cmds.listRelatives(wrapper, s = True)[0]
    wrapperBaseShape = cmds.listRelatives(wrapperBase, s = True)[0]
    
    try:
        cmds.addAttr(wrapper, ln = 'dropoff', at = 'float', k = 1, dv = 4.0, hasMinValue = True, min = 0.0, hasMaxValue = True, max = 20.0)
    except:
        pass
    try:
        cmds.addAttr(wrapper, ln = 'smoothness', at = 'float', k = 1, dv = 0.0, hasMinValue = True, min = 0.0)
    except:
        pass
    try:
        cmds.addAttr(wrapper, ln = 'influenceType', at = 'long', k = 0, dv = 2, hasMinValue = True, min = 1, hasMaxValue = True, max = 2)
    except:
        pass
    
    wrapNode = cmds.createNode('wrap')
    
    cmds.connectAttr(wrapperBaseShape + '.worldMesh[0]', wrapNode + '.basePoints[0]')
    cmds.connectAttr(wrapperShape + '.worldMesh[0]', wrapNode + '.driverPoints[0]')
    
    cmds.connectAttr(wrapper + '.dropoff', wrapNode + '.dropoff[0]')
    cmds.connectAttr(wrapper + '.smoothness', wrapNode + '.smoothness[0]')
    cmds.connectAttr(wrapper + '.influenceType', wrapNode + '.inflType[0]')
    
    cmds.connectAttr(wrappedShape + '.worldMatrix[0]', wrapNode + '.geomMatrix')
    cmds.connectAttr(wrapNode + '.outputGeometry[0]', wrappedShape + '.inMesh')
#-----------------------------------------------------------------------------
def createMirrorShapeAlongLocalAxis(sculptShape, baseShape, localAxis = 'x', newShape = ''):    
    baseWrapped = cmds.duplicate(baseShape)[0]
    baseWrapper = cmds.duplicate(baseShape)[0]

    if localAxis == 'x' or localAxis == 'X':
        cmds.setAttr(baseWrapper + '.scaleX', -1)
    elif localAxis == 'y' or localAxis == 'Y':
        cmds.setAttr(baseWrapper + '.scaleY', -1)
    elif localAxis == 'z' or localAxis == 'Z':
        cmds.setAttr(baseWrapper + '.scaleZ', -1)
    else:
        cmds.error('Unknown mirror axis.')
        cmds.delete(baseWrapped, baseWrapper)
        return None

    tempBS = cmds.blendShape(sculptShape, baseWrapper)[0]

    cmds.select(cl = True)
    cmds.select(baseWrapped)
    cmds.select(baseWrapper, add = True)
    cmds.CreateWrap()
    cmds.select(cl = True)

    # TODO:
    # Cannot guarantee name is 'wrap1', hard coded wrap node name here is problematic.
    cmds.setAttr('wrap1.exclusiveBind', 1)

    cmds.setAttr(tempBS + '.' + sculptShape, 1)

    res = cmds.duplicate(baseWrapped, name = newShape)[0]
    cmds.delete(baseWrapped, baseWrapper)

    return res
#-----------------------------------------------------------------------------