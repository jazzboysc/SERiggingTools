import os
import cPickle
import PoseConfig
import maya.cmds as cmds

PoseRootPath = os.path.dirname(PoseConfig.__file__)

def savePose( PoseData ):
    print'try save pose!!!'
    
    saveDataToFile(PoseData)

def openPoseLibraryFile():
    try: f = open( PoseRootPath + "\\PoseLibrary.txt" , "r");
    except:
        cmds.confirmDialog(title = "Save Pose", icon = "critical", message = "Unable to open" + PoseRootPath + "\\PoseLibrary.txt" )
        print "openfail"
        raise;
    #PoseLibrary = cPickle.load(f)
    try: PoseLibrary = cPickle.load(f);
    except:
        #cmds.confirmDialog(title = "Save Pose", icon = "critical", message = "Unable to open" + PoseRootPath + "\\PoseLibrary.txt" )
        print "openfail"
        return None
        raise;
    f.close();

    # if os.path.exists(PoseRootPath + "\\PoseLibrary.txt"):
    #     f = open(PoseRootPath + "\\PoseLibrary.txt", 'r')
    #     if f.read() == '':
    #         return None
    #     else:
    #         print "djaksjdlasjdlkjaslkdjaslkdjals"
            
    #         try:PoseLibrary = cPickle.load(f)
    #         except :
    #             cmds.confirmDialog(title = "Save Pose", icon = "critical", message = "Unable to open" + PoseRootPath + "\\PoseLibrary.txt" )
    #         #print PoseLibrary
    #     f.close();
    # else:
    #     cmds.confirmDialog(title = "Save Pose", icon = "critical", message = "Unable to open" + PoseRootPath + "\\PoseLibrary.txt" )
    return PoseLibrary

def saveDataToFile(PoseData):
    # print PoseData
    # print PoseData['poseName']
    # print "11111111111111111111111111111111111111111111111111"
    # PoseLibraryData = openPoseLibraryFile()
    if os.path.exists(PoseRootPath + "\\PoseLibrary.txt"):
        PoseList = openPoseLibraryFile()
    else:
        PoseList = []

    try: f = open( PoseRootPath + "\\PoseLibrary.txt" , "w");
    except:
        cmds.confirmDialog(title = "Save Pose", icon = "critical", message = "Unable to open" + PoseRootPath + "\\PoseLibrary.txt" )
        raise;

    
    PoseSaveData = {}
    PoseSaveData[PoseData["poseName"]] = PoseData
    if PoseList == None:
        PoseList = [PoseSaveData]
    else :
        #PoseList = PoseLibraryData.get("PoseLibrary")
        # todo add unique
        PoseList.append(PoseSaveData)

    #PoseList.append(PoseSaveData)
    print "PoseList : " 
    print PoseList
    cPickle.dump(PoseList, f)
    f.close();