import sys
import maya.api.OpenMaya as OpenMaya

def maya_useNewAPI():
	pass

kPluginRigCharacterTypeNodeName = 'RigCharacterType'
kPluginRigCharacterTypeNodeClassify = 'utility/general'
kPluginRigCharacterTypeNodeId = OpenMaya.MTypeId(0x00001)

#-----------------------------------------------------------------------------
# Rig Character Type Class
# Sun Che
#-----------------------------------------------------------------------------
class RigCharacterType(OpenMaya.MPxNode):
    def __init__(self):
        OpenMaya.MPxNode.__init__(self)
        
    def compute(self, pPlug, pDataBlock):
        pass

def rigCharacterTypeNodeCreator():
    return  RigCharacterType()

def rigCharacterTypeNodeInitializer():
    pass

kPluginRigComponentTypeNodeName = 'RigComponentType'
kPluginRigComponentTypeNodeClassify = 'utility/general'
kPluginRigComponentTypeNodeId = OpenMaya.MTypeId(0x00002)

#-----------------------------------------------------------------------------
# Rig Component Type Class
# Sun Che
#-----------------------------------------------------------------------------
class RigComponentType(OpenMaya.MPxNode):
    def __init__(self):
        OpenMaya.MPxNode.__init__(self)
        
    def compute(self, pPlug, pDataBlock):
        pass

def rigComponentTypeNodeCreator():
    return  RigComponentType()

def rigComponentTypeNodeInitializer():
    pass

kPluginRigControlTypeNodeName = 'RigControlType'
kPluginRigControlTypeNodeClassify = 'utility/general'
kPluginRigControlTypeNodeId = OpenMaya.MTypeId(0x00003)

#-----------------------------------------------------------------------------
# Rig Control Type Class
# Sun Che
#-----------------------------------------------------------------------------
class RigControlType(OpenMaya.MPxNode):
    def __init__(self):
        OpenMaya.MPxNode.__init__(self)
        
    def compute(self, pPlug, pDataBlock):
        pass

def rigControlTypeNodeCreator():
    return  RigControlType()

def rigControlTypeNodeInitializer():
    pass


#-----------------------------------------------------------------------------
def initializePlugin(mobject):
    mplugin = OpenMaya.MFnPlugin(mobject)

    try:
        mplugin.registerNode(kPluginRigCharacterTypeNodeName, kPluginRigCharacterTypeNodeId, rigCharacterTypeNodeCreator,
                             rigCharacterTypeNodeInitializer, OpenMaya.MPxNode.kDependNode, kPluginRigCharacterTypeNodeClassify)
    except:
        sys.stderr.write('Failed to register node: ' + kPluginRigCharacterTypeNodeName)
        raise

    try:
        mplugin.registerNode(kPluginRigComponentTypeNodeName, kPluginRigComponentTypeNodeId, rigComponentTypeNodeCreator,
                             rigComponentTypeNodeInitializer, OpenMaya.MPxNode.kDependNode, kPluginRigComponentTypeNodeClassify)
    except:
        sys.stderr.write('Failed to register node: ' + kPluginRigComponentTypeNodeName)
        raise

    try:
        mplugin.registerNode(kPluginRigControlTypeNodeName, kPluginRigControlTypeNodeId, rigControlTypeNodeCreator,
                             rigControlTypeNodeInitializer, OpenMaya.MPxNode.kDependNode, kPluginRigControlTypeNodeClassify)
    except:
        sys.stderr.write('Failed to register node: ' + kPluginRigControlTypeNodeName)
        raise

#-----------------------------------------------------------------------------
def uninitializePlugin(mobject):
    mplugin = OpenMaya.MFnPlugin(mobject)

    try:
        mplugin.deregisterNode(kPluginRigCharacterTypeNodeId)
    except:
        sys.stderr.write('Failed to deregister node: ' + kPluginRigCharacterTypeNodeName)
        raise

    try:
        mplugin.deregisterNode(kPluginRigComponentTypeNodeId)
    except:
        sys.stderr.write('Failed to deregister node: ' + kPluginRigComponentTypeNodeName)
        raise

    try:
        mplugin.deregisterNode(kPluginRigControlTypeNodeId)
    except:
        sys.stderr.write('Failed to deregister node: ' + kPluginRigControlTypeNodeName)
        raise