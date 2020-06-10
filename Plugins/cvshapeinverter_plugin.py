"""
The MIT License (MIT)

Copyright (c) 2014 Chad Vernon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMaya as OpenMaya
import math

API_VERSION = OpenMaya.MGlobal.apiVersion()

#-----------------------------------------------------------------------------
class cvShapeInverter(OpenMayaMPx.MPxDeformerNode):
    kPluginNodeName = "cvShapeInverter"
    kPluginNodeId = OpenMaya.MTypeId(0x00115805)
    aMatrix = OpenMaya.MObject()
    aCorrectiveGeo = OpenMaya.MObject()
    aDeformedPoints = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxDeformerNode.__init__(self)
        self.__initialized = False
        self.__matrices = []
        self.__deformedPoints = OpenMaya.MPointArray()

    def deform(self, data, itGeo, localToWorldMatrix, geomIndex):
        # Get the corrective mesh
        oMesh = data.inputValue(cvShapeInverter.aCorrectiveGeo).asMesh()
        if oMesh.isNull():
            # Not connected yet
            return
        fnMesh = OpenMaya.MFnMesh(oMesh)
        correctivePoints = OpenMaya.MPointArray()
        fnMesh.getPoints(correctivePoints)

        # Read the matrices
        if not self.__initialized:
            hMatrix = data.inputArrayValue(cvShapeInverter.aMatrix)
            matrixCount = hMatrix.elementCount()
            if matrixCount == 0:
                # No data yet
                return
            for i in range(matrixCount):
                hMatrix.jumpToArrayElement(i)
                self.__matrices.append(hMatrix.inputValue().asMatrix())

            oDeformedPoints = data.inputValue(cvShapeInverter.aDeformedPoints).data()
            fnData = OpenMaya.MFnPointArrayData(oDeformedPoints)
            fnData.copyTo(self.__deformedPoints)
            self.__initialized = True


        # Perform the inversion calculation
        while not itGeo.isDone():
            index = itGeo.index()
            delta = correctivePoints[index] - self.__deformedPoints[index]

            if (math.fabs(delta.x) < 0.001
                    and math.fabs(delta.y) < 0.001
                    and math.fabs(delta.z) < 0.001):
                itGeo.next()
                continue

            offset = delta * self.__matrices[index]
            pt = itGeo.position() + offset
            itGeo.setPosition(pt)
            itGeo.next()

#-----------------------------------------------------------------------------
def creator():
    return OpenMayaMPx.asMPxPtr(cvShapeInverter())

#-----------------------------------------------------------------------------
def initialize():
    mAttr = OpenMaya.MFnMatrixAttribute()
    tAttr = OpenMaya.MFnTypedAttribute()
    nAttr = OpenMaya.MFnNumericAttribute()

    if API_VERSION < 201600:
        outputGeom = OpenMayaMPx.cvar.MPxDeformerNode_outputGeom
    else:
        outputGeom = OpenMayaMPx.cvar.MPxGeometryFilter_outputGeom

    cvShapeInverter.aCorrectiveGeo = tAttr.create('correctiveMesh', 'cm', OpenMaya.MFnData.kMesh)
    cvShapeInverter.addAttribute(cvShapeInverter.aCorrectiveGeo)
    cvShapeInverter.attributeAffects(cvShapeInverter.aCorrectiveGeo, outputGeom)

    cvShapeInverter.aDeformedPoints = tAttr.create('deformedPoints', 'dp',
            OpenMaya.MFnData.kPointArray)
    cvShapeInverter.addAttribute(cvShapeInverter.aDeformedPoints)

    cvShapeInverter.aMatrix = mAttr.create('inversionMatrix', 'im')
    mAttr.setArray(True)
    cvShapeInverter.addAttribute(cvShapeInverter.aMatrix)

#-----------------------------------------------------------------------------
def initializePlugin(mobject):
    plugin = OpenMayaMPx.MFnPlugin(mobject)
    plugin.registerNode(cvShapeInverter.kPluginNodeName, cvShapeInverter.kPluginNodeId, creator,
            initialize, OpenMayaMPx.MPxNode.kDeformerNode)

#-----------------------------------------------------------------------------
def uninitializePlugin(mobject):
    plugin = OpenMayaMPx.MFnPlugin(mobject)
    plugin.deregisterNode(cvShapeInverter.kPluginNodeId)
#-----------------------------------------------------------------------------
