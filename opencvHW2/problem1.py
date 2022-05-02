import cv2
# Open the image pic1.jpg and display it with the name pic1. Convert the image to grayscale and display in a separate window to compare with the original image.
pic1 = cv2.imread("pic1.jpg")

pic1_gray = cv2.cvtColor(cv2.imread("pic1.jpg"), cv2.COLOR_BGR2GRAY)


cv2.imshow("pic1",pic1)
cv2.imshow("pic2",pic1_gray)
cv2.waitKey(0)