import cv2, numpy as np

image = np.full((480, 640, 3), 255, np.uint8)
# full (size, BGR Color, )
cv2.imshow('white', image)
cv2.waitKey()
cv2.destroyAllWindows()

image = np.full((480, 640, 3), (0, 0, 255), np.uint8)
cv2.imshow('red', image)
cv2.waitKey()
cv2.destroyAllWindows()

image[240, 160] = image[240, 320] = image[240, 480] = (255, 255, 255)
cv2.imshow('red with white pixels', image)
cv2.waitKey()
cv2.destroyAllWindows()