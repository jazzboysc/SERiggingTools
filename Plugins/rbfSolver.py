import math
from maya import OpenMaya, OpenMayaMPx

#-----------------------------------------------------------------------------
class MatrixNN( object ):
	'''
	row list form matrices
	exemple  A = [[0,3,1],[2,1,0],[1,0,3]]
	'''

	def __init__(self):
		
		# dimension
		# row column values
		self.dim = None
		self.rc  = None
	
	def setDimension( self, dim ):
		self.dim	= dim
		self.setIdentity()
	
	def setIdentity(self):
		self.rc	= [[float(i == j) for i in range(self.dim)] for j in range(self.dim)]
	
	def remove_rc(self, r, c):
		'''remove row [r] and column [c] in all remaining rows
		and reduce the dim of course'''
		
		self.rc.pop( r )
		self.dim	-= 1
		
		for i in range(self.dim) :
			self.rc[ i ].pop( c )
		
	def reduceDim(self, m,n,M):
		'''returns matrix A without the m th row and the n th column'''
		Mlin = len(M)
		result = []
		red = []
		for i in range(Mlin):
			if i != m:
				for j in range(Mlin):
					if (j != n):
						result.append(M[i][j])

		for k in range(0, len(result), Mlin - 1):
			red.append(result[k:k+Mlin-1])

		return red
	
	def determinant(self, A):
		'''returns the determinate of matrix A'''
		if len(A) == 1:
			return A[0][0]
		if len(A) == 2:
			r = A[0][0]*A[1][1]-A[0][1]*A[1][0]
			return r
		else:
			s = 0
			j = 0
			while j < len(A):
				B = self.reduceDim(j,0,A)
				if j%2 == 0:
					s = s+A[j][0]*self.determinant(B)
				else:
					s = s-A[j][0]*self.determinant(B)
				j = j+1
			return s
	
	def comat(self, A):
		'''Gives the comatrix of a matrix A'''
		n=self.dim
		k=0
		com=[None]*n
		while k<n:
			com[k]=[0]*n
			l=0
			while l<n:
				B=self.reduceDim(k,l,A)
				if (k+l)%2==0:
					com[k][l]=(self.determinant(B))
				else:
					com[k][l]=((-1)*self.determinant(B))
				l=l+1
			k=k+1
		return com
	
	def transpos(self, A):
		'''Gives the transposition of a matrix A'''
		n=self.dim
		M=[None]*n
		for i in xrange(n):
			M[i]=[0]*n
			for j in xrange(n):
				M[i][j]=A[j][i]
		return M
	
	def multCoef(self, A,r):
		'''Give the product of a matrix A by the coefficient r'''
		n=self.dim
		Mat=[None]*n
		for i in xrange(n):
			Mat[i]=[0]*n
			for j in xrange(n):
				Mat[i][j]=r*A[i][j]
		return Mat
	
	def inverse(self, A):
		'''returns the inverse of a square matrix'''
		d=self.determinant(A)
		if d == 0:
			return 'The matrix is not invertable'
		else:
			B=self.multCoef(self.comat(A),1./d)
			inv=self.transpos(B)
		return inv
	
	
	def mult(self, A, B):
		'''returns the product of the 2 '''
		TB = zip(*B)
		return [ [ sum(ea*eb for ea,eb in zip(a,b))  for b in TB ] for a in A ]
	
	def factorize_LU( self ):
		'''decomposition A = LU L lower triangular matrix and U upper triangular
		also return permutation ids'''
		
		# LU is an initially a copy of self
		LU	= list( self.rc )
		
		nRows, nCols	= self.dim, self.dim
		if nRows <= 1 :
			return None, None
		
		# Permutation Indices
		Pids		= range(self.dim)
		
		# already find the biggest ones by line:
		s	= [.0]*nRows
		for i in range( nRows ):
			smax = 0.0
			for j in range( nRows ):
				smax = max(smax, abs(LU[i][j]) )
			s[i] = smax
		
		for k in range(nRows-1):
			
			# Find the remaining row with the largest scaled pivot.
			#colMax	= LU[k][k]
			Pid = k
			rmax = 0.0
			
			for i in range( k, nRows ):
				
				r	= abs(LU[Pids[i]][k] / s[Pids[i]])
				if r > rmax :
					rmax = r
					j = i
			# Row j has the largest scaled pivot, so "swap" that row with the current row (row k). 
			# The swap is not actually done by copying rows, but by swaping two entries in an index vector.
			
			Pids[j], Pids[k] = Pids[k], Pids[j]
			
			# Now carry out the next elimination step as usual, except for the
			# added complication of the index vector.
			for i in range(k+1, nRows):
				xmult = LU[Pids[i]][k] / LU[Pids[k]][k]
				LU[Pids[i]][k] = xmult
				
				for j in range(k+1,  nCols):
					LU[Pids[i]][j] = LU[Pids[i]][j] - xmult*LU[Pids[k]][j]

		return LU, Pids
	
	def solve_LU( self, LU, Pids, b ):
		'''Solve LUx= b '''
		
		nRows, nCols = self.dim, self.dim
		x = [.0]*nRows
		
		for k in range( nRows-1):
			for i in range( k+1, nRows):
				b[Pids[i]] = b[Pids[i]] - LU[Pids[i]][k] * b[Pids[k]]
		
		for i in range( nRows-1, -1,-1):
			sum_ = b[Pids[i]]
			for j in range( i+1, nRows):
				sum_ = sum_ - LU[Pids[i]][j] * x[j]
			x[i] = sum_ / LU[Pids[i]][i]
		
		return x
