import matplotlib.pyplot as plt
import cv2

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 原图
img = cv2.imread("img/homework1.bmp", 0)  # 直接读为灰度图像

# 142, 148二值化处理

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
# 3.2 邻域内⾼斯加权
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)

cv2.imshow("th2", th2)
cv2.imshow("th3", th3)


ret, thresh1 = cv2.threshold(img, 142, 148, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 142, 148, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 142, 148, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 142, 148, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 142, 148, cv2.THRESH_TOZERO_INV)

cv2.imshow("img", img)
cv2.imshow("BINARY", thresh1)
cv2.imshow("BINARY_INV", thresh2)
cv2.imshow("TRUNC", thresh3)
cv2.imshow("TOZERO", thresh4)
cv2.imshow("THRESH_TOZERO_INV", thresh5)
cv2.waitKey(0)

titles = ['img', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# 设置SimpleBlodDetector参数
params = cv2.SimpleBlobDetector_Params()
# 改变阈值
params.minThreshold = 10
params.maxThreshold = 200
# 通过面积滤波
params.filterByArea = True
params.minArea = 1500
# 通过圆度滤波
params.filterByCircularity = True
params.minCircularity = 0.1
# 通过凸度滤波
params.filterByConvexity = True
params.minConvexity = 0.87
# 通过惯性比滤波
params.filterByInertia = True
params.minInertiaRatio = 0.01
# 创建一个检测器并使用默认参数
ver = (cv2.version).split(',')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)
