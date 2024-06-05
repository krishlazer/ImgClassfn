import cv2
import os
import face_recognition

imbg = cv2.imread('E:/KrishM/ML/IMG/AllCopies/forprac/billgroup.jpg')
imbg = cv2.cvtColor(imbg, cv2.COLOR_BGR2RGB)
imbg = cv2.resize(imbg, (450, 450))
faces = face_recognition.face_locations(imbg)
print(faces)

for pc in range(len(faces)):
    cv2.rectangle(imbg, (faces[pc][3], faces[pc][0]), (faces[pc][1], faces[pc][2]), (0, 255, 0), 2)

cv2.imshow('bg1', imbg)
cv2.waitKey()