#-----------------------------------------------------------------------------
class RbfSolver(OpenMayaMPx.MPxNode):
	
	kPluginNodeName	= "rbfSolver"
	kPluginNodeId = OpenMaya.MTypeId(0x0B8D357)

	epsilon	= 10e-15

	def euclidian_distance(dim, vec1, vec2):
		subVector = [vec1[n]-vec2[n] for n in range(dim)]
		powi_sum = sum(pow(subVector[i], 2) for i in range(dim))

		return pow(powi_sum, 0.5)
	
	def angular_distance(dim, vec1, vec2):
		'''vectors must be normalized and dimension 3 maximum'''

		dot	= sum(vec1[n]*vec2[n] for n in range(dim))
		if dot > 1.0:
			dot = 1.0
		elif dot < -1.0:
			dot = -1.0

		angle_rad = math.acos(dot)
		
		return angle_rad
	
	# for an angular distance the dimensionN cannot exceed 3 and the vectors must be 
	# normalized Whatever the function, fScale is multiplied by the distance.
	distance_functions = (euclidian_distance, angular_distance)

	def set_range(self, x, x0, x1, y0, y1):
		y = 1.0*(y0 + (x-x0)*(y1-y0)/(x1-x0))
		return y

	def linear_RBF(d):
		return d
		
	def gaussian_RBF(d):
		return math.exp(-d*d)

	def multiquadric(d):
		return math.sqrt(1.0 + d*d)
		
	def inverseQuadratic_RBF(d):
		return 1.0 / (1.0 + d*d)
		
	def inverseMultiquadratic_RBF(d):
		return 1.0 / math.sqrt((1.0 + d*d))
		
	def cubic_RBF(d):
		return d*d*d + 1.0
		
	def thinPlate_RBF(d):
		# not defined at 0 so use an epsilon
		if d < RbfSolver.epsilon:
			d = RbfSolver.epsilon
		return  d*d*math.log(d)

	rbf_functions = (linear_RBF,
					gaussian_RBF,
					multiquadric,
					inverseQuadratic_RBF,
					inverseMultiquadratic_RBF,
					cubic_RBF,
					thinPlate_RBF)
	
	@classmethod
	def nodeCreator(cls):
		return OpenMayaMPx.asMPxPtr(cls())

	@classmethod
	def nodeInitializer(cls):
		numAttr	= OpenMaya.MFnNumericAttribute()
		compAttr = OpenMaya.MFnCompoundAttribute()
		enumAttr = OpenMaya.MFnEnumAttribute()
		
		cls.NDimension = numAttr.create('NDimension', 'nd', OpenMaya.MFnNumericData.kInt, 1)
		numAttr.setMin(1)

		cls.MDimension = numAttr.create('MDimension', 'md', OpenMaya.MFnNumericData.kInt, 1)
		numAttr.setMin(1)
	
		cls.distanceMode = enumAttr.create('distanceMode', 'dist', 0)
		enumAttr.addField('Euclidian', 0)
		enumAttr.addField('Angular', 1)
		
		cls.rbfMode	= enumAttr.create('rbfMode', 'rbf', 1)
		enumAttr.addField('Linear', 0)
		enumAttr.addField('Gaussian' , 1)
		enumAttr.addField('Multiquadratic', 2)
		enumAttr.addField('Inverse Quadratic', 3)
		enumAttr.addField('Inverse Multiquadratic', 4)
		enumAttr.addField('Cubic', 5)
	
		# Scale is multiplied by distance
		cls.scale = numAttr.create('scale', 'sc', OpenMaya.MFnNumericData.kFloat, 1.0)
		numAttr.setMin(cls.epsilon)
		
		cls.normalize = numAttr.create('normalize', 'nz', OpenMaya.MFnNumericData.kBoolean, True)
		
		# force output in 0-1 range
		cls.blendShapeMode = numAttr.create('blendShapeMode', 'bsm', OpenMaya.MFnNumericData.kBoolean, False)

		cls.nInput = numAttr.create('nInput', 'ni', OpenMaya.MFnNumericData.kFloat, 0.0)
		numAttr.setKeyable(True)
		numAttr.setArray(True)
		
		# Poses
		cls.state = numAttr.create('enable', 'en', OpenMaya.MFnNumericData.kBoolean, True)
		#cls.weight	= numAttr.create( "weight","w",OpenMaya.MFnNumericData.kFloat, 1.0)

		cls.nKey = numAttr.create('nKey', 'nk', OpenMaya.MFnNumericData.kFloat, 0.0)
		numAttr.setArray(True)

		cls.mValue = numAttr.create('mValue', 'mv', OpenMaya.MFnNumericData.kFloat, 0.0)
		numAttr.setArray(True)
		
		cls.poses = compAttr.create('poses', 'ps')
		compAttr.addChild(cls.state)
		#compAttr.addChild(cls.weight)
		compAttr.addChild(cls.nKey)
		compAttr.addChild(cls.mValue)
		compAttr.setArray(True)
		
		# Output
		cls.solved = numAttr.create('solved', 'sv', OpenMaya.MFnNumericData.kBoolean, True)
		numAttr.setHidden(True)
		
		cls.mOutput	= numAttr.create('mOutput', 'mo', OpenMaya.MFnNumericData.kFloat, 0.0)
		numAttr.setWritable(False)
		numAttr.setArray(True)
		numAttr.setUsesArrayDataBuilder(True)

		# Add Addributes
		for attr in (cls.NDimension, cls.MDimension, cls.scale, cls.normalize, cls.blendShapeMode, cls.solved, cls.nInput, cls.distanceMode, cls.poses, cls.rbfMode, cls.mOutput):
			cls.addAttribute(attr)

		# Everything EXCEPT nInput regenerates the system.
		for attr in (cls.NDimension, cls.MDimension, cls.distanceMode, cls.rbfMode, cls.scale, cls.normalize, cls.poses):
			cls.attributeAffects(attr, cls.solved)

		# All recalculate the outputs.
		for attr in (cls.NDimension, cls.MDimension, cls.distanceMode, cls.rbfMode, cls.scale, cls.normalize, cls.blendShapeMode, cls.solved, cls.poses, cls.nInput):
			cls.attributeAffects(attr, cls.mOutput)
		
		# AE reorder
		cls.init_AETemplate()

	@classmethod
	def init_AETemplate(cls):
		AE_cmd = '''
		global proc AE[nodeType]Template(string $nodeName)
		{
		editorTemplate -beginScrollLayout;
			editorTemplate -beginLayout "Main Attributes" -collapse 0;
				editorTemplate -addControl "NDimension";
				editorTemplate -addControl  "MDimension" ;
				editorTemplate -addSeparator ;
				editorTemplate -addControl "distanceMode";
				editorTemplate -addControl "rbfMode";
				editorTemplate -addSeparator ;
				editorTemplate -addControl "scale";
				editorTemplate -addControl "normalize";
				editorTemplate -addSeparator ;
				editorTemplate -addControl "blendShapeMode";
				editorTemplate -addControl "nInput";
				editorTemplate -addControl "poses";
			editorTemplate -endLayout;
			editorTemplate -addExtraControls;
		editorTemplate -endScrollLayout;
		}
		'''.replace("[nodeType]", cls.kPluginNodeName)
		OpenMaya.MGlobal.executeCommand(AE_cmd)
	
	def __init__(self):
		OpenMayaMPx.MPxNode.__init__(self)
		
		# basic info queried in the rebuild_solver 
		# useless to re-query them each time
		self.N = 1
		self.M = 1
		self.fScale	= 1.0
		
		# info calculated in the rebuild_solver
		self.distance_function = None
		self.rbf_function = None
		self.poseUsed_ids = []
		
		# avoid the dicos for the framerate !!
		# nVector per pose containing the key poses
		# weight per pose
		self.nKeys = []
		self.weights = []
		
		# mVector containing solved coefficient
		self.mX = []

	def rebuild_solver(self, data):
		'''recalculate the solver using matrixMM
		no input or output in this code '''
		
		self.N = data.inputValue(self.NDimension).asInt()
		self.M = data.inputValue(self.MDimension).asInt()
		
		poses_H	= data.inputArrayValue(self.poses)
		pose_ids = OpenMaya.MIntArray()
		OpenMaya.MPlug(self.thisMObject(), self.poses).getExistingArrayAttributeIndices(pose_ids)
	
		self.poseUsed_ids = []
		
		# find the necessary information to create the system
		self.nKeys   = []
		mValues      = []
		self.weights = []
		
		for i in pose_ids:
			
			poses_H.jumpToElement(i)
			pose_H = poses_H.inputValue()
			
			state = pose_H.child(self.state).asBool()
			#wgt = pose_H.child(self.weight).asFloat()
			
			#if not (state and wgt>self.epsilon):
			#	continue
			if not state:
				continue

			nKey_H = OpenMaya.MArrayDataHandle(pose_H.child(self.nKey))
			nKey = []
			mValue_H = OpenMaya.MArrayDataHandle(pose_H.child(self.mValue))
			mValue = []
			
			for n in range(self.N):
				# try in case there is nothing connected ...
				try:
					nKey_H.jumpToElement(n)
					key	= nKey_H.inputValue().asFloat()
					nKey.append(key)
				except:
					nKey.append(0.0)
			
			# ignore the keys already present
			if nKey in self.nKeys:
				OpenMaya.MGlobal.displayWarning('key[%s] %s  can not be used more than once' %(i, nKey))
				continue
			
			for m in range(self.M):
				try:
					mValue_H.jumpToElement(m)
					value = mValue_H.inputValue().asFloat()
					mValue.append(value)
				except: 
					mValue.append(0.0)
			
			self.nKeys.append(nKey)
			mValues.append(mValue)
			#self.weights.append(wgt)
			
			self.poseUsed_ids.append(i)
		
		poseUsed_num = len(self.poseUsed_ids)
		
		if poseUsed_num in (0, 1):
			OpenMaya.MGlobal.displayError('RbfSolver failed: valid poses number is less than 2')
			return False
		
		# for the continuation need to know the functions used:
		# Distance function ?
		# RBF function ?
		normalize = data.inputValue(self.normalize).asBool()
		distance_id = data.inputValue(self.distanceMode).asInt()
		self.distance_function = self.distance_functions[distance_id]
		rbf_id = data.inputValue(self.rbfMode).asInt()
		self.rbf_function = self.rbf_functions[rbf_id]
	
		# matrixNN to solve systems AX = Y
		# factorize la and solve la for each m
		# store the X (m) in self.mX
		distanceMax	= 0.0
		mat = MatrixNN()
		mat.setDimension(poseUsed_num)
		
		#** for duplicate poses
		# remove the [row-column] containing .0 outside the diagonal
		toRemove = []
		
		for i in range(poseUsed_num) :
			for j in range(poseUsed_num) :
				
				if i == j :
					# here the distance of a pose on itself
					mat.rc[i][j] = 0.0
				else:
					# distance from each pose to each pose
					distance = self.distance_function( self.N, self.nKeys[ i ], self.nKeys[ j ]  )
					
					# stores the maximum distance between 2 exposures
					# this will be used to standardize the system
					if distance > distanceMax :
						distanceMax = distance
					
					mat.rc[i][j]	= distance
		
		# use the scale for smoother more or less
		# if you want the standardized system, you have to divide the scale by the distanceMax
		fScale = data.inputValue( self.scale ).asFloat()
		if fScale < self.epsilon :
			fScale = self.epsilon
		
		if normalize :
			self.fScale	= fScale / distanceMax
		else :
			self.fScale	= fScale
		
		# RBF each element
		for i in range(poseUsed_num) :
			for j in range(poseUsed_num) :
				
				# Euclidean or angular? Or other...
				mat.rc[i][j] = self.rbf_function( mat.rc[i][j] * self.fScale )
			
		# factorizeLU and save the ids of the swapped lines
		LU, Pids = mat.factorize_LU()

		# for each m of each pose
		# solv_LU and store the X (m) in self.mX
		# mX =  m * nVector
		self.mX	= []
		
		for m in range(self.M):
			
			Y = [mValues[ i ][ m ]  for i in range(poseUsed_num)]
			X = mat.solve_LU(LU, Pids, Y)  # nVector coeff
			self.mX.append(X)
		
		#*** setClean indicates that the system is solved
		solved_H = data.outputValue(self.solved)
		solved_H.setClean()
		
		OpenMaya.MGlobal.displayInfo( "RbfSolver recomputed using poses :  %s" %self.poseUsed_ids )
		return True
	
	def compute(self, plug, data):
				
		if not plug == self.mOutput:
			return
		
		if not data.isClean( self.solved ):
			status	= self.rebuild_solver( data )
			
			if not status :
				return
	
		# find the nVector nInput
		nInput_H = data.inputArrayValue( self.nInput )
		nInput = []
		
		for n in range(self.N):
			try :
				nInput_H.jumpToElement( n )
				input_	= nInput_H.inputValue().asFloat()
				nInput.append( input_ )
			except :
				nInput.append(0.0)
		
		# just apply Somme des Xi * || p-Di || for each m
		output_Handle = data.outputArrayValue( self.mOutput )
		poseUsed_num = len(self.poseUsed_ids)
		outputs = [0.0] * self.M
		
		for m in range(self.M):
			for i in range(poseUsed_num):
				
				# calculate distance
				# applique pose weight
				# applique RBF
				# applique coeff Xi
				distance = self.distance_function( self.N, nInput, self.nKeys[ i ]  )
				distance = self.rbf_function( distance * self.fScale  )
				distance = self.mX[m][i] * distance
				outputs[m]  +=  distance
		
		blendShapeMode  = data.inputValue(self.blendShapeMode).asBool()
		if blendShapeMode == True :
			
			min = None 
			for m in range(self.M):
				if (m == 0) or (outputs[m] < min):
					min = outputs[m]
			
			sum = 0.0
			for m in range(self.M):
				outputs[m] = self.set_range( outputs[m], min, 1.0, .0, 1.0 )
				sum += outputs[m]
			
			for m in range(self.M):
				outputs[m] /= sum

		for m in range(self.M):
			try :
				output_Handle.jumpToElement( m )
				output_Handle.outputValue().setFloat( outputs[m] )
			except :
				pass
		
		output_Handle.setAllClean()
		data.setClean(plug)
#-----------------------------------------------------------------------------
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject, "Hans Godard -- zapan669@hotmail.com", "1.0", "Any")
	try:
		mplugin.registerNode(RbfSolver.kPluginNodeName, RbfSolver.kPluginNodeId, RbfSolver.nodeCreator, RbfSolver.nodeInitializer)
	except:
		OpenMaya.MGlobal.displayError("Failed to register node: %s\n" % RbfSolver.kPluginNodeName)
		raise
#-----------------------------------------------------------------------------
def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterNode(RbfSolver.kPluginNodeId)
	except:
		OpenMaya.MGlobal.displayError("Failed to unregister node: %s\n" % RbfSolver.kPluginNodeName)
		raise
#-----------------------------------------------------------------------------