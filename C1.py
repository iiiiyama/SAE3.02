from threading import Thread
import socket

Host = 'localhost'
Port = 12

def Send(socket_client):
    msg = ""
    while msg != "Kill" and msg != "Reset" and msg != "Disconnect" :
        msg = input("->")
        socket_client.send(msg.encode())

def Reception(socket_client):
    msg_serveur = ""
    while msg_serveur != "Disconnect":
        msg_serveur = socket_client.recv(500).decode()
        print(f"Received from server: ' + {msg_serveur}")

if __name__ == '__main':

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((Host, Port))

    envoi = Thread(target=Send, args=[socket_client])
    recep = Thread(target=Reception, args=[socket_client])

    envoi.start()
    recep.start()

    recep.join()