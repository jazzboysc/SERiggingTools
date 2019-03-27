import maya.cmds as cmds
import maya.OpenMaya as om
from maya.api.OpenMaya import MVector, MMatrix, MPoint

from math import sqrt

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
    return hitPoints

def getWorldTransform(object):
    return MMatrix(cmds.xform(object, q = True, matrix = True, ws = True))
    
def getLocalVecToWorldSpace(object, vec = MVector.kXaxisVector):
    matrix = getWorldTransform(object)
    vec = (vec * matrix).normal()
    return vec