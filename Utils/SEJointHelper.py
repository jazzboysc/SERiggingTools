import maya.cmds as cmds
from ..Base import SERigEnum

def listHierarchy(topJoint, withEndJoints = True):

    listedJoints = cmds.listRelatives(topJoint, type = 'joint', ad = True)
    listedJoints.append(topJoint)
    listedJoints.reverse()

    res = listedJoints[:]

    if not withEndJoints:
        res = [j for j in listedJoints if cmds.listRelatives(j, c = 1, type = 'joint')]

    return res

def duplicateHierarchy(topJoint, newPrefix = ''):

    res = []

    newJoints = cmds.duplicate(topJoint, n = newPrefix + topJoint, parentOnly = False, renameChildren = True)
    res.append(newJoints[0])
    for i in range(len(newJoints) - 1):
        oldName = newJoints[i + 1][:-1]
        newName = newPrefix + oldName
        cmds.rename(newJoints[i + 1], newName)
        res.append(newName)

    return res

def getJointSide(joint):

    token = joint.split('_')
    if token[0] == 'L' or token[0] == 'l':
        return SERigEnum.eRigSide.RS_Left
    elif token[0] == 'R' or token[0] == 'r':
        return SERigEnum.eRigSide.RS_Right
    elif token[0] == 'C' or token[0] == 'c':
        return SERigEnum.eRigSide.RS_Center
    else:
        return SERigEnum.eRigSide.RS_Unknown

def getFirstChildJoint(parent):

    # Find child joint.
    childJoint = None

    childJointList = cmds.listRelatives(parent, c = 1, type = 'joint')
    if childJointList != None:
        childJoint = childJointList[0]

    return childJoint

def getFirstParentJoint(child):

    parentJoint = None
    parentJointList = cmds.listRelatives(child, p = 1, type = 'joint')
    if parentJointList == None:
        print('No parent joint found for:' + child)
    else:
        parentJoint = parentJointList[0]

    return parentJoint