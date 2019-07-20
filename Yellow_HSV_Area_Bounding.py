#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 03:20:19 2019

@author: calsoft
"""

import numpy as np
import cv2 as cv

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()
    yellow = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    low = np.array([10,100,100])
    high = np.array([100,255,255])
   
    yellow_mask = cv.inRange(yellow,low,high)
    yellow_mask = cv.GaussianBlur(yellow_mask,(7,7),0)
    
    contours, hierarchy = cv.findContours(yellow_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for con in contours:
        area  =  cv.contourArea(con)
        if area > 1000:
            cv.drawContours(frame, con, -1, (0,255,0), 3)
    
    cv.imshow("Frame",frame)
    cv.imshow("Frame 2",yellow_mask)
    
    key = cv.waitKey(1)
    if key ==27:
        break

cap.release()
cv.destroyAllWindows()