# The goal here is to not perform the processing on the same thread as the camera. 
# This should prevent it dropping some frames. For example you could capture the frame
# and print it somewhere every 5 seconds as opposed to constantly streaming the video.

from picamera2 import Picamera2

def main():
    picam2 = Picamera2()
    picam2.start()
    request = picam2.capture_request()
    request.save("main", "image.jpg")
    print(request.get_metadata()) # this is the metadata for this image
    request.release()

if __name__ == '__main__':
    main()    