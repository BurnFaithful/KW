import cv2
import numpy as np

image = cv2.imread('../Scraping_001/lena.png')
image = image.astype(np.float32) / 255
print('Shape :', image.shape)
print('Data Type :', image.dtype)

# cv2.imshow('image', np.clip(image * 2, 0, 1))
image[:, :, [0, 2]] = image[:, :, [2, 0]]
cv2.imshow('blue_and_red_swapped', image)
cv2.waitKey()
cv2.destroyAllWindows()