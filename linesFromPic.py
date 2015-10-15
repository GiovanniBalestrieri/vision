#!usr/bin/env python

import cv2
import numpy as np
from math import *
import matplotlib.pyplot as plt
import Tkinter as tk
root = tk.Tk()


font = cv2.FONT_HERSHEY_SIMPLEX
# Define ROI
x1 = 0; y1 = 0; x2 = 2900; y2 = 1050

xStreet1 = 0; yStreet1 = 700; xF = 2600; yF = 1050

img = cv2.imread('image4-2.jpeg')
img1 = img[yStreet1:yF, xStreet1:xF]
imgL = img[yStreet1:yF, xStreet1:xF/2]
imgR = img[yStreet1:yF, xF/2:xF]
#img1 = img
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
grayR = cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
grayL = cv2.cvtColor(imgL,cv2.COLOR_BGR2GRAY)


vehicle_classifier = cv2.CascadeClassifier('cars2.xml')
vehicles = vehicle_classifier.detectMultiScale(gray, 1.1, 2, minSize=(100,100))
print 'Vehicles detected: %d' % (len(vehicles))

for (x,y,w,h) in vehicles:
	#cv.CaptureFromFile( '/home/mhughes/sintel_trailer-480p.mp4' )
	cv2.rectangle(img1, (x,y), (x+w, y+h),(255,0,0),4)

cv2.imwrite('cars.jpg',cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))


edgesL = cv2.Canny(grayL,22,66,apertureSize = 3)
edges = cv2.Canny(gray,22,66,apertureSize = 3)
edgesR = cv2.Canny(grayR,22,66,apertureSize = 3)
#cv2.imwrite('grey.jpg',gray)
cv2.imwrite('edgesR.jpg',edgesR)
cv2.imwrite('edgesL.jpg',edgesL)
cv2.rectangle(img, (x1,y1), (xF,yF), (255,255,0), thickness=3, lineType=8, shift=0)
cv2.rectangle(img, (xStreet1,yStreet1), (xF/2,yF), (255,100,255), thickness=4, lineType=8, shift=0)
cv2.rectangle(img, (xF/2,yStreet1), (xF,yF), (255,255,100), thickness=4, lineType=8, shift=0)

linesL = cv2.HoughLines(edgesL,1,pi/180,100)
for rho,theta in linesL[0]:
	angl =  theta*180/pi
	print angl, " L "
	a = cos(theta)
	b = sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	#cv2.line(img1,(x1,y1),(x2,y2),(100,255,255),2)
	if (angl >= 40) and (angl <= 50):
		a = cos(theta)
		b = sin(theta)
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))
		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a))
		cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),5)
		print "Found seconda corsia" 
	if (angl >= 75) and (angl <= 78):
		a = cos(theta)
		b = sin(theta)
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))
		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a))
		cv2.line(img1,(x1,y1),(x2,y2),(0,255,0),5)
		print "Found prima corsia" 
	
linesR = cv2.HoughLines(edgesR,1,pi/180,105)
for rho,theta in linesR[0]:
	angl =  theta*180/pi
	#print angl, " R "
	a = cos(theta)
	b = sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	#cv2.line(img1,(x1,y1),(xF,y2),(100,255,255),2)
	if (angl >= 110) and (angl <= 115):
		a = cos(theta)
		b = sin(theta)
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))
		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a))
		cv2.line(img1,(x1+xF/2,y1),(x2+xF/2,y2),(0,0,255),5)
		print "Found seconda corsia" 
	if (angl >= 102) and (angl <= 105):
		a = cos(theta)
		b = sin(theta)
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))
		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a))
		cv2.line(img1,(x1+xF/2,y1),(x2+xF/2,y2),(255,0,255),5)
		print "found terza corsia" 
	

cv2.imwrite('houghlines3.jpg',img)

x = root.winfo_pointerx()
y = root.winfo_pointery()
print x, "  ", y 