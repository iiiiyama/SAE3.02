from threading import Thread
import socket


def Send(socket):
    msg = ''
    while msg != 'kill' and msg != 'reset' and msg != 'disconnect':
        msg = input("->")
        msg = msg.encode('utf-8')
        socket.send(msg)
    socket.close()


def Reception(socket):
    msg = "->"
    while msg != 'disconnect':
        data = socket.recv(1024)
        data = data.decode("utf-8")
        print(data)
    socket.close()


Host = "127.0.0.1"
Port = 5070

# Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((Host, Port))

envoi = Thread(target=Send, args=[socket])
recep = Thread(target=Reception, args=[socket])

envoi.start()
recep.start()
