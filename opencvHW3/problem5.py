import cv2
import numpy as np
blank = np.zeros((400, 400), dtype = 'uint8')


rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 100, -1)

circle = cv2.circle(blank.copy(), (200, 200), 200, 100, -1)


#image 1
bitwise_xor = cv2.bitwise_xor(circle,rectangle)
cv2.imshow('image1', bitwise_xor)

#image 2
bitwise_or = cv2.bitwise_or(circle,rectangle)
cv2.imshow('image2', bitwise_or)

#image 3
blank = np.zeros((400, 400, 3), dtype = 'uint8')
pink = (int(255*0.8),int(255*0.75), 255)

rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), pink, -1)
circle = cv2.circle(blank.copy(), (200, 200), 200, pink, -1)
bitwise_xor2 = cv2.bitwise_xor(circle,rectangle)
cv2.imshow('image3', bitwise_xor2)
cv2.waitKey(0)

