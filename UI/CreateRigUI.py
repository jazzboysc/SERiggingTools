import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
import maya.mel
import sys
import maya.cmds as cmds
import maya.OpenMayaUI as mui
from PySide2 import QtCore, QtGui, QtWidgets , QtUiTools
import shiboken2
import os
import time

import cPickle
#"E:/Users/admin/Documents/GitHub/SERiggingTools/UI/LoadRiggingUI.ui"
uifile_path = "E:/Users/admin/Documents/GitHub/SERiggingTools/UI/ControlRig.ui"

def OpenMayaWindow():
	''' todo: stop open more than one window'''
	# global ui
	# ui = loadUI(uifile_path)
	# ui.show()


	global mainWin
	mainWin = mainRigWindow()
	mainWin.show()
	pass

def loadUI(uifile_path):
	QtCore.QResource.addSearchPath("E:/Users/admin/Documents/GitHub/SERiggingTools/UI")
	uifile = QtCore.QFile(uifile_path)
	print(uifile)
	uifile.open(QtCore.QFile.ReadOnly)
	#QtCore.QResource.registerResource("E:/Users/admin/Documents/GitHub/SERiggingTools/UI/UIResource.qrc")
	uiWindow = QtUiTools.QUiLoader().load(uifile)
	uifile.close()

	rrr = QtCore.QResource.searchPaths()
	print(rrr)

	#uiWindow.label.setPixmap(QtGui.QPixmap(("E:/Users/admin/Documents/GitHub/SERiggingTools/UI/equipment_11_1.png")))
	return uiWindow

def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)

