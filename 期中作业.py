import matplotlib.pyplot as plt
import cv2
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 原图
img = cv2.imread("img/homework1.bmp", 0)  # 直接读为灰度图像

# 增加图像亮度
# 注意需要使用cv.add(),不能直接x+y
res1 = np.uint8(np.clip((cv2.add(1 * img, 30)), 0, 255))
# 增加图像对比度
res2 = np.uint8(np.clip((cv2.add(1.5 * img, 0)), 0, 255))
tmp = np.hstack((img, res1, res2))  # 三张图片横向合并（便于对比显示）
cv2.imshow('image', img)
cv2.imshow('res1', res1)
cv2.imshow('res2', res2)
# cv2.waitKey(0)


# 142, 148二值化处理
img = res1
ret, thresh1 = cv2.threshold(img, 168, 175, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 168, 175, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 168, 175, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 168, 175, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 168, 175, cv2.THRESH_TOZERO_INV)

cv2.imshow("img", img)
cv2.imshow("BINARY", thresh1)
cv2.imshow("BINARY_INV", thresh2)
cv2.imshow("TRUNC", thresh3)
cv2.imshow("TOZERO", thresh4)
cv2.imshow("THRESH_TOZERO_INV", thresh5)

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

# 2 Canny边缘检测
lowThreshold = 0
max_lowThreshold = 100
canny = cv2.Canny(thresh5, lowThreshold, max_lowThreshold)
cv2.imshow("canny", canny)


cv2.waitKey(0)

titles = ['img', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
