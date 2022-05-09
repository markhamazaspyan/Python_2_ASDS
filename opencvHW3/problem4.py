import cv2
import numpy as np

# Open the image pic2.jpg and display it with the name pic2.
# Apply the correct method so that only a circle of radius of 70 pixels is left right in the middle of the picture.
# Your result should look similar to the example below.


pic2 = cv2.imread("pic2.jpg")
h,w = pic2.shape[:2]
blank = np.zeros((h,w), dtype = 'uint8')

circle = cv2.circle(blank.copy(), (int(w/2), int(h/2)), 70, 255, -1)

bitwise_and = cv2.bitwise_and(pic2, pic2, mask=circle)

cv2.imshow("bitwise_and",bitwise_and)
cv2.waitKey(0)
