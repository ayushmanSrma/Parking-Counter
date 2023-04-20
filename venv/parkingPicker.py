import  cv2
import  pickle


width, height = 107, 48 # these are the ht and wdt of rectangle
try:
    with open('CarParkPos','rb') as f:
     posList = pickle.load(f)
except:
    posList = []    #to determine the starting pt x&y (ht and width is entered here)

#here we are defining the mouseClick function
def mouseClick(events,x,y,flags,params):  #we are passing the parameters in the function
    if events == cv2.EVENT_LBUTTONDOWN:  #if events = leftbutton clicked
        posList.append((x,y))             #posList will append(x&y)
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:   #to check the pos is within the dimensions of rectangle or not
                posList.pop(i)                     #this function is to remove the box
    
    with open('CarParkPos','wb') as f:             #creating a new file to store the rectangle boxes
        pickle.dump(posList, f)                    #dumping the posList in file f

while True:
    img  = cv2.imread('/Users/ayushmansharma/PycharmProjects/parkingCounter/venv/carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos,(pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    #cv2.rectangle(img,(50,192),(157,240),(255,0,255),2) #these are the dimensions of the rectangle to for the ROI in parking space
    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image",mouseClick)
    cv2.waitKey(1)