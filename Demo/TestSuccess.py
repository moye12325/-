import cv2
import numpy as np
img = cv2.imread('../img/firewatch-landscape-forest-minimalistic-games-6993-2560x1440.jpg', cv2.IMREAD_COLOR)  #引号里面的图片地址自己改
cv2.imshow("test_read_pic", img)        #这里引号里面代表出来的框的标题
cv2.waitKey(0)