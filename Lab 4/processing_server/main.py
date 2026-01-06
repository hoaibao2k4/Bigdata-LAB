import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\DELL\AppData\Local\Programs\Python\Python310\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\DELL\AppData\Local\Programs\Python\Python310\python.exe"
from processing_server.receiver import start_server
from common.protocol import unpack_frame
from processing_server.spark_processor import process_frames
conn = start_server()
buffer = []

try:
    while True:
        packet = unpack_frame(conn)
        if packet is None:
            break

        buffer.append(packet)

        if len(buffer) >= 10:  # micro-batch
            process_frames(buffer)
            buffer.clear()

except KeyboardInterrupt:
    print("Processing stopped")

conn.close()
