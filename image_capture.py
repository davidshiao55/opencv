from picamera2 import Picamera2, MappedArray
import cv2

picam2 = Picamera2()

picam2.start()


while True:
    im = picam2.capture_array()
    cv2.imshow("Camera", im)
    cv2.waitKey(1)
