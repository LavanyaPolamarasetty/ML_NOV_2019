# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:41:25 2019

@author: APSSDC
"""

import cv2
face_cascade = cv2.CascadeClassifier("DC\\Desktop\\haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
    ret,img= cap.read() # ret return keyword mandotory
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) # 255,255,0--BRG, box_thickmness-2
        cv2.imwrite("myimage.jpg",img)
    cv2.imshow("img",img)
    k=cv2.waitkey(30) & 0xff
    if k == 27 :
        break
cap.release()
cv2.destroyAllWindows()