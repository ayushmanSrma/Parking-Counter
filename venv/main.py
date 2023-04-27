import cv2
import pickle
import cvzone
import numpy as np

#Video feed
cap = cv2.VideoCapture('/Users/ayushmansharma/PycharmProjects/parkingCounter/venv/carPark.mp4')

with open('CarParkPos','rb') as f:
     posList = pickle.load(f)

width, height = 107, 48 # these are the ht and wdt of rectangle

def checkParkPos():
    for pos in posList:
        x,y = pos
        imgCrop = img[y:y+height,x:x+width]
        cv2.imshow(str(x*y),imgCrop)
    
while True:
    #to make the video run in loop 
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT): #if current frame== Total frame
        cap.set(cv2.CAP_PROP_POS_FRAMES,0) #if so then current frame =0 (i.e it'll again start from frame 0)

    success, img = cap.read() #to get the frame in video
    checkParkPos()

    for pos in posList:
        cv2.rectangle(img, pos,(pos[0] + width, pos[1] + height), (255, 0, 255), 2) #this is moved down so not to make the
                                                                                     #boxes appear in the cropped img
    cv2.imshow('Image',img)  #to show the video
    cv2.waitKey(1)          #video speed

    