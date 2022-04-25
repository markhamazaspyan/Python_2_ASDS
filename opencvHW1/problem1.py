import cv2
#  Problem 1.
# Open images pic1.jpg, pic2.jpg and pic3.jpg and display in separate windows with the names pic1, pic2 and pic3 correspondingly.
pic1 = cv2.imread("pic1.jpg")
pic2 = cv2.imread("pic2.jpg")
pic3 = cv2.imread("pic3.jpg")

cv2.imshow("pic1",pic1)
cv2.imshow("pic2",pic2)
cv2.imshow("pic3",pic3)
cv2.waitKey(0)