import cv2 as cv
import time
import numpy as np
import winsound
import math
from matplotlib import pyplot as plt

right = cv.VideoCapture(0)

while True:

    _, rightFrame = right.read()
    frameL = rightFrame[:, :320]
    frame0_new = cv.cvtColor(frameL, cv.COLOR_BGR2GRAY)
    frame1 = rightFrame[:, 320:]
    frame1_new = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

    stereo = cv.StereoBM_create(numDisparities=0,blockSize=13)
    disparity = stereo.compute(frame0_new, frame1_new)


    foc = 736
    B = 6.00/100
    dist = foc*B/disparity
    actualDist = 0.0
    minActualDist = math.sqrt(math.pow(160,2) + math.pow(120,2) + math.pow(dist[239,319],2))
    for i in range(239):
        for j in range(319):
            actualDist = math.sqrt(math.pow((160-i),2) + math.pow((120-j),2) + math.pow(dist[i,j],2))
            if actualDist < minActualDist:
                minActualDist = actualDist

    print("Distance : ",minActualDist*4)

    if  minActualDist*4.0 <= 1.5:
        winsound.PlaySound('mb3D_L.wav',winsound.SND_FILENAME)
    if minActualDist * 4 == 11.04:
        winsound.PlaySound('mb3D-old1.wav',winsound.SND_FILENAME)
    if minActualDist*4 > 11.04:
        winsound.PlaySound('mb3D.wav',winsound.SND_FILENAME)

right.release()