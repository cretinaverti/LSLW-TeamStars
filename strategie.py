from classes import *
from protocole import *

def vid_pla_is(carte):
    mes_pla=carte.liste_planetes
    for pla in mes_pla:
        voisines=pla.liste_voisins
        if len(voisines)==1:'''Vérifie que la planète est isolée'''
            toOrderMsg(carte.id_joueur, 100, pla.identifiant, voisines[0])

'''Vider les planetes sécurisées mais non isolées: cas au moins une planete voisines est non sécurisée. ex: 1(moi)__2(moi)___3(moi)__4(moi)__5(autre)
L'algo peut transférer de 3 vers 4 mais pas de 2 vers 3. Avec l'algo précédent, on peut effectuer le déplacement 1 vers 2.
Pour le cas 2 vers 3 il faut connaitre le chemin.'''

def vid_pla_protegees(carte):
    mes_pla=carte.liste_planetes
    for pla in mes_pla:
        voisines=pla.liste_voisins
        vois_amies=carte.planetes_voisines('amies', pla)
        if len(voisines)==len(vois_amies): '''N'effectue les ordres que si la planete n'est entourée que de planètes amies'''
        '''J'utilise un while car voisines est une liste de listes'''
        i=0
        while i<len(voisines) and carte.planetes_voisines('amies', carte.get_planete_by(voisines[i][1]))==carte.get_planete_by(voisines[i][1]).liste_voisins: '''Ignore les voisines amies entourées d'amies'''
            i+=1
         if i<len(voisines):
            toOrderMsg(carte.id_joueur, 100, pla.identifiant, destination) '''Envoie vers la 1ère planète voisine amie non-entourée d'amies'''

