def etude_planetes_proches(carte, ma_planete):
    planetes_isolees=[]
    lg=len(ma_planete.liste_voisins)
    for i in range (0, lg):    
        long=ma_planete.liste_voisins[i][1].liste_voisins
        if long==1:
            planetes_isolees.append(ma_planete.liste_voisins[i][1])
    return planetes_isolees

#Fonction de visualisation
#Nécessite une fonction d'attaque si on juge bon de conquérir


    
    
