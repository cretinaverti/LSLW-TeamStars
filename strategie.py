from classes import *
from protocole import *

def planete_en_peril(carte):
	'''
	Appel de la fonction order ?

	'''
	planete_en_peril = carte.planete_moins_defendue()
	nos_pla = carte.mes_planetes()

	i, j = 0, 0
	while i < len(planete_en_peril.liste_voisins) and planete_en_peril.liste_voisins[i][1] != nos_pla[j].identifiant:
		for pla in nos_pla:
			

	toOrderMsg(carte.id_joueur, )

