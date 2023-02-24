import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./img/test.jpg', 0)

# 转化为float32
img_float32 = np.float32(img)

# 使用Numpy查找傅立叶变换，FFT软件包来执行此操作
dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
# 首先创建一个掩码，中心正方形为1，其余全为零
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1

mag_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# RGB的值超出，缩小到0-255
log_unit8 = cv2.convertScaleAbs(mag_spectrum)

fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
img_back = cv2.convertScaleAbs(img_back)

cv2.imshow("img", img)
cv2.imshow("log_unit8", log_unit8)
cv2.imshow("img_back", img_back)
img_back
cv2.waitKey(0)
