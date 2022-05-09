import cv2
import numpy as np

# Open the image pic1.jpg and display it with the name pic1.
# Separate the image into its 3 channels. Display both the colored and grayscale versions of each channel in separate windows.

pic1 = cv2.imread("pic1.jpg")

b,g,r = cv2.split(pic1)

blank = np.zeros(pic1.shape[:2], dtype = 'uint8')
blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

b_gray = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
g_gray = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
r_gray = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)



cv2.imshow("pic1",pic1)
cv2.imshow("b",blue)
cv2.imshow("g",green)
cv2.imshow("r",red)

cv2.imshow("b_gray",b_gray)
cv2.imshow("g_gray",g_gray)
cv2.imshow("r_gray",r_gray)
cv2.waitKey(0)