import cv2
import numpy as np
import face_recognition
#import PIL
# import cmake
# import dlib

elontrain = face_recognition.load_image_file('E:/KrishM/ML/IMG/elon/elimg5.jpg')
elontrain = cv2.cvtColor(elontrain, cv2.COLOR_BGR2RGB)

billfaces = face_recognition.load_image_file('E:/KrishM/ML/IMG/bill/billind.jpg')
print('bill in india')
print(billfaces)
billfaces = cv2.cvtColor(billfaces, cv2.COLOR_BGR2RGB)
billfacelocation = face_recognition.face_locations(billfaces)
billfacetrain = face_recognition.face_locations(billfaces)[0]
print(type(billfacelocation))
print(billfacelocation)

cv2.rectangle(billfaces,(billfacetrain[3], billfacetrain[0]), (billfacetrain[1], billfacetrain[2]), (255, 0, 255), 1)

cv2.imshow('billall', billfaces)
cv2.waitKey(0)

elontest = face_recognition.load_image_file('E:/KrishM/ML/IMG/elon/elimg4.jpg')
elontest = cv2.cvtColor(elontest, cv2.COLOR_BGR2RGB)
#print(elontest.shape)

print('..1..')
print(elontrain)

#faceloco = face_recognition.face_locations(elontrain)[0]
facetrain = face_recognition.face_locations(elontrain)[0]
print('facetrain')
print(facetrain)
encodefacetrain = face_recognition.face_encodings(elontrain)[0]
#print(encodefaceloco)
print(type(encodefacetrain))
print('.....')

cv2.rectangle(elontrain, (facetrain[3], facetrain[0]), (facetrain[1], facetrain[2]), (255, 0, 255), 2)

cv2.imshow('elono', elontrain)
cv2.waitKey(0)

faceloct = face_recognition.face_locations(elontest)[0]
encodefaceloct = face_recognition.face_encodings(elontest)[0]

cv2.rectangle(elontest, (faceloct[3], faceloct[0]), (faceloct[1], faceloct[2]), (255, 0, 255), 2)
cv2.imshow('elont', elontest)
cv2.waitKey(0)

#results = face_recognition.compare_faces(encodefacetrain, encodefaceloct)
#facedist = face_recognition.face_distance(encodefacetrain, encodefaceloct)
#print(encodefacetrain)
#print(results, facedist)

#cv2.putText(elontest, f'{results} {round(facedist[0],2)}', (80,80), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

# faceloct = face_recognition.face_locations(elontest)[0]
# print(faceloct)
# encodefaceloct = face_recognition.face_encodings(elontest)
# print(encodefaceloct)



# def facediff(arr1, arr2):
#     return np.sqrt(np.square(arr1-arr2))
#
# res1 = facediff(encodefaceloco, encodefaceloct)
# print(res1)
print('....for new image....')
newimg = cv2.imread('E:/KrishM/ML/IMG/zuc/zuck1.jpg')
#newimg = face_recognition.load_image_file('E:/KrishM/ML/IMG/zuc/zuck1.jpg')
newimgencode = face_recognition.face_encodings(newimg)
print(newimgencode)



