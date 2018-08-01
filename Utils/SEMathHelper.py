import maya.cmds as cmds
from math import sqrt

def getWorldPosition(object):
    res = cmds.xform(object, q = True, t = True, ws = True)
    return res

def getDistance3(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]

    res = sqrt(dx*dx + dy*dy + dz*dz)
    return res
