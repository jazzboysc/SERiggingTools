import maya.cmds as cmds
from math import sqrt

def getWorldPosition(object):
    res = cmds.xform(object, q = True, t = True, ws = True)
    return res

def setWorldPosition(object, wPos):
    cmds.xform(object, t = wPos, ws = True)

def getDistance3(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]

    res = sqrt(dx*dx + dy*dy + dz*dz)
    return res

def movePivotTo(object, target):

    targetPos = cmds.xform(target, q = True, t = True, ws = True)
    cmds.move(targetPos[0], targetPos[1], targetPos[2], object + '.scalePivot',  object + '.rotatePivot', rpr = 1)