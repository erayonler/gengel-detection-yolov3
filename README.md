# gengel-detection-yolov3

<a href src="https://pjreddie.com/darknet/yolo/">YOLO</a> is well known and famous object detector. In this study we used YOLOv3 to detect cardoon on an image(video or even live video)

1. we prepared dataset consist of 80 images of cardoon which are taken from the field bys using free annotation tool <a href src="https://github.com/tzutalin/labelImg">LabelIMG</a>.
3. Trained a YOLOv3 model with that custom dataset on <a href="colab.research.google.com">GOOGLE COLAB</a> tool
4. Saved these trained weights to try on test video

<img src="gengel_dataset.png"></img>

and then we tested our trained model on a video file by using <a href src="opencv.org">OpenCV library</a>:

* reading input video
* loading YOLOv3 Network with pretrained weights
* Reading video frames in the loop
* getting blob from the frame
* implementing forward pass
* getting bounding boxes
* non-maximum supression
* drawing bounding boxes and adding text to that box
* writing processed frames to a new video file

<img src="gengel_detection_on_video.png"></img>

# Results
* avg accuracy reached to 0.08 (this is not very good, it is suggested to stop training below 0.0607)
* dataset is very limited (just 80 sample). need more data to increase accuracy
* we can tweak network parameters to have robust detector
* it takes ~9 hours of training
