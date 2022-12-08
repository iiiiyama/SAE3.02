from threading import Thread
import socket

Host = 'localhost'
Port = 5898

def Send(client):
    msg_client = ""
    while msg_client != "disconnect":
        msg = input("Serveur -> ")
        msg = msg.encode()
        client.send(msg)
    else:
        socket.close()


def Reception(client):
    msg_client = ""
    while msg_client != "kill" and msg_client != "reset" and msg_client != "disconnect":
        print("en attente d'un message ...")
        msg_client = client.recv(1024).decode()
        print(f' {msg_client}\n')
    else:
        print("Je ferme la socket")
        client.close()


if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((Host, Port))
    socket.listen(1)
    print("Client t'es ou ?")

    client, ip = socket.accept()
    print("connected to :", ip[0], "on the port", ip[1])

    Send = Thread(target=Send, args=[client])
    Receive = Thread(target=Reception, args=[client])

    Send.start()
    Receive.start()

    Receive.join()
