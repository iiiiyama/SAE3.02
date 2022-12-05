import socket


def serveur():
    host = "127.0.0.1"
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn_client, client_address = server_socket.accept()
    while True:
        data = conn_client.recv(1024).decode()
        print(f"from connected user{host}:" + str(data))
        if data == 'bye':
            print ("bye")
            conn_client.send('bye'.encode())
            conn_client.close()
            server_socket.close()
            break
        data = input("->")
        conn_client.send(data.encode())


if __name__ == '__main__':
    serveur()
