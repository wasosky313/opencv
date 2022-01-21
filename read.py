import cv2 as cv

# Read image
img = cv.imread('Resources\Photos\cat.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)
