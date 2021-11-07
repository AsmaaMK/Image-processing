import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

imgPath = 'img/before_contrast_stretching.png'
img = cv.imread(imgPath)

original = img.copy()

xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]

x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')
img = cv.LUT(img, table)
cv.imwrite('output-imgs/streched-img.png', img)

cv.imshow("original", original)
cv.imshow("Output", img)

# show the histogram of the source image
srcHistogram = cv.calcHist([original],[0],None,[256],[0,256]) 
plt.figure()
plt.plot(srcHistogram) 
plt.show() 

# show the histogram of the equalized image
dstHistogram = cv.calcHist([img],[0],None,[256],[0,256]) 
plt.figure()
plt.plot(dstHistogram) 
plt.show() 

cv.waitKey(0)