'''Dernier cas à étudier: si la planète est entourée d'amies, elles-même entourées d'amies. Le 1er if n'est pas utile dans la version mixée'''
def vid_pla_protegees_autre(carte):
    mes_pla=carte.liste_planetes
    for pla in mes_pla:
        voisines=pla.liste_voisins
        vois_amies=carte.planetes_voisines('amies', pla)
        if len(voisines)>len(vois_amies):
            pla_enn=carte.get_planetes_ennemies()
            cout_min, chemin_mieux=carte.chemin_le_moins_couteux(pla.identifiant, pla_enn[0].identifiant) '''Initialisation du chemin le moins couteux'''
            for pl in pla_enn: '''Recherche de la planete ennemie vers laquelle ca coutera moins cher d'expédier les unités''' 
                cout, chemin=carte.chemin_le_moins_couteux(pla.identifiant, pl.identifiant)
                if cout<cout_min:
                    cout_min=cout
                    chemin_mieux=chemin '''J'ai considéré que le chemin renvoyer est sous la forme d'une liste d'indentifiant genre: 1__2__3__4__5 Pour aller de 3 à 5 ca renvoie [3,4,5]. J'espère que c'est ça...'''
        i=1 '''Permet de ne pas étudier 0 qui est la planete d'où partent les unités'''
        while i< len(chemin_mieux) and carte.get_planete_by(chemin_mieux[i]).getProprietaire(carte)==carte.couleur: '''While car on veut accéder à 2 planetes à la fois de la liste'''
            if len(carte.get_planete_by(chemin_mieux[i]).liste_voisins)==len(carte.planetes_voisines('amies', carte.get_planete_by(chemin_mieux[i])): '''N'envoie à la planete suivante qui si elle est protégée'''
                toOrder(carte.id_joueur, 100, chemin_mieux[i-1], chemin_mieux[i)) '''Envoie du départ i-1 à la planete dont on a étudié la situation i'''
        toOrder(carte.id_joueur, 100, chemin_mieux[i-1], chemin_mieux[i)) '''Permet d'envoyer sur la première planète non protégée ou la dernière planète (ennemie) si elles étaient toutes protégées'''
        

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
        unites_a_env = 100*(carte.get_planete_by(l_pla[0]).getNb_def(carte) + carte.get_planete_by(l_pla[0]).getNb_off(carte))/planete.getNb_off(carte)

        if unites_a_env > 100:
            toOrderMsg(carte.id_joueur, 100, planete.identifiant, l_pla[0])
        else:
            toOrderMsg(carte.id_joueur, unites_a_env, planete.identifiant, l_pla[0])
        

            
#Attention! Il y a peut-être une erreur (de ma part) qui traine encore dans les parametres de la fonction mes-planetes
#voir après le commit de Jo
#Faiblesses de la fonction qui suit: Le cout du chemin totalise indifféremment les unités de mes planetes et celles de
#celles des ennemis
            #Rq: Elle peut être utilisée décomposée
def conquete_planetes_productrices(carte):
    liste_pla_prod=carte.planetes_productrices()

#1) planetes productrices proches des miennes
    for planete in liste_pla_prod:
        _,voisines=carte.planetes_voisines('amies', planete)
        for voisine in voisines:
            nb_a_envoyer= 100*(planete.getNb_def(carte) + planete.getNb_off(carte))/carte.get_planet_by(voisine).getNb_off(carte)

            if nb_a_envoyer < 100:
                toOrderMsg(carte.id_joueur, nb_a_envoyer, voisine, planete.identifiant)

#2) planetes prod éloignées des miennes
    for pla in liste_pla_prod:
        if carte.planetes_voisines('neutre', pla)==carte.planetes_voisines('toutes', pla):
            #a) recherche de ma planete la plus proche de la planete prod examinée
            cout_1, chemin_2=chemin_le_moins_couteux(pla.identifiant, carte.mes_planetes()[0])
            for pla_m in carte.mes_planetes():
                cout_a, chemin_a=carte.chemin_le_moins_couteux(pla_m.identifiant,pla.identifiant)
                if cout_a<cout_1:
                    cout_1=cout_a
                    chemin_1=chemin_a
            #b)Recherche de la planete ennemie la plus proche de la planete prod examinée

                #Initialisation plus compliquée que le cas précédent (a voir si je n'ai
                #pas oublié un cas qui risque de provoquer une boucle infinie...)
            pla_ini=None
            i=0
            while pla_ini==None:
                i+=1
                if carte.liste_planete[i].getProprietaire(carte)!=carte.couleur:
                    pla_ini=carte.liste_planetes[i]
                                                     
            cout_2, chemin_2=chemin_le_moins_couteux(pla.identifiant,pla_ini.identifiant)
            for pla_enn in carte.liste_planete:
                cout_b,chemin_b=carte.chemin_le_moins_couteux(pla_enn.identifiant, pla.identifiant)
                if cout_b<cout_2:
                    cout_2=cout_b

                    #3) Maintenant on compare les longeurs des 2 chemins
            if cout_1<cout_2:
                j=0
                for plapla in chemin_1:
                    j+=1 #Permet d'accéder à la planète d'après
                    if carte.planetes_voisines('amies', carte.get_planete_by(plapla))==carte.planetes_voisines('toutes', carte.get_planete_by(plapla)):
                        toOrderMsg(carte.id_joueur, 100, plapla, chemin_1[j])
                    else:
                        nb_a_envoyer_2=100*(carte.get_planete_by(chemin_1[j]).getNb_def(carte) + carte.get_planete_by(chemin_1[j]).getNb_off(carte))/carte.get_planete_by(plapla).getNb_off(carte)
                        if nb_a_envoyer_2<100:
                            toOrderMsg(carte.id_joueur, nb_a_envoyer, plapla, chemin_1[j])

#A faire boucler si on veut tout conquérir!! Ne vérifie pas la menace ennemie...
#Elle lance une attaque sur le voisin le moins défendu de chacune de mes planètes                            
def offensive_vague(carte):
    mes_planetes=carte.mes_planetes()
    
    for pla in mes_planetes:
        #trouver voisin le moins défendu de ma planete examinée
            #initialisation super relou :(
        _,pp=carte.planetes_voisines('ennemies', pla)
        defense=carte.get_planete_by(pp[0]).getNb_off(carte)+carte.get_planete_by(pp[0]).getNb_def(carte)
        for voisin in pp:
            
            def_1=carte.get_planete_by(voisin).getNb_off(carte)+carte.get_planete_by(voisin).getNb_def(carte)
            if def_1<defense:
                defense=def_1
                vois=voisin
            #attaque du voisin le plus faible (que si ma planete est plus forte)
        #détermination unités à envoyer (voir si liste_aretes existe et si la cadence est remplie...)
        i=0
        while (carte.liste_aretes[i].extremites[0]!=pla.identifiant or carte.liste_aretes[i].extremites[1]!=pla.identifiant) and (carte.liste_aretes[i].extremites[0]!=vois or carte.liste_aretes[i].extremites[1]!=vois):
            i+=1
        cad=vois.cadence_prod
        if cad==3:
            mult=1
        elif cad==2:
            mult=2/3
        else:
            mult=1/2

        sup=carte.liste_arete[i].distance*(mult+1/2) #sup=production supplementaire pendant déplacement(mult pour prod offensive, 1/2 pour prod défensive)
        nb_a_envoyer_2=100*(carte.get_planete_by(vois).getNb_def(carte) + carte.get_planete_by(vois).getNb_off(carte) + sup)/pla.getNb_off(carte)
        #Si manque d'infos ou erreur difficile à corriger, remplacer de i=0 jusqu'à la ligne au-dessus d'ici par:
        #nb_a_envoyer_2=100*(carte.get_planete_by(vois).getNb_def(carte) + carte.get_planete_by(vois).getNb_off(carte))/pla.getNb_off(carte)

        if nb_a_envoyer<100:
            toOrderMsg(carte.id_joueur, nb_a_envoyer, pla.identifiant, vois)

#La première qu'on a fait fonctionner
def offensive_bourrin(carte):
    print("ICIIIIIIIIIIIIIIIIII")

    while (not (carte.game_over or carte.end_of_game)):        #mise en place des stratégies et du robot
        mes_planetes=carte.mes_planetes()
        for planete in mes_planetes:

            i = 0
            l,liste=carte.planetes_voisines('toutes',planete)
            while i < l and carte.get_planete_by(liste[i]).getProprietaire(carte) == carte.couleur:
                i += 1
                
                if i != l:
                    toOrderMsg(carte.id_joueur,100, planete.identifiant, liste[i])

#considère qu'il existe carte.liste_aretes donc inutile si ce n'est pas le cas...
#attend avant de conquérir une planete neutre si elle est attaquée
                    #utilise le getteur flotte
                    
def offensive_vague_neutre(carte):
    mes_planetes=carte.mes_planetes()
    
    for pla in mes_planetes:
        #trouver voisin neutre le moins défendu de ma planete examinée
            #initialisation super relou :(
        _,pp=carte.planetes_voisines('neutre', pla)
        defense=carte.get_planete_by(pp[0]).getNb_off(carte)+carte.get_planete_by(pp[0]).getNb_def(carte)
        for voisin in pp:
            
            def_1=carte.get_planete_by(voisin).getNb_off(carte)+carte.get_planete_by(voisin).getNb_def(carte)
            if def_1<defense:
                defense=def_1
                vois=voisin
        #fonction d'attaque avec attente
        for arete in carte.liste_aretes:
            if arete.extremites[0]==vois or arete.extremites[1]==vois:
                f= arete.getFlotte_traverse(carte)
                if len(f)>0:
                    #voir si c'est correct et judicieux...
                    #le /2 c'est parce que j'ai la flemme de chercher la longueur de l'arete ma_planete---planete_neutre
                    time.sleep(arete.distance/2)
        #a voir si  c'est bien calculé :p...
            for i in f:
                if i.couleur:
                    som_flottes+=i.nb_unites
            nb_a_envoyer=100*(carte.get_planete_by(vois).getNb_def(carte) + carte.get_planete_by(vois).getNb_off(carte)+som_flottes)/pla.getNb_off(carte)
            if nb_a_envoyer<100:
                toOrderMsg(carte.id_joueur, nb_a_envoyer, pla.identifiant, vois)
