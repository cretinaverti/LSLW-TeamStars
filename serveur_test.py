import socket

hote = ''
port = 12881

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((hote, port))
conn.listen(5)

# le serveur écoute sur le port 12892
conn, infos_connexion = conn.accept()


msg = conn.recv(1024)

print(msg.decode('UTF-8'))
# attention : les données sont codées en bytes object


conn.send(b"test(param)")
conn.close()
