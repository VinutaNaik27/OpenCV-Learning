import cv2
face_cascade = cv2.CascadeClassifier(
    r"haarcascade_frontalface_default.xml"
)


if face_cascade.empty():
    print("Error: Haar Cascade file not found!")
    exit()
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,6)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,"Face Detected",(x, y - 10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 255, 0),2)
    
    cv2.imshow("face detection",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        print("Quitting!!!")
        break

cap.release()
cv2.destroyAllWindows()        