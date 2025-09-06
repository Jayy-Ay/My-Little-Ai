import cv2 as cv

# Resizing
def resizeFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)     # shape[1] = width, shape[0] = height
    height = int(frame.shape[0] * scale)    # Converted float value to int
    dim = (width, height)

    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

# Reading Images
img = cv.imread('My-Little-Ai/data/photos/cat.jpg')  # Read the image from path
cv.imshow('cat', img)                                # Display the image in a window
cv.waitKey(0)                                        # Wait for key press to close window


# Reading Videos
capture = cv.VideoCapture('My-Little-Ai/data/videos/dog.mp4')   # -215:Assertion failed = Can't find frame(s) in path
while True:                                                     # Reading frame-by-frame
    isTrue, frame = capture.read()                              # Read the video frame by frame
    resized_frame = resizeFrame(frame, 0.2)                    # Resize based on scale
    cv.imshow('Video', resized_frame)                           # Show frame

    if cv.waitKey(20) & 0xFF==ord('d'):                         # If end of video or 'd' is pressed, break
        break

capture.release                                                 # Release the pointer
cv.destroyAllWindows()                                          # Clear/Destroy all windows

