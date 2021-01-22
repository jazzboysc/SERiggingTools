from pyfbsdk import FBMenuManager, FBMessageBox

from ..MoboToMayaTools.MoboServer2020 import startMotionbuilderServer
from ..MoboToMayaTools.SendAnimationToMayaTool import showSendToMayaUI

def OnMenuClick(eventName):
    if eventName == "Start Mobo Server":
        startMotionbuilderServer()
    elif eventName == "Send To Maya":
        showSendToMayaUI()
    else:
        FBMessageBox("Error...", "Menu Error: This option hasn't been set up yet.", "OK")


# Creates the menu.
def LoadMenu():
       
    def MenuOptions(control, event):
        eventName = event.Name
        OnMenuClick(eventName)
    
    mainMenuName = "MoboToMaya"
    
    menuManager = FBMenuManager()
    
    menuManager.InsertLast( None, mainMenuName )
    menuManager.InsertLast( mainMenuName, "Start Mobo Server" )
    menuManager.InsertLast( mainMenuName, "" )
    menuManager.InsertLast( mainMenuName, "Send To Maya" )
    
    # Example menu structure for future menu items...
    # Line break:                   menuManager.InsertLast( mainMenuName, "" )
    # Sub-menu:                     menuManager.InsertLast( mainMenuName, "TestSubMenu" )
    # Menu option inside sub-menu:  menuManager.InsertLast( mainMenuName + "/TestSubMenu", "TestFunction" )

    # Adds the created menu to the Mobo tool bar.    
    def AddMenu(mainMenuName, subMenuName = ""):
        menu = FBMenuManager().GetMenu( mainMenuName + subMenuName)
        if menu:
            menu.OnMenuActivate.Add( MenuOptions )
    
    AddMenu(mainMenuName)