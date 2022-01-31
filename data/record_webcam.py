from tkinter import W
import cv2
import time

class WebcamImage:
    def __init__(self):
        pass

    def record_image(self):
        
        camera = cv2.VideoCapture(0)
        time.sleep(2)
        ret,frame = camera.read() # returns a single frame as reference
        self.image = frame
        camera.release()

    def get_grayscale(self):

        self.grayscale = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def downsample(self, image, scale):
        
        width = int(image.shape[1] * scale )
        height = int(image.shape[0] * scale)
        dim = (width, height)

        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        
        return resized



