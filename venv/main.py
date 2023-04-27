import cv2
import pickle
import cvzone
import numpy as np

#Video feed
cap = cv2.VideoCapture('/Users/ayushmansharma/PycharmProjects/parkingCounter/venv/carPark.mp4')

while True:
    #to make the video run in loop 
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT): #if current frame== Total frame
        cap.set(cv2.CAP_PROP_POS_FRAMES,0) #if so then current frame =0 (i.e it'll again start from frame 0)

   

    success, img = cap.read() #to get the frame in video
    cv2.imshow('Image',img)  #to show the video
    cv2.waitKey(1)          #video speed

    