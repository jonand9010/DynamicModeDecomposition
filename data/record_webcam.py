import cv2
import time

camera = cv2.VideoCapture(0)
time.sleep(1)
ret,reference_frame = camera.read() # returns a single frame as reference

cv2.imshow('Reference image',reference_frame) # display the captured image
cv2.waitKey(0)