import socket
import threading
import multiprocessing
import time
from _thread import *

no_print = threading.Lock()


def thread(conn_client):
    while True:
        data = conn_client.recv(1024)
        if not data:
            print("bye")
            no_print.release()
            break
        conn_client.send(data)
    conn_client.close()


def serveur():
    host = ""
    port = 5092
    msg = ''
    T = []

    while msg != 'kill':

        # crée le socket, peut réutiliser la même adresse et port, associe l'host et le port puis écoute le port
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)

        while msg != 'kill' and msg != 'reset':

            print("en attente d'un client ...")
            # accepte la connexion du client
            conn_client, client_address = server_socket.accept()

            while msg != 'disconnect':
                # reçoit les message envoyé par le client
                msg = conn_client.recv(1024).decode()
                # précise à quel adresse le cllient est connecté et sur quel port
                print("connected to :", client_address[0], "on the port", client_address[1])
                T.append(threading.Thread(target=conn_client))

            server_socket.close()
        server_socket.close()
    server_socket.close()


if __name__ == '__main__':
    serveur()