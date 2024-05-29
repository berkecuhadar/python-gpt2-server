import socket
import generateGPT2 as gpt2
isSelected = False
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((HOST,PORT))
    server.listen()
    print("Server is running...")

    conn, addr = server.accept()
    with conn:
        print("Client Address is:",addr)
        isConnected = True
        while isConnected:
            data = conn.recv(1024)
            if not data:
                break
            input = data.decode(encoding="utf-8")
            print(f"Received: {input}")
            output = str(gpt2.generate(input))
            conn.sendall(output.encode(encoding="utf-8"))
            print(f"Sent: {output}")

    
            
