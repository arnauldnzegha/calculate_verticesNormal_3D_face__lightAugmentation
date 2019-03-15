import numpy as np

class Object3D(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.vertices=np.array(0)
		self.textures=np.array(0)
		self.faceNormals=np.array(0)
		self.faces=np.array(0)
		self.facesT=np.array(0)


	def readObjetVF(self):
		vertices=[]
		textures=[]
		faces=[]
		facesT=[]
		normals=[]
		#f = open("lfw/Serena_Williams/Serena_Williams_0004.obj", "r")
		f = open("lfw/Serena_Williams/Serena_Williams_0003.obj", "r")
		for line in f:
			elts=line.split()
			if elts[0]=='v':
				vertices.extend([[float(elts[1]),float(elts[2]),float(elts[3])]])
			if elts[0]=='f':
				elt1=elts[1].split('/')
				v1=int(elt1[0])
				t1=int(elt1[1])
				elt1=elts[2].split('/')
				v2=int(elt1[0])
				t2=int(elt1[1])
				elt1=elts[3].split('/')
				v3=int(elt1[0])
				t3=int(elt1[1])
				faces.extend([[v1,v2,v3]])
				facesT.extend([[t1,t2,t3]])
			if elts[0]=='vt':
				textures.extend([[float(elts[1]),float(elts[2])]])


		self.faces=np.asarray(faces)
		self.facesT=np.asarray(facesT)
		self.vertices=np.asarray(vertices)
		self.textures=np.asarray(textures)
		#print(self.faces)


	def calculateFaceNormal(self):
		faceNormals=[]
		for f in self.faces:
			(v1,v2,v3)=(np.asarray(vertices[f[0]-1]),np.asarray(vertices[f[1]-1]),np.asarray(vertices[f[2]-1]))
			normal=np.cross(v2-v1,v3-v1)
			normals.extend([normal])
		self.faceNormals=np.asarray(faceNormals)
		return self.faceNormals


	def calculateVerticesNormal():
		faceNorm, fIndex=self.faceNorm, 0
		verticesNor=np.array([[0.0,0.0,0.0] for x in self.vertices])
		for f in self.faces:
			fn=faceNorm[fIndex]
			for vf in f:
		        vn=verticesNor[vf-1]
		        vn[0]=float(vn[0])+fn[0]
		        vn[1]=float(vn[0])+fn[1]
		        vn[2]=float(vn[0])+fn[2]
		        verticesNor[vf-1]=np.asarray(vn)
		    fIndex=fIndex+1
		verticesNor=np.asarray(verticesNor)

		for i in range(verticesNor.shape[0]):
		    verticesNor[i]=verticesNor[i]/np.linalg.norm(verticesNor[i])
		self.verticesNor=verticesNor
		return self.verticesNor

	def getOBJElements(self):
		self.readObjetVF()
		self.calculateFaceNormal()
		return (self.vertices, self.faces, self.facesT, self.faceNormals, self.textures)