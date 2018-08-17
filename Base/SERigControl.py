import maya.cmds as cmds
from . import SERigEnum
from . import SERigNaming

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
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v']
                 ):
        
        # Create control object and control group.

        ctrlObj = None
        ctrlGrp = None

        ctrlObj = self._createControlShape(rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale)
        if ctrlObj:
            # Parent to control group.
            ctrlGrp = cmds.group(n = prefix + SERigNaming.sControlGroup, em = 1)
            cmds.parent(ctrlObj, ctrlGrp)

            # Translate control group to target translation object.
            if cmds.objExists(translateTo):
                cmds.delete(cmds.pointConstraint(translateTo, ctrlGrp))

            # Rotate control group to target rotation object.
            if cmds.objExists(rotateTo):
                cmds.delete(cmds.orientConstraint(rotateTo, ctrlGrp))

            # Parent the control group to the given parent.
            if cmds.objExists(parent):
                cmds.parent(ctrlGrp, parent)

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

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale):
        return None

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
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v']
                 ):

        RigControl.__init__(self, rigSide, rigType, rigFacing, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale):
        
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
                 transparency = 0.75
                 ):

        self.CubeScaleX = cubeScaleX
        self.CubeScaleY = cubeScaleY
        self.CubeScaleZ = cubeScaleZ
        self.Transparency = transparency

        RigControl.__init__(self, rigSide, rigType, rigFacing, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale):

        # Create control shape.
        resShape = cmds.polyCube(n = prefix + SERigNaming.sControl,
                                 w = 1, h = 1, d = 1, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 0)[0]
        cmds.move(-0.5, resShape + '.scalePivot', resShape + '.rotatePivot', moveX = 1, relative = 1)
        cmds.move(0.5, resShape, moveX = 1, relative = 1)

        if rigSide == SERigEnum.eRigSide.RS_Right:
            self.CubeScaleX *= -1
        cmds.scale(self.CubeScaleX, self.CubeScaleY, self.CubeScaleZ, xyz = 1, relative = 1)
        cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0,  pn = 1)

        # Create a new lamber shader.
        resShader = cmds.shadingNode('lambert', asShader = 1)
        resSet = cmds.sets(n = resShader + 'SG', renderable = True, noSurfaceShader = True, em = 1)
        cmds.connectAttr(resShader + '.outColor', resSet + '.surfaceShader', f = 1)

        # Assign the shader to the shape.
        cmds.sets(resShape, e = True, forceElement = resSet)

        # Set material color.
        if rigSide == SERigEnum.eRigSide.RS_Center:
            cmds.setAttr(resShader + '.color', 0.4, 0.9, 0.9, type = 'double3')
        elif rigSide == SERigEnum.eRigSide.RS_Left:
            cmds.setAttr(resShader + '.color', 0.0, 0.0, 1.0, type = 'double3')
        elif rigSide == SERigEnum.eRigSide.RS_Right:
            cmds.setAttr(resShader + '.color', 1.0, 0.0, 0.0, type = 'double3')
        else:
            pass

        cmds.setAttr(resShader + '.transparency', self.Transparency, self.Transparency, self.Transparency, type = 'double3')

        return resShape

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
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v'],
                 scaleX = 60.0,
                 scaleZ = 60.0
                 ):

        self.ScaleX = scaleX
        self.ScaleZ = scaleZ

        RigControl.__init__(self, rigSide, rigType, rigFacing, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale):
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
# Rig Foot Control Class
# Sun Che
#-----------------------------------------------------------------------------
class RigFootControl(RigControl):
    def __init__(
                 self,
                 rigSide = SERigEnum.eRigSide.RS_Unknown,
                 rigType = SERigEnum.eRigType.RT_Unknown,
                 rigFacing = SERigEnum.eRigFacing.RF_Y,
                 prefix = 'new', 
                 scale = 1.0, 
                 matchBoundingBoxScale = False,
                 translateTo = '', 
                 rotateTo = '', 
                 parent = '',
                 lockChannels = ['s', 'v'],
                 scaleX = 20.0,
                 scaleZ = 20.0
                 ):

        self.ScaleX = scaleX
        self.ScaleZ = scaleZ

        RigControl.__init__(self, rigSide, rigType, rigFacing, prefix, 
                            scale, matchBoundingBoxScale, translateTo, rotateTo, parent, lockChannels)

    def _createControlShape(self, rigSide, rigType, rigFacing, prefix, scale, matchBoundingBoxScale):
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

        newScaleX = self.ScaleX
        newScaleZ = self.ScaleZ
        if matchBoundingBoxScale:
            bb = cmds.exactWorldBoundingBox(newShapeName)
            xExt = bb[3] - bb[0]
            zExt = bb[5] - bb[2]
            newScaleX = newScaleX / zExt * 1.5
            newScaleZ = newScaleX

        cmds.select(newShapeName)
        cmds.scale(newScaleX, 1.0, newScaleZ, xyz = 1, relative = 1)
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