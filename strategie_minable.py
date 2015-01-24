print("ICIIIIIIIIIIIIIIIIII")
while (not (carte.game_over or carte.end_of_game)):        #mise en place des stratégies et du robot
    mes_planetes=carte.mes_planetes(carte)
    for planete in mes_planetes:

        i = 0

        while i < len(carte.planete_voisines('toutes',planete)) and carte.get_planete_by(carte.planete_voisines(planete)[i][1]).proprietaire == carte.couleur:
            i += 1
            
            if i != len(carte.planete_voisines('toutes',planete)):
                time.sleep(1)
                toOrderMsg(carte.id_joueur,100, planete.identifiant, carte.planete_voisines(planete)[i][1])

