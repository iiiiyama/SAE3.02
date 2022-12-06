from threading import Thread
import socket




def Send(client):
    msg = ''
    while msg != 'disconnect':
        msg = ("->")
        msg = msg.encode("utf-8")
        client.send(msg)
    client.close()


def Reception(client):
    msg = ''
    while msg != 'kill' and msg != 'reset' and msg != 'disconnect':
        data = client.recv(1024)
        data = data.decode('utf-8')
        print(data)
        if not data:
            print("connexion closed")
            break
    client.close()


Host = "127.0.0.1"
Port = 5010
msg = ''

while msg != 'kill':
    # crée le socket, peut réutiliser la même adresse et port, associe l'host et le port puis écoute le port
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.bind((Host, Port))
    socket.listen(1)

    while msg != 'kill' and msg != 'reset':
        # accepte la connexion du client
        client, ip = socket.accept()
        # précise à quel adresse le cllient est connecté et sur quel port
        print("connected to :", ip[0], "on the port", ip[1])

        envoi = Thread(target=Send, args=[client])
        recep = Thread(target=Reception, args=[client])

        envoi.start()
        recep.start()

        recep.join()

        client.close()
    socket.close()

