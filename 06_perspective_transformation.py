import cv2
import numpy as np

# Dewarp selections
img = cv2.imread('resources/sign.jpg')

width, height = 250, 350

pts1 = np.float32([[920, 227], [1216, 244], [873, 780], [1182, 809]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width,height))


cv2.imshow('Image', imgOutput)
cv2.waitKey(5000)