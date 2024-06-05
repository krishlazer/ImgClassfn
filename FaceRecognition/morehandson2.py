import cv2
import os
import face_recognition

iminsb1 = cv2.imread('E:/KrishM/ML/IMG/AllCopies/forprac/kmsb.png')
#iminsb1 = face_recognition.load_image_file('E:/KrishM/ML/IMG/AllCopies/forprac/kmsb.png')
faceloc = face_recognition.face_locations(iminsb1)[0]
print(faceloc)
cv2.rectangle(iminsb1, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255, 0, 0), 2)
cv2.imshow('sb1', iminsb1)
cv2.waitKey()

imsw1 = cv2.imread('E:/KrishM/ML/IMG/AllCopies/forprac/zuckwf.jpg')
#imsw1 = face_recognition.load_image_file('E:/KrishM/ML/IMG/AllCopies/forprac/zuckwf.jpg')
imsw1 = cv2.cvtColor(imsw1, cv2.COLOR_BGR2RGB)
faces = face_recognition.face_locations(imsw1)
print(faces)
cv2.rectangle(imsw1, (faces[0][3], faces[0][0]), (faces[0][1], faces[0][2]), (0, 255, 0), 2)
cv2.rectangle(imsw1, (faces[1][3], faces[1][0]), (faces[1][1], faces[1][2]), (0, 255, 0), 2)
cv2.imshow('zw', imsw1)
cv2.waitKey()





# cv2.rectangle(iminsb1, (180, 551), (546, 971), (255, 0,0), 2)
# cv2.imshow('im2', iminsb1)
# cv2.waitKey()


# cv2.imshow('sb1', iminsb1)
# cv2.waitKey()

