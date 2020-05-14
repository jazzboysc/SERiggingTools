import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
import re

from . import SEStringHelper
from ..Base import SERigNaming
from ..Base import SERigEnum
from ..Rig import SERigHumanFacialComponent

#-----------------------------------------------------------------------------
def getMeshVertexPosition(vtxName):
    # Get vertex number and object having that vertex
    testVtx = re.search('(?<=\[)(?P<vtxNum>[\d]+)(?=\])', str(vtxName))
    if testVtx:
        vtxNum = int(testVtx.group('vtxNum'))
        vtxObj = vtxName.split('.')[0]
    else:
        return

    # Get Api MDagPath for object
    activList = om.MSelectionList()
    activList.add(vtxObj)
    pathDg = om.MDagPath()
    activList.getDagPath(0, pathDg)

    # Iterate over all the mesh vertices and get position of required vtx
    mItVtx = om.MItMeshVertex(pathDg)
    vtxPos = []
    while not mItVtx.isDone():
        if mItVtx.index() == vtxNum:
            point = om.MPoint()
            point = mItVtx.position(om.MSpace.kWorld)
            vtxPos = [round(point.x, 5), round(point.y, 5), round(point.z, 5)]
            break
        mItVtx.next()

    return vtxPos
#-----------------------------------------------------------------------------
def batchRemovePrefix():
    selected = cmds.ls(sl = 1)
    for i in selected:
        newName = SEStringHelper.SE_RemovePrefix(i)
        cmds.rename(i, newName)
