from classes import *
from protocole import *


def strategie_minable(carte):
    lg=len(carte.mes_planetes())
    l=len(carte.liste_planetes)
    tab=[]
    while lg<l:
        '''Faire un state pour réactualiser lg, l, liste_mes planetes'''
        tab=getTabPlanetes(state):
            mes_planetes==[]
        for p in tab:
            if p.proprietaire==id_joueur:
                mes_planetes.append(p)
        for i in mes_planetes:
            for j in mes_planetes[i].liste_voisins:
                while (j.proprietaire!=carte.id_joueur):
                    toOrderMsg(carte.id_joueur, 100, i.dentifiant, j.identifiant)
