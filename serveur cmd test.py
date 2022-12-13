import socket

host = "127.0.0.1"
port = 5008
msg = ''


def serveur():
    while msg != 'kill':
        server_socket = socket.socket()
        # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((host, port))
        server_socket.listen(1)

        while msg != 'kill' and msg != 'reset':
            print("en attente d'un client ...")
            conn_client, client_address = server_socket.accept()
            print("connected to :", client_address[0], "on the port", client_address[1])

            while msg != 'kill' and msg != 'reset' and msg != 'disconnect':
                data = conn_client.recv(1024).decode()
                print(f"from connected user {host}: " + str(data))
                if data == 'bye':
                    conn_client.send('bye'.encode())
                    conn_client.close()
                    server_socket.close()
                    break
                data = input("->")
                conn_client.send(data.encode())
            server_socket.shutdown(socket.SHUT_RDWR)
            conn_client.send('kill'.encode())
        server_socket.shutdown(socket.SHUT_RDWR)


if __name__ == '__main__':
    serveur()
