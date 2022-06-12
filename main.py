import cv2
import time

cap = cv2.VideoCapture(0)


flag = 1

def detector(frame,frame1):
    diff = cv2.absdiff(frame,frame1)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    cv2.imshow("dd",dilated)
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours,-1,(0,0,255),2)
    
    for cnt in contours:
        if cv2.contourArea(cnt) < 20000:
            continue
        x, y ,w , h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
        return 1
    return 0

while True:
    _,frame = cap.read()
    _,frame1 = cap.read()

    i = detector(frame,frame1)
    if i == 1 and flag:
        print("se detecto movimiento")
        flag = 0

    if cv2.waitKey(10) == ord("q"):
        break
    #cv2.imshow("Detector",frame)
time.sleep(2)
