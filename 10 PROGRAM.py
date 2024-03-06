import cv2
import numpy as np
image = cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/2 image.jpeg")
tx, ty = 100, 50
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
height, width = image.shape[:2]
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
