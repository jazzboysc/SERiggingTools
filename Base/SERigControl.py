import maya.cmds as cmds
from . import SERigEnum
from . import SERigNaming
from ..Utils import SERigObjectTypeHelper
from ..Utils import SEMathHelper
from maya.api.OpenMaya import MVector, MMatrix, MPoint

def setControlRGBColor(control, color = (1.0, 1.0, 1.0)):
    
    rgb = ("R","G","B")
    cmds.setAttr(control + ".overrideEnabled",1)
    cmds.setAttr(control + ".overrideRGBColors",1)

    for channel, color in zip(rgb, color):    
        cmds.setAttr(control + ".overrideColor%s" %channel, color)

#-----------------------------------------------------------------------------
# Rig Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigControl():
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_X,
                 rigControlIndex = 0,
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v'],
                 flipScaleX = False,
                 flipScaleY = False,
                 flipScaleZ = False,
                 preRotateX = 0.0,
                 preRotateY = 0.0,
                 preRotateZ = 0.0,
                 overrideControlColor = False,
                 controlColor = (0.0, 0.0, 0.0),
                 fitToSurroundingMeshes = False,
                 surroundingMeshes = [],
                 postFitScale = 1.0,
                 overrideFitRayDirection = False, 
                 fitRayDirection = (0, 1, 0)
                 ):
        
        # Create control object and control group.

        ctrlObj = None
        ctrlGrp = None

        ctrlObj = self._createControlShape(rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale, 
                                           preRotateX, preRotateY, preRotateZ, overrideControlColor, controlColor,
                                           fitToSurroundingMeshes, surroundingMeshes, postFitScale, translateTo, rotateTo,
                                           overrideFitRayDirection = overrideFitRayDirection, fitRayDirection = fitRayDirection)
        if ctrlObj:
            # Parent to control group.
            ctrlGrp = cmds.group(n = prefix + SERigNaming.sControlGroup, em = 1)
            cmds.parent(ctrlObj, ctrlGrp)

            # Link to control group.
            SERigObjectTypeHelper.linkRigObjects(ctrlGrp, ctrlObj, 'ControlObject')

            # Translate control group to target translation object.
            if cmds.objExists(translateTo):
                cmds.delete(cmds.pointConstraint(translateTo, ctrlGrp))

            # Rotate control group to target rotation object.
            if cmds.objExists(rotateTo):
                cmds.delete(cmds.orientConstraint(rotateTo, ctrlGrp))

            # Parent the control group to the given parent.
            if cmds.objExists(parent):
                cmds.parent(ctrlGrp, parent)

            if rigSide == SERigEnum.eRigSide.RS_Right and flipScaleX == True:
                cmds.setAttr(ctrlGrp + '.scaleX', -1)

            if rigSide == SERigEnum.eRigSide.RS_Right and flipScaleY == True:
                cmds.setAttr(ctrlGrp + '.scaleY', -1)

            if rigSide == SERigEnum.eRigSide.RS_Right and flipScaleZ == True:
                cmds.setAttr(ctrlGrp + '.scaleZ', -1)

            # Lock control channels.
            singleAttributeLockList = []
            for lc in lockChannels:
                if lc in ['t', 'r', 's']:
                    for axis in ['x', 'y', 'z']:
                        attr = lc + axis
                        singleAttributeLockList.append(attr)
                else:
                    singleAttributeLockList.append(lc)

            for attr in singleAttributeLockList:
                cmds.setAttr(ctrlObj + '.' + attr, l = 1, k = 0)

        # Add public members.
        self.ControlObject = ctrlObj
        self.ControlGroup = ctrlGrp
        self.RigSide = rigSide
        self.RigType = rigType
        self.RigControlIndex = rigControlIndex
        self.FlipScaleX = flipScaleX
        self.FlipScaleY = flipScaleY
        self.FlipScaleZ = flipScaleZ
        self.Prefix = prefix
        self.TranslateTo = translateTo, 
        self.RotateTo = rotateTo, 

        # Add component instance info to top group.
        cmds.addAttr(self.ControlGroup, ln = 'RigSide', dt = 'string')
        cmds.addAttr(self.ControlGroup, ln = 'RigType', dt = 'string')
        cmds.addAttr(self.ControlGroup, ln = 'RigControlIndex', dt = 'string')

        cmds.setAttr(self.ControlGroup + '.' + 'RigSide', SERigEnum.eRigSideStringTable[self.RigSide], type = 'string', l = 1)
        cmds.setAttr(self.ControlGroup + '.' + 'RigType', SERigEnum.eRigTypeStringTable[self.RigType], type = 'string', l = 1)
        cmds.setAttr(self.ControlGroup + '.' + 'RigControlIndex', str(self.RigControlIndex), type = 'string', l = 1)

        # Create control type node.
        SERigObjectTypeHelper.createRigObjectTypeAttr(self.ControlGroup, 'RigControlType')

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale, overrideControlColor, controlColor, 
                            fitToSurroundingMeshes, surroundingMeshes, postFitScale, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection):
        return None

    def _getFitSize(self, surroundingMeshes, translateTo, rotateTo, overrideFitRayDirection = False, fitRayDirection = (0, 0, 1)):
        minDis = 9999999
        secondMinDis = minDis
        minHit  = None
        secondMinHit = None
        rayDir = None
        if overrideFitRayDirection:
            rayDir = fitRayDirection
        else:
            if rotateTo and cmds.objExists(rotateTo):
                rayDir = SEMathHelper.getLocalVecToWorldSpace(rotateTo, MVector.kZaxisVector)
            else:
                cmds.warning('RotateTo object does not exist. Using default fit ray direction.')
                rayDir = fitRayDirection

        rayStartPos = SEMathHelper.getWorldPosition(translateTo)

        for mesh in surroundingMeshes:
            res = SEMathHelper.rayIntersect(mesh, rayStartPos, rayDir)
            if res[0]:
                curFirstHit = (res[0].x, res[0].y, res[0].z)
                curDis = SEMathHelper.getDistance3(curFirstHit, rayStartPos)
                if curDis < minDis:
                    minDis = curDis
                    minHit = curFirstHit
                elif curDis < secondMinDis:
                    secondMinDis = curDis
                    secondMinHit = curFirstHit

        res = None
        if secondMinHit:
            # Create debug sphere.
            #s = cmds.sphere()[0]
            #cmds.setAttr(s + '.tx', secondMinHit[0])
            #cmds.setAttr(s + '.ty', secondMinHit[1])
            #cmds.setAttr(s + '.tz', secondMinHit[2])
            res = secondMinDis
        elif minHit:
            # Create debug sphere.
            #s = cmds.sphere()[0]
            #cmds.setAttr(s + '.tx', minHit[0])
            #cmds.setAttr(s + '.ty', minHit[1])
            #cmds.setAttr(s + '.tz', minHit[2])
            res = minDis

        return res


    def adjustControlGroupOffset(self, offsetX = 0, offsetY = 0, offsetZ = 0):
        cmds.move(offsetX, offsetY, offsetZ, self.ControlGroup, moveXYZ = True, relative = True)

    def InsertNewGroup(self, groupName = ''):
        newGrp = None
        if cmds.objExists(self.ControlObject):
            # Create a new empty group.
            newGrp = cmds.group(n = groupName, em = 1)
            cmds.delete(cmds.parentConstraint(self.ControlObject, newGrp, mo = 0))

            # Insert the new group into hierarchy.
            parentGrp = cmds.listRelatives(self.ControlObject, p = 1, type = 'transform')
            if parentGrp:
                cmds.parent(newGrp, parentGrp)
            cmds.parent(self.ControlObject, newGrp)
        else:
            cmds.warning('Cannot insert new group for:' + self.ControlObject)

        return newGrp


