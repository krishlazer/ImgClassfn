import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x-w, y-h), (255, 0, 0), 2)
        cv2.imshow('im1', img)





# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# testimg = cv2.imread('E:/KrishM/ML/IMG/AllCopies/forprac/googletop.jpg')
# testgray = cv2.cvtColor(testimg, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(testgray, 1.1, 1)

for (x, y, w, h) in faces:
    cv2.rectangle(testimg, (x, y), (x-w, y-h),(255, 0, 0), 2)

cv2.imshow('gt', testimg)
cv2.waitKey()