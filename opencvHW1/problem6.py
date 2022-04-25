import cv2
# Problem 6.
# Draw an orange rectangle with thickness 2 on the image pic2.jpg.
# Use appropriate measures for the rectangle so that the whole rectangle is visible. Display the original image and the changed one in separate windows.

pic2 = cv2.imread("pic2.jpg")

point1=(300,100)
point2=(600,300)
color=(0,165,255)

thickness=2

pic2_rect = cv2.rectangle(pic2.copy(), point1, point2, color, thickness)

cv2.imshow('pic2', pic2)
cv2.imshow('pic2_rect', pic2_rect)

cv2.waitKey(0)
