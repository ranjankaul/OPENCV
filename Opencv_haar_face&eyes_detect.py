#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:39:05 2018

@author: calsoft
"""
import numpy as np
import cv2 ,sys ,os


cap = cv2.VideoCapture(0)

while(True):
 
    ret, frame = cap.read()                        # Capture frame-by-frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Our operations on the frame come here
   
    
    haar_face_cascade = cv2.CascadeClassifier('/home/calsoft/anaconda3/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
    faces = haar_face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    print('HAAR Faces found: ', len(faces))
    
    haar_eyes_cascade = cv2.CascadeClassifier('/home/calsoft/anaconda3/share/OpenCV/haarcascades/haarcascade_eye.xml')    
   
    for (i, (x, y, w, h)) in enumerate(faces):   # Surround cascade with rectangle
     cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 2)
     cv2.putText(gray, 'HAAR face' + " #{}".format(i + 1), (x, y - 10),
     cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
     eyes = haar_eyes_cascade.detectMultiScale(gray)
     for (ex,ey,ew,eh) in eyes:
         cv2.rectangle(gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#    
    
    cv2.imshow('frame',gray)                        # Display the resulting frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()                                       # When everything done, release the capture 
cv2.destroyAllWindows()
cv2.waitKey(0)
sys.exit()