#-----------------------------------------------------------------------------
# Rig Circle Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigCircleControl(RigControl):
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_X,
                 rigControlIndex = 0,
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v'],
                 flipScaleX = False,
                 flipScaleY = False,
                 flipScaleZ = False,
                 preRotateX = 0.0,
                 preRotateY = 0.0,
                 preRotateZ = 0.0,
                 fitToSurroundingMeshes = False,
                 surroundingMeshes = [],
                 postFitScale = 1.0,
                 overrideFitRayDirection = False, 
                 fitRayDirection = (0, 1, 0)
                 ):

        RigControl.__init__(self, rigSide, rigType, rigFacing, rigControlIndex, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels,
                            flipScaleX, flipScaleY, flipScaleZ, 
                            fitToSurroundingMeshes = fitToSurroundingMeshes, surroundingMeshes = surroundingMeshes, postFitScale = postFitScale,
                            overrideFitRayDirection = overrideFitRayDirection, fitRayDirection = fitRayDirection)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale, 
                            preRotateX, preRotateY, preRotateZ, overrideControlColor, controlColor, 
                            fitToSurroundingMeshes, surroundingMeshes, postFitScale, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection):
        
        circleNormal = [1, 0, 0]
        if rigFacing == SERigEnum.eRigFacing.RF_X:
            circleNormal = [1, 0, 0]
        elif rigFacing == SERigEnum.eRigFacing.RF_Y:
            circleNormal = [0, 1, 0]
        elif rigFacing == SERigEnum.eRigFacing.RF_Z:
            circleNormal = [0, 0, 1]
        else:
            pass

        ctrlObj = cmds.circle(n = prefix + SERigNaming.sControl, ch = False, normal = circleNormal, radius = scale)[0]

        if fitToSurroundingMeshes and surroundingMeshes and len(surroundingMeshes) > 0:
            fitSize = self._getFitSize(surroundingMeshes, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection)
            # Debug info.
            #print(prefix + ':fitSize:' + str(fitSize))

            if fitSize:
                shapeBB = cmds.exactWorldBoundingBox(ctrlObj)
                if rigFacing == SERigEnum.eRigFacing.RF_X:
                    shapeSizeY = (shapeBB[4] - shapeBB[1]) * 0.5
                    fitScale = fitSize / shapeSizeY * postFitScale

                    cmds.select(ctrlObj)
                    cmds.scale(1.0, fitScale, fitScale, xyz = 1, relative = 1)
                    cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

                elif rigFacing == SERigEnum.eRigFacing.RF_Y:
                    shapeSizeX = (shapeBB[3] - shapeBB[0]) * 0.5
                    fitScale = fitSize / shapeSizeX * postFitScale
                    
                    cmds.select(ctrlObj)
                    cmds.scale(fitScale, 1.0, fitScale, xyz = 1, relative = 1)
                    cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

                elif rigFacing == SERigEnum.eRigFacing.RF_Z:
                    shapeSizeX = (shapeBB[3] - shapeBB[0]) * 0.5
                    fitScale = fitSize / shapeSizeX * postFitScale
                    
                    cmds.select(ctrlObj)
                    cmds.scale(fitScale, fitScale, 1.0, xyz = 1, relative = 1)
                    cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

                else:
                    pass

        # Set control color.
        ctrlShape = cmds.listRelatives(ctrlObj, s = 1)[0]
        cmds.setAttr(ctrlShape + '.ove', 1)

        if rigSide == SERigEnum.eRigSide.RS_Left:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Blue)
        elif rigSide == SERigEnum.eRigSide.RS_Right:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Red)
        elif rigSide == SERigEnum.eRigSide.RS_Center:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Yellow)
        else:
            # TODO:
            pass

        return ctrlObj

