import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("img/firewatch-landscape-forest-minimalistic-games-6993-2560x1440.jpg", 0)
image = cv2.imread("img/homework1.bmp", 0)  # 直接读为灰度图像
equ = cv2.equalizeHist(image)

width = 500
height=500  #指定值改变图像大小
# height = int(image.shape[0] * width / image.shape[1])
image = cv2.resize(image, (width, height), interpolation=cv2.INTER_NEAREST)

cv2.imshow("hist", image)
cv2.imshow("equ", image)
cv2.waitKey(0)

hist1 = cv2.calcHist([image], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([equ], [0], None, [256], [0, 256])

print(hist1)
plt.plot(hist1, color='b')
plt.xlim([0, 256])
# plt.show()

print(hist2)
plt.plot(hist2, color='g')
plt.xlim([0, 256])
plt.show()
