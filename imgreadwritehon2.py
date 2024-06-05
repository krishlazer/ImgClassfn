import imutils
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2

# img1 = cv2.imread('E:/KrishM/MyDocs1101/MyDocs/Photos/lazer.jpg')
# print(img1)
# print(img1.shape)
# img1.reshape(100)
# #cv2.imread('laz1', img1)



imgel1 = cv2.imread('E:/KrishM/ML/IMG/elon/elimg4.jpg')
imgel2 = cv2.imread('E:/KrishM/ML/IMG/elon/elimg5.jpg')

img5 = cv2.imread('E:/KrishM/ML/IMG/elon/elon5.jpg')
img5c = cv2.imread('E:/KrishM/ML/IMG/elon/elimg5.jpg')


#imgel1gr = cv2.cvtColor(imgel1, cv2.COLOR_BGR2GRAY)
#imgel2gr = cv2.cvtColor(imgel2, cv2.COLOR_BGR2GRAY)

# img5gr = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
# img5cgr = cv2.cvtColor(img5c, cv2.COLOR_BGR2GRAY)

#resized1 = cv2.resize(imgel1gr, (194, 259))
#resized2 = cv2.resize(imgel2gr, (194, 259))
# resized1 = cv2.resize(img5gr, (194, 259))
# resized2 = cv2.resize(img5cgr,(194, 259))


# print(imgel1.shape)
# print(imgel1)
# print(imgel2)
# print('as float')
# cimgel1 = imgel2.astype('float')
# print(cimgel1)
#
# def imgdiff(img1, img2):
#     err = np.sum((img1.astype('float')-img2.astype('float'))**2)
#     err /=  float(img2.shape[0] * img2.shape[1])
#     return err
#
# errimg = imgdiff(img5, img5c)
# print(errimg)

# print(imgel1[0][0])
# print(imgel2[0][0])
# print(resized1.shape)
# print(resized2.shape)
# cv2.imwrite('resizedel1.jpg', resized1)
# cv2.imwrite('resizedel2.jpg', resized2)

# print('....magic............')
#
# imgc1 = cv2.imread('E:/KrishM/ML/IMG/prac/showcar1.jpg')
# imgc2 = cv2.imread('E:/KrishM/ML/IMG/prac/showcar1.jpg', 0)
# print(imgc1)
# h, w, c = imgc1.shape
# print(imgc1.shape)
# print(str(h))
# print(str(w))
# print(str(c))
#cv2.imshow('car1', imgc1)
#cv2.waitKey(0)

# (B, G, R) = imgc1[100, 50]
# print('B = {}, G = {}, R = {}' .format(B, G, R))
# print(imgc1.shape)
# print(imgc1[100, 50])
# print('....grey.....')
# print(imgc2)
# print(imgc2.shape)
# print(imgc2[1, 299])
# g = imgc2[1, 299]
# print (g)
# #print(imgc1[0][0][1])
# print('....roi......')
# roi = imgc1[40:250, 100:210]
# cv2.imshow('ROI', roi)
# cv2.waitKey(0)

# carresize = cv2.resize(imgc1, (200, 200))
# carrsimg = cv2.imshow('carrz', carresize)
# cv2.waitKey(0)

# ar = 150.0 / w
# dim = (150, int(h*ar))
# resized = cv2.resize(imgc1, dim)
# cv2.imshow('carrze', resized)
# cv2.waitKey(0)
print('....on cats.....')
imgct1 = cv2.imread('E:/KrishM/PythonPrjs/PyDatasets/ctdgex/dog vs cat/dataset/training_set/showcat1.jpg')
print(imgct1)
print(imgct1.shape)
imgct2 = cv2.cvtColor(imgct1, cv2.COLOR_BGR2GRAY)
cv2.imwrite('E:/KrishM/PythonPrjs/PyDatasets/ctdgex/dog vs cat/dataset/training_set/showcat2.jpg', imgct2)
imgct1rz = cv2.resize(imgct1, (250, 250))
print(imgct1rz.shape)
cv2.imshow('ctshow1', imgct1rz)
cv2.waitKey(0)

h1, w1, d1 = imgct1.shape
ar1 = 250.0 / w1
dim = 250.0 / int(h1*ar1)
rsz = cv2.resize(imgct1rz, dim)
cv2.imshow('cataspect', rsz)
cv2.waitKey(0)









