from classes import *
from protocole import *
import re

carte = Carte(0,0)

def register_pooo(uid):
   global carte
   carte.id_joueur = uid
   print("YOLOOOOOOOOOOOOOOOOOOOOO")


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
   print("YOLOO 2")
   print(carte.liste_planetes[0])


#faudra tester avec une autre chaine quand même
#init_pooo("INIT20ac18ab-6d18-450e-94af-bee53fdc8fcaTO6[2];1;3CELLS:1(23,9)'2'30'8'I,2(41,55)'1'30'8'II,3(23,103)'1'20'5'I;2LINES:1@3433OF2,1@6502OF3")

def test():

   carte = Carte(2, 1)

   # La liste est triée suivant le nombre d'unité défensive.
   liste_plan = sorted([
      Planete(1, 0, 0, 5, 0, 2, 2), 
      Planete(2, 0, 0, 4, 0, 0, 1), 
      Planete(3, 0, 0, 5, 0, 0, 1), 
      Planete(4, 0, 0, 4, 0, 0, 1),
      Planete(5, 0, 0, 5, 0, 0, 1),
      Planete(6, 0, 0, 3, 0, 0, 1),
      Planete(7, 0, 0, 5, 0, 1, 2)
      ])



   # Insertion des voisins (distances).
   liste_plan[0].liste_voisins = [[1, 2], [1, 3]]
   liste_plan[1].liste_voisins = [[1, 1]]
   liste_plan[2].liste_voisins = [[1, 1], [3, 4], [1, 6]]
   liste_plan[3].liste_voisins = [[1, 3], [1, 7]]
   liste_plan[4].liste_voisins = [[1, 3], [1, 6], [1, 7]]
   liste_plan[5].liste_voisins = [[1, 3], [1, 5]]
   liste_plan[6].liste_voisins = [[1, 5], [1, 4]]

   carte.liste_planetes = liste_plan

   # Création des classes aretes pour la classe Carte.
   liste_aretes = []

   for i in range(1, 8):
      carte.liste_aretes.append(Arete(1, i))


   # Début stratégie.
   # for planete in carte.extremites:
   #    if planete.proprio == None:
   #       chaine_order = toOrderMsg(carte.id_joueur, 50, 0, planete)


   carte.dict = carte.graphe_dictionnaire_generator()
   print(carte.dict)
   longueur, chemin = carte.plus_court_chemin(1, 7)
   print("Le plus court chemin pour aller de 1 à 7 est:", chemin, "(longueur=", longueur, ")")
   longueur, chemin = carte.plus_court_chemin(1, 5)
   print("Le plus court chemin pour aller de 1 à 5 est:", chemin, "(longueur=", longueur, ")")


