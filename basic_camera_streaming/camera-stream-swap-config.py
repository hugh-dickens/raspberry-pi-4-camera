#!/usr/bin/python3

# This script has been written to test out the picamera capabilities in terms of fps.

from picamera2 import Picamera2
import time

def main():

    picam2 = Picamera2()
    preview_config = picam2.create_preview_configuration()
    capture_config = picam2.create_still_configuration()
    picam2.configure(preview_config)
    picam2.start(show_preview=True)
    time.sleep(1)
    picam2.switch_mode(capture_config)
    array = picam2.capture_array("main")
    picam2.switch_mode(preview_config)


if __name__ == '__main__':
    main()