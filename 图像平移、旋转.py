# 图像翻转
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./img/test.jpg')

# 水平翻转
hor = cv.flip(img,1)
# 垂直翻转
ver = cv.flip(img,0)
# 水平垂直翻转
hor_ver = cv.flip(img,-1)

plt.figure(1)
plt.subplot(2,2,1)
plt.imshow(img)
plt.title('Original')
plt.xticks([]),plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(hor)
plt.title('horizontal')
plt.xticks([]),plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(ver)
plt.title('vertical')
plt.xticks([]),plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(hor_ver)
plt.title('horizontal_and_vertical')
plt.xticks([]),plt.yticks([])

plt.show()
