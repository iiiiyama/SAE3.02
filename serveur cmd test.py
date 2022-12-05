import socket
import threading

host = "127.0.0.1"
port = 5034


def co_client(conn):
    data = ''

    while data != 'kill':
        data = conn.recv(1024).decode()
        if data == 'bye':
            print("bye")
            conn.send('bye'.encode())
            break
        conn.send(data.encode())
    conn.close()


def serveur():
    data = ''

    while data != 'kill':
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)

        while data != 'kill' and data != 'reset':
            print("en attente d'un client ...")
            conn_client, client_address = server_socket.accept()
            t1 = threading.Thread(target=co_client)
            t1.start()

            while data != 'kill' and data != 'reset' and data != 'disconnect':
                data = conn_client.recv(1024).decode()
                server_socket.send(data.encode())
                print(f"from connected user{host}:" + str(data))
            conn_client.close()
        server_socket.close()


if __name__ == '__main__':
    serveur()
