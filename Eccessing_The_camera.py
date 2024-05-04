import cv2
import time

cam = cv2.VideoCapture(0)
time.sleep(1)

while True:
    _,img = cam.read()
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cam.release()