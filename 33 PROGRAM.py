import cv2
import numpy as np
image=cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/1 image.jpeg")
kernel=np.ones((5,5),np.uint8)
dilation=cv2.dilate(image,kernel,iterations=1)
erosion=cv2.erode(image,kernel,iterations=1)
gradient=cv2.subtract(dilation,erosion)
cv2.imshow("Morphlogical Gradient",gradient)
cv2.waitkey(0)
cv2.destoryAllWindows()
