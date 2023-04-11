
import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cv2.namedWindow('Trackbar')
cv2.moveWindow('Trackbar', 1320, 0)

cv2.createTrackbar('hueLower', 'Trackbar', 50, 179, nothing)
cv2.createTrackbar('hueHigher', 'Trackbar', 100, 179, nothing)

cv2.createTrackbar('hueLower1', 'Trackbar', 50, 179, nothing)
cv2.createTrackbar('hueHigher1', 'Trackbar', 100, 179, nothing)

cv2.createTrackbar('setLower', 'Trackbar', 100, 255, nothing)
cv2.createTrackbar('setHigher', 'Trackbar', 255, 255, nothing)
cv2.createTrackbar('valLow', 'Trackbar', 100, 255, nothing)
cv2.createTrackbar('valHigh', 'Trackbar', 255, 255, nothing)

while True:
    ret, frame = cap.read()
    #frame=cv2.imread('images/image.png')
    
    smallwindow = cv2.resize(frame, (400, 400))
    cv2.imshow("small", smallwindow)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hueLower = cv2.getTrackbarPos('hueLower', 'Trackbar')
    hueHigher = cv2.getTrackbarPos('hueHigher', 'Trackbar')
    hueLower1 = cv2.getTrackbarPos('hueLower1', 'Trackbar')
    hueHigher1 = cv2.getTrackbarPos('hueHigher1', 'Trackbar')

    satL = cv2.getTrackbarPos('setLower', 'Trackbar')
    satH = cv2.getTrackbarPos('setHigher', 'Trackbar')

    valL = cv2.getTrackbarPos('valLow', 'Trackbar')
    valH = cv2.getTrackbarPos('valHigh', 'Trackbar')

    l_b = np.array([hueLower, satL, valL])
    u_b = np.array([hueHigher, satH, valH])
    l_b1 = np.array([hueLower1, satL, valL])
    u_b1 = np.array([hueHigher1, satH, valH])

    mask1 = cv2.inRange(hsv, l_b1, u_b1)
    mask2 = cv2.inRange(hsv, l_b, u_b)
    fmcomp = cv2.add(mask1, mask2)
    fmsamll = cv2.resize(fmcomp, (600, 600))
    cv2.imshow('fmcomp', fmsamll)

    fg = cv2.bitwise_and(frame, frame, mask=fmcomp)
    fgs = cv2.resize(fg, (600, 600))
    cv2.imshow('fgs', fgs)

    mask = cv2.inRange(hsv, l_b, u_b)
    smallmask = cv2.resize(mask, (400, 400))
    cv2.imshow('mask', smallmask)

    fgmask = cv2.bitwise_and(frame, frame, mask=mask)
    smallfgmask = cv2.resize(fgmask, (400, 400))
    cv2.imshow('fgmask', smallfgmask)

    bgmask = cv2.bitwise_not(mask)
    smallbgmask = cv2.resize(bgmask, (400, 400))
   

    cv2.imshow('bgmask', smallbgmask)

    fask = cv2.cvtColor(bgmask, cv2.COLOR_GRAY2BGR)
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    final = cv2.bitwise_or(mask_bgr, fask)
    finalwindow = cv2.resize(final, (400, 400))
    cv2.imshow('finall', finalwindow)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
