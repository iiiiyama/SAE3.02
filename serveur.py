import socket
import threading


def thread(conn_client):
    while True:
        data = conn_client.recv(1024)
        if not data:
            print("bye")
            break
        conn_client.send(data)
    conn_client.close()


def serveur():
    host = ""
    port = 5182
    msg = ''
    t = []

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

            # précise à quel adresse le cllient est connecté et sur quel port
            print("connected to :", client_address[0], "on the port", client_address[1])
            t.append(threading.Thread(target=thread(conn_client)))

            while msg != 'kill' and msg != 'reset' and msg != 'disconnect':
                # reçoit les message envoyé par le client
                msg = conn_client.recv(1024).decode()

            conn_client.close()
        server_socket.close()


if __name__ == '__main__':
    serveur()