#-----------------------------------------------------------------------------
# Rig Cube Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigCubeControl(RigControl):
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_X,
                 rigControlIndex = 0,
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v'],
                 cubeScaleX = 1.0,
                 cubeScaleY = 1.0,
                 cubeScaleZ = 1.0,
                 transparency = 0.75,
                 preRotateX = 0.0,
                 preRotateY = 0.0,
                 preRotateZ = 0.0,
                 overrideControlColor = False, 
                 controlColor = (0.0, 0.0, 0.0),
                 fitToSurroundingMeshes = False,
                 surroundingMeshes = [],
                 postFitScale = 1.0,
                 overrideFitRayDirection = False, 
                 fitRayDirection = (0, 1, 0)
                 ):

        self.CubeScaleX = cubeScaleX
        self.CubeScaleY = cubeScaleY
        self.CubeScaleZ = cubeScaleZ
        self.Transparency = transparency

        RigControl.__init__(self, rigSide, rigType, rigFacing, rigControlIndex, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels, 
                            overrideControlColor = overrideControlColor, controlColor = controlColor,
                            fitToSurroundingMeshes = fitToSurroundingMeshes, surroundingMeshes = surroundingMeshes, postFitScale = postFitScale,
                            overrideFitRayDirection = overrideFitRayDirection, fitRayDirection = fitRayDirection)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale, 
                            preRotateX, preRotateY, preRotateZ, overrideControlColor, controlColor,
                            fitToSurroundingMeshes, surroundingMeshes, postFitScale, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection):

        ## Create control shape.
        #resShape = cmds.polyCube(n = prefix + SERigNaming.sControl,
        #                         w = 1, h = 1, d = 1, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 0)[0]
        #cmds.move(-0.5, resShape + '.scalePivot', resShape + '.rotatePivot', moveX = 1, relative = 1)
        #cmds.move(0.5, resShape, moveX = 1, relative = 1)

        #if rigSide == SERigEnum.eRigSide.RS_Right:
        #    self.CubeScaleX *= -1
        #cmds.scale(self.CubeScaleX, self.CubeScaleY, self.CubeScaleZ, xyz = 1, relative = 1)
        #cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        ## Create a new lamber shader.
        #resShader = cmds.shadingNode('lambert', asShader = 1)
        #resSet = cmds.sets(n = resShader + 'SG', renderable = True, noSurfaceShader = True, em = 1)
        #cmds.connectAttr(resShader + '.outColor', resSet + '.surfaceShader', f = 1)

        ## Assign the shader to the shape.
        #cmds.sets(resShape, e = True, forceElement = resSet)

        ## Set material color.
        #if overrideControlColor:
        #    cmds.setAttr(resShader + '.color', controlColor[0], controlColor[1], controlColor[2], type = 'double3')
        #else:
        #    if rigSide == SERigEnum.eRigSide.RS_Center:
        #        cmds.setAttr(resShader + '.color', 0.4, 0.9, 0.9, type = 'double3')
        #    elif rigSide == SERigEnum.eRigSide.RS_Left:
        #        cmds.setAttr(resShader + '.color', 0.0, 0.0, 1.0, type = 'double3')
        #    elif rigSide == SERigEnum.eRigSide.RS_Right:
        #        cmds.setAttr(resShader + '.color', 1.0, 0.0, 0.0, type = 'double3')
        #    else:
        #        pass

        #cmds.setAttr(resShader + '.transparency', self.Transparency, self.Transparency, self.Transparency, type = 'double3')

        list = []
        list.append(cmds.curve( p =[(1.0, 0.5, -0.5), (1.0, 0.5, 0.5), 
                                    (1.0, -0.5, 0.5), (1.0, -0.5, -0.5), 
                                    (1.0, 0.5, -0.5), (0.0, 0.5, -0.5), 
                                    (0.0, -0.5, -0.5), (1.0, -0.5, -0.5), 
                                    (1.0, -0.5, 0.5), (0.0, -0.5, 0.5), 
                                    (0.0, -0.5, -0.5), (0.0, 0.5, -0.5), 
                                    (0.0, 0.5, 0.5), (0.0, -0.5, 0.5), 
                                    (1.0, -0.5, 0.5), (1.0, 0.5, 0.5), 
                                    (0.0, 0.5, 0.5)], per = False, d=1, k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
        fp = cmds.listRelatives(list[0], f = True)[0]
        shapeName = fp.split("|")[1]

        newShapeName = prefix + SERigNaming.sControl
        cmds.rename(shapeName, newShapeName)

        cmds.select(newShapeName)
        if rigSide == SERigEnum.eRigSide.RS_Right:
            self.CubeScaleX *= -1
        cmds.scale(self.CubeScaleX, self.CubeScaleY, self.CubeScaleZ, xyz = 1, relative = 1)
        cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        if fitToSurroundingMeshes and surroundingMeshes and len(surroundingMeshes) > 0:
            fitSize = self._getFitSize(surroundingMeshes, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection)
            if fitSize:
                shapeBB = cmds.exactWorldBoundingBox(newShapeName)
                shapeSizeY = (shapeBB[4] - shapeBB[1]) * 0.5
                fitScale = fitSize / shapeSizeY * postFitScale

                cmds.select(newShapeName)
                cmds.scale(1.0, fitScale, fitScale, xyz = 1, relative = 1)
                cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)


        # Set control color.
        ctrlShapes = cmds.listRelatives(newShapeName, s = 1)
        ctrlColor = SERigEnum.eRigColor.RC_Blue
        
        if overrideControlColor:
            for ctrlShape in ctrlShapes:
                setControlRGBColor(ctrlShape, controlColor)
        else:
            if rigSide == SERigEnum.eRigSide.RS_Left:
                ctrlColor = SERigEnum.eRigColor.RC_Blue
            elif rigSide == SERigEnum.eRigSide.RS_Right:
                ctrlColor = SERigEnum.eRigColor.RC_Red
            elif rigSide == SERigEnum.eRigSide.RS_Center:
                ctrlColor = SERigEnum.eRigColor.RC_Yellow
            else:
                # TODO:
                pass
        
            for ctrlShape in ctrlShapes:
                cmds.setAttr(ctrlShape + '.ove', 1)
                cmds.setAttr(ctrlShape + '.ovc', ctrlColor)
            
        return newShapeName


#-----------------------------------------------------------------------------
# Rig Spike Cross Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigSpikeCrossControl(RigControl):
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_Y,
                 rigControlIndex = 0,
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v'],
                 scaleX = 60.0,
                 scaleZ = 60.0,
                 preRotateX = 0.0,
                 preRotateY = 0.0,
                 preRotateZ = 0.0
                 ):

        self.ScaleX = scaleX
        self.ScaleZ = scaleZ

        RigControl.__init__(self, rigSide, rigType, rigFacing, rigControlIndex, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale, 
                            preRotateX, preRotateY, preRotateZ, overrideControlColor, controlColor,
                            fitToSurroundingMeshes, surroundingMeshes, postFitScale, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection):
        list = []
        list.append(cmds.curve(p =[(0.5698271508338371, 4.091121663662989e-09, -2.132883735050939e-05), 
                                   (0.4208952391731131, 0.1488873944517639, -1.5755096100633637e-05), 
                                   (0.2720931419242101, 4.073556049855043e-05, -1.0184545420344193e-05), 
                                   (0.4209398007112384, -0.1487613617926744, -1.5755096101521815e-05), 
                                   (0.5698271508338371, 4.091121663662989e-09, -2.132883735050939e-05), 
                                   (0.42091194939155674, 6.301549556786412e-05, -0.1488401347819135), 
                                   (0.2720931419242101, 4.073556049855043e-05, -1.0184545420344193e-05), 
                                   (0.42092309049279564, 6.301716352297149e-05, 0.14880862458971134), 
                                   (0.5698271508338371, 4.091121663662989e-09, -2.132883735050939e-05), 
                                   (0.4208952391731131, 0.1488873944517639, -1.5755096100633637e-05), 
                                   (0.2720931419242101, 4.073556049855043e-05, -1.0184545420344193e-05), 
                                   (-0.2720931291529265, -0.0001260413294232876, 1.0184545417679658e-05), 
                                   (-0.4209971894939688, -6.30282570215357e-05, 0.14884013797247952), 
                                   (-0.5698271380625544, -8.530986004595675e-05, 2.1328837348733032e-05), 
                                   (-0.4210083305952077, -6.302992497664306e-05, -0.1488086213991462), 
                                   (-0.2720931291529265, -0.0001260413294232876, 1.0184545417679658e-05), 
                                   (-0.42085456057731463, 0.14876116408473417, 1.5751905531047328e-05), 
                                   (-0.5698271380625544, -8.530986004595675e-05, 2.1328837348733032e-05), 
                                   (-0.4209804792755252, -0.14888740721321847, 1.575828666666723e-05), 
                                   (-0.2720931291529265, -0.0001260413294232876, 1.0184545417679658e-05), 
                                   (-0.2720931291529265, -0.0001260413294232876, 1.0184545417679658e-05), 
                                   (0.0, -1.3322676295501878e-15, 0.0), (-1.1141101238898443e-05, -1.6679564396326896e-09, 0.2721144031802565), 
                                   (0.00014271626145045957, 0.14882419235483146, 0.42093877648166433), 
                                   (0.0, -1.3322676295501878e-15, 0.569763162551884), (1.671021844362741e-05, -0.14882437895619827, 0.42093878286606934), 
                                   (-1.1141101238898443e-05, -1.6679564396326896e-09, 0.2721144031802565), 
                                   (-0.14882987953462568, -2.2281592690021057e-05, 0.4209443534141677), 
                                   (0.0, -1.3322676295501878e-15, 0.569763162551884), (0.14890412937122033, -6.29878057401001e-05, 0.42093320912223664), 
                                   (-1.1141101238898443e-05, -1.6679564396326896e-09, 0.2721144031802565), 
                                   (-3.151178319171777e-05, -4.717688018018862e-09, -0.2721144015837451), 
                                   (-5.935678879254169e-05, 0.14882437257149927, -0.4209387812697942), 
                                   (-4.265288443061621e-05, -6.385641793116292e-09, -0.5697631609553717), 
                                   (-1.4801564748090357e-05, -0.1488243836738845, -0.42093878126955797), 
                                   (-3.151178319171777e-05, -4.717688018018862e-09, -0.2721144015837451), 
                                   (-0.1488613913178174, -2.2286310378039076e-05, -0.4209332107214614), 
                                   (-4.265288443061621e-05, -6.385641793116292e-09, -0.5697631609553717), 
                                   (0.1488726175880286, -6.299252342767403e-05, -0.42094435501339156), 
                                   (-3.151178319171777e-05, -4.717688018018862e-09, -0.2721144015837451)],
                                   per = False, d=1, k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]))
                                    
        for x in range(len(list)-1):
            cmds.makeIdentity(list[x+1], apply=True, t=1, r=1, s=1, n=0)
            shapeNode = cmds.listRelatives(list[x+1], shapes=True)
            cmds.parent(shapeNode, list[0], add=True, s=True)
            cmds.delete(list[x+1])

        newShapeName = prefix + SERigNaming.sControl
        cmds.rename(list[0], newShapeName)

        cmds.select(newShapeName)
        cmds.scale(self.ScaleX, 1.0, self.ScaleZ, xyz = 1, relative = 1)
        cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        # Set control color.
        ctrlShape = cmds.listRelatives(newShapeName, s = 1)[0]
        cmds.setAttr(ctrlShape + '.ove', 1)

        if rigSide == SERigEnum.eRigSide.RS_Left:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Blue)
        elif rigSide == SERigEnum.eRigSide.RS_Right:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Red)
        elif rigSide == SERigEnum.eRigSide.RS_Center:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Yellow)
        else:
            # TODO:
            pass

        return newShapeName


