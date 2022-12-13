import socket


def client():

    host = 'localhost'
    port = 5008
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    client_socket.connect((host, port))
    msg = ''

    while msg != 'kill' and msg != 'disconnect' and msg != 'reset':
        send = input("->")
        client_socket.send(send.encode())
        data = client_socket.recv(1024)
        print('received from server: ' + (data.decode()))
        if data.lower() == "bye":

            client_socket.close()

    client_socket.close()
    client_socket.send('kill'.encode())


if __name__ == '__main__':
    client()
