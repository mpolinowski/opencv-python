import cv2
import numpy as np

# Image grayscale, blur and edge detection
img = cv2.imread('resources/shenzhen-subway.jpg')
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (9, 9), 0)
imgLowEdge = cv2.Canny(img, 100, 100)
imgHighEdge = cv2.Canny(img, 200, 300)
imgDilation = cv2.dilate(imgLowEdge, kernel, iterations=5)
imgEroded = cv2.erode(imgDilation, kernel, iterations=3)

cv2.imshow("Grayscale Image", imgGray)
cv2.imshow("Blurred Image", imgBlur)
cv2.imshow("Low Edge Threshold Image", imgLowEdge)
cv2.imshow("High Edge Threshold Image", imgHighEdge)
cv2.imshow("Increased Edge Thickness", imgDilation)
cv2.imshow("Decreased Edge Thickness", imgEroded)
cv2.waitKey(5000)