#-----------------------------------------------------------------------------
# Rig Arrow Cross Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigArrowCrossControl(RigControl):
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_Y,
                 rigControlIndex = 0,
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v'],
                 scaleX = 6.0,
                 scaleZ = 6.0,
                 preRotateX = 0.0,
                 preRotateY = 0.0,
                 preRotateZ = 0.0,
                 fitToSurroundingMeshes = False,
                 surroundingMeshes = [],
                 postFitScale = 1.0,
                 overrideFitRayDirection = False, 
                 fitRayDirection = (0, 1, 0)
                 ):

        self.ScaleX = scaleX
        self.ScaleZ = scaleZ

        RigControl.__init__(self, rigSide, rigType, rigFacing, rigControlIndex, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels,
                            fitToSurroundingMeshes = fitToSurroundingMeshes, surroundingMeshes = surroundingMeshes, postFitScale = postFitScale,
                            overrideFitRayDirection = overrideFitRayDirection, fitRayDirection = fitRayDirection)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale, 
                            preRotateX, preRotateY, preRotateZ, overrideControlColor, controlColor,
                            fitToSurroundingMeshes, surroundingMeshes, postFitScale, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection):
        curve1 = []
        curve1.append(cmds.curve( p =[(-1.0, 0.0, -6.0), (-1.0, 0.0, -4.0), (1.0, 0.0, -4.0), (1.0, 0.0, -6.0), (2.0, 0.0, -6.0), (0.0, 0.0, -8.0), (-2.0, 0.0, -6.0), (-1.0, 0.0, -6.0)],per = False, d=1, k=[0, 1, 2, 3, 4, 5, 6, 7]))
        curve1.append(cmds.curve( p =[(6.0, 0.0, -1.0), (4.0, 0.0, -1.0), (4.0, 0.0, 1.0), (6.0, 0.0, 1.0), (6.0, 0.0, 2.0), (8.0, 0.0, 0.0), (6.0, 0.0, -2.0), (6.0, 0.0, -1.0)],per = False, d=1, k=[0, 1, 2, 3, 4, 5, 6, 7]))
        curve1.append(cmds.curve( p =[(1.0, 0.0, 6.0), (0.9999999999999998, 0.0, 4.0), (-1.0000000000000002, 0.0, 4.0), (-1.0, 0.0, 6.0), (-2.0, 0.0, 6.0), (2.4492935982947064e-16, 0.0, 8.0), (2.0, 0.0, 6.0), (1.0, 0.0, 6.0)],per = False, d=1, k=[0, 1, 2, 3, 4, 5, 6, 7]))
        curve1.append(cmds.curve( p =[(-6.0, 0.0, 1.0), (-4.0, 0.0, 1.0), (-4.0, 0.0, -1.0), (-6.0, 0.0, -1.0), (-6.0, 0.0, -2.0), (-8.0, 0.0, 0.0), (-6.0, 0.0, 2.0), (-6.0, 0.0, 1.0)],per = False, d=1, k=[0, 1, 2, 3, 4, 5, 6, 7]))
        for x in range(len(curve1)-1):
	        cmds.makeIdentity(curve1[x+1], apply=True, t=1, r=1, s=1, n=0)
	        shapeNode = cmds.listRelatives(curve1[x+1], shapes=True)
	        cmds.parent(shapeNode, curve1[0], add=True, s=True)
	        cmds.delete(curve1[x+1])
        fp = cmds.listRelatives(curve1[0], f=True)[0]
        oldShapeName = fp.split("|")[1]

        newShapeName = prefix + SERigNaming.sControl
        cmds.rename(oldShapeName, newShapeName)

        cmds.select(newShapeName)
        cmds.scale(self.ScaleX, 1.0, self.ScaleZ, xyz = 1, relative = 1)
        cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        if fitToSurroundingMeshes and surroundingMeshes and len(surroundingMeshes) > 0:
            fitSize = self._getFitSize(surroundingMeshes, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection)
            if fitSize:
                shapeBB = cmds.exactWorldBoundingBox(newShapeName)
                shapeSizeX = (shapeBB[3] - shapeBB[0]) * 0.5
                fitScale = fitSize / shapeSizeX * postFitScale

                cmds.select(newShapeName)
                cmds.scale(fitScale, 1.0, fitScale, xyz = 1, relative = 1)
                cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        # Set control color.
        ctrlShapes = cmds.listRelatives(newShapeName, s = 1)
        ctrlColor = SERigEnum.eRigColor.RC_Blue
        
        if overrideControlColor:
            for ctrlShape in ctrlShapes:
                setControlRGBColor(ctrlShape, controlColor)
        else:
            if rigSide == SERigEnum.eRigSide.RS_Left:
                ctrlColor = SERigEnum.eRigColor.RC_Blue
            elif rigSide == SERigEnum.eRigSide.RS_Right:
                ctrlColor = SERigEnum.eRigColor.RC_Red
            elif rigSide == SERigEnum.eRigSide.RS_Center:
                ctrlColor = SERigEnum.eRigColor.RC_Yellow
            else:
                # TODO:
                pass
        
            for ctrlShape in ctrlShapes:
                cmds.setAttr(ctrlShape + '.ove', 1)
                cmds.setAttr(ctrlShape + '.ovc', ctrlColor)

        return newShapeName


