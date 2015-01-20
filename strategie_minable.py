from classes import *
from protocole import *

"Réactualiser les données puis relancer cette fonction jusqu'à la fin du match"
def strategie_minable(carte):
    mes_planetes=carte.mes_planetes
    lg=len(carte.mes_planetes())
    l=len(carte.liste_planetes)
    while lg<l:
        for p in mes_planetes:
            for voisin in p.liste_voisins:
                while (voisin.proprietaire != carte.id_joueur):
                    toOrderMsg(carte.id_joueur, 100, p.identifiant, voisin.identifiant)
                mes_planetes.append(voisin)
