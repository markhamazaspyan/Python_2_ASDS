import cv2

# Open the image pic2.jpg and display it with the name pic2.
# Blur the picture using average and bilateral blurring methods and display in separate windows.
# (For the parameters, use the values of your choice).
# Write a short comment if you see any particular difference when using different
# parameter values for the second method and comparing it to the averaging method.

pic2 = cv2.imread("pic2.jpg")

average = cv2.blur(pic2, (5,5))
bilateral1 = cv2.bilateralFilter(pic2, 7, 30, 30,)


# looks smugged, similar to average blur but with edges preserved.

cv2.imshow('pic2', pic2)
cv2.imshow('average blur', average)
cv2.imshow('bilateral1', bilateral1)
cv2.waitKey(0)
