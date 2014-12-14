def etude_planetes_isolees_proches(carte, ma_planete):
    planetes_isolees=[]
    lg=len(ma_planete.liste_voisins)
    for i in range (0, lg):    
        long=ma_planete.liste_voisins[i][1].liste_voisins
        if long==1:
            planetes_isolees.append(ma_planete.liste_voisins[i][1])
    return planetes_isolees

#Fonction de visualisation: cherche s'il y a des planètes isolées
#autour de "ma_planete"
#Nécessite une fonction d'attaque si on juge bon de conquérir

def etude_planetes_proches_droite(carte, ma_planete):
    planetes_isolees=[]
    planetes_isolees_possibles=[]
    lg=len(ma_planete.liste_voisins)
    for i in range (0, lg):    
        long=ma_planete.liste_voisins[i][1].liste_voisins
        if long==1:
            planetes_isolees.append(ma_planete.liste_voisins[i][1])
        else:
            if long==2:
                lo1=ma_planete.liste_voisins[1][1]
                lo=ma_planete.liste_voisins[1][1].liste_voisins
                while len(lo)==2:
                    lo=lo[1][1].liste_voisins
                if len(lo)==1:
                    planetes_isolees.append(lo1)              
    return planetes_isolees

#Idem mais prend en compte les planetes appartenant à une demie droite
#terminée par une planète isolée
#Gros risque d'erreurs :(...

def etude_planete(ma_planete):
    lg=len(ma_planete.liste_voisins)
    if lg>2:
        return 0
    #inutile
    else:
        if lg==1:
            return 1
        #isolée
        else:
            return 2
        #appartient à une droite

#Etudie si "ma_planete" est isolée ou appartient à une droite

def etude_planete_droite(ma_planete):
    if len(ma_planete.liste_voisins)==1:
        return 0
    else:
        return(etude_planete_droite(ma_planete.liste_voisins[0][1])
                or etude_planete_droite(ma_planete.liste_voisins[1][1]))
#non-testée donc gros risque d'erreurs...
#retourne 0 si la planete appartient à une demie-droite
# ou 1 si elle appartient à une droite
        
