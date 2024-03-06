import cv2
import numpy as np
image = cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/1 image.jpeg", 0)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
