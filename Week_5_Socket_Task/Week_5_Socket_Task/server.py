import socket

server_socket = socket.socket()
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("✅ Server is listening on port 12345...")

conn, addr = server_socket.accept()
print(f"📡 Connected with {addr}")
message = conn.recv(1024).decode()
print(f"📩 Message from client: {message}")
conn.send("✅ Server received your message!".encode())
conn.close()
