import cv2
from camera_server.camera import Camera
from camera_server.frame_sender import FrameSender
import time

time.sleep(0.05)
camera = Camera(0, 240, 280)
sender = FrameSender("localhost", 9999)

try:
    while True:
        frame = camera.read()
        if frame is None:
            break

        cv2.imshow("Camera Client", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        sender.send(frame)

except KeyboardInterrupt:
    pass

camera.release()
sender.close()
cv2.destroyAllWindows()
