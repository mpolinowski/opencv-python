import cv2
import numpy as np

def getContours(img): # Retrieve contours from detected shapes
    contours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt) # Get areas for all contours
        # print(area) # Print calculated areas
        if area > 400: # Set threshold to exclude noise
            cv2.drawContours(imgBlack, cnt, -1, (255, 0, 0), 1)  # Draw those areas onto the image
            peri = cv2.arcLength(cnt, True) # Get contour perimeter
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) # Approximate polygonal curve
            # print(len(approx)) # Print the number corner points of each contour
            objCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx) # Get coordinates from curve

            if objCorners == 3:
                objectType = "Triangle" # Define object based on corner count

            elif objCorners == 4:
                aspectRatio = w/float(h) # Check if w/h=1 => square
                if 0.95 < aspectRatio < 1.05: objectType = "Square"
                else: objectType = "Rectangle"

            elif objCorners == 5:
                objectType = "Pentagon"

            elif objCorners == 6:
                objectType = "Hexagon"

            elif objCorners == 7:
                objectType = "Heptagon"

            elif objCorners > 7:
                objectType = "Circle?"

            else: objectType = "Unknown"

            cv2.rectangle(imgBlack, (x, y), (x+w, y+h), (0, 0, 255, 1)) # Print bounding box
            cv2.putText(imgBlack, objectType,
                        (x+(w//2)-10, y+(h//2)-10), # Put objectType in Center
                        cv2.QT_FONT_NORMAL, 0.5, (255, 255, 0), 1)

# Contours and Shape detection
path = 'resources/objects_dark.png'
# path = 'resources/objects_light.png'
img = cv2.imread(path)
imgBlack = np.zeros_like(img)
# imgWhite = np.ones_like(img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgEdge = cv2.Canny(imgBlur, 50, 50)

getContours(imgEdge)

cv2.imshow("Shape", imgBlack)
cv2.imshow("Original", img)
cv2.waitKey(15000)