import socket
from threading import Thread


def envoi(client):
    msg = ''
    while msg != 'disconnect' and msg != 'reset' and msg != 'kill':
        msg = input("->")
        msg = msg.encode()
        client.send(msg)


def reception(client):
    msg = ''
    while msg != 'kill' and msg != 'reset' and msg != 'disconnect':
        # reçoit les message envoyé par le client
        data = client.recv(1024)
        data = data.decode()
        print(data)
        if not data:
            print("connexion closed")
            break
    client.close()


def serveur():
    host = ""
    port = 5102
    msg = ''

    while msg != 'kill':

        # crée le socket, peut réutiliser la même adresse et port, associe l'host et le port puis écoute le port
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)

        while msg != 'kill' and msg != 'reset':

            print("en attente d'un client ...")

            # accepte la connexion du client
            conn_client, client_address = server_socket.accept()

            # précise à quel adresse le client est connecté et sur quel port
            print("connected to :", client_address[0], "on the port", client_address[1])

        server_socket.close()


if __name__ == '__main__':
    serveur()
    send = Thread(target=envoi, args=[client])
    recep = Thread(target=reception, args=[client])
