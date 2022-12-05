import socket


def client():

    host = 'localhost'
    port = 5000
    client_socket = socket.socket()

    client_socket.connect((host, port))
    while True:
        message = input("->")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('received from server: ' + data)
        if data.lower() == "bye":
            client_socket.close()


if __name__ == '__main__':
    client()