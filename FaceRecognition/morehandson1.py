import numpy as np
import face_recognition
import os
import cv2

imggt1 = cv2.imread('E:/KrishM/ML/IMG/AllCopies/forprac/googletop.jpg')
print(imggt1)
print(imggt1.shape)
faces = face_recognition.face_locations(imggt1)
print(type(faces))
print(faces)
for f in faces:
    print(f)

encodefaces = face_recognition.face_encodings(imggt1)
print(type(encodefaces))
#print(encodefaces)
print('....face - wise.....')
# for gf in encodefaces:
#     print(gf)
#     print(len(gf))

print(encodefaces[2])

print(type(encodefaces))

blfl1 = cv2.imread('E:/KrishM/ML/IMG/AllCopies/forprac/billgroup.jpg')
blfl1faces = face_recognition.face_locations(blfl1)
print('...first faces.....')
print(blfl1faces)
# blfl = cv2.resize(blfl, (250, 250))
# billgroupnew = cv2.imwrite('E:/KrishM/ML/IMG/AllCopies/forprac/bilnew.jpg', blfl)
# blfl2 = cv2.imread('E:/KrishM/ML/IMG/AllCopies/forprac/bilnew.jpg')
# blflfaces2 = face_recognition.face_locations(blfl2)
# print(len(blflfaces2))
# print('.....count faces....')
# print(blflfaces2)

zuck1 = cv2.imread('E:/KrishM/ML/IMG/AllCopies/forprac/zuckwf.jpg')
print(zuck1)
zfs1 = face_recognition.face_locations(zuck1)
print(type(zfs1))
print(zfs1)