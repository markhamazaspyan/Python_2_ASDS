import cv2
import numpy as np
# Problem 5.
# Open the image pic2.jpg and display it with the name pic2. Translate the image to go down by 200 pixels and to the right by 50 pixels.
# Then rotate the image around its center by 50 degrees. Then flip the resulting image both vertically and horizontally. Display the result after each action in a separate window.

#### coment: I used pic1 as pic2 shape is small for 200 x 50 transfrom only black returned.

pic2 = cv2.imread("pic1.jpg")
cv2.imshow('pic2', pic2)
cv2.waitKey(0)

def translate(img, x, y):

    transMat = np.float32([[1, 0, x], [0, 1, y]]) #translation matrix
    dimentions = (img.shape[1], img.shape[0]) #(width, height)

    return cv2.warpAffine(img, transMat, dimentions)

translated = translate(pic2, 50, 200)
cv2.imshow('translated', translated)
cv2.waitKey(0)


def rotate(img, angle, rotPoint=None):

    (height, width) = (img.shape[0], img.shape[1])

    if rotPoint == None:
        rotPoint = (width//2, height//2)

    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0) # 1.0 - scale
    dimentions = (width, height)

    return cv2.warpAffine(img, rotMat, dimentions)


rotated = rotate(translated, 50)
cv2.imshow('rotated', rotated)
cv2.waitKey(0)

flip = cv2.flip(rotated, -1)

cv2.imshow('flipped', flip)
cv2.waitKey(0)