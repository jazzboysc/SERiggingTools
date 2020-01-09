import maya.cmds as cmds
import maya.OpenMaya as om
from maya.api.OpenMaya import MVector, MMatrix, MPoint

from math import sqrt
from ..Base import SERigNaming

def getWorldPosition(object):
    res = cmds.xform(object, q = True, t = True, ws = True)
    return res

def setWorldPosition(object, wPos):
    cmds.xform(object, t = wPos, ws = True)

def getWorldRotation(object):
    res = cmds.xform(object, q = True, ro = True, ws = True)
    return res

def setWorldRotation(object, wRot):
    cmds.xform(object, ro = wRot, ws = True)

def getDistance3(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]

    res = sqrt(dx*dx + dy*dy + dz*dz)
    return res

def getDistanceBetweenObjects(object1, object2):
    d = -1.0
    if cmds.objExists(object1) and cmds.objExists(object2):
        pos1 = getWorldPosition(object1)
        pos2 = getWorldPosition(object2)
        d = getDistance3(pos1, pos2)

    return d

def movePivotTo(object, target):

    targetPos = cmds.xform(target, q = True, t = True, ws = True)
    cmds.move(targetPos[0], targetPos[1], targetPos[2], object + '.scalePivot',  object + '.rotatePivot', rpr = 1)


def rayIntersect(mesh, point, direction):
    hitPoints = None
    try:
        cmds.select(cl = True)
        om.MGlobal.selectByName(mesh)
        sList = om.MSelectionList()

        om.MGlobal.getActiveSelectionList(sList)
        item = om.MDagPath()
        sList.getDagPath(0, item)
        item.extendToShape()

        fnMesh = om.MFnMesh(item)

        raySource = om.MFloatPoint(point[0], point[1], point[2], 1.0)
        rayDir = om.MFloatVector(direction[0], direction[1], direction[2])
        faceIds = None
        triIds = None
        idsSorted = False
        testBothDirections = False
        worldSpace = om.MSpace.kWorld
        maxParam = 999999
        accelParams = None
        sortHits = True
        hitPoints = om.MFloatPointArray()

        hitRayParams = om.MFloatArray()
        hitFaces = om.MIntArray()
        hitTris = None
        hitBarys1 = None
        hitBarys2 = None
        tolerance = 0.0001

        hit = fnMesh.allIntersections(raySource, rayDir, faceIds, triIds, idsSorted, worldSpace, maxParam,
                                            testBothDirections, accelParams, sortHits, hitPoints, hitRayParams, hitFaces,
                                            hitTris, hitBarys1, hitBarys2, tolerance)

        om.MGlobal.clearSelectionList()

    except:
        pass

    return hitPoints

def getWorldTransform(object):
    return MMatrix(cmds.xform(object, q = True, matrix = True, ws = True))
    
def getLocalVecToWorldSpace(object, vec = MVector.kXaxisVector):
    matrix = getWorldTransform(object)
    vec = (vec * matrix).normal()
    return vec

def getMeshVertices(mesh):
    cmds.select(cl = True)
    om.MGlobal.selectByName(mesh)
    sList = om.MSelectionList()

    om.MGlobal.getActiveSelectionList(sList)
    item = om.MDagPath()
    sList.getDagPath(0, item)
    item.extendToShape()

    fnMesh = om.MFnMesh(item)

    vertices = om.MPointArray()
    fnMesh.getPoints(vertices, om.MSpace.kObject)
    return vertices

def createFacialSkinProxyJoints(cageMesh, facialMesh):
    if not cmds.objExists(cageMesh) or not cmds.objExists(facialMesh):
        cmds.error('Cage mesh or facial mesh does not exist.')
        return

    vertices = getMeshVertices(cageMesh)
    proxyJnts = []
    for i in range(vertices.length()):
        proxyJnt = cmds.createNode('joint', n = SERigNaming.sFacialProxyJointPrefix + str(i))
        proxyJnts.append(proxyJnt)
        
        # Tagging skin proxy joints.
        cmds.setAttr(proxyJnt + '.type', 18)
        cmds.setAttr(proxyJnt + '.otherType', SERigNaming.sJointTagFacialProxy, type = 'string')
        cmds.setAttr(proxyJnt + '.radius', 0.5)

        cmds.setAttr(proxyJnt + '.tx', vertices[i].x)
        cmds.setAttr(proxyJnt + '.ty', vertices[i].y)
        cmds.setAttr(proxyJnt + '.tz', vertices[i].z)

    # Create a one-to-one influence relationship between cage mesh vertices and skin proxy joints. 
    cageMeshSC = cmds.skinCluster(proxyJnts, cageMesh, normalizeWeights = 2, maximumInfluences = 1)[0]

    # Bind skin proxy joints to facial mesh.
    facialMeshSC = cmds.skinCluster(proxyJnts, facialMesh, normalizeWeights = 2, maximumInfluences = 4)[0]

    cageMeshCurUVSet = cmds.polyUVSet(cageMesh, query = True, currentUVSet = True)[0]
    facialMeshCurUVSet = cmds.polyUVSet(facialMesh, query = True, currentUVSet = True)[0]

    # Transfer cage mesh's skin weights to facial mesh based on their current uv sets.
    cmds.copySkinWeights(ss = cageMeshSC, ds = facialMeshSC, noMirror = True, surfaceAssociation = 'closestPoint', 
        uvSpace = (cageMeshCurUVSet, facialMeshCurUVSet), influenceAssociation = 'closestJoint', normalize = True)

    # We have done skin weights transfer, unbind cage mesh's skin.
    cmds.skinCluster(cageMesh, e = True, ub = True)

