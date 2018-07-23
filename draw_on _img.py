#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:39:05 2018

@author: calsoft
"""
import numpy as np
import cv2,sys,os,time
from datetime import datetime 
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()                        # Capture frame-by-frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Our operations on the frame come here
    
    cv2.line(frame,(256,186),(384,314),(255,255,255))
    
    cv2.circle(frame,(320,250), 64, (0,0,255))
    cv2.circle(frame,(320,250), 32, (0,0,255))
    cv2.circle(frame,(320,250), 16, (0,0,255))
    
    
    cv2.imshow('frame',frame)                       # Display the colour frame 
    
   
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()  
                                  # When everything done, release the capture 
cv2.destroyAllWindows()
cv2.waitKey(0)
sys.exit()