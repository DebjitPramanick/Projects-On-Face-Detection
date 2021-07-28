import cv2, time

# Get files from here https://github.com/opencv/opencv/tree/master/data/haarcascades

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    ch, frame = video.read()
    if ch:
        face = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

        for x,y,w,h in face:
            img = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,5), 1)
            img[y: y+h, x:x+w] = cv2.medianBlur(img[y:y+h, x:x+w], 25)

        cv2.imshow('Video Frame',img)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    else: 
        break

video.release()
cv2.destroyAllWindows()