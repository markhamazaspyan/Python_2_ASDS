import cv2
# Problem 7.
# Draw a line starting from the left lower corner and ending in the right upper corner of the image pic1.jpg.
# Display the original image and the changed one in separate windows.


pic1 = cv2.imread("pic1.jpg")


point1 = (0,pic1.shape[0])
point2 = (pic1.shape[1],0)
pic1_line = cv2.line(pic1.copy(), point1, point2, color=(0,0,255), thickness=2)

cv2.imshow('pic1', pic1)
cv2.imshow('pic1_line', pic1_line)

cv2.waitKey(0)

