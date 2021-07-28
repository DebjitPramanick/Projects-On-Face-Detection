import cv2
import time
import numpy as np

# Get files from here https://github.com/opencv/opencv/tree/master/data/haarcascades

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    'haarcascades/haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')

while True:
    ch, frame = video.read()
    if ch:
        face = face_cascade.detectMultiScale(
            frame, scaleFactor=1.1, minNeighbors=5)

        for x, y, w, h in face:
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 5), 1)
            smile = smile_cascade.detectMultiScale(
                frame, scaleFactor=1.8, minNeighbors=20)
            for x1, y1, w1, h1 in smile:
                img = cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (155, 0, 0), 3)

        cv2.imshow('Video Frame',frame)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    else: 
        break

video.release()
cv2.destroyAllWindows()
