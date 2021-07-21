import cv2
import numpy as np

image = cv2.imread("rubix.png")

image[np.where((image == [0, 255, 255]).all(axis=2))] = [255, 0, 0]
image[np.where((image == [255, 255, 0]).all(axis=2))] = [0, 0, 255]
image[np.where((image == [255, 0, 255]).all(axis=2))] = [0, 255, 0]

cv2.imwrite('Rubik.png', image)
cv2.imshow('out', image)
cv2.waitKey()