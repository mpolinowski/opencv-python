import cv2
import numpy as np

# Adding Shapes and Text
img = np.zeros((512, 512, 3), np.uint8) # 512x512 black image background with 3 colour channels BGR
imageDim = str(img.shape[0]) + ' : ' + str(img.shape[1])

img[:] = 255, 0, 0 # Colour entire image blue
img[112:400, 112:400] = 0, 255, 0 # Add a green square in the middle

# cv2.line(img, (0, 0), (512, 512), (0, 0, 255), 3) # Draw a line from the top left to bottom right
# cv2.line(img, (512, 0), (0, 512), (0, 0, 255), 3) # Draw a line from the top right to bottom left
# Do the same thing - but for an image of unknown dimensions
# with img.shape[1]=width and img.shape[0]=height
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)
cv2.line(img, (img.shape[1], 0), (0, img.shape[0]), (0, 0, 255), 3)

cv2.rectangle(img, (3, 3), (509, 509), (0, 0, 255), 5) # Draw a rectangle around the image
cv2.rectangle(img, (212, 212), (300, 300), (0, 0, 255), cv2.FILLED) # Draw square in the middle

cv2.circle(img, (256, 256), 30, (0, 255, 255), cv2.FILLED) # Add a circle in the middle

cv2.putText(img, imageDim, (180, 70), cv2.QT_FONT_NORMAL, 1, (255, 255, 255), 1) # Print image dimensions

cv2.imshow("Image", img)
cv2.waitKey(5000)