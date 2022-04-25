import cv2
# Problem 5.
# Draw a red filled circle in the middle of the image pic2.jpg.
# Use an appropriate radius value so that the whole circle is visible. Display the original image and the changed one in separate windows.


pic2 = cv2.imread("pic2.jpg")

sh = pic2.shape
center=(int(sh[1]/2), int(sh[0]/2))
radius = 100
color=(0, 0, 255)
thickness = -1

pic2_circle = cv2.circle(pic2.copy(), center, radius, color, thickness)

cv2.imshow('pic2', pic2)
cv2.imshow('pic2_circle', pic2_circle)

cv2.waitKey(0)
