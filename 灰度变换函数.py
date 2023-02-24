import cv2
import numpy as np
import math

img = cv2.imread('./img/homework1.bmp',cv2.IMREAD_COLOR)

reverse_img = 255 - img


def logTransform(c, img):
    h, w, d = img.shape[0], img.shape[1], img.shape[2]
    new_img = np.zeros((h, w, d))
    for i in range(h):
        for j in range(w):
            for k in range(d):
                new_img[i, j, k] = c * (math.log(1.0 + img[i, j, k]))
    cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)
    new_img = cv2.convertScaleAbs(new_img)
    return new_img


def gammaTranform(c, gamma, image):
    h, w, d = image.shape[0], image.shape[1], image.shape[2]
    new_img = np.zeros((h, w, d), dtype=np.float32)
    for i in range(h):
        for j in range(w):
            new_img[i, j, 0] = c * math.pow(image[i, j, 0], gamma)
            new_img[i, j, 1] = c * math.pow(image[i, j, 1], gamma)
            new_img[i, j, 2] = c * math.pow(image[i, j, 2], gamma)
    cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)
    new_img = cv2.convertScaleAbs(new_img)

    return new_img


log_img = logTransform(0.2, img)
gamma_img = gammaTranform(1, 2.5, img)
cv2.imshow('srcimg', img)
cv2.imshow('reverse_img', reverse_img)
cv2.imshow('log_img', log_img)
cv2.imshow('gamma_img', gamma_img)
cv2.waitKey(0)
