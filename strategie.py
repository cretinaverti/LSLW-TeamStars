from classes import *
from protocole import *

"""A repréciser si dans le toOrder le départ et la destination sont le nom
    des planètes ou les planètes elles-mêmes. Ici, j'ai mis la planète."""
'''Attention!!! Il faut renvoyer l'ordre, pas la chaine comme elle est dans
    des boucles!!'''

def sauver_planete_en_peril(carte):
	'''
	Fournir des ressources d'une planete voisine mieux défendue
	à notre planète la moins défendue
	'''
	planete_en_peril = carte.planete_moins_defendue()
	somme_v=0
	somme=planete_en_peril.nb_off+planete_en_peril.nb_def
	for voisin in planete_en_peril.liste_voisins:
            if voisin.entouree_amis(carte.id_joueur):
                toOrderMsg(carte.id_joueur,"choisir pourcentage",voisin,planete_en_peril)
            

def vidage_planetes_securisees(carte):
    '''
    Déplace les ressources des planètes protégées
    '''
        mes_planetes=carte.mes_planetes()
    for pla in mes_planetes:
        if pla.entouree_amis(carte.id_joueur):
            '''A completer: Trouver le plus court chemin (de planetes protégées)
               vers une planete touchant au moins une planete ennemies. Faire
               les transferts le long du chemin'''

def prise_planete_prod(carte):
    
        '''A completer'''

def prise_voisins_isoles_ou_unique_ennemi_proche(carte):
    '''Seulement si notre planete a plus d'unités off que lui de défense totale'''
    mes_planetes=carte.mes_planetes()
    defense=0
    for i in mes_planetes:
        if i.unique_ennemi_voisin(carte.id_joueur)!=False:
            defense=i.unique_ennemi_voisin(carte.id_joueur).nb_off+i.unique_ennemi_voisin(carte.id_joueur).nb_def
            if i.nb_off>defense:
                toOrderMsg(carte.id_joueur,"choisir pourcentage",i,i.unique_ennemi_voisin(carte.id_joueur))
                

        
 
        
            

