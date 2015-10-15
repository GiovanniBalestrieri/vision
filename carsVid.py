#!usr/bin/env python
import cv
import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
# Define ROI
x00 = 0; y00= 0; x22 = 2900; y22 = 1050

xStreet1 = 0; yStreet1 = 700;

video = cv2.VideoCapture( 'Nride.avi' )
while(video.isOpened()):

    ret, frame = video.read()
    if frame != None:
        img1 = frame[yStreet1:y22, xStreet1:x22]
        if img1 != None:
            gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

        #vehicle_classifier = cv2.CascadeClassifier('cars2.xml')
        #if gray != None:
        #    vehicles = vehicle_classifier.detectMultiScale(gray, 1.1, 2, minSize=(100,100))
        #print 'Vehicles detected: %d' % (len(vehicles))

        #for (x,y,w,h) in vehicles:
        #    cv2.rectangle(img1, (x,y), (x+w, y+h),(255,0,0),4)

        if gray != None:
            edges = cv2.Canny(gray,50,150,apertureSize = 3)
        else:
            print "Gray None"

        cv2.rectangle(frame, (x00,y00), (x22,y22), (255,255,0), thickness=3, lineType=8, shift=0)

        if edges != None:
            lines = cv2.HoughLines(edges,2,np.pi/180,250)
        #print lines

        if lines != None:
            #for x1,y1,x2,y2 in lines[0]:
            for rho,theta in lines[0]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),2)
                #cv2.line(img1,(x1,y1),(x2,y2),(0,255,0),2)

        #lines = None

        small = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 
        cv2.imshow('frame',small)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
