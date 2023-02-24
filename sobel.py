import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./img/test.jpg')

media = cv2.medianBlur(img, 3)
# gaussianBlur = cv2.GaussianBlur(img, (3, 3), 1.5)
sobel_x = cv2.Sobel(media, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(media, cv2.CV_64F, 0, 1, ksize=3)

cv2.imshow("sobel_x", sobel_x)
cv2.imshow("sobel_y", sobel_y)
cv2.waitKey(0)
