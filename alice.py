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


			
			carte.flush_moves() #on vide les flottes sur toutes les aretes
			
			# mise à jour des moves
			for new_arete in moves:
				#on rajoute les flottes
				arete = carte.get_arete_by_extremites(new_arete)
				arete.flotte_traverse = new_arete.flotte_traverse
				
				#on met à jour l'interface graphique
				i = 1
				for move in new_arete.flotte_traverse:
					carte.map.itemconfigure(arete.flottes[i],text="j"+str(move.couleur)+" de "+str(move.nb_unite)+" unites vers "+str(move.destination)+", dist: "+str(move.distance))

					

			
			carte.mutex.release()
		else:
			print("ERREUR : message du serveur non reconnu\n\n")
			print(msg)



def ia(carte):
	print("ICIIIIIIIIIIIIIIIIII")
	carte.dict_distances = carte.graphe_dictionnaire_generator("t_distances")
	print(carte.dict_distances)
	a,b = carte.plus_court_chemin(0,len(carte.liste_planetes)-1)
	print("a : ",a)
	print("b : ",b)
	while (not (carte.game_over or carte.end_of_game)): #mise en place des stratégies et du robot
		mes_planetes=carte.mes_planetes()
		for planete in mes_planetes:
		#conquete_planete_solitaire_proche(carte, planete)
			pla_vois=planete.liste_voisins
			if len(pla_vois)==1:
				toOrderMsg(carte.id_joueur, 100, planete.identifiant, pla_vois[0][1])
			i=0	
			while i<len(pla_vois) and carte.get_planete_by(pla_vois[i][1]).getProprietaire(carte)==carte.couleur:
				i+=1
			if i<len(pla_vois):
				j=0
				toOrderMsg(carte.id_joueur,100, planete.identifiant, pla_vois[i][1])				
				
			else:
				pla_enn=carte.get_planetes_ennemies()
				u=0
				dist0, chemin0=carte.plus_court_chemin(planete.identifiant, pla_enn[0].identifiant)
				while u<len(pla_enn):
					dist, chemin=carte.plus_court_chemin(planete.identifiant, pla_enn[u].identifiant) 
					
					if dist<dist0:
						dist0=dist
						chemin0=chemin0
					u+=1
				toOrderMsg(carte.id_joueur, 100, chemin0[0], chemin0[1]) 
