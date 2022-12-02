import socket
from threading import Thread


def envoi(socket):
    msg = ''
    while msg != 'disconnect' and msg != 'reset' and msg != 'kill':
        msg = input("->")
        msg = msg.encode()
        socket.send(msg)


def reception(socket):
    msg = ''
    while msg != 'kill' and msg != 'reset' and msg != 'disconnect':
        # reçoit les message envoyé par le client
        data = socket.recv(1024)
        data = data.decode()
        print(data)
        if not data:
            print("connexion closed")
            break
    socket.close()


def client():

    host = 'localhost'
    port = 5102
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
    send = Thread(target=envoi, args=[client])
    recep = Thread(target=reception, args=[client])
    send.start()
    recep.start()
