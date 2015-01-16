from classes import *
from protocole import *

"Réactualiser les données puis relancer cette fonction jusqu'à la fin du match"
def strategie_minable(carte):
    mes_planetes=carte.mes_planetes
    lg=len(carte.mes_planetes())
    l=len(carte.liste_planetes)
    while lg<l:
        for p in mes_planetes:
            for j in mes_planetes[p].liste_voisins:
                while (j.proprietaire!=carte.id_joueur):
                    toOrderMsg(carte.id_joueur, 100, p.dentifiant, j.identifiant)
                mes_planetes.append(j)
