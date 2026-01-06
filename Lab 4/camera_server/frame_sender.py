import socket
from common.protocol import pack_frame

class FrameSender:
    def __init__(self, host="localhost", port=9999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.frame_id = 0

    def send(self, frame):
        packet = pack_frame(frame, self.frame_id)
        self.sock.sendall(packet)
        self.frame_id += 1

    def close(self):
        self.sock.close()
