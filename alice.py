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


			'''
			carte.flush_moves() #on vide les flottes sur toutes les aretes
			
			# mise à jour des moves
			for move in moves:
				arete = carte.get_arete_by_extremites(move)
				
			
			
			#carte.liste_flottes = moves   # pas encore utilisé

			
			
			for new_arete in moves:
					arete = carte.get_arete_by(new_arete.ide)
					arete.flotte_traverse = new_arete.flotte_traverse

			'''
			carte.mutex.release()
		else:
			print("ERREUR : message du serveur non reconnu\n\n")
			print(msg)



def ia(carte):
	print("ICIIIIIIIIIIIIIIIIII")
	'''carte.dict_distances = carte.graphe_dictionnaire_generator("t_distances")
	print(carte.dict_distances)
	a,b = carte.plus_court_chemin(0,len(carte.liste_planetes)-1)
	print("a : ",a)
	print("b : ",b)'''
	while (not (carte.game_over or carte.end_of_game)):        #mise en place des stratégies et du robot
		mes_planetes=carte.mes_planetes()
		for planete in mes_planetes:
				#conquete_planete_solitaire_proche(carte, planete)

			
			pla_vois=planete.liste_voisins
			i=0			
			while i<len(pla_vois) and carte.get_planete_by(pla_vois[i][1]).getProprietaire(carte)==carte.couleur:
				i+=1
			toOrderMsg(carte.id_joueur,100, planete.identifiant, pla_vois[i][1])
		

			vid_pla_is(carte)
			vid_pla_protegees_autre(carte)
			'''Si ces deux fonctions marchent, tenter de les remplacer par la fonction vid_pla, la même mais en une seule fonction'''

