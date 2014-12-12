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

carte = Carte(2, 1)

# La liste est triée suivant le nombre d'unité défensive.
liste_planete = sorted([
   Planete(1, 0, 0, 5, 0, 2, 2), 
   Planete(2, 0, 0, 4, 0, 0, 1), 
   Planete(3, 0, 0, 5, 0, 0, 1), 
   Planete(4, 0, 0, 4, 0, 0, 1),
   Planete(5, 0, 0, 5, 0, 0, 1),
   Planete(6, 0, 0, 3, 0, 0, 1),
   Planete(7, 0, 0, 5, 0, 1, 2)
   ])



# Insertion des voisins (distances).
liste_planete[0].liste_voisins = [[1, 2], [1, 3]]
liste_planete[1].liste_voisins = [[1, 1]]
liste_planete[2].liste_voisins = [[1, 1], [1, 4], [1, 3]]
liste_planete[3].liste_voisins = [[1, 3], [1, 7]]
liste_planete[4].liste_voisins = [[1, 3], [1, 6], [1, 7]]
liste_planete[5].liste_voisins = [[1, 3], [1, 5]]
liste_planete[6].liste_voisins = [[1, 5], [1, 4]]

carte.liste_planete = liste_planete

# Création des classes aretes pour la classe Carte.
liste_aretes = []

for i in range(1, 8):
   carte.liste_aretes.append(Arete(1, i))




