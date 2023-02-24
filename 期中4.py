import cv2
image = cv2.imread("img/homework1.bmp", 0)
# image = cv2.imread('1.jpg')
original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    if area > 50:
        cv2.drawContours(original, [c], -1, (36, 255, 12), -1)

cv2.imshow('thresh', thresh)
cv2.imshow('original', original)
cv2.imwrite('original.png', original)
cv2.waitKey()