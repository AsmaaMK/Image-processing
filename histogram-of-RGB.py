import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

imgPath = 'img/rgb.png'
src = cv.imread(imgPath)

color = ('b','g','r')
for k,color in enumerate(color):
  histogram = cv.calcHist([src],[k],None,[256],[0,256])
  plt.figure()
  plt.plot(histogram,color = color)
  plt.xlim([0,256])

plt.show()