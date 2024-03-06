import cv2
import numpy as np
image = cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/2 image.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
sharpened_image = cv2.add(gray_image, laplacian)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
