import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./img/classs.png')
cv2.imshow("img", img)


resizeimg = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow("resizeimg", resizeimg)

affine_arr = np.float32([[1, 0, 50], [0, 1, 50]])
img_array = np.array(img)

transimg = cv2.warpAffine(img, affine_arr, (img_array.shape[0] * 2, img_array.shape[1] * 2))
cv2.imshow("transimg", transimg)

roatM = cv2.getRotationMatrix2D((resizeimg.shape[0] / 2, resizeimg.shape[1] / 2), -45, 0.5)
rotaimg = cv2.warpAffine(resizeimg, roatM, (resizeimg.shape[1] * 2, resizeimg.shape[0] * 2))
cv2.imshow("rotaimg", rotaimg)

H_rows, W_cols = img.shape[:2]
pt1 = np.float32([[425, 278], [600, 280], [3, 452], [1008, 457]])
pt2 = np.float32([[0, 0], [W_cols, 0], [0, H_rows], [W_cols, H_rows]])
warpM = cv2.getPerspectiveTransform(pt1, pt2)
warpimg = cv2.warpPerspective(img, warpM, (img.shape[1], img.shape[0]))
cv2.imshow("warpimg", warpimg)

cv2.waitKey(0)
