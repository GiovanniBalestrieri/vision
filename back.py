import numpy as np
import cv2

cap = cv2.VideoCapture('NRide.avi')

#fgbg = cv2.createBackgroundSubtractorMOG()
fgbg = cv2.BackgroundSubtractorMOG()
while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
