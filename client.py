import socket
import platform


def client():

    host = 'localhost'
    port = 5182
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    client_socket.connect((host, port))
    msg = input("->")

    while msg != 'kill' and msg != 'disconnect' and msg != 'reset':
        msg = input("->")
        client_socket.send(msg.encode())
        data = client_socket.recv(1024)
        print('received from server: ' + (data.decode()))

    client_socket.close()


if __name__ == '__main__':
    client()