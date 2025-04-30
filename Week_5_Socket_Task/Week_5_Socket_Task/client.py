import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 12345))
client_socket.send("Hello from Client 👋".encode())
reply = client_socket.recv(1024).decode()
print(f"📨 Reply from server: {reply}")
client_socket.close()
