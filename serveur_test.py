import socket
import time

hote = ''
port = 12887

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((hote, port))
conn.listen(5)

# le serveur écoute sur le port 12892
conn, infos_connexion = conn.accept()


#msg = conn.recv(1024)

#print(msg.decode('UTF-8'))
# attention : les données sont codées en bytes object


conn.send(b"register_pooo(0947e717-02a1-4d83-9470-a941b6e8ed07)")

time.sleep(1)

conn.send(b"init_pooo(salut)")


conn.close()
