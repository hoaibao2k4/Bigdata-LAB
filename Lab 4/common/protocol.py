import struct
import pickle

HEADER_SIZE = 8

def pack_frame(frame, frame_id):
    payload = {
        "frame_id": frame_id,
        "frame": frame
    }
    data = pickle.dumps(payload)
    header = struct.pack("Q", len(data))
    return header + data

def unpack_frame(conn):
    header = conn.recv(HEADER_SIZE)
    if not header:
        return None

    size = struct.unpack("Q", header)[0]
    data = b""
    while len(data) < size:
        data += conn.recv(size - len(data))

    return pickle.loads(data)
