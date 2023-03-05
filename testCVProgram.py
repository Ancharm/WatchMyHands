from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.resolution = (1920,1080)
camera.annotate_background = Color('blue')
camera.framerate = 15
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
