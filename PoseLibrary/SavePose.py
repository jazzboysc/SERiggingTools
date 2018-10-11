import os
import cPickle
import PoseConfig
import maya.cmds as cmds

PoseRootPath = os.path.dirname(PoseConfig.__file__)
PoseDataParh = PoseRootPath + "\\PoseFile\\"
print "PoseRootPath :"
print PoseRootPath

def savePose( PoseData ):
    print'try save pose!!!'
    
    saveDataToFile(PoseData)

def openPoseLibraryFile():
    Paths = os.listdir(PoseDataParh)
    PoseLibrary = []
    for x in Paths:
        PoseLibrary.append(x.split('.')[0])
    return PoseLibrary

def getDataByName(PoseName):
    try: f = open( PoseDataParh + PoseName + ".pose" , "r");
    except:
        cmds.confirmDialog(title = "Save Pose", icon = "critical", message = "Unable to open" + PoseDataParh + PoseName + ".pose" )
        return
    try:PoseData = cPickle.load(f)
    except :
        cmds.confirmDialog(title = "Save Pose", icon = "critical", message = "Unable to Load" + PoseDataParh + PoseName + ".pose" )
    f.close()
    return PoseData

def saveDataToFile(PoseData):
    try:
        f = open( PoseRootPath + "\\PoseFile\\" + PoseData["poseName"]+".pose" , "w");
    except :
        cmds.confirmDialog(title = "Save Pose", icon = "critical", message = "Unable to open" + PoseRootPath + "\\PoseFile\\" + PoseData["poseName"]+".txt" )
        raise 
    cPickle.dump(PoseData, f)
    f.close();