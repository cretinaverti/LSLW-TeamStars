from classes import *
from protocole import *
import maMap
from poooc import *

def watchdog(carte):
    while (not Game_over):
        state = state_on_update()
        planetes = getTabPlanetes
        moves = getMoves(state)

        carte.mutex.acquire()

        #mise à jour des planètes
	
        for new_planete in planetes:
                p = carte.get_planete_by(new_planete.identifiant)
                p.nb_off = new_planete.nb_off
                p.nb_def = new_planete.nb_def

        # mise à jour des moves
        #carte.liste_flottes = moves   # pas encore utilisé

        carte.flush_moves() #on vide les flottes sur toutes les aretes
        
        for new_arete in moves:
                arete = carte.get_arete_by(new_arete.ide)
                arete.flottte_traverse = new_arete.flotte_traverse

        carte.carte_a_jour = False
        carte.mutex.release()


def ia(carte):
    
    while (not Game_Over()):        #mise en place des stratégies et du robot
        pass
