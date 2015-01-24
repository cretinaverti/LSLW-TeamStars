from classes import *
from protocole import *
import maMap
from poooc import *
import time
from random import randint
from strategie import *

def watchdog(carte):
    tabCouleur = ["blue","red","green","yellow","purple","orange"]
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

            #on renseigne les identifiants des aretes du tableau de moves, car ils n'y sont pas encore
            for arete in moves:
                arete.ide = carte.get_arete_by_extremites(arete)

            carte.mutex.acquire()

            #mise à jour des planètes
            
            for new_planete in planetes:
                    p = carte.get_planete_by(new_planete.identifiant)
                    p.proprietaire = new_planete.proprietaire
                    p.nb_off = new_planete.nb_off
                    p.nb_def = new_planete.nb_def
                    #mise à jour de l'interface graphique
                    if(p.proprietaire == -1):
                        carte.map.itemconfigure(p.contour,outline="white")
                    else:
                        carte.map.itemconfigure(p.contour,outline=tabCouleur[p.proprietaire])
                    carte.map.itemconfigure(p.off,text=p.nb_off)
                    carte.map.itemconfigure(p.deff,text=p.nb_def)
                    

            # mise à jour des moves
            #carte.liste_flottes = moves   # pas encore utilisé

            carte.flush_moves() #on vide les flottes sur toutes les aretes
            
            for new_arete in moves:
                    arete = carte.get_arete_by(new_arete.ide)
                    arete.flotte_traverse = new_arete.flotte_traverse

            carte.mutex.release()
        else:
            print("ERREUR : message du serveur non reconnu\n\n")
            print(msg)


def ia(carte): 
    while (not (carte.game_over or carte.end_of_game)):        #mise en place des stratégies et du robot
        mes_planetes=carte.mes_planetes(carte)
        for planete in mes_planetes:

            i = 0

            while i < len(carte.planete_voisines('toutes',planete)) and carte.get_planete_by(carte.planete_voisines(planete)[i][1]).proprietaire == carte.couleur:
                i += 1
                
                if i != len(carte.planete_voisines('toutes',planete)):
                    time.sleep(1)
                    toOrderMsg(carte.id_joueur,100, planete.identifiant, carte.planete_voisines(planete)[i][1])

