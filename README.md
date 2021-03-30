# gengel-detection-yolov3

YOLO is well known and famous object detector. In this study we used YOLOv3 to detect cardoon on an image(video or even live video)

1st step: we prepared dataset consist of 80 images of cardoon which are taken from the field.

we test our trained model on a video:
* reading input video
* loading YOLOv3 Network
* Reading video frames in the loop
* getting blob from the frame
* implementing forward pass
* getting bounding boxes
* non-maximum supression
* drawing bounding boxes and adding text to that box
* writing processed frames to an new video file
