#!/usr/bin/python3

# This script has been written to test out the picamera capabilities in terms of fps.

from picamera2 import Picamera2, Preview

def main():

    picam2 = Picamera2()
    picam2.start_preview(Preview.QTGL)
    config = picam2.create_video_configuration(controls={"FrameDurationLimits": (8300, 40000)}) # 120-25 fps
    picam2.configure(config)

    picam2.start()

    while True:
        frameRate = 1 / (picam2.capture_metadata()["FrameDuration"]) * 1000000 # convert from micro to base units
        print('Frame rate =', frameRate)

if __name__ == '__main__':
    main()