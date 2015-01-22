from classes import *
from protocole import *
from tkinter import *
import re
import alice
import maMap
import threading
import time

carte = Carte(0,0)

def register_pooo(uid):
        global carte
        carte.id_joueur = uid


def init_pooo(init):
        global carte

        print("\n\nINIT :::\n\n")
        print(init)

        carte.match_id = re.match("INIT(.*)TO",init).group(1)
        carte.nb_joueur = int(re.match(".*TO(\d+)\[",init).group(1))
        carte.couleur = int(re.match(".*TO\d+\[(\d+)\]",init).group(1))
        carte.vitesse = int(re.match(".*;(\d+);",init).group(1))
        nbCellules = int(re.match(".*\];\d+;(\d+)CELLS",init).group(1))

        cellules = re.split(",(\d+\(\d+,\d+\)'\d+'\d+'\d+'I+)",re.match(".*CELLS:(.*);\d+LINES",init).group(1))

        # on récupère les données de chaque planète
        carte.liste_planetes = []
        for i in cellules:
                if(i != ""):
                        planete = Planete(0, 0, 0, 0, 0, 0, 0)
                        planete.identifiant = int(re.match("\d+",i).group(0))
                        planete.x = int(re.match(".*\((\d+),",i).group(1))
                        planete.y = int(re.match(".*\(\d+,(\d+)\)",i).group(1))
                        planete.rad = int(re.match(".*\)'(\d+)'",i).group(1))
                        planete.unit_max_off = int(re.match(".*\)'\d+'(\d+)'\d+'",i).group(1))
                        planete.unit_max_def = int(re.match(".*\)'\d+'\d+'(\d+)'",i).group(1))
                        planete.cadence_prod = len(re.match(".*'(I*)",i).group(1))
                        carte.liste_planetes.append(planete)
        if(int(nbCellules) != len(carte.liste_planetes)):
                print("planetes"+str(len(carte.liste_planetes)))
                print("autre"+str(nbCellules))
                raise Exception("on a pas récupéré le bon nombre de planètes dans le init_pooo")

        #on récupère les données de chaque arete
        carte.liste_aretes = []
        carte.nb_aretes = re.match(".*;(\d+)LINES",init).group(1)
        aretes = re.split(",",re.match(".*LINES:(.*)",init).group(1))
        for i in aretes:
                a = Arete(0)
                a.ide = int(re.match("\d+",i).group(0))
                a.extremites.append(int(re.match("(\d+)@",i).group(1)))
                a.extremites.append(int(re.match(".*OF(\d+)",i).group(1)))
                a.distance = int(re.match(".*@(.*)OF",i).group(1))
                carte.liste_aretes.append(a)

        carte.dict_distances = carte.graphe_dictionnaire_generator("t_distances")

        carte.threads.append(threading.Thread(target=maMap.boucle_principale, name="interface", args=(carte,)))
        carte.threads[0].start()


def play_pooo():
        global carte
        time.sleep(1)
        carte.threads.append(threading.Thread(target=alice.watchdog, name="watchdog", args=(carte,)))
        carte.threads[1].start()

        carte.threads.append(threading.Thread(target=alice.ia, name="robot_joueur", args=(carte,)))
        carte.threads[2].start()

        for t in carte.threads:
                t.join()



