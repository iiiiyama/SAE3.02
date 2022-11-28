import socket
import platform


def client():

    host = 'localhost'
    port = 5000
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    client_socket.connect((host, port))
    while True:
        msg = input("->")
        client_socket.send(msg.encode())
        data = client_socket.recv(1024)
        print('received from server: ' + (data.decode()))
        #if data.lower() == "bye":
        #    client_socket.close()

        #if msg == 'os' or msg == 'OS':
        #    if platform.system() == 'Windows':
        #        print(platform.system())
        #    if msg == 'ip' or msg == 'ipconfig':
        #        print([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0])

        #    elif platform.system() == 'Linux':
        #        print(platform.system())
        #        if msg == 'ip a' or 'ip address':
        #            print([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0])
    client_socket.close()


if __name__ == '__main__':
    client()