import cv2
import numpy as np
image=cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/1 image.jpeg")
kernel=np.ones((5,5),np.uint8)
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
cv2.imshow("Closing",closing)
cv2.waitkey(0)
cv2.destoryAllWindows()