#-----------------------------------------------------------------------------
# Rig Foot Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigFootControl(RigControl):
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_Y,
                 rigControlIndex = 0,
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v'],
                 scaleX = 20.0,
                 scaleZ = 20.0,
                 flipScaleX = False,
                 flipScaleY = False,
                 flipScaleZ = False,
                 preRotateX = 0.0,
                 preRotateY = 0.0,
                 preRotateZ = 0.0
                 ):

        self.ScaleX = scaleX
        self.ScaleZ = scaleZ

        RigControl.__init__(self, rigSide, rigType, rigFacing, rigControlIndex, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels, flipScaleX, flipScaleY, flipScaleZ,
                            preRotateX, preRotateY, preRotateZ)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale, 
                            preRotateX, preRotateY, preRotateZ, overrideControlColor, controlColor,
                            fitToSurroundingMeshes, surroundingMeshes, postFitScale, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection):
        list = []
        list.append(cmds.curve( p =[(0.4249371493353358, 4.798237340988468e-17, 0.05965626747485875), (0.02479363526881334, 6.785732323110913e-17, -0.3369861890540169), 
                                    (-0.4476029328500644, 4.798237340988471e-17, 0.059656267474858304), (-0.16523211069250432, 1.966335461618786e-32, 0.8432678923660822), 
                                    (-0.61616597431764, -4.7982373409884694e-17, 1.635912638052866), (-0.5208473195637784, -6.785732323110915e-17, 2.405743087588424), 
                                    (0.606808540733522, -4.798237340988472e-17, 1.7619653609862764), (0.46646824825008704, -3.644630067904792e-32, 1.2868969494440572), 
                                    (0.4249371493353358, 4.798237340988468e-17, 0.05965626747485875), 
                                    (0.02479363526881334, 6.785732323110913e-17, -0.3369861890540169), 
                                    (-0.4476029328500644, 4.798237340988471e-17, 0.059656267474858304)],
                                    per = True, d=3, k=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        for x in range(len(list)-1):
            cmds.makeIdentity(list[x+1], apply=True, t=1, r=1, s=1, n=0)
            shapeNode = cmds.listRelatives(list[x+1], shapes=True)
            cmds.parent(shapeNode, list[0], add=True, s=True)
            cmds.delete(list[x+1])

        newShapeName = prefix + SERigNaming.sControl
        cmds.rename(list[0], newShapeName)

        # Adjust foot shape via hard coded CV position.
        cmds.select(newShapeName + '.cv[5]', r = 1)
        cmds.move(0.35, 0, 0, r = 1, os = 1, wd = 1)

        newScaleX = self.ScaleX
        newScaleZ = self.ScaleZ
        newScaleY = 1
        if matchBoundingBoxScale:
            bb = cmds.exactWorldBoundingBox(newShapeName)
            xExt = bb[3] - bb[0]
            zExt = bb[5] - bb[2]
            newScaleX = newScaleX / zExt * 1.5
            newScaleZ = newScaleX

        cmds.select(newShapeName)
        cmds.scale(newScaleX, newScaleY, newScaleZ, xyz = 1, relative = 1)
        cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)
        
        # Set control color.
        ctrlShape = cmds.listRelatives(newShapeName, s = 1)[0]
        cmds.setAttr(ctrlShape + '.ove', 1)

        if rigSide == SERigEnum.eRigSide.RS_Left:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Blue)
        elif rigSide == SERigEnum.eRigSide.RS_Right:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Red)
        elif rigSide == SERigEnum.eRigSide.RS_Center:
            cmds.setAttr(ctrlShape + '.ovc', SERigEnum.eRigColor.RC_Yellow)
        else:
            # TODO:
            pass

        return newShapeName

