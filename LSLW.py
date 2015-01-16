import os
import time

# os.system("idle3 -r coucou.py")

newpid = os.fork()
if newpid == 0:
    os.system("idle3 -r poooserver.py")
else:
    time.sleep(1)
    newpid = os.fork()
    if newpid == 0:
        os.system("./pooobot.py -s localhost:9876 -b botneutre LEGROSNUL")
    else:
        os.system("./pooobot.py -s localhost:9876 -b initialisation titi")
