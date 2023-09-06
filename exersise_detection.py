import cv2
import numpy as np

# Create a VideoCapture object to capture video from your camera (0 for default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the red color range in HSV
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 30])

    # Create a mask to detect red color in the frame
    mask = cv2.inRange(hsv_frame, lower_black, upper_black)

    # Apply the mask to the original frame
    result = cv2.bitwise_or(frame, frame, mask=mask)

    # Display the original frame, mask, and the result
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Red Mask', mask)
    cv2.imshow('Result', result)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
