import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

imgPath = 'img/rgb.png'
src = cv.imread(imgPath)

# extract red channel
redChannel = src[:,:,2]

# create empty image with same shape as that of src image
redImg = np.zeros(src.shape)

#assign the red channel of src to empty image
redImg[:,:,2] = redChannel

#save image
cv.imwrite('output-imgs/rgb.png-red-channel.png',redImg) 

# extract green channel
greenChannel = src[:,:,1]
greenImg = np.zeros(src.shape)
greenImg[:,:,1] = greenChannel
cv.imwrite('output-imgs/rgb.png-green-channel.png',greenImg) 

# extract blue channel
blueChannel = src[:,:,0]
blueImg = np.zeros(src.shape)
blueImg[:,:,0] = blueChannel
cv.imwrite('output-imgs/rgb.png-blue-channel.png',blueImg)