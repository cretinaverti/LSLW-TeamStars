import socket
import re

hote = "localhost"
port = 12881

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((hote, port))

print("Connection avec le serveur")

conn.send(b"coucou")
# Ici, le client reçoit les messages du serveur, il est donc succeptible
# d'appeler des fonctions comme init_pooo() et d'autres en fonction de
# ce que le serveur lui demande

# plus tard, le client sert à envoyer les state() et order()

#########################
# réception des commandes d'initialisation envoyées par le serveur
#########################

msg = conn.recv(1024).decode('UTF-8')
fonc = re.match("(.*)\(",msg).group(1)
param = re.match(".*\((.*)[,)]",msg).group(1)
print(str(fonc)+"("+str(param)+")")


conn.close()
