import socket
import rc4

def client_program():
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("enter the message: ")
    message = rc4.encryptData(message)

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('server: ' + data)

        message = input("enter the message: ")

    client_socket.close()

client_program()
