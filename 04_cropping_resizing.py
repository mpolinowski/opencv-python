import cv2

# Image cropping and resizing
img = cv2.imread('resources/shenzhen-subway.jpg')
print(img.shape)
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

imgCropped = img[0:250, 624:824] # height,width

cv2.imshow("Resized Image", imgResize)
cv2.imshow("Image Crop", imgCropped)
cv2.waitKey(5000)