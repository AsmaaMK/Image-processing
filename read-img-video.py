import cv2 as cv

# image read and show
imgPath = 'resources/1.jpg'
img = cv.imread(imgPath)
cv.imshow('Image', img)
cv.waitKey(0)

# video read and show
# videoPath = 'resources/2.mp4'
# cap = cv.VideoCapture(videoPath)
# while True:
#     isTrue, img = cap.read()
#     cv.imshow("Video", img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#       break
