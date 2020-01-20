import maya.cmds as cmds

from . import SERigObjectTypeHelper

def createRivetConstraint(surfaceGeometry, rivetObject, hideChannels = []):
    res = None

    if cmds.objExists(surfaceGeometry) and cmds.objExists(rivetObject):
        surfaceGeometryShape = cmds.listRelatives(surfaceGeometry, s = True)[0]
        closest = cmds.createNode('closestPointOnMesh')
        cmds.connectAttr(surfaceGeometryShape + '.outMesh', closest + '.inMesh')
        cmds.connectAttr(surfaceGeometryShape + '.worldMatrix[0]', closest + '.inputMatrix') # Must support world space surface geometry.
        pos = cmds.xform(rivetObject, rp = True, q = True, ws = True) # Must support world space rivet object.
        cmds.setAttr(closest + '.inPositionX', pos[0])
        cmds.setAttr(closest + '.inPositionY', pos[1])
        cmds.setAttr(closest + '.inPositionZ', pos[2])
        
        follicle = cmds.createNode('follicle')
        follicleTrans = cmds.listRelatives(follicle, type = 'transform', p = True)[0]
        cmds.connectAttr(follicle + '.outRotate', follicleTrans + '.rotate')
        cmds.connectAttr(follicle + '.outTranslate', follicleTrans + '.translate')
        cmds.connectAttr(surfaceGeometryShape + '.worldMatrix', follicle + '.inputWorldMatrix')
        cmds.connectAttr(surfaceGeometryShape + '.worldMesh', follicle + '.inputMesh')
        cmds.setAttr(follicle + '.simulationMethod', 0)
        
        u = cmds.getAttr(closest + '.result.parameterU')
        v = cmds.getAttr(closest + '.result.parameterV')
        cmds.setAttr(follicle + '.parameterU', u)
        cmds.setAttr(follicle + '.parameterV', v)
        
        cmds.parentConstraint(follicleTrans, rivetObject, mo = True)
        cmds.delete(closest)

        # Hide follicle channels.
        SERigObjectTypeHelper.hideTransObjectChannels(follicleTrans, hideChannels)

        res = follicleTrans

    else:
        cmds.warning('Failed creating rivet constraint for:' + surfaceGeometry + ' and ' + rivetObject)

    return res