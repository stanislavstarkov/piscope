import cv2 as cv
from time import sleep

def take_pic():
    FRAME_WIDTH = 1920 #4056
    FRAME_HEIGHT = 1080 #3040
    EXPOSURE = 100000
    WORKDIR = './photos/'
    IMAGE_NAME = f'{WORKDIR}test.jpg'
    cap = cv.VideoCapture(-1)
    print(f'isOpened: {cap.isOpened()}')
    # PROP_FRAME_WIDTH = cv.CAP_PROP_FRAME_WIDTH
    # PROP_FRAME_HEIGHT = cv.CAP_PROP_FRAME_HEIGHT
    # cap.set(cv.CAP_PROP_FORMAT, cv.CV_8UC3)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    # cap.set(cv.CAP_PROP_EXPOSURE, EXPOSURE)
    # cap.set(PROP_FRAME_WIDTH, 4056)
    # cap.set(PROP_FRAME_HEIGHT, 3040)
    ret_code, image = cap.read()
    # print(f'raw image:{image}')
    print(f'Return code: {ret_code}')
    # ret, jpeg = cv.imencode('.jpg', image)
    cap.release()
    # cv.imshow('frame', image)
    # k = cv.waitKey(0)
    cv.imwrite(IMAGE_NAME, image)


if __name__ == '__main__':
    take_pic()
