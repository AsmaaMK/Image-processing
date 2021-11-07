import cv2 as cv

imgPath = 'img/cameraman.png'
img = cv.imread(imgPath)
negImg = 255 - img

cv.imshow('Original Image', img)
cv.imshow('Negative Image', negImg)
cv.waitKey(0)