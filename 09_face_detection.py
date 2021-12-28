import cv2

# Face Detection
faceCascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
imagePath = 'resources/hongkong-metro.png'
img = cv2.imread(imagePath)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Create grayscale image

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4) # Detect all faces in image

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("Face Detection", img)
cv2.waitKey(5000)