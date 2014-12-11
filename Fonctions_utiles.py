def nb_unit_imm(carte, joueur):
    lg=len(carte.liste_planetes)
    nb=0
    for i in range (0, lg):
        if carte.liste_planetes[i].proprietaire==joueur:
            nb=nb+carte.liste_planetes[i].nb_off+carte.liste_planetes[i].nb_def
    return nb

#Cas liste d'arêtes
def nb_unit_mobiles(carte, joueur):
    lg=len(carte.liste_aretes)
    nb=0
    for i in range (0, lg):
        long=carte.liste_aretes
        for j in range(0,long):
            if carte.liste_aretes[i].flotte_traverse[j].couleur==joueur:
                nb=nb+carte.liste_aretes[i].flotte_traverse[j].nb_unite
    return nb

#Fonction principale
def unites_totales(carte, joueur):
    return (nb_unit_imm(carte, joueur)+nb_unit_mobiles(carte, joueur))
