import cv2
import numpy as np

# Color Detection
from time import time, sleep
path = 'resources/songhua-river.jpg'
# Create a hue slider that helps us
# find the correct colour to select
def empty(a):
    pass
cv2.namedWindow('TrackBars') # Create the Window
cv2.resizeWindow('TrackBars', 640, 240) # Give it a size
cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty) # Add a slider for min Hue 0-179
cv2.createTrackbar('Hue Max', 'TrackBars', 179, 179, empty) # Add a slider for max Hue 179
cv2.createTrackbar('Sat Min', 'TrackBars', 107, 255, empty) # Add a slider for min Saturation 0-255
cv2.createTrackbar('Sat Max', 'TrackBars', 255, 255, empty) # Add a slider for max Saturation 255
cv2.createTrackbar('Val Min', 'TrackBars', 180, 255, empty) # Add a slider for min Value 0-255
cv2.createTrackbar('Val Max', 'TrackBars', 255, 255, empty) # Add a slider for max Value 255

while True: # Run loop to continuously update from trackbars
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBars')

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper) # Create a selection mask based on thresholds
    imgSelection = cv2.bitwise_and(img, img, mask=mask) # Apply layer mask to image

    imgHor = np.hstack((img, imgSelection))

    cv2.imshow('Original & Selection', imgHor)
    cv2.imshow('Mask', mask)
    cv2.waitKey(5000)