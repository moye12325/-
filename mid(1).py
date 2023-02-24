import cv2
import numpy as np
from PIL import Image

def resize1(imgpath):

    img = np.array(Image.open(imgpath))
    img = img[0:160, 0:652]
    #
    # # img_pad = np.pad(img, ((246, 246), (0, 0)), 'constant', constant_values=0)
    # #
    # # return Image.fromarray(img_pad.astype(np.uint8))
    width = len(img[1])
    p=0
    return img,width,p

def resize2(imgpath):

    img = np.array(Image.open(imgpath))
    img = img[0:160, 500:1800]

    # img_pad = np.pad(img, ((246, 246), (0, 0)), 'constant', constant_values=0)
    #
    # return Image.fromarray(img_pad.astype(np.uint8))
    width=len(img[1])
    p=500
    return img,width,p

def resize3(imgpath):

    img = np.array(Image.open(imgpath))
    img = img[0:160, 1000:2608]

    # img_pad = np.pad(img, ((246, 246), (0, 0)), 'constant', constant_values=0)
    #
    # return Image.fromarray(img_pad.astype(np.uint8))
    width=len(img[1])
    p=1000
    return img,width,p

def resize4(imgpath):

    img = np.array(Image.open(imgpath))
    img = img[0:160, 1000:2608]

    # img_pad = np.pad(img, ((246, 246), (0, 0)), 'constant', constant_values=0)
    #
    # return Image.fromarray(img_pad.astype(np.uint8))
    width=len(img[1])
    p=1000
    return img,width,p
def resize5(imgpath):

    img = np.array(Image.open(imgpath))
    img = img[0:160, 0:1000]

    # img_pad = np.pad(img, ((246, 246), (0, 0)), 'constant', constant_values=0)
    #
    # return Image.fromarray(img_pad.astype(np.uint8))
    width=len(img[1])
    p
    return img,width,p
path =r"C:\Users\86138\Downloads\Hough-Rectangle-and-Circle-Detection-main\python\1.bmp"
img =cv2.imread(path,cv2.COLOR_BGR2GRAY)
# print(img.shape)
cv2.imshow("nature",img)
cropped_image_nature, width, p= resize1(path)
# cropped_image_nature = np.ascontiguousarray(cropped_image_nature)
#2608*160
cv2.imshow("img",cropped_image_nature)


#增加亮度
res = cv2.convertScaleAbs(cropped_image_nature, alpha=1.5, beta=0)
cv2.imshow("light",res)

#局部直方图均衡化
clahe = cv2.createCLAHE (clipLimit =9.5 , tileGridSize=(4, 4))  #对图像进行分割 4*4
img3 = clahe.apply(res)
cv2.imshow("clahe",img3)

# #高斯平滑
#
# gaussianBlur =cv2.GaussianBlur(img,(3,3),1,0)


for i in range(160):
    for j in range(width):
        if img3[i][j] < 210:
            img3[i][j]=0
#高斯模糊
gaussianBlur =cv2.GaussianBlur(img3,(7,7),1,0)

#降噪
ret,thresh =cv2.threshold(gaussianBlur,127,255,cv2.THRESH_BINARY)

# #Sobel边缘算子
# sobelxy = cv2.Sobel(src=img3, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# sobelx = cv2.Sobel(src=img3, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
# sobely = cv2.Sobel(src=img3, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis

#
for i in range(160):
    for j in range(652):
        if res[i][j] < 210:
            res[i][j]=0

cv2.imshow("res1",res)

cv2.imshow("img3",img3)
cv2.imshow("gaussianBlur",gaussianBlur)
cv2.imshow("thresh",thresh)

#Canny边缘检测
Canny = cv2.Canny(thresh, 64, 128)
cv2.imshow("Canny",Canny)

# 裁剪图像
cut = Canny[50:140, 0:width]
cv2.imshow("cut",cut)

#获得轮廓
contours, hierarchy = cv2.findContours(cut, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# #35 1 2
# #31 1 2
# #12 1 2
# contour=[]
# k=0
# for contour in contours:
#
#     x,y,w,h = cv2.boundingRect(contour)
#     rectangle = cv2.rectangle(img,(x,y),(x+w,y+h),0)
#     cv2.imshow("rectangle",rectangle)
for contour in contours:
        for con in contour:
            for cc in con:
                cc[1] = cc[1]+50
                cc[0] = cc[0]+p
              

# cv2.drawContours(img, bb, -1, (0, 255, 0), 3)
# for i in range(len(contours)):
#     if contours[i].shape in((39,1,2),(36,1,2) ,(14,1,2),):
#         contour.append(contours[i])
# # #
# #
# 绘制轮廓
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow("draw", img)
# cv2.imshow("sobelx",sobelx)
# cv2.imshow("sobely",sobely)
# cv2.imshow("sobelxy",sobelxy)
# cv2.imshow("Canny",Canny)

# cv2.imshow("medianBlur",medianBlur)
# cv2.imshow("gaussianBlur",gaussianBlur)
# cv2.imshow("img3",img3)
# cv2.imshow("res",res)
# cv2.imshow("sobelx",sobelx)
# cv2.imshow("sobely",sobely)
# cv2.imshow("Laplacian",sobelxy)

cv2.waitKey(0)

