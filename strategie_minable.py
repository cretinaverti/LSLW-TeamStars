from classes import *
from protocole import *

def strategie_minable(carte):
    state=None
    mes_planetes=carte.mes_planetes(carte)
    lg=len(mes_planetes)
    l=len(carte.liste_planetes)

    while lg<l and not(Game_Over(state)) and not(End_of_Game(state):
        
        for planete in mes_planetes:
            i = 0
    
            while i < len(carte.planete_voisines(planete.identifiant)) and carte.get_panete_by(carte.planete_voisines(planete.identifiant)[i][1]).proprietaire == carte.couleur:
                i += 1
                
                if i != len(carte.planete_voisines(planete.identifiant)):
                    toOrderMsg(carte.id_joueur,100, planete.identifiant, carte.planete_voisines(p.identifiant)[i][1])
        state=state()
    
