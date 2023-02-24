import cv2 as cv
import cv2
import numpy as np
import time
import torch


def dilation_demo(image):
    #src = cv.imread("C:\mo\save2022.jpg")
    #src = image
    #src = image[:, :, 0]
    kernel = np.ones((3, 3), np.uint8)
    dilation = cv.dilate(image, kernel, iterations=3)
    cv.imshow("dilation", dilation)
    cv.imwrite(r"C:\mo\image\3_2.jpg", dilation)
    return dilation

def findcontour(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 图像灰度化
    #gray = img
    ret, binary = cv.threshold(gray,130, 235, cv.THRESH_BINARY)  # 图像二值化
    contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 查找物体轮廓
    #print(contours)
    return contours, hierarchy, binary

def contrast_img(img1, c, b):  # 亮度就是每个像素所有通道都加上b
    rows, cols, channels = img1.shape

    # 新建全零(黑色)图片数组:np.zeros(img1.shape, dtype=uint8)
    blank = np.zeros([rows, cols, channels], img1.dtype)
    dst = cv2.addWeighted(img1, c, blank, 1-c, b)
    cv2.imshow('original_img', img)
    cv2.imshow("contrast_img", dst)
    cv2.imwrite(r"C:\mo\image\4_2.jpg", dst)
    return dst

if __name__ == '__main__':


    img = cv2.imread("img/homework1.bmp", 0)  # 直接读为灰度图像
    #img = contrast_img(img, 1.8, 3.5)
    img = cv2.GaussianBlur(img, (7, 7), 0)
    #ret, img = cv2.threshold(gaussian, 127, 255, cv2.THRESH_BINARY)
    r2 = cv2.Canny(img,100,130)
    contours, hierarchy = cv2.findContours(r2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # 检测图像中出现的所有轮廓
    cv2.drawContours(img, contours, -1, (0, 0, 255), 4)  # 在原图中绘制轮廓
    # cv2.imwrite('./result/'+'Canny'+name,img)                #保存边缘图像

    cv2.imshow("ontours", img)

    cv.imwrite(r"C:\mo\image\1_2.jpg", img)
    #cv.imshow('Canny Edges', img)

    # img[img > 120] + 80

    #cv.imshow("my_img", img)
    #print(img.shape)
    #cv.waitKey(0)
    # kernel = np.ones((4, 4), np.uint8)
    # dilation = cv.dilate(img, kernel, iterations=4)
    # cv.imshow("my_img1111", img)

    src = dilation_demo(img)

    pt1 = (0,0)
    pt2 = (src.shape[1],src.shape[0])
    cv.rectangle(src,pt1,pt2,(0,0,255), 12)#红
    cv.imshow("123", src)
    cv.imwrite(r"C:\mo\image\123_2.jpg", src)
    #src = dilation_demo(src)
    # kernel = np.ones((3, 3), np.uint8)
    # src = cv.dilate(src, kernel, iterations=3)


    contours, hierarchy, my_threshold = findcontour(src)

    #print(contours[0])
    #cnt = contours[0]
    cv.imshow("my_threshold", my_threshold)
    nums = len(contours)
    for i in range(nums):
        cnt = contours[i]
    #M = cv.moments(cnt)
    #print(M)
        area = cv.contourArea(cnt)
        print(area)
    #src2 = cv.drawContours(src, contours, -1, (0, 0, 255), 1)  # 绘制所有轮廓,最后一个参数是修改轮廓的粗细
    img = cv2.drawContours(src, contours, -1, (0, 0, 255), 3)
    cv.imshow("drawContours", img)
    #cv.imshow("contour", my_threshold)
    cv.imwrite(r"C:\mo\image\2_2.jpg",img)
    cv.waitKey()


'''
    dilation_demo(src)

    cv.waitKey(0)

    nums = len(contours)
    #print(nums)
    color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    contourssplit = []'''
'''
    for i in range(nums):

        temp = np.zeros(src.shape, np.uint8)
        contourssplit.append(temp)
        contourssplit[i] = cv.drawContours(contourssplit[i], contours, i, color[i], 2)
        a = cv.moments(contours[i])

        #print("轮廓" + str(i) + "的面积:%d" % cv.moments(contours[i])['m00'])'''