import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv
from itertools import compress

def findEncodings(StudentImages):
    encodeList = []
    for img in StudentImages:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def findLoc(StudentImages):
    for img in StudentImages:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faceLoc = face_recognition.face_locations(img)[0]
        cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
        print(faceLoc)

def findEncodings1(StudentUplaodedImages):
    #encodeList1 = []
    for img1 in StudentUplaodedImages:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        return face_recognition.face_encodings(img1)
    #     encodeList1.append(encode1)
    # return encodeList1

def findLoc1(StudentUplaodedImages):
    for img1 in StudentUplaodedImages:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        return face_recognition.face_locations(img1)
        # cv2.rectangle(img1, (faceLoc1[3], faceLoc1[0]), (faceLoc1[1], faceLoc1[2]), (255, 0, 255), 2)
        # print(faceLoc1)



# def getEncoding(StudentUplaodedImages):
#     img1 = cv2.cvtColor(StudentUplaodedImages, cv2.COLOR_BGR2RGB)
#     return face_recognition.face_encodings(img1)[0]

def calculateMatchPercent(loc):
    return round((1-loc)*100)

def Run():
    path = 'rollcallmodule/StudentImages'
    StudentImages = []
    classNames = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        StudentImages.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    encodeListKnown = findEncodings(StudentImages)
    print(len(encodeListKnown))
    print('Encoding Complete')

    path = 'rollcallmodule/StudentUplaodedImages'
    StudentUplaodedImages = []
    classNames1 = []
    myList1 = os.listdir(path)
    print(myList1)

    for cl1 in myList1:
        curImg = cv2.imread(f'{path}/{cl1}')
        StudentUplaodedImages.append(curImg)
        classNames1.append(os.path.splitext(cl1)[0])
    print(classNames1)

    encodeListKnown1 = findEncodings1(StudentUplaodedImages)
    print(len(encodeListKnown1))
    print('Encoding Complete')

    LocList1 = findLoc1(StudentUplaodedImages)
    print(LocList1)
    print(len(LocList1))

    matchedStudents = []
    myDict={}
   # for img in StudentUplaodedImages:
    for encodeFace, faceLoc in zip(encodeListKnown1, findLoc1(StudentUplaodedImages)):
        result = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print("Given match list is : " + str(result))
        print("Face Distance is", faceDis)
        res = list(compress(range(len(result)), result))
        print("Indices having True values are : " + str(res))
        matchIndex = np.argmin(faceDis)
        if True in result:
            print("The uploaded file was matched with the existing photos")
        else:
            print("Not photos matched")
        if result[matchIndex]:
            name = classNames[matchIndex].upper()
            matchedStudents.append(name)
            print("Matched photo ID is:", name)
            myDict[name]=calculateMatchPercent(faceDis[matchIndex])


    print("Matched Id's: ", matchedStudents)
    print(myDict)
    return myDict

        # print("Given list is : " + str(result))
        # res = list(compress(range(len(result)), result))
        # print("Indices having True values are : " + str(res))
        # print("List index-value are : ")
        # for i in range(len(result)):
        #     print(i, end=" ")
        #     print(result[i])
        # if True in result:
        #     print("Matched")
        # else:
        #     print("Not matched")
        # matchIndex = np.argmin(faceDis)
        #
        # if result[matchIndex]:
        #     name = classNames[matchIndex].upper()
        #     print(name)
        #     # y1,x2,y2,x1 = faceLoc
        #     # y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
        #     # cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        #     # cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
        #     # cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        #     markAttendance(name)

