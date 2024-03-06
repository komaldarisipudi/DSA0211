import cv2
main_image = cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/2 image.jpeg")
watermark_image = cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/2 image.jpeg", cv2.IMREAD_UNCHANGED)
if watermark_image is None:
    print("Error: Could not load watermark image")
    exit(1)
watermark_resized = cv2.resize(watermark_image, (main_image.shape[1], main_image.shape[0]))
alpha = 0.5  
watermarked_image = cv2.addWeighted(main_image, 1, watermark_resized, alpha, 0)
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
