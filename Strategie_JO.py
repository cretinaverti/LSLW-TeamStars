print("ICIIIIIIIIIIIIIIIIII")
    carte.dict_distances = carte.graphe_dictionnaire_generator("t_distances")
    print(carte.dict_distances)
    a,b = carte.plus_court_chemin(0,len(carte.liste_planetes)-1)
    print("a : ",a)
    print("b : ",b)
    while (not (carte.game_over or carte.end_of_game)):        #mise en place des stratégies et du robot
        mes_planetes=carte.mes_planetes(carte)
        for planete in mes_planetes:
            conquete_planete_solitaire_proche(carte, planete)

            i = 0

            while i < len(carte.planete_voisines(planete)) and carte.get_planete_by(carte.planete_voisines(planete)[i][1]).proprietaire == carte.couleur:
                i += 1
                
                if i != len(carte.planete_voisines(planete)):
                    toOrderMsg(carte.id_joueur,100, planete.identifiant, carte.planete_voisines(planete)[i][1])


        report_unites(carte)
 
