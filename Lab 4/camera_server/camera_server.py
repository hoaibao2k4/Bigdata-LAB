import socket
import cv2
import struct
import pickle

HOST = "localhost"
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((HOST, PORT))

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data = pickle.dumps(frame)
        message = struct.pack("Q", len(data)) + data
        server_socket.sendall(message)

except Exception as e:
    print("Camera error:", e)

cap.release()
server_socket.close()
