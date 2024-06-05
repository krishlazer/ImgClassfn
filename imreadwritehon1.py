import numpy as np
import cv2

cimg1 = cv2.imread('E:/KrishM/PythonPrjs/PyDatasets/ctdgex/dataset/training_set/cats/cat.83.jpg')
print(cimg1)
catn1 = cv2.imread(cimg1)
catn1show = cv2.imshow('c1', catn1)
cv2.waitKey(0)

cimg2 = cv2.imwrite('cpycimg1.jpg', cimg1)
cat1 = cv2.imshow('catcpy1', cimg2)
cv2.waitKey(0)