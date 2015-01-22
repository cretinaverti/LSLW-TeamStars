from classes import *
from protocole import *

def report_unites(carte):

    carte.dict_unites = carte.graphe_dictionnaire_generator("t_unites")

    for pla in carte.liste_planetes:
        _, l_pla = carte.planetes_voisines("amis", pla)

        if len(l_pla) == 1:
            toOrderMsg(carte.id_joueur, 100, pla.identifiant, l_pla[0].identifiant)

        l_pla_enn = carte.get_planetes_ennemies()

        cout_1, l_ennemis_la_plus_proche_1 = carte.chemin_le_moins_couteux(pla.identifiant, l_pla_enn[0])
        for pla_enn in l_pla_enn:
                cout_2, l_ennemis_la_plus_proche_2 = carte.chemin_le_moins_couteux(pla.identifiant, pla_enn.identifiant)
                    if cout_2 < cout_1:
                        cout_1 = cout_2
                        l_ennemis_la_plus_proche_1 = l_ennemis_la_plus_proche_2

        for destination in l_ennemis_la_plus_proche_1:
            _, l_pla_vois_enn = carte.planete_voisines('ennemies', carte.get_by_planete(destination))
            if l_pla_enn == [] and pla.identifiant != destination:
                toOrderMsg(carte.id_joueur, 100, pla.identifiant, destination)

        if pla.identifiant != destination:
            toOrderMsg(carte.id_joueur, 100, pla.identifiant, destination)

def conquete_planete_solitaire_proche(carte, planete):
    '''
    Appel de cette fonction si l'on a assez d'unités.

    '''
    
    nb_voisins, l_pla = carte.planetes_voisines("neutre", planete)

    if nb_voisins == 1:
        unites_a_env = 100*carte.get_planete_by(l_pla[0]).getNb_def(carte) + carte.get_planete_by(l_pla[0]).getNb_off(carte)/planete.getNb_off(carte)

        if unites_a_env > 100:
            toOrderMsg(carte.id_joueur, 100, planete.identifiant, l_pla[0])
        else:
            toOrderMsg(carte.id_joueur, unites_a_env, planete.identifiant, l_pla[0])
        
            

def conquete_planete_productrice_proche(carte, planete):
    pass