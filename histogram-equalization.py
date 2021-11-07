import cv2 as cv
from matplotlib import pyplot as plt 

imgPath = 'img/1.jpg'

# read image and convert it to gray scal image
src = cv.imread(imgPath)
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# store the output of the equalized image
dst = cv.equalizeHist(src)

# show the source and the equalized images 
cv.imshow('Source image', src)
cv.imshow('Equalized Image', dst)

# show the histogram of the source image
srcHistogram = cv.calcHist([src],[0],None,[256],[0,256]) 
plt.plot(srcHistogram) 
plt.show() 

# show the histogram of the equalized image
dstHistogram = cv.calcHist([dst],[0],None,[256],[0,256]) 
plt.plot(dstHistogram) 
plt.show() 

cv.waitKey()