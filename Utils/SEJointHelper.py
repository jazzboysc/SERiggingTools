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

def getFirstChildGroup(parent):

    # Find child group.
    childGroup = None

    childGroupList = cmds.listRelatives(parent, c = 1, type = 'transform')
    if childGroupList != None:
        childGroup = childGroupList[0]

    return childGroup

def getFirstParentJoint(child):

    parentJoint = None
    parentJointList = cmds.listRelatives(child, p = 1, type = 'joint')
    if parentJointList == None:
        print('No parent joint found for:' + child)
    else:
        parentJoint = parentJointList[0]

    return parentJoint

def createNewParentJoint(child, alignNewParentToOldParent = False):
    newParent = None
    if cmds.objExists(child):
        oldParent = getFirstParentJoint(child)

        # Create a new parent for the child.
        newParent = cmds.createNode('joint', n = child + '_Par')
        if alignNewParentToOldParent and oldParent:
            cmds.delete(cmds.parentConstraint(oldParent, newParent, mo = 0))
        else:
            cmds.delete(cmds.parentConstraint(child, newParent, mo = 0))

        cmds.parent(child, newParent)
        cmds.makeIdentity(newParent, apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        # Parent new parent to old parent.
        if oldParent:
            cmds.parent(newParent, oldParent)

    return newParent

def isZeroRotation(joint, epsilon = 0.0001):
    res = False

    if cmds.objExists(joint):
        rx = cmds.getAttr(joint + '.rotateX')
        ry = cmds.getAttr(joint + '.rotateY')
        rz = cmds.getAttr(joint + '.rotateZ')
        dx = abs(rx)
        dy = abs(ry)
        dz = abs(rz)

        if dx <= epsilon and dy <= epsilon and dz <= epsilon:
            res = True

    return res

def createJointAlongCurve(curve, jointCount = 2, jointName = ''):
    joints = []

    if cmds.objExists(curve):
        if jointCount < 2:
            jointCount = 2

        preParent = None
        for i in range(0, jointCount):
            cmds.select(cl = True)
            if jointName == '':
                curJoint = cmds.joint()
            else:
                curJoint = cmds.joint(n = jointName + str(i))
            motionPath = cmds.pathAnimation(curJoint, c = curve, fractionMode = True)
            cmds.cutKey(motionPath + '.u', time = ())
            cmds.setAttr(motionPath + '.u', i*(1.0/(jointCount - 1)))
            cmds.delete(curJoint + '.tx', icn = True)
            cmds.delete(curJoint + '.ty', icn = True)
            cmds.delete(curJoint + '.tz', icn = True)
            cmds.delete(motionPath)

            if preParent:
                cmds.parent(curJoint, preParent)

            preParent = curJoint
            joints.append(curJoint)

        cmds.joint(joints[0], e = True, oj = 'xyz', sao = 'yup', ch = True, zso = True)
    else:
        cmds.warning('Cannot find curve:' + curve)

    return joints

def adjustIKTwist(ikHandle, 
                  startJoint, 
                  startTwistValue = -270, 
                  endTwistValue = 270, 
                  twistValueStep = 90,
                  epsilon = 0.01):
    isZeroRot = isZeroRotation(startJoint, epsilon = epsilon)
    if isZeroRot:
        print('No need twisting IK value for: %s' % startJoint)
        return

    twistValues = range(startTwistValue, endTwistValue + twistValueStep, twistValueStep)
    for twistValue in twistValues:
        cmds.setAttr(ikHandle + '.twist', twistValue)
        isZeroRot = isZeroRotation(startJoint, epsilon = epsilon)
        if isZeroRot:
            print('Twisting IK value succeeded for: %s' % startJoint)
            break

    if isZeroRot == False:
        cmds.error('Twisting IK value failed for: %s' % startJoint)