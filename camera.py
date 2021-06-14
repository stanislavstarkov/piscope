from picamerax import PiCamera
from time import sleep, localtime, strftime
from fractions import Fraction
from picamera.array import PiRGBArray
import cv2 as cv


class Camera(PiCamera):
    def __init__(self, frame_width=4056, frame_height=3040,
                 iso=1600, exposure=1500000):
        super().__init__(resolution=(frame_width, frame_height),
                         framerate=Fraction(1, 6),
                         sensor_mode=3
                         )

        self.iso = iso
        sleep(30)

        self.exposure_mode = 'off'
        self.awb_mode = 'off'
        self.awb_gains = 6.0
        self.shutter_speed = exposure

    def take_pic(self, qnt):
        # rawCapture = PiRGBArray(self)
        # self.capture(rawCapture, format="bgr")
        # image = rawCapture.array
        for i in range(1, qnt+1):
            time = strftime("%H %M", localtime())
            self.capture(f'./photos/pic-{time}-sec{i}.jpg', 'jpeg')
        # return image
    
    def get_frame(self):
        self.capture()


if __name__ == '__main__':
    camera = Camera()
    time = strftime("%H %M", localtime())
    camera.take_pic(10)
        # cv.imwrite(f'./photos/pic-{time}-sec{i}.jpg', image)
