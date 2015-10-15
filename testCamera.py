import cv2

cam = cv2.VideoCapture(0)
cam.open(0)
results = [ cam.read()[0] for i in range(100) ]
print results