#-----------------------------------------------------------------------------
# Rig Rotation Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigRotationControl(RigControl):
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_Z,
                 rigControlIndex = 0,
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 't', 'v'],
                 flipScaleX = False,
                 flipScaleY = False,
                 flipScaleZ = False,
                 preRotateX = 0.0,
                 preRotateY = 0.0,
                 preRotateZ = 0.0
                 ):

        RigControl.__init__(self, rigSide, rigType, rigFacing, rigControlIndex, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels, flipScaleX, flipScaleY, flipScaleZ,
                            preRotateX, preRotateY, preRotateZ)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale, 
                            preRotateX, preRotateY, preRotateZ, overrideControlColor, controlColor,
                            fitToSurroundingMeshes, surroundingMeshes, postFitScale, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection):

        list = []
        list.append(cmds.curve( p =[(0.33587352900359235, 3.552713678800501e-15, 0.7361468691490706), (0.4304251528553422, 0.03022134593976844, 0.6908148502394227), (0.5107046042608197, 0.07247276978952044, 0.6274377144647979), (0.5684975545498538, 0.12400997464880348, 0.5501319071758723), (0.5684975545498538, 0.12400997464880348, 0.5501319071758723), (0.5684975545498538, 0.12400997464880348, 0.5501319071758723), (0.5819931861859438, 0.12400997464880348, 0.5346306603447717), (0.5819931861859438, 0.12400997464880348, 0.5346306603447717), (0.5819931861859438, 0.12400997464880348, 0.5346306603447717), (0.5819931861859438, 0.12400997464880348, 0.5346306603447717), (0.5402530010360955, 0.08197748359885182, 0.5946770761304137), (0.4852738226242117, 0.0455134352238602, 0.6467685738089757), (0.41921829926566545, 0.015501246831103543, 0.6896431286557706), (0.41921829926566545, 0.015501246831103543, 0.6896431286557706), (0.41921829926566545, 0.015501246831103543, 0.6896431286557706), (0.7077292503941841, 0.015501246831103543, 0.43808875481816606), (0.8080009216827335, 0.015501246831103543, -0.016811817720621902), (0.6943482219457628, 0.015501246831103543, -0.34108941639861884), (0.5527220271320097, 0.015501246831103543, -0.5148315398676033), (0.33489352471512746, 0.015501246831103543, -0.6771644412642893), (0.17585601860228905, 0.015501246831103543, -0.7201406688717121), (0.015501247071298963, 0.015501246831103543, -0.7361468691392242)],per = False, d=3, k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19, 19]))
        list.append(cmds.curve( p =[(0.33587352900359235, -3.552713678800501e-15, 0.7361468691490706), (0.4304251528553422, -0.03022134593976844, 0.6908148502394227), (0.5107046042608197, -0.07247276978952044, 0.6274377144647979), (0.5684975545498538, -0.12400997464880348, 0.5501319071758723), (0.5684975545498538, -0.12400997464880348, 0.5501319071758723), (0.5684975545498538, -0.12400997464880348, 0.5501319071758723), (0.5819931861859438, -0.12400997464880348, 0.5346306603447717), (0.5819931861859438, -0.12400997464880348, 0.5346306603447717), (0.5819931861859438, -0.12400997464880348, 0.5346306603447717), (0.5819931861859438, -0.12400997464880348, 0.5346306603447717), (0.5402530010360955, -0.08197748359885182, 0.5946770761304137), (0.4852738226242117, -0.0455134352238602, 0.6467685738089757), (0.41921829926566545, -0.015501246831103543, 0.6896431286557706), (0.41921829926566545, -0.015501246831103543, 0.6896431286557706), (0.41921829926566545, -0.015501246831103543, 0.6896431286557706), (0.7077292503941841, -0.015501246831103543, 0.43808875481816606), (0.8080009216827335, -0.015501246831103543, -0.016811817720621902), (0.6943482219457628, -0.015501246831103543, -0.34108941639861884), (0.5527220271320097, -0.015501246831103543, -0.5148315398676033), (0.33489352471512746, -0.015501246831103543, -0.6771644412642893), (0.17585601860228905, -0.015501246831103543, -0.7201406688717121), (0.015501247071298963, -0.015501246831103543, -0.7361468691392242)],per = False, d=3, k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19, 19]))
        list.append(cmds.curve( p =[(-0.33587352900359235, 3.552713678800501e-15, 0.7361468691490706), (-0.4304251528553422, 0.03022134593976844, 0.6908148502394227), (-0.5107046042608197, 0.07247276978952044, 0.6274377144647979), (-0.5684975545498538, 0.12400997464880348, 0.5501319071758723), (-0.5684975545498538, 0.12400997464880348, 0.5501319071758723), (-0.5684975545498538, 0.12400997464880348, 0.5501319071758723), (-0.5819931861859438, 0.12400997464880348, 0.5346306603447717), (-0.5819931861859438, 0.12400997464880348, 0.5346306603447717), (-0.5819931861859438, 0.12400997464880348, 0.5346306603447717), (-0.5819931861859438, 0.12400997464880348, 0.5346306603447717), (-0.5402530010360955, 0.08197748359885182, 0.5946770761304137), (-0.4852738226242117, 0.0455134352238602, 0.6467685738089757), (-0.41921829926566545, 0.015501246831103543, 0.6896431286557706), (-0.41921829926566545, 0.015501246831103543, 0.6896431286557706), (-0.41921829926566545, 0.015501246831103543, 0.6896431286557706), (-0.7077292503941841, 0.015501246831103543, 0.43808875481816606), (-0.8080009216827335, 0.015501246831103543, -0.016811817720621902), (-0.6943482219457628, 0.015501246831103543, -0.34108941639861884), (-0.5527220271320097, 0.015501246831103543, -0.5148315398676033), (-0.33489352471512746, 0.015501246831103543, -0.6771644412642893), (-0.17585601860228905, 0.015501246831103543, -0.7201406688717121), (-0.015501247071298963, 0.015501246831103543, -0.7361468691392242)],per = False, d=3, k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19, 19]))
        list.append(cmds.curve( p =[(-0.33587352900359235, -3.552713678800501e-15, 0.7361468691490706), (-0.4304251528553422, -0.03022134593976844, 0.6908148502394227), (-0.5107046042608197, -0.07247276978952044, 0.6274377144647979), (-0.5684975545498538, -0.12400997464880348, 0.5501319071758723), (-0.5684975545498538, -0.12400997464880348, 0.5501319071758723), (-0.5684975545498538, -0.12400997464880348, 0.5501319071758723), (-0.5819931861859438, -0.12400997464880348, 0.5346306603447717), (-0.5819931861859438, -0.12400997464880348, 0.5346306603447717), (-0.5819931861859438, -0.12400997464880348, 0.5346306603447717), (-0.5819931861859438, -0.12400997464880348, 0.5346306603447717), (-0.5402530010360955, -0.08197748359885182, 0.5946770761304137), (-0.4852738226242117, -0.0455134352238602, 0.6467685738089757), (-0.41921829926566545, -0.015501246831103543, 0.6896431286557706), (-0.41921829926566545, -0.015501246831103543, 0.6896431286557706), (-0.41921829926566545, -0.015501246831103543, 0.6896431286557706), (-0.7077292503941841, -0.015501246831103543, 0.43808875481816606), (-0.8080009216827335, -0.015501246831103543, -0.016811817720621902), (-0.6943482219457628, -0.015501246831103543, -0.34108941639861884), (-0.5527220271320097, -0.015501246831103543, -0.5148315398676033), (-0.33489352471512746, -0.015501246831103543, -0.6771644412642893), (-0.17585601860228905, -0.015501246831103543, -0.7201406688717121), (-0.015501247071298963, -0.015501246831103543, -0.7361468691392242)],per = False, d=3, k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19, 19]))
        list.append(cmds.curve( p =[(-7.105427357601002e-15, -0.3358735290035888, 0.7361468691490706), (-0.030221345939771993, -0.43042515285533867, 0.6908148502394227), (-0.072472769789524, -0.5107046042608161, 0.6274377144647979), (-0.12400997464880703, -0.5684975545498503, 0.5501319071758723), (-0.12400997464880703, -0.5684975545498503, 0.5501319071758723), (-0.12400997464880703, -0.5684975545498503, 0.5501319071758723), (-0.12400997464880703, -0.5819931861859402, 0.5346306603447717), (-0.12400997464880703, -0.5819931861859402, 0.5346306603447717), (-0.12400997464880703, -0.5819931861859402, 0.5346306603447717), (-0.12400997464880703, -0.5819931861859402, 0.5346306603447717), (-0.08197748359885537, -0.540253001036092, 0.5946770761304137), (-0.04551343522386375, -0.48527382262420815, 0.6467685738089757), (-0.015501246831107096, -0.4192182992656619, 0.6896431286557706), (-0.015501246831107096, -0.4192182992656619, 0.6896431286557706), (-0.015501246831107096, -0.4192182992656619, 0.6896431286557706), (-0.015501246831107096, -0.7077292503941806, 0.43808875481816606), (-0.015501246831107096, -0.80800092168273, -0.016811817720621902), (-0.015501246831107096, -0.6943482219457593, -0.34108941639861884), (-0.015501246831107096, -0.5527220271320061, -0.5148315398676033), (-0.015501246831107096, -0.3348935247151239, -0.6771644412642893), (-0.015501246831107096, -0.1758560186022855, -0.7201406688717121), (-0.015501246831107096, -0.01550124707129541, -0.7361468691392242)],per = False, d=3, k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19, 19]))
        list.append(cmds.curve( p =[(3.552713678800501e-15, -0.3358735290035959, 0.7361468691490706), (0.03022134593976844, -0.43042515285534577, 0.6908148502394227), (0.07247276978952044, -0.5107046042608232, 0.6274377144647979), (0.12400997464880348, -0.5684975545498574, 0.5501319071758723), (0.12400997464880348, -0.5684975545498574, 0.5501319071758723), (0.12400997464880348, -0.5684975545498574, 0.5501319071758723), (0.12400997464880348, -0.5819931861859473, 0.5346306603447717), (0.12400997464880348, -0.5819931861859473, 0.5346306603447717), (0.12400997464880348, -0.5819931861859473, 0.5346306603447717), (0.12400997464880348, -0.5819931861859473, 0.5346306603447717), (0.08197748359885182, -0.5402530010360991, 0.5946770761304137), (0.0455134352238602, -0.48527382262421526, 0.6467685738089757), (0.015501246831103543, -0.419218299265669, 0.6896431286557706), (0.015501246831103543, -0.419218299265669, 0.6896431286557706), (0.015501246831103543, -0.419218299265669, 0.6896431286557706), (0.015501246831103543, -0.7077292503941877, 0.43808875481816606), (0.015501246831103543, -0.8080009216827371, -0.016811817720621902), (0.015501246831103543, -0.6943482219457664, -0.34108941639861884), (0.015501246831103543, -0.5527220271320132, -0.5148315398676033), (0.015501246831103543, -0.334893524715131, -0.6771644412642893), (0.015501246831103543, -0.1758560186022926, -0.7201406688717121), (0.015501246831103543, -0.015501247071302515, -0.7361468691392242)],per = False, d=3, k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19, 19]))
        list.append(cmds.curve( p =[(0.0, 0.33587352900359235, 0.7361468691490706), (-0.030221345939764888, 0.4304251528553422, 0.6908148502394227), (-0.07247276978951689, 0.5107046042608197, 0.6274377144647979), (-0.12400997464879993, 0.5684975545498538, 0.5501319071758723), (-0.12400997464879993, 0.5684975545498538, 0.5501319071758723), (-0.12400997464879993, 0.5684975545498538, 0.5501319071758723), (-0.12400997464879993, 0.5819931861859438, 0.5346306603447717), (-0.12400997464879993, 0.5819931861859438, 0.5346306603447717), (-0.12400997464879993, 0.5819931861859438, 0.5346306603447717), (-0.12400997464879993, 0.5819931861859438, 0.5346306603447717), (-0.08197748359884827, 0.5402530010360955, 0.5946770761304137), (-0.045513435223856646, 0.4852738226242117, 0.6467685738089757), (-0.01550124683109999, 0.41921829926566545, 0.6896431286557706), (-0.01550124683109999, 0.41921829926566545, 0.6896431286557706), (-0.01550124683109999, 0.41921829926566545, 0.6896431286557706), (-0.01550124683109999, 0.7077292503941841, 0.43808875481816606), (-0.01550124683109999, 0.8080009216827335, -0.016811817720621902), (-0.01550124683109999, 0.6943482219457628, -0.34108941639861884), (-0.01550124683109999, 0.5527220271320097, -0.5148315398676033), (-0.01550124683109999, 0.33489352471512746, -0.6771644412642893), (-0.01550124683109999, 0.17585601860228905, -0.7201406688717121), (-0.01550124683109999, 0.015501247071298963, -0.7361468691392242)],per = False, d=3, k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19, 19]))
        list.append(cmds.curve( p =[(3.552713678800501e-15, 0.33587352900359235, 0.7361468691490706), (0.03022134593976844, 0.4304251528553422, 0.6908148502394227), (0.07247276978952044, 0.5107046042608197, 0.6274377144647979), (0.12400997464880348, 0.5684975545498538, 0.5501319071758723), (0.12400997464880348, 0.5684975545498538, 0.5501319071758723), (0.12400997464880348, 0.5684975545498538, 0.5501319071758723), (0.12400997464880348, 0.5819931861859438, 0.5346306603447717), (0.12400997464880348, 0.5819931861859438, 0.5346306603447717), (0.12400997464880348, 0.5819931861859438, 0.5346306603447717), (0.12400997464880348, 0.5819931861859438, 0.5346306603447717), (0.08197748359885182, 0.5402530010360955, 0.5946770761304137), (0.0455134352238602, 0.4852738226242117, 0.6467685738089757), (0.015501246831103543, 0.41921829926566545, 0.6896431286557706), (0.015501246831103543, 0.41921829926566545, 0.6896431286557706), (0.015501246831103543, 0.41921829926566545, 0.6896431286557706), (0.015501246831103543, 0.7077292503941841, 0.43808875481816606), (0.015501246831103543, 0.8080009216827335, -0.016811817720621902), (0.015501246831103543, 0.6943482219457628, -0.34108941639861884), (0.015501246831103543, 0.5527220271320097, -0.5148315398676033), (0.015501246831103543, 0.33489352471512746, -0.6771644412642893), (0.015501246831103543, 0.17585601860228905, -0.7201406688717121), (0.015501246831103543, 0.015501247071298963, -0.7361468691392242)],per = False, d=3, k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19, 19]))
        for x in range(len(list)-1):
            cmds.makeIdentity(list[x+1], apply=True, t=1, r=1, s=1, n=0)
            shapeNode = cmds.listRelatives(list[x+1], shapes=True)
            cmds.parent(shapeNode, list[0], add=True, s=True)
            cmds.delete(list[x+1])
        cmds.select(list[0])
        
        newShapeName = prefix + SERigNaming.sControl
        cmds.rename(list[0], newShapeName)

        newScaleX = scale
        newScaleZ = scale
        newScaleY = scale
        cmds.select(newShapeName)
        cmds.scale(newScaleX, newScaleY, newScaleZ, xyz = 1, relative = 1)
        cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        # Set control color.
        ctrlShapes = cmds.listRelatives(newShapeName, s = 1)
        ctrlColor = SERigEnum.eRigColor.RC_Blue
        if rigSide == SERigEnum.eRigSide.RS_Left:
            ctrlColor = SERigEnum.eRigColor.RC_Blue
        elif rigSide == SERigEnum.eRigSide.RS_Right:
            ctrlColor = SERigEnum.eRigColor.RC_Red
        elif rigSide == SERigEnum.eRigSide.RS_Center:
            ctrlColor = SERigEnum.eRigColor.RC_Yellow
        else:
            # TODO:
            pass

        for ctrlShape in ctrlShapes:
            cmds.setAttr(ctrlShape + '.ove', 1)
            cmds.setAttr(ctrlShape + '.ovc', ctrlColor)

        return newShapeName

