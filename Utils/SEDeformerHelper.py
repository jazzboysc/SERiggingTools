import maya.cmds as cmds
import maya.mel as mel

from . import SEStringHelper

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
    mel.eval('doWrapArgList "7" { "1", "0", "1", "2", "1", "1", "0", "0" }')
    cmds.select(cl = True)

    cmds.setAttr(tempBS + '.' + sculptShape, 1)

    res = cmds.duplicate(baseWrapped, name = newShape)[0]
    cmds.delete(baseWrapped, baseWrapper)

    # Delete junk shape orig data.
    junkName = res + 'ShapeOrig'
    if cmds.objExists(junkName):
        cmds.delete(junkName)

    return res
#-----------------------------------------------------------------------------
def findSymmetricalBlendshape(inputShape, pattern_R = 'R', pattern_r = 'r', pattern_L = 'L', pattern_l = 'l'):
    if not cmds.objExists(inputShape):
        cmds.warning('Input shape does not exist: ' + inputShape)
        return None

    shapeName = SEStringHelper.SE_RemoveSuffix(inputShape)
    suffix = SEStringHelper.getSuffix(inputShape)
    if suffix == None:
        cmds.warning('Suffix not found for input shape: ' + inputShape)
        return None

    if suffix == pattern_R or suffix == pattern_r:
        # Try to find left side shape and suffix pattern.
        shapeName_L = shapeName + '_' + pattern_L
        shapeName_l = shapeName + '_' + pattern_l

        symmetricalBS = None
        symmetricalPattern = None
        if cmds.objExists(shapeName_L):
            symmetricalBS = shapeName_L
            symmetricalPattern = pattern_L
        elif cmds.objExists(shapeName_l):
            symmetricalBS = shapeName_l
            symmetricalPattern = pattern_l
        else:
            cmds.warning('Symmetrical blend shape does not exist for input shape: ' + inputShape)

        return [symmetricalBS, symmetricalPattern, shapeName_L]

    elif suffix == pattern_L or suffix == pattern_l:
        # Try to find right side shape and suffix pattern.
        shapeName_R = shapeName + '_' + pattern_R
        shapeName_r = shapeName + '_' + pattern_r

        symmetricalBS = None
        symmetricalPattern = None
        if cmds.objExists(shapeName_R):
            symmetricalBS = shapeName_R
            symmetricalPattern = pattern_R
        elif cmds.objExists(shapeName_l):
            symmetricalBS = shapeName_r
            symmetricalPattern = pattern_r
        else:
            cmds.warning('Symmetrical blend shape does not exist for input shape: ' + inputShape)

        return [symmetricalBS, symmetricalPattern, shapeName_R]
    
    else:
        # Blendshape that matches symmetrical pattern not found.
        cmds.warning('Blendshape that matches symmetrical pattern not found for input shape: ' + inputShape)
        return None 
#-----------------------------------------------------------------------------
def findConnectedBaseShape(inputShape):
    bsNode = cmds.listConnections(inputShape + '.worldMesh[0]')[0]
    res = cmds.listConnections(bsNode + '.outputGeometry[0]')[0]
    return res
#-----------------------------------------------------------------------------
def getBlendshapTargetIndexByName(blsNode, targetName):
    attr = blsNode + '.w[{}]'
    weightCount = cmds.blendShape(blsNode, q = True, wc = True)
    for index in xrange(weightCount):
        if cmds.aliasAttr(attr.format(index), q = True) == targetName:
            return index

    return -1
#-----------------------------------------------------------------------------
def updateSymmetricalBlendshape(cleanBaseMesh, createIfNotFound = True, pattern_R = 'R', pattern_r = 'r', pattern_L = 'L', pattern_l = 'l'):
    selected = cmds.ls(sl = 1)
    if len(selected) != 1:
        cmds.warning('Please select one blendshape mesh.')
        return
    selected = selected[0]
        
    findRes = findSymmetricalBlendshape(selected, pattern_R, pattern_r, pattern_L, pattern_l)
    if findRes == None:
        cmds.warning('Unable to update symmetrical blendshape.')
        return
    symmetricalBS = findRes[0]

    if symmetricalBS:
        # Symmetrical blendshape exists, update shape.
        connectedBlendshapeNodeAttr = cmds.listConnections(symmetricalBS + '.worldMesh[0]', p = 1)[0]
        
        selectedClean = cmds.duplicate(selected, rr = True)[0]
        newMirrorShape = createMirrorShapeAlongLocalAxis(selectedClean, cleanBaseMesh, newShape = symmetricalBS)
        cmds.showHidden(newMirrorShape)
        
        cmds.disconnectAttr(symmetricalBS + '.worldMesh[0]', connectedBlendshapeNodeAttr)
        cmds.connectAttr(newMirrorShape + '.worldMesh[0]', connectedBlendshapeNodeAttr)
        
        tx = cmds.getAttr(symmetricalBS + '.tx')
        ty = cmds.getAttr(symmetricalBS + '.ty')
        tz = cmds.getAttr(symmetricalBS + '.tz')
        cmds.setAttr(newMirrorShape + '.tx', tx)
        cmds.setAttr(newMirrorShape + '.ty', ty)
        cmds.setAttr(newMirrorShape + '.tz', tz)
        
        cmds.delete(symmetricalBS)
        cmds.delete(selectedClean)
        cmds.rename(newMirrorShape, symmetricalBS)
    else:
        # Symmetrical blendshape does not exist, possibly create a new shape.
        if createIfNotFound:
            print('Creating new symmetrical blendshape for: ' + selected)
            
            selectedClean = cmds.duplicate(selected, rr = True)[0]
            newMirrorShape = createMirrorShapeAlongLocalAxis(selectedClean, cleanBaseMesh, newShape = findRes[2])
            cmds.showHidden(newMirrorShape)

            cmds.delete(selectedClean)

            baseShape = findConnectedBaseShape(selected)

        else:
            print('No new symmetrical blendshape created for: ' + selected)
#-----------------------------------------------------------------------------