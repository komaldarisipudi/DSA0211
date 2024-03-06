import cv2
import numpy as np
image=cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/1 image.jpeg")
kernel=np.ones((5,5),np.uint8)
tophat=cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)
cv2.imshow("Original Image",image)
cv2.imshow("Top Hat",tophat)
cv22.waitkey(0)
cv2.destroyAllWindows()
