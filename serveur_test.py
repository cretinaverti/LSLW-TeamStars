import socket
import time

hote = ''
port = 12888

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

conn.send(b"INIT20ac18ab-6d18-450e-94af-bee53fdc8fcaTO6[2];1;3CELLS:1(23,9)'2'30'8'I,2(41,55)'1'30'8'II,3(23,103)'1'20'5'I;2LINES:1@3433OF2,1@6502OF3")

time.sleep(1)

conn.send(b"play")

conn.close()
