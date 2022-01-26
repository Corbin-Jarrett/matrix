import numpy as np
import cv2

def getMask(frame, lower_bound, upper_bound, img):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #getting hsv image from BGR
    mask = cv2.inRange(hsv, lower_bound, upper_bound) #Removing all colour except between lower and upper bound
    return mask

cap = cv2.VideoCapture(0)
img = cv2.imread('new_matrix.jpg', 1)
lower_black = np.array([0,0,0])
upper_black = np.array([180,255,90])
#upper_black = np.array([180,255,120])
white = (255,255,255)
green = (127,230,130)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    # Making everything black except dark objects
    mask = getMask(frame, lower_black, upper_black, img)

    #Making dark objects green, and black background matrix
    frame[mask > 0] = green
    frame[mask == 0] = img[mask == 0]

    # To make wireframe
    # edges = cv2.Canny(mask, 200, 400)
    # frame[edges == 0] = img[edges == 0]

    cv2.imshow('Video Capture', frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()