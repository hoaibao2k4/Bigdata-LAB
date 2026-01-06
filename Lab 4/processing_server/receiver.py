import socket
def start_server(host="localhost", port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print("Waiting for camera connection...")
    conn, addr = server.accept()
    print("Connected from", addr)
    return conn
