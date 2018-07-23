#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:22:58 2018

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
    
    edges = cv2.Canny(frame,480,640)
    
    cv2.imshow('edges',edges)                        # Display the resulting frame
    cv2.imshow('frame',frame)                       # Display the colour frame 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()  
                                  # When everything done, release the capture 
cv2.destroyAllWindows()
cv2.waitKey(0)
sys.exit()