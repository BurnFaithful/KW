import cv2
import numpy as np

image = cv2.imread('../Scraping_001/lena.png', 0)
image = image.astype(np.float32) / 255

gamma = 0.5
corrected_image = np.power(image, gamma)

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# print('Shape :', gray.shape)
# print('Data Type :', gray.dtype)
cv2.imshow('image', image)
cv2.imshow('corrected_image', corrected_image)
cv2.waitKey()
cv2.destroyAllWindows()