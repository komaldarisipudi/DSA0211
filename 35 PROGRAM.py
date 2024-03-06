import cv2
import numpy as np
img=cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/2 image.jpeg",cv2.IMREAD_GRAYSCALE)
kernel=np.ones((5,5),np.uint8)
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("Original Image",img)
cv2.imshow("Black Hat",blackhat)
cv2.waitkey(0)
cv2.destoryAllWindows
