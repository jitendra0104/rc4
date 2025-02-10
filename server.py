import socket
import rc4

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print("Data before decryption: " + str(data))
        data = rc4.decryptData(data)
        print("Client(after decryption of the data): " + str(data))
        data = input('enter the message: ')
        conn.send(data.encode())
    conn.close()
server_program()
