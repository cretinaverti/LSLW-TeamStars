from classes import *
from protocole import *
import maMap
from poooc import *

def watchdog(carte):
    while (not (carte.game_over or carte.end_of_game)):
        msg = state_on_update()

        if 'GAMEOVER' in msg:
            #on voit si on est mort
            if Game_Over(msg) == carte.couleur:
                carte.game_over = True
            else:
                #virer de la liste des joueurs le joueur mort
                pass
        if 'ENDOFGAME' in msg:
            carte.end_of_game = True
        if 'STATE' in msg:
            
            planetes = getTabPlanetes(msg)
            moves = getMoves(msg)

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
        else:
            print("ERREUR : message du serveur non reconnu\n\n")
            print(msg)


def ia(carte):
    
    while (not (carte.game_over or carte.end_of_game)):        #mise en place des stratégies et du robot
        pass
