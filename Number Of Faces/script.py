import cv2, time

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

while True:
    ch, frame = video.read()

    if ch:
        face = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
        i = 1
        for x, y, w, h in face:
            corX = x+(h//2)
            corY = y+(h//2)
            frame[y: y+h, x:x+w] = cv2.medianBlur(frame[y:y+h, x:x+w], 25)
            cv2.putText(frame, "Face: "+str(i), (x, y-20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (30,144,255), 2)
            img = cv2.circle(frame, (corX, corY), h//2, (0,0,255), 3)
            i+=1

        cv2.imshow("Video Frame",frame)
   
        k = cv2.waitKey(1)
        if k == ord('q'): break
    else:
        break

video.release()
cv2.destroyAllWindows()