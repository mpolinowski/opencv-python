import cv2

# License Plate Detection
lpCascade = cv2.CascadeClassifier('resources/haarcascade_russian_plate_number.xml')
imagePath = 'resources/HK_Taxi.jpg'
img = cv2.imread(imagePath)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Create grayscale image

plates = lpCascade.detectMultiScale(imgGray, 1.1, 4) # Detect all faces in image

for (x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("License Plate Detection", img)
cv2.waitKey(5000)