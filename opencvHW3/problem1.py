import cv2

# Open the image pic1.jpg and display it with the name pic1.
# Convert the image to the following formats and display in separate windows: RGB, HSV, LAB, grayscale.

pic1 = cv2.imread("pic1.jpg")

pic1_rgb = cv2.cvtColor(pic1, cv2.COLOR_BGR2RGB)
pic1_hsv = cv2.cvtColor(pic1, cv2.COLOR_BGR2HSV)
pic1_lab = cv2.cvtColor(pic1, cv2.COLOR_BGR2LAB)
pic1_gray = cv2.cvtColor(pic1, cv2.COLOR_BGR2GRAY)


cv2.imshow("pic1",pic1)
cv2.imshow("pic1_rgb",pic1_rgb)
cv2.imshow("pic1_hsv",pic1_hsv)
cv2.imshow("pic1_lab",pic1_lab)
cv2.imshow("pic1_gray",pic1_gray)
cv2.waitKey(0)