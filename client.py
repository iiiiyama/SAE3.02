import socket
import platform


def client():

    host = 'localhost'
    port = 5000
    client_socket = socket.socket()

    client_socket.connect((host, port))
    while True:
        msg = input("->")
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        print('received from server: ' + data)
        if data.lower() == "bye":
            client_socket.close()

        if msg == 'os' or 'OS':
            if platform.system() == 'Windows':
                print(platform.system())
                if msg == 'ip' or 'ipconfig':
                    print([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0])

            elif platform.system() == 'Linux':
                print(platform.system())
                if msg == 'ip a' or 'ip address':
                    print([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0])


if __name__ == '__main__':
    client()