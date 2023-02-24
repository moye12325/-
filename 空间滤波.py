# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
#
# # image = cv2.imread("img/test.jpg", 0)
# image = cv2.imread('./img/homework1.bmp',cv2.IMREAD_COLOR)
# blur = cv2.blur(image, (3, 3))
#
# # width = 500
# # height = 500  # 指定值改变图像大小
#
# median = cv2.medianBlur(image, 3)
# gaussianBlur = cv2.GaussianBlur(image, (3, 3), 1.5)
#
# ret,threshold1 = cv2.threshold(image,127,255, cv2.THRESH_BINARY)
# ret,threshold2 = cv2.threshold(gaussianBlur,127,255, cv2.THRESH_BINARY)
#
#
# cv2.imshow("image", image)
# cv2.imshow("blur", blur)
# cv2.imshow("gaussianBlur", gaussianBlur)
# cv2.waitKey(0)


# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
#
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
#
# # 1 读取图像
# img = cv.imread("img/homework1.bmp", 0)
# # img = cv.imread('./image/horse.jpg',0)
# # 2 计算Sobel卷积结果
# x = cv.Sobel(img, cv.CV_16S, 1, 0)
# y = cv.Sobel(img, cv.CV_16S, 0, 1)
# # 3 将数据进⾏转换
# Scale_absX = cv.convertScaleAbs(x)  # convert 转换 scale 缩放
# Scale_absY = cv.convertScaleAbs(y)
# # 4 结果合成
# result = cv.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
# # 5 图像显示
# cv.imshow("res", result)
# cv.waitKey(0)
# plt.figure(figsize=(10, 8), dpi=100)
# plt.subplot(121), plt.imshow(img, cmap=plt.cm.gray), plt.title('原图')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(result, cmap=plt.cm.gray), plt.title('Sobel滤波后结果:')
# plt.xticks([]), plt.yticks([])
# plt.show()
#
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
# # 1 读取图像
# img = cv.imread("img/homework1.bmp", 0)
# # 2 设计⾼通滤波器(傅⾥叶变换结果中有两个通道，所以⾼通滤波中也有两个通道)
# rows,cols = img.shape
# mask = np.ones((rows,cols,2),np.uint8)
# mask[int(rows/2)-30:int(rows/2)+30,int(cols/2)-30:int(cols/2)+30,:] = 0
# # 3 傅⾥叶变换
# # 3.1 正变换
# dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
# # 3.2 频谱中⼼化
# dft_shift = np.fft.fftshift(dft)
# # 3.3 滤波
# dft_shift = dft_shift * mask
# # 3.4 频谱去中⼼化
# dft_shift = np.fft.fftshift(dft_shift)
# # 3 傅⾥叶逆变换
# # 3.1 反变换
# img_back = cv.idft(dft_shift)
# # 3.2 计算灰度值
# img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])
# cv.imshow("res", img_back)
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('输⼊图像'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
# plt.title('⾼通滤波结果'), plt.xticks([]), plt.yticks([])
# plt.show()

