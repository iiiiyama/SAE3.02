from threading import Thread
import socket

Host = "127.0.0.1"
Port = 5070


def Send(client):
    msg = client.recv(1024)
    while msg != 'disconnect':
        msg = msg.encode("utf-8")
        client.send(msg)
    client.close()


def Reception(client):
    msg = client.recv(1024)
    while msg != 'kill' and msg != 'reset' and msg != 'disconnect':
        data = client.recv(1024)
        data = data.decode('utf-8')
        print(data)

        if not data:
            print("connexion closed")
            break
    client.close()


class serveur(socket):
        msg = ''
        while msg != 'kill':
            # crée le socket, peut réutiliser la même adresse et port, associe l'host et le port puis écoute le port
            socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            socket.bind((Host, Port))
            socket.listen(5)

            while msg != 'kill' and msg != 'reset':
                # accepte la connexion du client
                client, ip = socket.accept()
                # précise à quel adresse le cllient est connecté et sur quel port
                print("connected to :", ip[0], "on the port", ip[1])

                while msg != 'kill' and msg != 'reset' and msg != 'disconnect':
                    data = client.recv(1024)
                    data = data.decode('utf-8')
                    print(data)

                socket.close()
                client.close()

                envoi = Thread(target=Send, args=[client])
                recep = Thread(target=Reception, args=[client])

                envoi.start()
                recep.start()

                recep.join()

            socket.close()

        socket.close()


if __name__ == '__main__':
    serveur()



