import cv2
import os

OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_frame(frame, frame_id):
    path = f"{OUTPUT_DIR}/frame_{frame_id}.jpg"
    cv2.imwrite(path, frame)