class mainRigWindow(QtWidgets.QDialog):
	"""docstring for mainWindow"""
	def __init__(self, parent=getMayaWindow()):
		super(mainRigWindow, self).__init__(parent)
		self.setWindowTitle('Load Rigging File')
		self.descLabel = QtWidgets.QLabel("Please choose the model and rig", parent=self)
		#self.arg = arg

		# ButtonOne = QtWidgets.QPushButton("Button1")
		# ButtonTwo = QtWidgets.QPushButton("Button2")

		# ButtonHLayout = QtWidgets.QHBoxLayout()
		# ButtonHLayout.addWidget(ButtonOne)
		# ButtonHLayout.addWidget(ButtonTwo)
		#ButtonHLayout.setParent(self)

		# LayoutOne = self.addLayoutOne()
		# LayoutTwo = self.addLayoutOne()
		

		TextLayoutModel = QtWidgets.QHBoxLayout()
		self.modelLine = QtWidgets.QLineEdit()
		TextLayoutModel.addWidget(QtWidgets.QLabel("model :"))
		TextLayoutModel.addWidget(self.modelLine)
		self.SetModelFileButton = QtWidgets.QPushButton("Set File")
		TextLayoutModel.addWidget(self.SetModelFileButton)

		TextLayoutRig = QtWidgets.QHBoxLayout()
		self.buliderLine = QtWidgets.QLineEdit()
		TextLayoutRig.addWidget(QtWidgets.QLabel("bulider   :"))
		TextLayoutRig.addWidget(self.buliderLine)
		self.SetBuilderFileButton = QtWidgets.QPushButton("Set File")
		TextLayoutRig.addWidget(self.SetBuilderFileButton)

		mainLayout = QtWidgets.QVBoxLayout(self)
		mainLayout.addWidget(self.descLabel)
		# mainLayout.addLayout(LayoutOne)
		# mainLayout.addLayout(LayoutTwo)
		mainLayout.addLayout(TextLayoutModel)
		mainLayout.addLayout(TextLayoutRig)
		self.SetBuilderConfigWeight(mainLayout)

		self.connect(self.SetModelFileButton, QtCore.SIGNAL("clicked()"), self.selectModelFile)
		self.connect(self.SetBuilderFileButton, QtCore.SIGNAL("clicked()"), self.selectBuilderFile)

		confirmLayout = QtWidgets.QHBoxLayout()
		self.ConfirmButton = QtWidgets.QPushButton("Create Rig")
		self.CancelButton = QtWidgets.QPushButton("Cancel")
		confirmLayout.addWidget(self.ConfirmButton)
		confirmLayout.addWidget(self.CancelButton)
		mainLayout.addLayout(confirmLayout)

		self.connect(self.ConfirmButton, QtCore.SIGNAL("clicked()"), self.CreateRig)
		self.connect(self.CancelButton, QtCore.SIGNAL("clicked()"), self.close)
		#mainLayout.addLayout(ButtonHLayout)
		#self.addLayout(ButtonHLayout)
		#self.setLayout(ButtonHLayout)
		self.resize(400, 10)


	#############################################################################################################################	

	def addLayoutOne(self):
		ButtonOne = QtWidgets.QPushButton("Button1")
		ButtonTwo = QtWidgets.QPushButton("Button2")

		ButtonHLayout = QtWidgets.QHBoxLayout()
		ButtonHLayout.addWidget(ButtonOne)
		ButtonHLayout.addWidget(ButtonTwo)
		return ButtonHLayout
		pass

	def selectModelFile(self):
		fileResult = cmds.fileDialog2( fm = 1 )
		if fileResult != None:
			print(fileResult[0])
			self.modelLine.setText(fileResult[0])
			#mainWin.show()
			mainWin.update()
			#cmds.file( fileResult[0], i=True );

	def selectBuilderFile(self):
		fileResult = cmds.fileDialog2( fm = 1 )
		if fileResult != None:
			print(fileResult[0])
			self.buliderLine.setText(fileResult[0])
			mainWin.update()

	def CreateRig(self):
		modelStr = self.modelLine.text()
		buliderStr = self.buliderLine.text()
		print(modelStr)
		cmds.file( modelStr, i=True );
		cmds.file( buliderStr, i=True );
		return

	#upperBodyUpperLimbKnobCount = 2, 
 	#upperBodyLowerLimbKnobCount = 2,
 	#lowerBodyUpperLimbKnobCount = 2,
 	#lowerBodyLowerLimbKnobCount = 1,
	def SetBuilderConfigWeight(self , mainLayout ):
		groupBox = QtWidgets.QVBoxLayout()
		upperBodyUpperLayout = QtWidgets.QHBoxLayout()
		upperBodyUpperLayout.addWidget(QtWidgets.QLabel("upperArmTwist :"))
		self.upperBodyUpperLine = QtWidgets.QLineEdit()
		#ValidatorOne = QtGui.QIntValidator(1,5)
		self.upperBodyUpperLine.setValidator(QtGui.QIntValidator(1,5))
		upperBodyUpperLayout.addWidget(self.upperBodyUpperLine)
		self.upperBodyUpperLine.setText(str(1))
		upperBodyUpperLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
		upperBodyUpperLayout.addSpacing(220)
		# self.upperBodyUpperSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		# self.upperBodyUpperSlider.setMaximum(5)
		# self.upperBodyUpperSlider.setMinimum(1)
		# self.connect(self.upperBodyUpperSlider, QtCore.SIGNAL('valueChanged(int)'),self.upperBodyUpperSliderChangeValue)
		# self.upperBodyUpperNum = QtWidgets.QLabel( str( self.upperBodyUpperSlider.value() ))
		# upperBodyUpperLayout.addWidget(self.upperBodyUpperNum)
		# upperBodyUpperLayout.addWidget(self.upperBodyUpperSlider)
		groupBox.addLayout(upperBodyUpperLayout)

		upperBodyLowerLayout = QtWidgets.QHBoxLayout()
		upperBodyLowerLayout.addWidget(QtWidgets.QLabel("lowerArmTwist :"))
		self.upperBodyLowerLine = QtWidgets.QLineEdit()
		self.upperBodyLowerLine.setValidator(QtGui.QIntValidator(1,5))
		upperBodyLowerLayout.addWidget(self.upperBodyLowerLine)
		self.upperBodyLowerLine.setText(str(1))
		upperBodyLowerLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
		upperBodyLowerLayout.addSpacing(220)
		# self.upperBodyLowerSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		# self.upperBodyLowerSlider.setMaximum(5)
		# self.upperBodyLowerSlider.setMinimum(1)
		# self.connect(self.upperBodyLowerSlider, QtCore.SIGNAL('valueChanged(int)'),self.upperBodyLowerSliderChangeValue)
		# self.upperBodyLowerNum = QtWidgets.QLabel( str( self.upperBodyLowerSlider.value() ))
		# upperBodyLowerLayout.addWidget(self.upperBodyLowerNum)
		# upperBodyLowerLayout.addWidget(self.upperBodyLowerSlider)
		groupBox.addLayout(upperBodyLowerLayout)

		lowerBodyUpperLayout = QtWidgets.QHBoxLayout()
		lowerBodyUpperLayout.addWidget(QtWidgets.QLabel("upperLegTwist :"))
		self.lowerBodyUpperLine = QtWidgets.QLineEdit()
		self.lowerBodyUpperLine.setValidator(QtGui.QIntValidator(1,5))
		lowerBodyUpperLayout.addWidget(self.lowerBodyUpperLine)
		self.lowerBodyUpperLine.setText(str(1))
		lowerBodyUpperLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
		lowerBodyUpperLayout.addSpacing(220)
		# self.lowerBodyUpperSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		# self.lowerBodyUpperSlider.setMaximum(5)
		# self.lowerBodyUpperSlider.setMinimum(1)
		# self.connect(self.lowerBodyUpperSlider, QtCore.SIGNAL('valueChanged(int)'),self.lowerBodyUpperSliderChangeValue)
		# self.lowerBodyUpperNum = QtWidgets.QLabel( str( self.lowerBodyUpperSlider.value() ))
		# lowerBodyUpperLayout.addWidget(self.lowerBodyUpperNum)
		# lowerBodyUpperLayout.addWidget(self.lowerBodyUpperSlider)
		groupBox.addLayout(lowerBodyUpperLayout)

		lowerBodyLowerLayout = QtWidgets.QHBoxLayout()
		lowerBodyLowerLayout.addWidget(QtWidgets.QLabel("lowerLegTwist :"))
		self.lowerBodyLowerLine = QtWidgets.QLineEdit()
		self.lowerBodyUpperLine.setValidator(QtGui.QIntValidator(1,5))
		lowerBodyLowerLayout.addWidget(self.lowerBodyLowerLine)
		self.lowerBodyLowerLine.setText(str(1))
		lowerBodyLowerLayout.addWidget(QtWidgets.QLabel("( 1 - 5)"))
		lowerBodyLowerLayout.addSpacing(220)
		# self.lowerBodyLowerSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		# self.lowerBodyLowerSlider.setMaximum(5)
		# self.lowerBodyLowerSlider.setMinimum(1)
		# self.connect(self.lowerBodyLowerSlider, QtCore.SIGNAL('valueChanged(int)'),self.lowerBodyLowerSliderChangeValue)
		# self.lowerBodyLowerNum = QtWidgets.QLabel( str( self.lowerBodyLowerSlider.value() ))
		# lowerBodyLowerLayout.addWidget(self.lowerBodyLowerNum)
		# lowerBodyLowerLayout.addWidget(self.lowerBodyLowerSlider)
		groupBox.addLayout(lowerBodyLowerLayout)
		mainLayout.addLayout(groupBox)
		return
	'''
	def upperBodyUpperSliderChangeValue(self):
		pos = self.upperBodyUpperSlider.value()
		print(pos)
		self.upperBodyUpperNum.setText(str(pos))
		return		

	def upperBodyLowerSliderChangeValue(self):
		pos = self.upperBodyLowerSlider.value()
		print(pos)
		self.upperBodyLowerNum.setText(str(pos))
		return

	def lowerBodyUpperSliderChangeValue(self):
		pos = self.lowerBodyUpperSlider.value()
		print(pos)
		self.lowerBodyUpperNum.setText(str(pos))
		return

	def lowerBodyLowerSliderChangeValue(self):
		pos = self.lowerBodyLowerSlider.value()
		print(pos)
		self.lowerBodyLowerNum.setText(str(pos))
		return
	'''
		