import cv2
# Problem 4.
# Open the image pic2.jpg and display it with the name pic2. Resize the image to have 2 times bigger width and the same height as the original image, use INTER_AREA interpolation.
# Then resize the original image to have 2 times smaller height and the same width as the original image, use INTER_CUBIC interpolation. Display both versions in separate windows.



pic2 = cv2.imread("pic2.jpg")

dimensions1 = int(pic2.shape[1]*2), pic2.shape[0]
pic2_rescaled1 = cv2.resize(pic2, dimensions1, interpolation=cv2.INTER_AREA)

dimensions2 = pic2.shape[1], int(pic2.shape[0]/2)
pic2_rescaled2 = cv2.resize(pic2, dimensions2, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Edges1', pic2_rescaled1)
cv2.imshow('Edges2', pic2_rescaled2)
cv2.waitKey(0)
