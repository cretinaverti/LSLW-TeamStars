 
print("ICIIIIIIIIIIIIIIIIII")
    carte.dict_distances = carte.graphe_dictionnaire_generator("t_distances")
    print(carte.dict_distances)
    a,b = carte.plus_court_chemin(0,len(carte.liste_planetes)-1)
    print("a : ",a)
    print("b : ",b)
    while (not (carte.game_over or carte.end_of_game)):        #mise en place des stratégies et du robot
        mes_planetes=carte.mes_planetes(carte)

        while len(carte.mes_planetes(carte)) != len(carte.liste_planetes):
            for planete in mes_planetes:
                time.sleep(1)
                i = randint(0,len(carte.planete_voisines(planete))-1)
                while (carte.get_planete_by(i) in mes_planetes and i not in b) or i == planete.identifiant:
                    i = randint(0,len(carte.planete_voisines(planete)))
                print("LE ORDER :")
                print(planete.identifiant)
                print("TO")
                print(i)
                #print(carte.planete_voisines(planete)[i][1])
                toOrderMsg(carte.id_joueur,100, planete.identifiant, i)
