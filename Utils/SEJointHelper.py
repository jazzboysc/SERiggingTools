import maya.cmds as cmds
from ..Base import SERigEnum

def SE_ListHierarchy(topJoint, withEndJoints = True):
    listedJoints = cmds.listRelatives(topJoint, type = 'joint', ad = True)
    listedJoints.append(topJoint)
    listedJoints.reverse()

    res = listedJoints[:]

    if not withEndJoints:
        res = [j for j in listedJoints if cmds.listRelatives(j, c = 1, type = 'joint')]

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