import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    low = np.array([10,100,100])
    high = np.array([100,255,255])

    yellow_mask = cv.inRange(hsv, low,high)
    yellow = cv.bitwise_and(frame, frame, mask=yellow_mask)

    cv.imshow("Yellow",yellow)
    #cv.imshow("HSV",hsv)
    #result = cv2.bitwise_and(frame, frame, mask=mask)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    w_mask = cv.inRange(hsv, low, high)
    result = cv.bitwise_and(frame, frame, mask=w_mask)
    #cv.imshow("Y", result)

    key = cv.waitKey(1)
    if key ==27:
        break

cap.release()