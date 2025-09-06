import cv2 as cv

# Changing Resolution (Only work for live videos)
def changeRes(width, height):
    capture.set(3, width)       # 3 = width
    capture.set(4, height)      # 4 = height


# Reading Webcam [TAKES A WHILE TO LOAD]
capture = cv.VideoCapture(0)            # 0 = default web camera
changeRes(640, 480)                     # Set res before starting (ex. 640x480)

while True:                             # Read frame-by-frame
    isTrue, frame = capture.read()      
    cv.imshow('Cam', frame)             # Show frame

    if cv.waitKey(20) & 0xFF==ord('d'): # If end or press 'd', break
        break
capture.release()
cv.destroyAllWindows()