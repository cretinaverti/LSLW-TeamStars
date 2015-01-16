from classes import *
from protocole import *

'''Pourcentage à préciser :)'''

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
      toOrderMsg("choisir pourcentage",voisin.identifiant,planete_en_peril.identifiant)
            

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
        toOrderMsg(100,i.identifiant,i.unique_ennemi_voisin(carte.id_joueur).identifiant)

def elimination_flotte_dangereuse_voisine(carte):
  destination, taille=flotte_la_plus_dangereuse(carte)
  if get_planete_by(destination.getProprietaire())==carte.getCouleur:
    for voisin in get_planete_by(destination).getListe_voisins:
      if voisin.getProprietaire==carte.getCouleur:
        if voisin.entouree_amis(self.getCouleur):
          toOrderMsg(100, voisin.getIdentifiant, get_planete_by(destination))
        else:
          toOrderMsg(50, voisin.getIdentifiant, get_planete_by(destination))
          '''Pourcentage à revoir'''
                                             
                        
                
        
        
        
                

        
 
        
            

