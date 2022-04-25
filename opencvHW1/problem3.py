import cv2
# Problem 3.
# Rescale the image pic1.jpg by 0.5 and display the original image and the rescaled one in separate windows.

pic1 = cv2.imread("pic1.jpg")

scale = 0.5
width = int(pic1.shape[1] * scale)
height = int(pic1.shape[0] * scale)
dimensions = (width, height)

pic1_rescaled = cv2.resize(pic1, dimensions, interpolation=cv2.INTER_AREA)

cv2.imshow('pic1', pic1)
cv2.imshow('pic1_rescaled', pic1_rescaled)

cv2.waitKey(0)
