import socket
import threading
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
    port = 5000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    while True:
        conn_client, client_address = server_socket.accept()
        no_print.acquire()
        print("connected to :", client_address[0], "on the port", client_address[1])
        start_new_thread(thread, (conn_client,))
    server_socket.close()
    # data = ''
    # if data == 'bye':
    #    conn_client.send('bye'.encode())
    #    conn_client.close()
    #
    #    break
    # conn_client.send(data.encode())


if __name__ == '__main__':
    serveur()