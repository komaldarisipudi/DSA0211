import cv2
import numpy as np
image = cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/2 image.jpeg")
blur = cv2.GaussianBlur(image, (0,0), 3)
high_boost_mask = cv2.subtract(image, blur)
boost_factor = 1.5
high_boost_mask = cv2.multiply(high_boost_mask, np.array([boost_factor]))
sharpened_image = cv2.add(image, high_boost_mask)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
