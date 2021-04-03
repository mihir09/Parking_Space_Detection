import cv2

cap = cv2.VideoCapture("videos/np_testing.mp4")
c = 1
frameRate = 150  # Frame number interception interval (one frame is intercepted every 100 frames)

while (True):
    ret, frame = cap.read()
    if ret:
        if (c % frameRate == 0):
            print("Start to capture video:" + str(c) + "frame")
            # Here you can do some operations: display the captured frame picture, save the captured frame to the local
            cv2.imwrite("capture_images/" + str(c) + '.jpg', frame)  # here is to save the captured image locally
        c += 1
        cv2.waitKey(0)
    else:
        print("All frames have been saved")
        break
