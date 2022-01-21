from turtle import shape

import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)

    dimentions = (width, heigth)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)


# Read image
img = cv.imread('Resources\Photos\cat.jpg')
img_resize = rescaleFrame(img)
cv.imshow('Cat', img_resize)

# Read video
capture = cv.VideoCapture('Resources\Videos\dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    # cv.imshow('VIDEO', frame)
    cv.imshow('VIDEO', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
