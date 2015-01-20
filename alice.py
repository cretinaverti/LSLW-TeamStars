from classes import *
from protocole import *
import maMap
from poooc import *

def watchdog(carte):
    while (not carte.game_over):
        state = poooc.state_on_update()
        


def ia(carte):
    
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
        # ICIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

    
'''
    while (not GameOver(state) or not End_of_Game(state)):
        state = state_on_update()
        moves = getMoves(state)
        #stratégie
'''
