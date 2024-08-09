import cv2

plateCascade= cv2.CascadeClassifier("C:/Users/shlok/OneDrive/Desktop/Practice/DataScience/Opencv/haarcascade_russian_plate_number.xml")

minArea=500
color=(0,255,0)
count=0
cap=cv2.VideoCapture(0)


while True:
    success, img=cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    nPlates = plateCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in nPlates:
        area=w*h
        if area>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,'Number Plate',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
            imgNplate=img[y:y+h,x:x+w]
            cv2.imshow('Number Plate',imgNplate)
    cv2.imshow('Result',img)

    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite('C:/Users/shlok/OneDrive/Desktop/Practice/DataScience/Opencv'+str(count)+'.jpg',imgNplate)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
