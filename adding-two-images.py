import cv2 as cv

# read two images
src1 = cv.imread('img/rgb.png', cv.IMREAD_COLOR)
src2 = cv.imread('img/opencv.png', cv.IMREAD_COLOR)

# add or blend the images
dst = cv.addWeighted(src1, 0.5, src2, 0.5, 0.0)

# save the output image
cv.imwrite('added-image.png', dst)