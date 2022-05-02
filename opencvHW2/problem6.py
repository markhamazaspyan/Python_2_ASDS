import cv2
import numpy as np
# Problem 6.
# Open the image pic3.jpg and display it with the name pic3. Find the edges of the image using Canny edge detector and then try to find its contours with parameters of your choice.
# Then convert the original image to grayscale and try to find the contours on a blurred version of the grayscale of the original image. Display the 2 results in separate windows to compare.

pic3 = cv2.imread("pic3.jpg")
cv2.imshow('pic3', pic3)
cv2.waitKey(0)


canny = cv2.Canny(pic3, 125, 175)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(len(contours))
blank = np.zeros(pic3.shape, dtype = 'uint8')
cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv2.imshow('blank', blank)
cv2.waitKey(0)



gray = cv2.cvtColor(pic3, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
cv2.imshow('blan', blur)
cv2.waitKey(0)

contours, hierarchies = cv2.findContours(blur, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
blank2 = np.zeros(pic3.shape, dtype = 'uint8')
cv2.drawContours(blank2, contours, -1, (0, 0, 255), 1)
cv2.imshow('blank2', blank2)
cv2.waitKey(0)
