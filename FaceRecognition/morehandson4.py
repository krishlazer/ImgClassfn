import cv2
import os
import face_recognition

bimg = cv2.imread('E:/KrishM/ML/IMG/AllCopies/forprac/billind.jpg')
bimg = cv2.cvtColor(bimg, cv2.COLOR_BGR2RGB)
cv2.resize(bimg, (450, 450))
faces = face_recognition.face_locations(bimg)[0]
print(faces)
cv2.rectangle(bimg, (faces[3], faces[0]), (faces[1], faces[2]), (0, 0, 255), 2)
cv2.imshow('Bill in Bihar', bimg)
cv2.waitKey()