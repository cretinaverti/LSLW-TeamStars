from classes import *
from protocole import *

carte = Carte(0,0)

def register_pooo(uid):
   global carte
   carte.id_joueur = uid


def init_pooo(init):
   global carte
   carte.match_id = re.match("INIT(.*)TO",init).group(1)
   carte.nb_joueur = re.match(".*TO(\d+)\[",init).group(1)
   carte.couleur = re.match(".*TO\d+\[(\d+)\]",init).group(1)
   carte.vitesse = re.match(".*;(\d+);",init).group(1)
   nbCellules = re.match(".*\];\d+;(\d+)CELLS",init).group(1)

   cellules = re.split(",(\d+\(\d+,\d+\)'\d+'\d+'\d+'I+)",re.match(".*CELLS:(.*);\d+LINES",init).group(1))

   # on récupère les données de chaque planète
   carte.liste_planetes = []
   for i in cellules:
      if(i != ""):
         planete = Planete(0, 0, 0, 0, 0, 0, 0)
         planete.identifiant = re.match("\d+",i).group(0)
         planete.x = re.match(".*\((\d+),",i).group(1)
         planete.y = re.match(".*\(\d+,(\d+)\)",i).group(1)
         planete.rad = re.match(".*\)'(\d+)'",i).group(1)
         planete.unit_max_off = re.match(".*\)'\d+'(\d+)'\d+'",i).group(1)
         planete.unit_max_def = re.match(".*\)'\d+'\d+'(\d+)'",i).group(1)
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
      a.extremites.append(int(re.match("(\d+)@",i).group(1)))
      a.extremites.append(int(re.match(".*OF(\d+)",i).group(1)))
      a.distance = re.match(".*@(.*)OF",i).group(1)
      carte.liste_aretes.append(a)

def play_pooo():
    global carte
    print("j'attends :)")

   