#-----------------------------------------------------------------------------
# Rig Diamond Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigDiamondControl(RigControl):
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_Y,
                 rigControlIndex = 0,
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'r', 'v'],
                 flipScaleX = False,
                 flipScaleY = False,
                 flipScaleZ = False,
                 preRotateX = 0.0,
                 preRotateY = 0.0,
                 preRotateZ = 0.0
                 ):

        RigControl.__init__(self, rigSide, rigType, rigFacing, rigControlIndex, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels, flipScaleX, flipScaleY, flipScaleZ,
                            preRotateX, preRotateY, preRotateZ)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale, 
                            preRotateX, preRotateY, preRotateZ, overrideControlColor, controlColor,
                            fitToSurroundingMeshes, surroundingMeshes, postFitScale, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection):

        list = []
        list.append(cmds.curve( p =[(0.0, -0.2016202582919906, 0.10123448014461145), (0.0, 1.425671083410407e-07, 0.30285488100370994), (0.20162040085909805, 1.425671083410407e-07, 0.1012344801446119), (0.0, -0.2016202582919906, 0.10123448014461145), (-0.20162040085909827, 1.425671083410407e-07, 0.1012344801446119), (0.0, 1.425671083410407e-07, 0.30285488100370994), (0.0, 0.2016202582919897, 0.1012344801446119), (-0.20162040085909827, 1.425671083410407e-07, 0.1012344801446119), (0.0, 0.2016202582919897, 0.1012344801446119), (0.20162040085909805, 1.425671083410407e-07, 0.1012344801446119), (0.0, 1.425671083410407e-07, 0.30285488100370994), (0.0, 0.2016202582919897, 0.1012344801446119), (0.0, 0.2016202582919897, -0.10134995950254133), (0.20162040085909805, -1.4256710922921911e-07, -0.101234480144611), (0.0, -0.00011562192503866697, -0.3028548810037095), (0.0, -0.2016202582919906, -0.10111900078668068), (0.20162040085909805, -1.4256710922921911e-07, -0.101234480144611), (0.20162040085909805, 1.425671083410407e-07, 0.1012344801446119), (0.0, -0.2016202582919906, 0.10123448014461145), (0.0, -0.2016202582919906, -0.10111900078668068), (-0.20162040085909827, -1.4256710922921911e-07, -0.101234480144611), (-0.20162040085909827, 1.425671083410407e-07, 0.1012344801446119), (-0.20162040085909827, -1.4256710922921911e-07, -0.101234480144611), (0.0, 0.2016202582919897, -0.10134995950254133), (0.20162040085909805, -1.4256710922921911e-07, -0.101234480144611), (0.0, -0.2016202582919906, -0.10111900078668068), (-0.20162040085909827, -1.4256710922921911e-07, -0.101234480144611), (0.0, -0.00011562192503866697, -0.3028548810037095), (0.0, -0.2016202582919906, -0.10111900078668068), (0.20162040085909805, -1.4256710922921911e-07, -0.101234480144611), (0.0, -0.00011562192503866697, -0.3028548810037095), (0.0, 0.2016202582919897, -0.10134995950254133), (-0.20162040085909827, -1.4256710922921911e-07, -0.101234480144611), (0.0, -0.00011562192503866697, -0.3028548810037095)],per = False, d=1, k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]))
        for x in range(len(list)-1):
            cmds.makeIdentity(list[x+1], apply=True, t=1, r=1, s=1, n=0)
            shapeNode = cmds.listRelatives(list[x+1], shapes=True)
            cmds.parent(shapeNode, list[0], add=True, s=True)
            cmds.delete(list[x+1])
        cmds.select(list[0])

        newShapeName = prefix + SERigNaming.sControl
        cmds.rename(list[0], newShapeName)

        newScaleX = scale
        newScaleZ = scale
        newScaleY = scale
        cmds.select(newShapeName)
        cmds.scale(newScaleX, newScaleY, newScaleZ, xyz = 1, relative = 1)
        cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        # Set control color.
        ctrlShapes = cmds.listRelatives(newShapeName, s = 1)
        ctrlColor = SERigEnum.eRigColor.RC_Blue
        if rigSide == SERigEnum.eRigSide.RS_Left:
            ctrlColor = SERigEnum.eRigColor.RC_Blue
        elif rigSide == SERigEnum.eRigSide.RS_Right:
            ctrlColor = SERigEnum.eRigColor.RC_Red
        elif rigSide == SERigEnum.eRigSide.RS_Center:
            ctrlColor = SERigEnum.eRigColor.RC_Yellow
        else:
            # TODO:
            pass

        for ctrlShape in ctrlShapes:
            cmds.setAttr(ctrlShape + '.ove', 1)
            cmds.setAttr(ctrlShape + '.ovc', ctrlColor)

        return newShapeName


