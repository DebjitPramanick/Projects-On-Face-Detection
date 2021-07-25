import cv2, time

video = cv2.VideoCapture(0)

while True:
    ch, frame = video.read()
    if ch:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Video Frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break

video.release()
cv2.destroyAllWindows()