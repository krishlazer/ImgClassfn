import os
import face_recognition
import numpy as np
import cv2

imgpath = 'E:/KrishM/ML/IMG/attendance/'
ceoimages = []
classnames = []

ceolist = os.listdir(imgpath)
print('CEO List')
print(ceolist)

for ceo in ceolist:
    #currimg = cv2.imread("E:/KrishM/ML/IMG/attendance/"+"f'{}'".format(ceo))
    currimg = cv2.imread(f'{imgpath}/{ceo}')
    ceoimages.append(currimg)
    classnames.append(os.path.splitext(ceo)[0])

print(classnames)
for i in ceoimages:
    print(i)

encodelist = []
def encodeimg(passedimages):
    for entimg in passedimages:
        entimg = cv2.cvtColor(entimg, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(entimg)[0]
        encodelist.append(encode)
    return encodelist

#codethem = encodeimg(ceoimages)

allcodes = encodeimg(ceoimages)
#for allc in allcodes:
    #print(allc)

print(len(allcodes))
print('Encoding of passed images done.')
print('....||....')
chek = [9, 3, 11, 2, 15, 4]
chekmin = np.argmin(chek)
print(chekmin)
print(chek[chekmin])



