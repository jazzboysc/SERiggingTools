import maya.cmds as cmds

def createRivetConstraint(surfaceGeometry, rivetObject):
    res = None

    if cmds.objExists(surfaceGeometry) and cmds.objExists(rivetObject):
        closest = cmds.createNode('closestPointOnMesh')
        cmds.connectAttr(surfaceGeometry + '.outMesh', closest + '.inMesh')
        cmds.connectAttr(surfaceGeometry + '.worldMatrix[0]', closest + '.inputMatrix') # Must support world space surface geometry.
        pos = cmds.xform(rivetObject, rp = True, q = True, ws = True) # Must support world space rivet object.
        cmds.setAttr(closest + '.inPositionX', pos[0])
        cmds.setAttr(closest + '.inPositionY', pos[1])
        cmds.setAttr(closest + '.inPositionZ', pos[2])
        
        follicle = cmds.createNode('follicle')
        follicleTrans = cmds.listRelatives(follicle, type = 'transform', p = True)[0]
        cmds.connectAttr(follicle + '.outRotate', follicleTrans + '.rotate')
        cmds.connectAttr(follicle + '.outTranslate', follicleTrans + '.translate')
        cmds.connectAttr(surfaceGeometry + '.worldMatrix', follicle + '.inputWorldMatrix')
        cmds.connectAttr(surfaceGeometry + '.outMesh', follicle + '.inputMesh')
        cmds.setAttr(follicle + '.simulationMethod', 0)
        
        u = cmds.getAttr(closest + '.result.parameterU')
        v = cmds.getAttr(closest + '.result.parameterV')
        cmds.setAttr(follicle + '.parameterU', u)
        cmds.setAttr(follicle + '.parameterV', v)
        
        cmds.parentConstraint(follicleTrans, rivetObject, mo = True)
        cmds.delete(closest)

        res = follicle

    else:
        cmds.warning('Failed creating rivet constraint for:' + surfaceGeometry + ' and ' + rivetObject)

    return res