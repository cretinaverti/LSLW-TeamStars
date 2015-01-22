from classes import *
from protocole import *
import maMap
from poooc import *
import time

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
    a,b = carte.plus_court_chemin(0,len(carte.liste_planetes)-1)

    while (not (carte.game_over or carte.end_of_game)):        #mise en place des stratégies et du robot
        mes_planetes=carte.mes_planetes(carte)

        while len(carte.mes_planetes(planete)) != len(carte.liste_planetes):
            for planete in mes_planetes:
                i = randint(0,len(carte.planete_voisines(planete)))
                while i in mes_planetes and i not in b:
                    i = randint(0,len(carte.planete_voisines(planete)))
                print("LE ORDER :")
                print(planete.identifiant)
                print("TO")
                print(carte.planete_voisines(planete)[i][1])
                toOrderMsg(carte.id_joueur,100, planete.identifiant, carte.planete_voisines(planete)[i][1])
##                i = 0
##
##                while i < len(carte.planete_voisines(planete)) and carte.get_planete_by(carte.planete_voisines(planete)[i][1]).proprietaire == carte.couleur:
##                    i += 1
##                
##                if i != len(carte.planete_voisines(planete)):
##                    time.sleep(1)
##                    print("LE ORDER :")
##                    print(planete.identifiant)
##                    print("TO")
##                    print(carte.planete_voisines(planete)[i][1])
##                    toOrderMsg(carte.id_joueur,100, planete.identifiant, carte.planete_voisines(planete)[i][1])
