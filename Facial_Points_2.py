import cv2 as cv
import numpy  as np
import dlib
from math import hypot

cap =  cv.VideoCapture(0)
detect = dlib.get_frontal_face_detector()
face_pred = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


while True:
    ret,frame = cap.read()

    faces = detect(frame)
    for face in faces:
        x0,y0 = face.left(),face.top()
        x1,y1 = face.right(),face.bottom()
        cv.rectangle(frame,(x0,y0),(x1,y1),(255,0,0),3)

        landmark = face_pred(frame,face)      # 68 landmark points Detector

        ## Right Eye ##
        x1,y1 = landmark.part(36).x,landmark.part(36).y
        x2,y2 = landmark.part(39).x,landmark.part(39).y

        hor_line = cv.line(frame,(x1,y1),(x2,y2),(0,0,255),1)

        ## Right eye Vertical Line ##
        center_top = midpoint(landmark.part(37), landmark.part(38))
        center_bottom = midpoint(landmark.part(41), landmark.part(40))
        ver_line = cv.line(frame, center_top, center_bottom, (0, 255, 0), 1)

        H_line_len = hypot((x1-x2),(y1-y2))
        V_line_len = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
        L_ratio = H_line_len / V_line_len


        ## Left Eye ##
        x1,y1 = landmark.part(42).x,landmark.part(42).y
        x2,y2 = landmark.part(45).x,landmark.part(45).y

        hor_line = cv.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)

        ## Left eye Vertical Line ##

        center_top = midpoint(landmark.part(43), landmark.part(44))
        center_bottom = midpoint(landmark.part(47), landmark.part(46))
        #hor_line = cv.line(frame, left_point, right_point, (0, 255, 0), 2)
        ver_line = cv.line(frame, center_top, center_bottom, (0, 255, 0), 1)

        H_line_len = hypot((x1-x2),(y1-y2))
        V_line_len = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

        R_ratio = H_line_len / V_line_len

        T_ratio = (L_ratio+R_ratio)/2


        if T_ratio > 4:
            cv.putText(frame, "BLINKING", (50, 150),cv.FONT_HERSHEY_PLAIN, 7, (255, 0, 0))
        #print(x,y)
        cv.imshow("Frame", frame)


    key = cv.waitKey(1)
    if key ==27:
        break

cap.release()