#-----------------------------------------------------------------------------
def _matchSourceBlendshapesToTarget(source, target):
    if not cmds.objExists(source) or not cmds.objExists(target):
        return

    sourceInputTargets = []
    bs = getConnectedInputBlendshapeNode(source)
    if bs:
        sourceInputTargets = cmds.listConnections(bs + '.inputTarget')
    cmds.delete(source, ch = 1)

    # Reset source transformation.
    cmds.setAttr(source + '.tx', 0)
    cmds.setAttr(source + '.ty', 0)
    cmds.setAttr(source + '.tz', 0)

    # Temporally disable target deformation otherwise we cannot match the source and target correctly.
    for node in cmds.listHistory(target):
        if cmds.nodeType(node) == 'skinCluster' or cmds.nodeType(node) == 'blendShape':
            cmds.setAttr(node + '.envelope', 0.0)

    sourcePos = getMeshVertexPosition(source + '.vtx[0]')
    targetPos = getMeshVertexPosition(target + '.vtx[0]')
    dx = targetPos[0] - sourcePos[0]
    dy = targetPos[1] - sourcePos[1]
    dz = targetPos[2] - sourcePos[2]

    cmds.setAttr(source + '.tx', dx)
    cmds.setAttr(source + '.ty', dy)
    cmds.setAttr(source + '.tz', dz)
    cmds.makeIdentity(source, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

    # Update all the source input targets to match our target mesh and freeze them.
    for sourceInputTarget in sourceInputTargets:
        cmds.setAttr(sourceInputTarget + '.tx', dx)
        cmds.setAttr(sourceInputTarget + '.ty', dy)
        cmds.setAttr(sourceInputTarget + '.tz', dz)
        cmds.makeIdentity(sourceInputTarget, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

    # Recreate blendshape node.
    cmds.blendShape(sourceInputTargets, source)

    # Restore target deformation.
    for node in cmds.listHistory(target):
        if cmds.nodeType(node) == 'skinCluster' or cmds.nodeType(node) == 'blendShape':
            cmds.setAttr(node + '.envelope', 1.0)
#-----------------------------------------------------------------------------
def matchSourceBlendshapesToTarget():
    selected = cmds.ls(sl = 1)
    source = selected[0]
    target = selected[1]

    _matchSourceBlendshapesToTarget(source, target)
#-----------------------------------------------------------------------------
def connectFACSDataBufferToAUBlendshape(facsDataBuffer, auBlendshapeNode, connectionMap = None):
    if connectionMap == None:
        connectionMap = SERigNaming.dataBufferAUsToBlendshapeAUsTable

    for auType in SERigEnum.facialActionUnitTypeList:
        src = SERigHumanFacialComponent.getFacialActionUnitAttrName(facsDataBuffer, auType)
        key = SERigNaming.auAttrList[auType]
        value = connectionMap[key]
        dst = getBlendshapTargetNameByMatchName(auBlendshapeNode, value, True)

        #print src,dst
        #print key,value
        if src and dst:
            cmds.connectAttr(src, dst, f = 1)
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
def getConnectedOutputBlendshapeNode(inputShape):
    # TODO:
    # Return the first connection that is blendshape.
    blsNode = cmds.listConnections(inputShape + '.worldMesh[0]')
    if blsNode:
        blsNode = blsNode[0]

    return blsNode
#-----------------------------------------------------------------------------
def getConnectedInputBlendshapeNode(inputShape):
    # TODO:
    # Return the first connection that is blendshape.
    blsNode = cmds.listConnections(inputShape + '.inMesh')
    if blsNode:
        blsNode = blsNode[0]

    return blsNode
#-----------------------------------------------------------------------------
def getConnectedBaseShape(inputShape):
    bsNode = getConnectedOutputBlendshapeNode(inputShape)
    res = cmds.listConnections(bsNode + '.outputGeometry[0]')[0]
    return res
#-----------------------------------------------------------------------------
def getBlendshapTargetIndexByName(blsNode, targetName, matchExactly = True, tokenSeparator = '_'):
    attr = blsNode + '.w[{}]'
    weightCount = cmds.blendShape(blsNode, q = True, wc = True)
    for index in xrange(weightCount):
        aliasName = cmds.aliasAttr(attr.format(index), q = True)
        if matchExactly:
            if aliasName == targetName:
                return index
        else:
            match = True
            aliasNameTokens = aliasName.split(tokenSeparator)

            for aliasNameToken in aliasNameTokens:
                if targetName.find(aliasNameToken) == -1:
                    match = False
                    break
            if match:
                return index

    return -1
#-----------------------------------------------------------------------------
def getBlendshapTargetNameByMatchName(blsNode, matchName, matchExactly = True, tokenSeparator = '_'):
    attr = blsNode + '.w[{}]'
    weightCount = cmds.blendShape(blsNode, q = True, wc = True)
    for index in xrange(weightCount):
        aliasName = cmds.aliasAttr(attr.format(index), q = True)
        if matchExactly:
            if aliasName == matchName:
                return blsNode + '.' + aliasName
        else:
            match = True
            aliasNameTokens = aliasName.split(tokenSeparator)

            for aliasNameToken in aliasNameTokens:
                if matchName.find(aliasNameToken) == -1:
                    match = False
                    break
            if match:
                return blsNode + '.' + aliasName

    return None
#-----------------------------------------------------------------------------
def getConnectedShapeInverter(inputShape):
    shapeInverterNode = cmds.listConnections(inputShape + '.outMesh')
    if shapeInverterNode:
        shapeInverterNode = shapeInverterNode[0]
        nodeType = cmds.nodeType(shapeInverterNode)
        if nodeType == 'cvShapeInverter':
            return shapeInverterNode
    
    return None
#-----------------------------------------------------------------------------
def updateSymmetricalBlendshape(cleanBaseMesh, createIfNotFound = True, pattern_R = 'R', pattern_r = 'r', pattern_L = 'L', pattern_l = 'l'):
    """Update symmetrical blendshape mesh for current selected mesh.

    @param[in] cleanBaseMesh A clean base mesh which has no inputs or outputs.
    @param[in] createIfNotFound Whether or not create a new mesh if symmetrical mesh is not found.
    @param[in] pattern_R Right side suffix pattern for the mesh name.
    @param[in] pattern_r Right side suffix pattern for the mesh name.
    @param[in] pattern_L Left side suffix pattern for the mesh name.
    @param[in] pattern_l Left side suffix pattern for the mesh name.
    @return Nothing.
    """

    selected = cmds.ls(sl = 1)
    if len(selected) != 1:
        cmds.warning('Please select one blendshape mesh.')
        return
    selected = selected[0]
    parentGrp = cmds.listRelatives(selected, p = True)
    if parentGrp:
        parentGrp = parentGrp[0]

    findRes = findSymmetricalBlendshape(selected, pattern_R, pattern_r, pattern_L, pattern_l)
    if findRes == None:
        cmds.warning('Unable to update symmetrical blendshape.')
        return
    symmetricalBS = findRes[0]

    if symmetricalBS:
        # Symmetrical blendshape exists, update shape.        
        selectedClean = cmds.duplicate(selected, rr = True)[0]
        newMirrorShape = createMirrorShapeAlongLocalAxis(selectedClean, cleanBaseMesh, newShape = symmetricalBS)
        cmds.showHidden(newMirrorShape)
        
        # If symmetrical shape is connected to a blendshape node, then update the connection.
        connectedBlendshapeNodeAttr = cmds.listConnections(symmetricalBS + '.worldMesh[0]', plugs = 1)
        if connectedBlendshapeNodeAttr:
            connectedBlendshapeNodeAttr = connectedBlendshapeNodeAttr[0]
            cmds.disconnectAttr(symmetricalBS + '.worldMesh[0]', connectedBlendshapeNodeAttr)
            cmds.connectAttr(newMirrorShape + '.worldMesh[0]', connectedBlendshapeNodeAttr)

        # If symmetrical shape is connected to a shape inverter node, then update the connection.
        shapeInverterNode = getConnectedShapeInverter(symmetricalBS)
        if shapeInverterNode:
            cmds.disconnectAttr(symmetricalBS + '.outMesh', shapeInverterNode + '.correctiveMesh')
            cmds.connectAttr(newMirrorShape + '.outMesh', shapeInverterNode + '.correctiveMesh')

        tx = cmds.getAttr(symmetricalBS + '.tx')
        ty = cmds.getAttr(symmetricalBS + '.ty')
        tz = cmds.getAttr(symmetricalBS + '.tz')
        cmds.setAttr(newMirrorShape + '.tx', tx)
        cmds.setAttr(newMirrorShape + '.ty', ty)
        cmds.setAttr(newMirrorShape + '.tz', tz)
        
        cmds.delete(symmetricalBS)
        cmds.delete(selectedClean)
        cmds.rename(newMirrorShape, symmetricalBS)

        if parentGrp:
            cmds.parent(symmetricalBS, parentGrp)
    else:
        # Symmetrical blendshape does not exist, possibly create a new shape.
        if createIfNotFound:
            print('Creating new symmetrical blendshape for: ' + selected)
            
            # Create new mirror shape.
            selectedClean = cmds.duplicate(selected, rr = True)[0]
            newMirrorShape = createMirrorShapeAlongLocalAxis(selectedClean, cleanBaseMesh, newShape = findRes[2])
            cmds.showHidden(newMirrorShape)
            cmds.delete(selectedClean)

            if parentGrp:
                cmds.parent(newMirrorShape, parentGrp)

            baseShape = getConnectedBaseShape(selected)
            blsNode = getConnectedOutputBlendshapeNode(selected)

            # Possibly add new mirror shape to the blendshape node.
            if blsNode:
                newTargetIndex = cmds.blendShape(blsNode, q = True, wc = True) + 1
                cmds.blendShape(baseShape, e = True, t = (baseShape, newTargetIndex, newMirrorShape, 1.0))

        else:
            print('No new symmetrical blendshape created for: ' + selected)
#-----------------------------------------------------------------------------