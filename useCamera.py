import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture(0)
#Set parameter of camera
# fps_set = 60
fps_now = 0
# resolution_x = round(800)
# resolution_y = round(resolution_x*9/16)
# cap.set(3,320)
# cap.set(4,240)
# cap.set(5,fps_set)
# cap.set(15,50)
# print('Current FPS is set to %d'%cap.get(5))

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    start_time = time.time()
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Show current FPS
    cv.putText(frame,'FPS:{:.2f}'.format(fps_now),(0,15),cv.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),1)
    cv.putText(frame,'%dx%d'%(cap.get(3),cap.get(4)),(0,30),cv.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),1)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
    fps_now = 1.0/(time.time()-start_time)
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()