#-----------------------------------------------------------------------------
# Rig Flat Hexagon Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigFlatHexagonControl(RigControl):
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_Y,
                 rigControlIndex = 0,
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'r', 'v'],
                 flipScaleX = False,
                 flipScaleY = False,
                 flipScaleZ = False,
                 preRotateX = 0.0,
                 preRotateY = 0.0,
                 preRotateZ = 0.0
                 ):

        RigControl.__init__(self, rigSide, rigType, rigFacing, rigControlIndex, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels, flipScaleX, flipScaleY, flipScaleZ, 
                            preRotateX, preRotateY, preRotateZ)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale, 
                            preRotateX, preRotateY, preRotateZ, overrideControlColor, controlColor,
                            fitToSurroundingMeshes, surroundingMeshes, postFitScale, translateTo, rotateTo, overrideFitRayDirection, fitRayDirection):

        list = []
        list.append(cmds.curve(p =[(-2.0, 0.0, -2.0), (2.0, 0.0, -2.0), (3.0, 0.0, 0.0), (2.0, 0.0, 2.0), (-2.0, 0.0, 2.0), 
                                   (-3.0, 0.0, 0.0), (-2.0, 0.0, -2.0)], per = False, d = 1, k = [0, 1, 2, 3, 4, 5, 6]))
        fp = cmds.listRelatives(list[0], f = True)[0]
        path = fp.split("|")[1]

        newShapeName = prefix + SERigNaming.sControl
        cmds.rename(path, newShapeName)

        cmds.setAttr(newShapeName + '.rotateX', preRotateX)
        cmds.setAttr(newShapeName + '.rotateY', preRotateY)
        cmds.setAttr(newShapeName + '.rotateZ', preRotateZ)
        cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        newScaleX = scale
        newScaleZ = scale
        newScaleY = scale
        cmds.select(newShapeName)
        cmds.scale(newScaleX, newScaleY, newScaleZ, xyz = 1, relative = 1)
        if rigFacing == SERigEnum.eRigFacing.RF_X:
            cmds.setAttr(newShapeName + '.rotateX', 90)
            cmds.setAttr(newShapeName + '.rotateY', 90)
        elif rigFacing == SERigEnum.eRigFacing.RF_Y:
            pass
        else:
            cmds.setAttr(newShapeName + '.rotateX', 90)
        cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        # Set control color.
        ctrlShapes = cmds.listRelatives(newShapeName, s = 1)
        ctrlColor = SERigEnum.eRigColor.RC_Blue
        if rigSide == SERigEnum.eRigSide.RS_Left:
            ctrlColor = SERigEnum.eRigColor.RC_Blue
        elif rigSide == SERigEnum.eRigSide.RS_Right:
            ctrlColor = SERigEnum.eRigColor.RC_Red
        elif rigSide == SERigEnum.eRigSide.RS_Center:
            ctrlColor = SERigEnum.eRigColor.RC_Yellow
        else:
            # TODO:
            pass

        for ctrlShape in ctrlShapes:
            cmds.setAttr(ctrlShape + '.ove', 1)
            cmds.setAttr(ctrlShape + '.ovc', ctrlColor)

        return newShapeName