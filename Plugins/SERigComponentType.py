import sys
import maya.api.OpenMaya as OpenMaya

def maya_useNewAPI():
	pass

kPluginNodeName = 'RigComponentType'
kPluginNodeClassify = 'utility/general'
kPluginNodeId = OpenMaya.MTypeId(0x00002)

class RigComponentType(OpenMaya.MPxNode):
    def __init__(self):
        OpenMaya.MPxNode.__init__(self)
        
    def compute(self, pPlug, pDataBlock):
        pass

def nodeCreator():
    return  RigComponentType()

def nodeInitializer():
    pass


def initializePlugin(mobject):
    mplugin = OpenMaya.MFnPlugin(mobject)
    try:
        mplugin.registerNode(kPluginNodeName, kPluginNodeId, nodeCreator,
                             nodeInitializer, OpenMaya.MPxNode.kDependNode, kPluginNodeClassify)
    except:
        sys.stderr.write('Failed to register node: ' + kPluginNodeName)
        raise

def uninitializePlugin(mobject):
    mplugin = OpenMaya.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(kPluginNodeId)
    except:
        sys.stderr.write('Failed to deregister node: ' + kPluginNodeName)
        raise