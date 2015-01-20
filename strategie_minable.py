from classes import *
from protocole import *

"Réactualiser les données puis relancer cette fonction jusqu'à la fin du match"
def strategie_minable(carte):
    mes_planetes=carte.mes_planetes
    lg=len(carte.mes_planetes())
    l=len(carte.liste_planetes)

    while lg<l:
        for p in mes_planetes:
            
            i = 0
            while i < len(carte.dict_distances[p.identifiant]) and carte.**get_PLanete_By**(carte.dict_distances[i]).proprietaire == carte.couleur:
                i += 1
                
            if i != len(carte.dict_distances[p.identifiant]):
                toOrderMsg(100, p.identifiant, p.liste_voisins[i])
         
                mes_planetes.append(voisin)
