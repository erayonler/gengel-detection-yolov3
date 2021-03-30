# import needed libraries
import numpy as np
import cv2
import time

# read video file
video = cv2.VideoCapture("IMG_2424.MOV")

writer = None
h, w = None, None



# create a YOLO v3 network with weights which is trained on custom dataset
network = cv2.dnn.readNetFromDarknet("yolov3_testing.cfg", "yolov3_training_final.weights")

layers_names_all = network.getLayerNames()
layers_names_output = [layers_names_all[i[0]-1] for i in network.getUnconnectedOutLayers()]


#setting minimum probability to eliminate weak predictions
probability_minimum = 0.5

#setting threshold for filtering weak bounding boxes
threshold = 0.3

color = [255, 0, 0]

# read video frame by frame, 
# forwardpass this frame in to network, 
# get results and draw founded object on frame,
# save as a new video
while True:
    ret, frame = video.read()

    if not ret:
        break

    if w is None or h is None:
        h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

    network.setInput(blob)
    output_from_network = network.forward(layers_names_output)

    bounding_boxes = []
    confidences = []
    class_numbers = []

    for result in output_from_network:
        for detected_objects in result:
            scores = detected_objects[5:]
            class_current = np.argmax(scores)
            confidence_current = scores[class_current]

            if confidence_current > probability_minimum:
                box_current = detected_objects[0:4] * np.array([w, h, w, h])

                x_center, y_center, box_width, box_height = box_current
                x_min = int(x_center - (box_width/2))
                y_min = int(y_center- (box_height/2))

                bounding_boxes.append([x_min, y_min, int(box_width), int(box_height)])
                confidences.append(float(confidence_current))
                class_numbers.append(class_current)

    
    results = cv2.dnn.NMSBoxes(bounding_boxes, confidences, probability_minimum, threshold)

    if len(results) > 0:
        for i in results.flatten():
            x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
            box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]

            cv2.rectangle(frame, (x_min, y_min), 
                        (x_min + box_width, y_min+box_height),
                        color, 5)
            text_box = "gengel"

            cv2.putText(frame, text_box, (x_min, y_min-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 3, color, 5)
    

    if writer is None:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        writer = cv2.VideoWriter("output02.mp4", fourcc, 30, (frame.shape[1], frame.shape[0]), True)
    
    writer.write(frame)

video.release()
writer.release()







