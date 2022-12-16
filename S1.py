from threading import Thread
import socket
import os
import readline
import platform
import psutil
import subprocess

Host = 'localhost'
Port = 5108

msg_client = ''


def cmd(msg_client):

    if msg_client == 'os':
        data = platform.system()

        return data
    elif msg_client == 'ip' or msg_client == 'ipconfig' or msg_client == 'ip a':
        data = socket.gethostbyname(socket.gethostname())

        return data
    elif msg_client == 'ram':
        ram = psutil.virtual_memory()[0]/1000000000
        ram2 = psutil.virtual_memory()[3] / 1000000000
        ram3 = psutil.virtual_memory()[4] / 1000000000

        return f"{ram} GB, {ram2} GB, {ram3} GB"

    elif msg_client == 'cpu':
        cpu = psutil.cpu_count()

        return f"{cpu}"

    elif msg_client == 'host' or msg_client == 'hostname' or msg_client == 'name':
        hostname = socket.gethostname()

        return f"{hostname}"

    # elif msg_client == ' ':
    #   dos = subprocess.Popen("echo %s", shell=True, stdout=subprocess.PIPE).stdout.read()

    #    return f"{dos}"

    else:
        return f"commande non reconnu"


def Send(client):
    msg_client = ""
    while msg_client != "disconnect":
        msg = input("Serveur -> ")
        msg = msg.encode()
        client.send(msg)

    # pour les utilisateurs linux
    #################################################################
    readline.parse_and_bind('')
    histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
    try:
        readline.read_history_file(histfile)
    except IOError:
        pass
    ##################################################################

    else:
        client.close()


def Reception(client):
    msg_client = ""
    while msg_client != "kill" and msg_client != "reset" and msg_client != "disconnect":
        print("en attente d'un message ...")
        msg_client = client.recv(1024).decode()
        print(f' {msg_client}\n')
        msg = cmd(msg_client)
        client.send(msg.encode())

    else:
        print("Je ferme la socket")
        client.close()
        socket_server.close()


if __name__ == '__main__':
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind((Host, Port))
    socket_server.listen(1)
    print("en attente d'un client ...")

    client, ip = socket_server.accept()
    print("connected to :", ip[0], "on the port", ip[1])

    Send = Thread(target=Send, args=[client])
    Receive = Thread(target=Reception, args=[client])

    Send.start()
    Receive.start()

    Receive.join()
