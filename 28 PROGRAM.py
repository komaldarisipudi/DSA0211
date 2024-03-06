import cv2
import numpy as np
image_path = "C:/Users/KOMAL DARISIPUDI/Desktop/cv images/2 image.jpeg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
sobel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])
edges_x = cv2.filter2D(image, -1, sobel_x)
edges_y = cv2.filter2D(image, -1, sobel_y)
edges = cv2.addWeighted(edges_x, 0.5, edges_y, 0.5, 0)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
