#!/usr/bin/python

import cv2
from math import *
import numpy as np

img = cv2.imread('image4-2.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,20,150,apertureSize = 3)
cv2.imwrite('houghlinesBfad.jpg',edges)
minLineLength = 100
maxLineGap = 20

def calcAngle(x0,x1,y0,y1f):
	xV = x1-x0
	yV = y1-y0
	mod = sqrt(xV**2+yV**2)
	phase = atan2(yV,xV)*180.0 / pi
	if phase<0:
		phase=phase+360
	return phase

lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
	phase = calcAngle(x2,x1,y2,y1)
	if phase > 179:
		print phase
		cv2.line(img,(x1,y1),(x2,y2),(0,255,255),5)

cv2.imwrite('houghlines5.jpg',img)
