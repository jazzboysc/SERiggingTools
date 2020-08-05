
import maya.cmds as cmds
import math
cmds.scriptJob(killAll = True)

class FixJointMode():
    
    def __init__(self):
        self.modeJob = None          #manage scriptJob of switch mode
        self.activeMode = False      #current switch mode
        self.lastJoint = ""          #last selected joint
        self.activeJoint = ""        #current selected joint
        self.jointJob = None         #manage scripJob when selected joint change
        self.defaultIKGroups = [[u'L_Hip', u'L_Knee', u'L_Ankle',"locator_L_LegPV"], [u'L_Shoulder', u'L_Elbow', u'L_Wrist',"locator_L_ArmPV"], [u'L_Thumb_0',u'L_Thumb_1', u'L_Thumb_2', u'L_Thumb_3'], 
        [u'L_Index_0',u'L_Index_1', u'L_Index_2', u'L_Index_3', u'L_Index_4'], [u'L_Middle_0',u'L_Middle_1', u'L_Middle_2', u'L_Middle_3', u'L_Middle_4'], 
        [u'L_Ring_0',u'L_Ring_1', u'L_Ring_2', u'L_Ring_3', u'L_Ring_4'], [u'L_Pinky_0',u'L_Pinky_1', u'L_Pinky_2', u'L_Pinky_3', u'L_Pinky_4']]
        self.IKGroups = self.defaultIKGroups  
        self.primaryAxis = [1,0,0]
        self.secondaryAxis = [0,0,1]          #the axis which perpendicular to the IKPlane
        self.secondaryAxisOrient = [-1,0,0]    #the world direction that secondaryAxis will orient without IKPlane
        self.debugMode = False
        self.displayAxis = []
        self.centerJoint = ["C_Pelvis","C_ChestBegin","C_Neck_0"]
        self.facialJoint = ["C_FacialRoot","C_Jaw","L_Eye"]
        self.lockedAttrDict = {}
        self.ignoreJoint = ["L_Eye","Root","C_FacialRoot",""]
        self.defaultMirrorJnt = ["L_Eye","L_Clav","L_Breast","L_Hip"]
        self.defaultMirrorLocator = ["locator_L_ChestHeadBegin","locator_L_ChestHeadEnd","locator_L_LegPV","locator_L_ArmPV","L_Eye_BS"]
        self.mirrorJoints = self.defaultMirrorJnt
        self.mirrorLocator = self.defaultMirrorLocator
              
    #change the mode on-off state and return the mode switch state(Boolean)
    def switchMode(self,switch):     
        #clean all the scriptJob ,avoide the old scriptJob effecting
        if self.modeJob != None:
            cmds.scriptJob(kill = self.modeJob)
            self.modeJob = None
        if self.jointJob != None:
            cmds.scriptJob(kill = self.jointJob)
            self.jointJob = None
        if switch:
            self.modeJob = cmds.scriptJob(event = ["SelectionChanged",self.setJointJob])
            self.fixJointOrient()
            self.activeMode = True
            print "FixJointMode On"
        else: 
            self.displayLocalAxis(self.displayAxis,False)
            self.activeMode = False
            print "FixJointMode Off"          
        return self.activeMode
    
    #register or delete the scriptJob of joint which active or last selected   
    def setJointJob(self):        
        self.getRelativeJoint()
        if self.activeJoint != "" and self.activeJoint != self.lastJoint:
            if self.jointJob != None:
                cmds.scriptJob(kill = self.jointJob)
                self.jointJob = None
            self.jointJob = cmds.scriptJob(attributeChange = [self.activeJoint+".xformMatrix",self.fixJointOrient],runOnce = True)#call fixJointOrient() when attribute of activeJoint changed
            self.lastJoint = self.activeJoint
     
    #set joint orient according to joint type             
    def setJointOrient(self,parentJnt,jnt,childList,secondAxisOrient):   
        print jnt+" setJointOrient"
        if jnt not in self.ignoreJoint:
            if jnt == "C_Pelvis":
                for j in childList:
                    cmds.parent(j,world = True)
                cmds.aimConstraint("C_Spine_0",jnt,aimVector = self.primaryAxis,upVector = self.secondaryAxis,worldUpVector = secondAxisOrient)
                cmds.aimConstraint("C_Spine_0",jnt, edit = True, remove = True)
                for j in childList:
                    cmds.parent(j,jnt)
            elif jnt == "L_Wrist":
                for j in childList:
                    cmds.parent(j,world = True)
                cmds.orientConstraint("L_Ring_0","L_Middle_0",jnt,weight = 1)
                cmds.orientConstraint("L_Ring_0","L_Middle_0",jnt, edit = True, remove = True)
                cmds.aimConstraint("L_Middle_0",jnt,aimVector = self.primaryAxis,upVector = self.secondaryAxis,worldUpVector = secondAxisOrient,skip = ["y","z"])
                cmds.aimConstraint("L_Middle_0", jnt, edit = True, remove = True)
                for j in childList:
                    cmds.parent(j,jnt)
            elif len(childList) == 0:      
                if parentJnt !="":
                    cmds.parent(jnt,world = True)              
                primaryAxis = []
                for i in self.primaryAxis:
                    primaryAxis.append(-i)
                cmds.aimConstraint(parentJnt,jnt,aimVector = primaryAxis,upVector = self.secondaryAxis,worldUpVector = secondAxisOrient)
                cmds.aimConstraint(parentJnt, jnt, edit = True, remove = True)
                if parentJnt !="":
                    cmds.parent(jnt, parentJnt) 
                
            elif len(childList) >= 1:
                for j in childList:
                    cmds.parent(j,world = True)
                cmds.aimConstraint(childList[0],jnt,aimVector = self.primaryAxis,upVector = self.secondaryAxis,worldUpVector = secondAxisOrient)
                cmds.aimConstraint(childList[0],jnt, edit = True, remove = True)
                for j in childList:
                    cmds.parent(j,jnt)
            cmds.makeIdentity(jnt,apply = True,rotate = True)     
           
    #call setJointOrient() according to joint type
    def fixJointOrient(self): 
        parentJnt,jnt,childJntList = self.getRelativeJoint()
        if jnt != "":
            inIK,indexJnt = self.judgeIK(jnt)
            if jnt.find("locator_") !=-1:
                if inIK:
                    self.handleIKGroups(jnt,indexJnt,onlyLocator = True)
                else:
                    return
            else:
                self.setJntAttrLock(False) 
                if inIK:
                    self.handleIKGroups(jnt,indexJnt)
                else:
                    self.setJointOrient(parentJnt,jnt,childJntList,self.secondaryAxisOrient)
                if parentJnt != "":
                    #correct orient of activeJoint's parentJoint
                    inIK,indexParent = self.judgeIK(parentJnt)
                    p,j,c = self.getRelativeJoint(parentJnt)
                    if inIK and indexParent != indexJnt:
                        self.handleIKGroups(parentJnt,indexParent)
                    elif not inIK:
                        self.setJointOrient(p,j,c,self.secondaryAxisOrient)
                self.keepFaceOrient(self.facialJoint)
                self.setJntAttrLock(True)
            cmds.select(jnt)             
            self.jointJob = cmds.scriptJob(attributeChange = [jnt+".xformMatrix",self.fixJointOrient],runOnce = True)
    
    #get the current activeJoint and its child and parent joint         
    def getRelativeJoint(self,jnt = ""):    
        if self.displayAxis !=[]:
            self.displayLocalAxis(self.displayAxis,False)
        if jnt == "":
            jointList = cmds.ls(sl=True,type="joint")
            if len(jointList) != 0:
                self.activeJoint = jointList[0]
                self.displayLocalAxis([self.activeJoint],True)
                childJointList = cmds.listRelatives(children = True)
                if childJointList == None:
                    childJointList = []
                parentJoint = cmds.listRelatives(parent = True)
                if parentJoint == None:
                    parentJoint = ""
                else:
                    parentJoint = parentJoint[0]
                self.displayLocalAxis([parentJoint],True)               
                return parentJoint,self.activeJoint,childJointList
            else:
                locatorList = cmds.ls(sl=True,type="transform")
                if len(locatorList) != 0 and locatorList[0].find("locator_")!=-1:
                    self.activeJoint = locatorList[0]
                    return "",locatorList[0],""
                else:
                    return "","",""
        else:   
            parentJoint = cmds.listRelatives(jnt,parent = True)
            if parentJoint == None:
                parentJoint = ""
            else:
                parentJoint = parentJoint[0]
            childJointList = cmds.listRelatives(jnt,children = True)
            if childJointList == None:
                childJointList = []
            return parentJoint,jnt,childJointList
             
    #change the display state of joint's loacl axis        
    def displayLocalAxis(self,jointList,switch):    
        for jnt in jointList:
            if jnt !="" and cmds.objExists(jnt) and cmds.objectType(jnt,isType = "joint"):    
                cmds.setAttr(jnt+".displayLocalAxis",switch)
                if switch == True:
                    self.displayAxis.append(jnt)
    
    #determines whether a given joint is in a IKgroup
    def judgeIK(self,jnt):
        print jnt+" judgeIK"
        inIK = False
        if self.IKGroups !=[]:
            for index in range(len(self.IKGroups)):
                if jnt in self.IKGroups[index]:
                    inIK = True
                    return inIK,index
        return inIK,-1
    
    #handle the orient of all joint in given IKGroup    
    def handleIKGroups(self,jnt,index,onlyLocator = False):
        print jnt+" handleIKGroups"
        head = self.IKGroups[index][0]
        end = self.IKGroups[index][-2]
        locator = self.IKGroups[index][-1]
        middle = jnt
        hasLocator = True
        if locator.find("locator_") ==-1:
            end = self.IKGroups[index][-1]
            hasLocator = False
            locator = ""
        if middle==head or middle==end or middle == locator:
            i = int(len(self.IKGroups[index])/2-1)
            middle = self.IKGroups[index][i]
        a = cmds.xform(head,query = True,worldSpace = True,translation = True)
        b = cmds.xform(middle,query = True,worldSpace = True,translation = True)
        c = cmds.xform(end,query = True,worldSpace = True,translation = True)
        ab = map(lambda x,y:x-y,b,a)
        ac = map(lambda x,y:x-y,c,a)
        normal = [ac[1]*ab[2]-ac[2]*ab[1],ac[2]*ab[0]-ac[0]*ab[2],ac[0]*ab[1]-ac[1]*ab[0]]
        length = math.sqrt(math.fsum(x**2 for x in normal))
        unitNormal = [normal[0]/length,normal[1]/length,normal[2]/length]
        if onlyLocator == False:
            for j in self.IKGroups[index]:                      
                if j not in [head,middle,end,locator]:
                    p,j,c = self.getRelativeJoint(j)
                    cmds.parent(j,world = True)
                    cmds.parent(c[0],world = True)
                    d = cmds.xform(j,query = True,worldSpace = True,translation = True)
                    da = map(lambda x,y:x-y,a,d)
                    temp = map(lambda x,y:x*y,unitNormal,da)
                    dot = temp[0]+temp[1]+temp[2]
                    newXform = [unitNormal[0]*dot,unitNormal[1]*dot,unitNormal[2]*dot]
                    cmds.xform(j,worldSpace = True,relative = True,translation = newXform)
                    cmds.parent(j,p)
                    cmds.parent(c[0],j)
            for j in self.IKGroups[index]:
                if j != locator:
                    p,j,c = self.getRelativeJoint(j)
                    self.setJointOrient(p,j,c,normal)
        if hasLocator:
            locatorOldXform = cmds.xform(locator,query = True,worldSpace = True,translation = True)
            print locatorOldXform
            bl = map(lambda x,y:x-y,locatorOldXform,b)
            oldLength = math.sqrt(math.fsum(x**2 for x in bl))
            acLength = math.sqrt(math.fsum(x**2 for x in ac))
            temp = map(lambda x,y:x*y,ac,ab)
            aeLength = (temp[0]+temp[1]+temp[2])/acLength
            ae = [ac[0]*aeLength/acLength,ac[1]*aeLength/acLength,ac[2]*aeLength/acLength]
            e = map(lambda x,y:x+y,a,ae)
            eb = map(lambda x,y:x-y,b,e)
            ebLength = math.sqrt(math.fsum(x**2 for x in eb))
            ebUnit = [eb[0]/ebLength,eb[1]/ebLength,eb[2]/ebLength]
            locatorNewXform = map(lambda x,y:x+oldLength*y,b,ebUnit)
            cmds.xform(locator,worldSpace = True,translation = locatorNewXform)          
        if self.debugMode:
            self.debugIKPlane(index)
                        
    #keep Face joint Orient always in specific orient                    
    def keepFaceOrient(self,jntList):
        for jnt in jntList:
            if cmds.objExists(jnt):
                p,j,c = self.getRelativeJoint(jnt)
                for child in c:
                    cmds.parent(child,world = True)              
                if jnt == "L_Eye":
                    cmds.makeIdentity(jnt,apply = True,rotate = True)
                    jointOrientY = cmds.getAttr(jnt+".jointOrientY")
                    cmds.parent(jnt,world = True)
                    cmds.makeIdentity(jnt,apply = True,rotate = True,jointOrient = True)
                    cmds.parent(jnt,p)
                    cmds.setAttr(jnt+".jointOrientY",jointOrientY)
                else:
                    cmds.parent(jnt,world = True)
                    cmds.makeIdentity(jnt,apply = True,rotate = True,jointOrient = True)
                    cmds.setAttr(jnt+".jointOrientY",-90)
                    cmds.parent(jnt,p)
                for child in c:
                    cmds.parent(child,jnt)
    
    #unlock or re-lock the channal of specific joints
    def setJntAttrLock(self,bool):
        for jnt,attr in self.lockedAttrDict.items():
            for a in attr:
                cmds.setAttr(jnt+a,lock = bool)
        print "setLock",bool    
      
                        
               
    def addIKGroups(self):
        selectJoints = cmds.ls(sl = True,type = ["joint","transform"],)
        if len(selectJoints) > 2:
            self.IKGroups.append(selectJoints)
        print "IKGroups = ",self.IKGroups

    def clearIKGroups(self): 
        self.IKGroups = []
        print "IKGroups = ",self.IKGroups
        
    def defaultIKGroup(self): 
        self.IKGroups = self.defaultIKGroups
        print "IKGroups = ",self.IKGroups   
         
    def displayIKGroups(self):
        for index in range(len(self.IKGroups)):
            cmds.select(self.IKGroups[index],add = True)
        print "IKGroups = ",self.IKGroups
        
    def switchDebugPlane(self,switch):
        if switch:
            self.debugMode = True
            print "DebugMode On"           
        else:
            self.debugMode = False
            print "DebugMode Off"
            if cmds.objExists("DebugPlane"):
                cmds.delete("DebugPlane")
            
    #draw debugPlane of given IKGroup
    def debugIKPlane(self,index):
        if cmds.objExists("DebugPlane"):
            cmds.delete("DebugPlane")
        planePoint = []
        for Joint in self.IKGroups[index]:
            planePoint.append(cmds.xform(Joint,query = True,worldSpace = True,translation = True))
        cmds.polyCreateFacet(name = "DebugPlane",point = planePoint)
        shadeGroup = cmds.listConnections("DebugPlaneShape",type = "shadingEngine")
        listConnected = cmds.listConnections(shadeGroup)
        material = cmds.ls(listConnected,materials = True)[0]
        cmds.setAttr(material+".ambientColor",0,1,0,0)
        cmds.setAttr(material+".transparency",0.7,0.7,0.7,0.7)
   
    def mirror(self,MirrorPlane):
        for jnt in self.mirrorJoints:
            if cmds.objExists(jnt):
                if MirrorPlane == "xy":
                    cmds.mirrorJoint(jnt,mirrorBehavior = True,mirrorXY = True,searchReplace = ["L_","R_"])
                elif MirrorPlane == "xz":
                    cmds.mirrorJoint(jnt,mirrorBehavior = True,mirrorXZ = True,searchReplace = ["L_","R_"])
                elif MirrorPlane == "yz":
                    cmds.mirrorJoint(jnt,mirrorBehavior = True,mirrorYZ = True,searchReplace = ["L_","R_"])
            else:
                print jnt+" of self.mirrorJoints doesn`t exist in scence" 
        for locator in self.mirrorLocator:
            if cmds.objExists(locator):
                copyName = locator.replace("L_","R_",1)
                cmds.duplicate(locator,name = copyName)
                if MirrorPlane == "xy":
                    i = cmds.getAttr(copyName+".translateZ")
                    cmds.setAttr(copyName+".translateZ",-i)              
                elif MirrorPlane == "xz":
                    i = cmds.getAttr(copyName+".translateY")
                    cmds.setAttr(copyName+".translateY",-i)           
                elif MirrorPlane == "yz": 
                    i = cmds.getAttr(copyName+".translateX")
                    cmds.setAttr(copyName+".translateX",-i)
        
    def displayMirror(self):
        for jnt in self.mirrorJoints:
            if jnt !="" and cmds.objExists(jnt):
                cmds.select(jnt,add = True)
            else:
                print jnt+" of mirrorJoints doesn`t exist in secne"
        for locator in self.mirrorLocator:
            if locator !="" and cmds.objExists(locator):
                cmds.select(locator,add = True)
            else:
                print locator+" of mirrorLocator doesn`t exist in secne"
        print "mirrorJoints = ",self.mirrorJoints
        print "mirrorLocators = ",self.mirrorLocator
        
    def defaultMirror(self): 
        self.mirrorJoints = self.defaultMirrorJnt
        self.mirrorLocator = self.defaultMirrorLocator
        print "mirrorJoints = ",self.mirrorJoints
        print "mirrorLocators = ",self.mirrorLocator
        
    def clearMirror(self):
        self.mirrorJoints = []
        self.mirrorLocator = []
        print "mirrorJoints = ",self.mirrorJoints 
        print "mirrorLocators = ",self.mirrorLocator
        
    def addMirror(self):
        selectJoints = cmds.ls(sl = True,type = ["joint","transform"])
        if len(selectJoints) > 0:
            for jnt in selectJoints:
                if cmds.objectType(jnt,isType = "joint"):
                    self.mirrorJoints.append(jnt)
                else:
                    self.mirrorLocator.append(jnt)
        print "mirrorJoints = ",self.mirrorJoints
        print "mirrorLocators = ",self.mirrorLocator
    
           
                  
fjm = FixJointMode()
#fjm.switchMode(True)
#fjm.switchDebugPlane()
#fjm.addIKGroups()
#fjm.cleanIKGroups()
                 