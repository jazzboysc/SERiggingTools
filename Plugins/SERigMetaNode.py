import sys
import maya.api.OpenMaya as OpenMaya

def maya_useNewAPI():
	pass

kPluginNodeName = 'RigMetaNode'
kPluginNodeClassify = 'utility/general'
kPluginNodeId = OpenMaya.MTypeId(0x00001)

sampleDefaultValue = 1

class RigMetaNode(OpenMaya.MPxNode):
    sampleInAttribute = OpenMaya.MObject()
    sampleOutAttribute = OpenMaya.MObject()
    
    def __init__(self):
        OpenMaya.MPxNode.__init__(self)
        
    def compute(self, pPlug, pDataBlock):

        if pPlug == myNode.sampleOutAttribute:
            
            sampleInDataHandle = pDataBlock.inputValue(myNode.sampleInAttribute)
            sampleOutDataHandle = pDataBlock.outputValue(myNode.sampleOutAttribute)
            
            sampleInValue = sampleInDataHandle.asFloat()
            
            sampleOutDataHandle.setFloat(sampleInValue)
            
            sampleOutDataHandle.setClean()
             
        else:
            return OpenMaya.kUnknownParameter

def nodeCreator():
    return  RigMetaNode()

def nodeInitializer():
    numericAttributeFn = OpenMaya.MFnNumericAttribute()
    
    global sampleDefaultValue
    RigMetaNode.sampleInAttribute = numericAttributeFn.create('myInputAttribute', 'i', OpenMaya.MFnNumericData.kFloat, sampleDefaultValue)
    numericAttributeFn.writable = True
    numericAttributeFn.storable = True
    numericAttributeFn.hidden = False
    RigMetaNode.addAttribute(RigMetaNode.sampleInAttribute)
    
    RigMetaNode.sampleOutAttribute = numericAttributeFn.create('myOutputAttribute', 'o', OpenMaya.MFnNumericData.kFloat)
    numericAttributeFn.storable = False
    numericAttributeFn.writable = False
    numericAttributeFn.readable = True
    numericAttributeFn.hidden = False
    RigMetaNode.addAttribute(RigMetaNode.sampleOutAttribute)
    
    RigMetaNode.attributeAffects(RigMetaNode.sampleInAttribute, RigMetaNode.sampleOutAttribute)
    
    
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