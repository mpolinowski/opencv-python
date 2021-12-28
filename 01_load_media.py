import cv2

# Load and Display an Image 5s
img = cv2.imread('resources/shenzhen-subway.jpg')
cv2.imshow("Output", img)
cv2.waitKey(5000)

###############################################################

# Capture a video to variable and display until `q` key is pressed
cap = cv2.VideoCapture('resources/sz-office.mp4')
try:
    while True:
        success, vid = cap.read()
        cv2.imshow('Video', vid)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except:
    print("Reached end of video file")

# Capture video from your webcam
cap = cv2.VideoCapture(0) #Capture video source zero `/dev/video0`
cap.set(16, 1920)
cap.set(9, 1080)

while True:
    success, vid = cap.read()
    cv2.imshow('Video', vid)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break