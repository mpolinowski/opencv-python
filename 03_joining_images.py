import cv2
import numpy as np

# Joining Images in Vertical or Horizontal Stacks
img = cv2.imread('resources/shenzhen-subway.jpg')
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (9, 9), 0)
imgLowEdge = cv2.Canny(img, 100, 100)
imgHighEdge = cv2.Canny(img, 200, 300)
imgDilation = cv2.dilate(imgLowEdge, kernel, iterations=5)
imgEroded = cv2.erode(imgDilation, kernel, iterations=3)

imgVer = np.vstack(( imgGray, imgBlur))
imgHor = np.hstack((imgLowEdge, imgHighEdge, imgDilation, imgEroded))

cv2.imshow("Posterized Image", imgHor)
cv2.imshow("Grayscale Image", imgVer)
cv2.waitKey(5000)