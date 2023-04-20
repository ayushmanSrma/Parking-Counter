import cv2
import pickle
import cvzone
import numpy as np

#Video feed
cap = cv2.VideoCapture()

while True:

    success,img = cap.read() #to get the frame in video
    cv2.imshow("Image",img)  #to show the video
    cv2.waitKey(1)          #video speed