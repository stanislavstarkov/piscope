from picamera import PiCamera
from time import sleep, localtime, strftime
from fractions import Fraction
from picamera.array import PiRGBArray
import cv2 as cv


class Camera:
    def __init__(self, frame_width=4056, frame_height=3040,
                 iso=1600, exposure=1500000):
        self.cam = PiCamera(
            resolution=(frame_width, frame_height),
            framerate=Fraction(1, 6),
            sensor_mode=3)
        self.cam.iso = iso
        sleep(30)
        self.cam.exposure_mode = 'night'
        self.cam.awb_mode = 'off'
        self.cam.awb_gains = 7.0
        self.cam.shutter_speed = exposure

    def take_pic(self):
        rawCapture = PiRGBArray(self.cam)
        # Finally, capture an image with a 6s exposure. Due
        # to mode switching on the still port, this will take
        # longer than 6 seconds
        # cam.capture('./photos/image.data', 'yuv')
        self.cam.capture(rawCapture, format="bgr")
        image = rawCapture.array
        return image


if __name__ == '__main__':
    camera = Camera()
    time = strftime("%H %M", localtime())
    for i in range(1, 2000):
        image = camera.take_pic()
        cv.imwrite(f'./photos/pic-{time}-sec{i}.jpg', image)
