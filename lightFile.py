import numpy as np
import cv2
import objFile
h=256
img = np.zeros([h,h,3])
imgGS = np.zeros([h,h])
obj=objFile.Object3D()
"""
vous importez la texture correspondante à l'obj importé
"""
imgT = cv2.imread("lfw/Serena_Williams/Serena_Williams_0003_texture.png")
(vertices, faces, faceT, faceNorm, textures)=obj.getOBJElements()
verticesNor=np.array([[0.0,0.0,0.0] for x in vertices])
#l=np.array([200,25,50])
#l=np.array([200,200,50])
e=0.5
eps=0.008
eps2=1
#source=np.array([245,245,110]);
sourceL=np.array([210,210,100])
sourceR=np.array([20,20,100])
sourceC=np.array([140,140,200])
sourceL2=np.array([140,140,200])
source=sourceR
fIndex=0
for f in faces:
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





"""for i in range(vertices.shape[0]):
    v=vertices[i]
    l=v-source
    t=textures[i]
    vn=verticesNor[i]
    lamb=np.vdot(l,vn)*e
    dist=((l[0])**2 +(l[1])**2 +(l[2])**2)**(0.5)
    lamb/= dist
    if lamb<eps and lamb>0:
        lamb=(2**(lamb))
    if lamb<=0 and lamb>-eps2:
        lamb=(2**(lamb))
    #img[500-int(v[1]),int(v[0])]=(imgT[256-int(t[1]*256),int(t[0]*256)]*lamb)/255.0
    #img[500-int(v[1]),int(v[0])]=np.array([0,250,0])
    #print(img[500-int(v[1]),int(v[0])])
    #np.vdot(v,w)"""
poids=np.array([[0.5,0.1,0.4],[0.1,0.9,0.0],[0.9,0.1,0.0],[0.5,0.2,0.3],[0.33,0.33,0.34],[0.3,0.5,0.2],[0.2,0.8,0.0],[0.5,0.25,0.25],[0.25,0.5,0.25],[0.25,0.25,0.5],[0.1,0.2,0.7],[0.3,0.5,0.2],[0.5,0.4,0.1]])






#ind=0
for f in faces:
    v1=vertices[f[0]-1]
    v2=vertices[f[1]-1]
    v3=vertices[f[2]-1]

    p1,p2,p3=[h-int(v1[1]),int(v1[0])], [h-int(v2[1]),int(v2[0])], [h-int(v3[1]),int(v3[0])]
    tt1=textures[f[0]-1]
    tt2=textures[f[1]-1]
    tt3=textures[f[2]-1]

    lamb,lt=np.zeros(3),np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
    for i in range(0,3):
        lt[i]=vertices[f[i]-1] - source
        ld=np.linalg.norm(lt[i])
        lt[i]=lt[i]/np.linalg.norm(lt[i])
        #lamb[i]=(1.008)**(np.vdot(lt[i],verticesNor[f[i]-1]))*e
        #print(np.vdot(lt[i],verticesNor[f[i]-1]))
        lamb[i]=np.vdot(lt[i],verticesNor[f[i]-1])
        #dist=((lt[i][0])**2 +(lt[i][1])**2 +(lt[i][2])**2)**(0.5)
        #lamb[i]/=(1.02)**(dist/200)
        """if lamb[i]<eps and lamb[i]>0:
            lamb[i]=(2**(lamb[i]))"""
        """if lamb[i]<=eps and lamb[i]>-eps2:
            #print(lamb[i])
            lamb[i]=((10)**(lamb[i]))/(0.7*(-lamb[i]))"""
        lamb[i]=lamb[i]*e
    t1,t2,t3=imgT[256-int(tt1[1]*256),int(tt1[0]*256)]*lamb[0]/255.0, imgT[256-int(tt2[1]*256),int(tt2[0]*256)]*lamb[1]/255.0, imgT[256-int(tt3[1]*256),int(tt3[0]*256)]*lamb[2]/255.0
    tx1,tx2,tx3=imgT[256-int(tt1[1]*256),int(tt1[0]*256)]/255.0, imgT[256-int(tt2[1]*256),int(tt2[0]*256)]/255.0, imgT[256-int(tt3[1]*256),int(tt3[0]*256)]/255.0
    #t1,t2,t3=imgT[256-int(tt1[1]*256),int(tt1[0]*256)]**lamb[0]/255.0, imgT[256-int(tt2[1]*256),int(tt2[0]*256)]**lamb[1]/255.0, imgT[256-int(tt3[1]*256),int(tt3[0]*256)]**lamb[2]/255.0
    #t1,t2,t3=imgT[256-int(tt1[1]*256),int(tt1[0]*256)]/255.0, imgT[256-int(tt2[1]*256),int(tt2[0]*256)]/255.0, imgT[256-int(tt3[1]*256),int(tt3[0]*256)]/255.0
    for prq in poids:
        c1=int(prq[0]*p1[0]+prq[1]*p2[0]+prq[2]*p3[0])
        c2=int(prq[0]*p1[1]+prq[1]*p2[1]+prq[2]*p3[1])

        img[c1,c2]=(prq[0]*tx1 +prq[1]*tx2 +prq[2]*tx3)+(prq[0]*t1 +prq[1]*t2 +prq[2]*t3)
        imgGS[c1,c2]=(img[c1,c2,0]+img[c1,c2,1]+img[c1,c2,0])/3.0

"""for c1 in range(3,h):
    for c2 in range(3,h):
        if (imgGS[c1-2,c2] - imgGS[c1,c2])**2 > 0.2 and (imgGS[c1-1,c2] - imgGS[c1,c2])**2 > 0.2 and (imgGS[c1-3,c2] - imgGS[c1,c2])**2 and (imgGS[c1,c2-1] - imgGS[c1,c2])**2>0.2:
            ig=imgGS[c1-4,c2]+imgGS[c1-3,c2]+imgGS[c1-2,c2]+2*imgGS[c1+8,c2]+0.5*imgGS[c1,c2]
            ig+=imgGS[c1-5,c2]+imgGS[c1-7,c2]

            ig+=imgGS[c1,c2-4]+imgGS[c1,c2-3]+imgGS[c1,c2-2]+0.5*imgGS[c1,c2+8]
            ig+=imgGS[c1,c2-6]+imgGS[c1,c2-8]
            imgGS[c1,c2]=ig/12"""
        #if (imgGS[c1,c2-2] - imgGS[c1,c2-1])**2 > 0.9 and (imgGS[c1,c2-1] - imgGS[c1,c2])**2 > 0.9:
            #imgGS[c1,c2]=(imgGS[c1,c2-3]+imgGS[c1,c2-2]+imgGS[c1,c2-1]+ 6*imgGS[c1,c2] +imgGS[c1,c2+3]+imgGS[c1,c2+2]+imgGS[c1,c2+1])/12.0
    #ind=ind+1




cv2.imshow("3D Illumination", img)
cv2.imshow("3D Illumination GS", imgGS)
cv2.waitKey(0)