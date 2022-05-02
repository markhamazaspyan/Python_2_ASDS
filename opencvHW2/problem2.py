import cv2
# Problem 2.
# Open the image pic1.jpg and display it with the name pic1. Blur the image using Gaussian blur using 2 different windows sizes: (3, 3) and (11, 11) and display both versions in separate windows to compare with the original image.

pic1 = cv2.imread("pic1.jpg")

pic1_blur1 = cv2.GaussianBlur(pic1, (3,3), cv2.BORDER_DEFAULT)
pic1_blur2 = cv2.GaussianBlur(pic1, (11,11), cv2.BORDER_DEFAULT)

cv2.imshow("pic1",pic1)
cv2.imshow("pic2",pic1_blur1)
cv2.imshow("pic3",pic1_blur2)
cv2.waitKey(0)