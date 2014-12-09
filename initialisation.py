from classes import *
from protocole import *
import re


def register_pooo(uid):
   notre_id = uid
    ### Comment on garde ça ? !!!!


def init_pooo(init):
   matchid = re.match("INIT(.*)TO",init).group(1)
   nombreDeJoueurs = re.match(".*TO(\d+)\[",init).group(1)
   notreCouleur = re.match(".*TO\d+\[(\d+)\]",init).group(1)
   speed = re.match(".*;(\d+);",init).group(1)
   nbCellules = re.match(".*\];\d+;(\d+)CELLS",init).group(1)

   cellules = re.split("((.*I),)+",re.match(".*CELLS:(.*);\d+LINES",init).group(1))

   #for i in cellules:
   print(cellules)

init_pooo("INIT20ac18ab-6d18-450e-94af-bee53fdc8fcaTO6[2];1;3CELLS:1(23,9)'2'30'8'I,2(41,55)'1'30'8'II,3(23,103)'1'20'5'I;2LINES:1@3433OF2,1@6502OF3")
