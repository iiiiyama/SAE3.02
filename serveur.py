import socket


def serveur():
    host = ""
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    client_socket, client_address = server_socket.accept()
    while True:
        data = client_socket.recv(1024).decode()
        print(f"from connected user {host}:" + str(data))
        if data == 'bye':
            client_socket.send('bye'.encode())
            client_socket.close()
            server_socket.close()
            break
        data = input("->")
        client_socket.send(data.encode())
    #while False:
        #print("en attente d'un client ...")


if __name__ == '__main__':
    serveur()
