from threading import Thread
import socket



# thread pour l'envoi
def Send(socket):
    msg = ''
    while msg != "kill" and msg != "reset" and msg != "disconnect":
        msg = input("->")
        msg = msg.encode()
        socket.send(msg)
    else:
        print("le serveur à fermer la connection")
        socket.close()


# thread pour la reception
def Reception(socket):
    msg = "->"
    while msg != "disconnect":
        data = socket.recv(1024)
        data = data.decode()
        print(f'received from server: {data}\n')
    else:
        print("le serveur à fermer la connection")
        socket.close()


Host = "127.0.0.1"
Port = 5108


# Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((Host, Port))

envoi = Thread(target=Send, args=[socket])
recep = Thread(target=Reception, args=[socket])

envoi.start()
recep.start()


