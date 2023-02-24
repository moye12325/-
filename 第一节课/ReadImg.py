import cv2
import numpy as np

img = cv2.imread('../img/firewatch-landscape-forest-minimalistic-games-6993-2560x1440.jpg',cv2.IMREAD_COLOR)
print(type(img))
print(img)
cv2.imshow("test_image",img)
cv2.waitKey(0)