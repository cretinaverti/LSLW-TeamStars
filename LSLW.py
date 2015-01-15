import os

# os.system("idle3 -r coucou.py")

newpid = os.fork()
if newpid == 0:
    os.system("idle3 -r client.py")
else:
    os.system("idle3 -r initialisation.py")
