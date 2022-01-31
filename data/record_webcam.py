from tkinter import W
import cv2
import time

class WebcamImage:
    def __init__(self):
        pass

    def record_image(self):
        self.camera = cv2.VideoCapture(0)
        time.sleep(2)
        ret,frame = self.camera.read() # returns a single frame as reference
        self.image = frame

    def get_grayscale(self):
        self.grayscale = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


webcam = WebcamImage()
webcam.record_image()
webcam.get_grayscale()

import matplotlib.pyplot as plt
plt.imshow(webcam.grayscale)
plt.show()
