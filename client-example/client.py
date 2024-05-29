import socket


HOST = '127.0.0.1'  
PORT = 65432        


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Connected.")
    while True:
        message = input("Type your message (press 'q' for exit): ")
        if message.lower() == 'q':
            break
        client_socket.sendall(message.encode(encoding="utf-8"))
        
        data = client_socket.recv(1024)
        print('Message from server:', data.decode(encoding="utf-8"))

print("Disconnected.")
