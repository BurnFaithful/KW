import cv2
import matplotlib.pyplot as plt

image = cv2.imread('../Scraping_001/lena.png')

edges = cv2.Canny(image, 200, 100)

plt.figure(figsize=(8, 5))
plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(image[:, :, [2, 1, 0]])
plt.subplot(122)
plt.axis('off')
plt.title('edges')
plt.imshow(edges, cmap='gray')
plt.tight_layout()
plt.show()