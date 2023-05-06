import cv2
import pickle
import cvzone
import numpy as np

#Video feed
cap = cv2.VideoCapture('/Users/ayushmansharma/PycharmProjects/parkingCounter/venv/carPark.mp4')

with open('CarParkPos','rb') as f:
     posList = pickle.load(f)

width, height = 107, 48 # these are the ht and wdt of rectangle

def checkParkPos(imgPro):
    spaceCounter =0
    occCount = 0

    for pos in posList:
        x,y = pos  #to store the pos of rectangle boxes in x&y
        imgCrop = imgPro[y:y+height,x:x+width]  #cropping the img from x,y to x+width,y+height 
        #cv2.imshow(str(x*y),imgCrop)  #to show the cropped img with name as coordinates to each img
        count = cv2.countNonZero(imgCrop) #for counting the non-zero pixels in the imgCrop
        cvzone.putTextRect(img,str(count),(x,y+height-3),scale = 1,offset=0,thickness=2,colorR=(0,0,255))


        if count <850 :
            color = (0,255,0) #red color
            thickness = 5
            spaceCounter +=1
        else :
            color = (0,0,255) #green color
            thickness = 2
            occCount +=1

        cv2.rectangle(img, pos,(pos[0] + width, pos[1] + height), color, thickness) #this is moved down so not to make the
                                                                                     #boxes appear in the cropped img    
        cvzone.putTextRect(img,f'free : {spaceCounter}/{len(posList)}',(100,50),scale = 2,offset=15,thickness=3,colorR=(0,200,0))

        cvzone.putTextRect(img,f'Occupied : {occCount}/{len(posList)}',(350,50),scale = 2,offset=15,thickness=3,colorR=(0,0,255))                                                                                     
                                                                                     



while True:
    #to make the video run in loop 
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT): #if current frame == Total frame
        cap.set(cv2.CAP_PROP_POS_FRAMES,0) #if so then current frame =0 (i.e it'll again start from frame 0)

    success, img = cap.read() #to get the frame in video
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Graysclling the image
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY_INV,25,16) #we are thresholding the image
    imgMedian = cv2.medianBlur(imgThreshold,5) #to remove noice/random dots from the threshold video 
    kernal = np.ones((3,3),np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernal,iterations=1)


    checkParkPos(imgDilate)

    #for pos in posList:
    cv2.imshow('Image',img)  #to show the video
    # cv2.imshow("ImageBlur",imgBlur)# to show the grayed & blured video
    # cv2.imshow('ImgThres',imgThreshold)#to show the threshold image video
    # cv2.imshow('ImgMedian',imgMedian)
    # cv2.imshow('ImgDilate',imgDilate)
    cv2.waitKey(1) #video speed control
    