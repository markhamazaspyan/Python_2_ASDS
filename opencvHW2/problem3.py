import cv2
# Problem 3.
# Open the image pic2.jpg and display it with the name pic2. Try to detect the image edges using Canny edge detector and display the result in a separate window.
# Then run the edge detector on a blurred version of an image (use a window size of your choice) and display the result in a different window to compare.

pic2 = cv2.imread("pic2.jpg")
canny = cv2.Canny(pic2, 125, 175)

pic_blur2 = cv2.GaussianBlur(pic2, (5,5), cv2.BORDER_DEFAULT)

canny_blur = cv2.Canny(pic_blur2, 125, 175)
cv2.imshow('Edges1', canny)
cv2.imshow('Edges2', canny_blur)
cv2.waitKey(0)
