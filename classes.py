import threading

class Carte:
            """docstring for Carte"""
            def __init__(self, nb_joueur, id_joueur):
                            self.liste_planetes = [] # liste des planètes de la carte
                            self.liste_aretes = []   # liste des arêtes de la carte
                            # self.liste_flottes = [] #liste des flottes en mouvement, pas encore utilisé
                            self.id_joueur = id_joueur#id de notre joueur (uid de register_pooo)
                            self.nb_joueur = nb_joueur #nombre de joueurs du match
                            self.couleur = 0  # la couleur de notre joueur
                            self.match_id = 0 # id du match
                            self.vitesse = 0  #vitesse du serveur
                            self.game_over = False #true si fin du match
                            self.end_of_game = False #true si fin du jeu, on arête tout
                            
                            self.dict_distances = {}
                            self.dict_unites = {}
                            

                            self.map = None # canevas de l'interface graphique
                            self.carte_a_jour = True #mis à false à chaque state
                            self.threads = [] #tableau des threads
                            self.mutex = threading.Lock() #exclusion mutuelle des attributs modifiés par le state
                            self.majMAP = False


            def get_planete_by(self, id_planete):
                    for pla in self.liste_planetes:
                            if pla.identifiant == id_planete:
                                    return pla

            def get_arete_by(self, id_arete):
                    for arete in self.liste_aretes:
                            if arete.ide == id_arete:
                                    return arete

            def flush_moves(self): #vide toutes les arêtes de leurs flottes
                for arete in self.liste_aretes:
                    arete.flotte_traverse = []





            def graphe_dictionnaire_generator(self, _type):
                    '''
                    Renvoie un dictionnaire de la forme suivantes:
                            Si _type = "t_distances": {id_planete_A: {id_voisin_de_A_1: poids_de_l'arete, id_voisin_de_A_2: poids_de_l'arete, ...}, id_planete_B: ... }
                            Si _type = "t_unites": {id_planete_A: {id_voisin_de_A_1: nb_off+nb_def, id_voisin_de_A_2: nb_off+nb_def, ...}, id_planete_B: ... }
                    '''
                    liste_ide_planetes = []
                    liste_ide_voisins = []
                    liste_poids = []


                    # Pour chaque planètes...
                    for planete in self.liste_planetes:

                            # On ajoute à liste_ide_planetes l'identifiant de la planète;
                            liste_ide_planetes.append(planete.identifiant)
                            
                            # on ajoute les voisins de la la planète courante;
                            _liste_ide_voisins = []
                            for voisin in planete.liste_voisins:
                                    _liste_ide_voisins.append(voisin[1])
                                    
                            # on créer une liste de liste de voisins.
                            liste_ide_voisins.append(_liste_ide_voisins)

                            _liste_poids = []
                            # Cas ou l'on veut la distance.
                            if _type == "t_distances":
                                    for voisin in planete.liste_voisins:
                                            _liste_poids.append(voisin[0])

                            # Cas ou l'on veut la somme des unités défensive et offensive.
                            elif _type == "t_unites":
                                    for voisin in planete.liste_voisins:
                                            _liste_poids.append(self.get_planete_by(voisin[1]).getNb_def(self) + self.get_planete_by(voisin[1]).getNb_off(self))

                            liste_poids.append(_liste_poids)
                    

                    l_dic_p = []
                    for i in range(len(liste_poids)):
                            l_dic_p.append( dict( zip(liste_ide_voisins[i], liste_poids[i]) ) )
                            

                    return dict( zip(liste_ide_planetes, l_dic_p) ) # Mettre "yield" si l'on veut un générateur (~ itérateur).


            def extremites(self):
                            extremites = []

                            for planete in self.getListe_planetes:
                                            if len(planete.getListe_voisins) == 1:
                                                            extremites.append(planete)
                            return extremites

            def planetes_ennemi(self):
            # Retourne la liste des planètes ennemies.
                            planetes_ennemi = []

                            for planete in self.liste_planetes:
                                            if planete.getProprietaire != self.getCouleur or planete.getProprietaire != 0:
                                                            planetes_ennemi.append(planete)

                            return planetes_ennemi

            def mes_planetes(self):
            # Retourne la liste de nos planètes
                            mes_planetes = []

                            for planete in carte.liste_planetes:
                                            if planete.getProprietaire(self) == carte.couleur:
                                                            mes_planetes.append(planete)

                            return mes_planetes



            # Fonctions servant à implémenter l'agorithme de Dijskra.
            def affiche_peres(self, pere, id_planete_A, extremite, trajet):
                    
                    if extremite == id_planete_A:
                            return [id_planete_A] + trajet
                    else:
                            return self.affiche_peres(pere, id_planete_A, pere[extremite], [extremite] + trajet)

            def dijskra(self, _type, etape, id_planete_B, visites, distances, pere, id_planete_A):
                    '''
                    On va utiliser l'algorithme de Dijskra: on calcule la distance minimale entre la planète en argument et une autre planète.
                    _type 			: chaine de caractère précisant le type de dictionnaire que doit utiliser l'algorithme de Dijskra. 
                    etape			: entier correpondant à l'id de la planète en cours d'étude.
                    id_planete_B	: entier.
                    visites			: listes des planetes déjà examinées.
                    distances		: dictionnaire.
                    pere			: dictionnaire.
                    id_planete_A	: entier.

                    '''

                    try:
                            if _type == "t_distances":
                                    self.dict_distances = self.graphe_dictionnaire_generator("t_distances")
                                    _dict = self.dict_distances
                            elif _type == "t_unites":
                                    self.dict_unites = self.graphe_dictionnaire_generator("t_unites")
                                    _dict = self.dict_unites
                    except ValueError:
                            print("Veillez à bien spécifier le type: t_distances ou t_unites.")


                    # Si on est à l'étape finale, on renvoit la distance et la liste 
                    # des planètes qu'il faut parcourir pour atteindre la planete B.
                    if etape == id_planete_B:
                            return distances[id_planete_B], self.affiche_peres(pere, id_planete_A, id_planete_B, [])

                    # Si la liste des visites est nulle, 
                    # on commence l'algorithme en initialisant la distance à 0.
                    if len(visites) == 0:
                            distances[etape] = 0

                    # On regarde les voisins de notre planète (étape).
                    for voisin in _dict[etape]:

                            # Si on ne l'a pas visitée...
                            if voisin not in visites:
                                    dist_voisin = distances.get(voisin, float('inf'))
                                    candidat_dist = distances[etape] + _dict[etape][voisin]

                                    if candidat_dist < dist_voisin:
                                            distances[voisin] = candidat_dist
                                            pere[voisin] = etape

                    visites.append(etape)
                    
                    non_visites = dict((s, distances.get(s, float('inf'))) for s in _dict if s not in visites)
                    noeud_plus_proche = min(non_visites, key = non_visites.get)

                    return self.dijskra(_type, noeud_plus_proche, id_planete_B, visites, distances, pere, id_planete_A)

            def plus_court_chemin(self, id_planete_A, id_planete_B):
                    return self.dijskra("t_distances", id_planete_A, id_planete_B, [], {}, {}, id_planete_A)

            def chemin_le_moins_couteux(self, id_planete_A, id_planete_B):
                    return self.dijskra("t_unites", id_planete_A, id_planete_B, [], {}, {}, id_planete_A)

            def planete_moins_defendue(self):

                            mini = self.mes_planetes()[0].getNb_def(self) + self.mes_planetes()[0].getNb_off(self)
                            ret_pla = self.mes_planetes()[0]

                            for planete in self.mes_planetes():
                                            if (planete.getNb_def(self) + planete.getNb_off(self) < mini) and not(planete.entouree_amis()):
                                                            ret_pla = planete
                                                            mini = planete.getNb_def(self) + planete.getNb_off(self)

                            return ret_pla

            ####
            def planete_la_plus_proche(self, id_planete_A, liste_ide_planetes):

                            l, chemin = self.plus_court_chemin(id_planete_A, liste_ide_planetes[0])
                            cp = _l + self.get_planete(ide_pla).nb_off + self.get_planete(ide_pla).nb_def

                            for ide_pla in liste_ide_planetes:
                                            _l, _ch = self.plus_court_chemin(id_planete_A, ide_pla)
                                            cp = cp + _l + self.get_planete(ide_pla).nb_off + self.get_planete(ide_pla).nb_def
                                            if  _l < l:
                                                            l, chemin = self.plus_court_chemin(id_planete_A, ide_pla)
                            return l, chemin

            def planetes_productrices_a_prendre(self):
                            '''Vérifier la façon d'écrire le niveau de production'''
                            liste_2=[]
                            liste_3=[]
                            for planete in self.getListe_planetes:
                                    if planete.getProprietaire!=self.getCouleur:
                                            if planete.getCadence_prod==2:
                                                    liste_2.append(planete)
                                            if planete.getCadence_prod==3:
                                                    liste_3.append(planete)
                            return (liste_3+liste_2)

            def planete_attaque_rapide(self, planete_ennemie):
                            mes_planetes=self.mes_planetes()
                            for proche in mes_planetes:
                                    dijkstra=plus_court_chemin(proche.identifiant,planete_ennemie.identifiant)

            def flotte_la_plus_dangereuse(self):
                aretes=self.getListe_aretes()
                taille_flotte=0
                for arete_exam in aretes:
                    for flotte in arete_exam.getFlotte_traverse():
                        if flotte.getNb_unite>taille_flotte:
                            taille_flotte=flotte.getNb_unite
                            destination=flotte.getDestination()
                            return destination,taille_flotte

            def planete_voisines(self,x): #retourne les voisins (identifiants) de la planete x (planete)
                            liste = []
                            for i in range (len(self.liste_aretes)):
                                            if x == self.liste_aretes[i].extremites[0]:
                                                            liste.append([self.liste_aretes[i].distance,self.liste_aretes[i].extremites[1]])
                                            elif x == self.liste_aretes[i].extremites[1]:
                                                            liste.append([self.liste_aretes[i].distance,self.liste_aretes[i].extremites[0]])
                            return liste

class Planete:
            """docstring for Cellule"""
            def __init__(self, ide, unit_max_off, unit_max_def, offs, defs, proprio, cadence_prod):
                self.identifiant = ide
                self.proprietaire = proprio
                self.unit_max_off = unit_max_off
                self.unit_max_def = unit_max_def
                self.liste_voisins = []
                # [(Poids_arete, id_Planete), ...]

                self.cadence_prod = cadence_prod
                self.nb_off = offs
                self.nb_def = defs

                #données pour la repr graphique
                self.x = 0
                self.y = 0
                self.rad = 0

                #objets de la repr graphique
                self.contour = None
                self.off = None
                self.deff = None


            #getteurs en exclusion mutuelle
            def getProprietaire(self,carte):
                
                carte.mutex.acquire()
                x = self.proprietaire
                carte.mutex.release()
                return x

            def getNb_off(self,carte):
                carte.mutex.acquire()
                x = self.nb_off
                carte.mutex.release()
                return x

            def getNb_def(self,carte):
                carte.mutex.acquire()
                x = self.nb_def
                carte.mutex.release()
                return x

    # Permet d'afficher une planète
            def __repr__(self):
              s = "Planete "+str(self.identifiant)+"\n"
              s += "Proprio : "+str(self.proprietaire)+"\n"
              s += "offs : "+str(self.nb_off)+"\n"
              s += "defs : "+str(self.nb_def)+"\n"
              return s


            # Sert à la méthode sort(); pour comparer les planetes entre elles, 
            # et donc à trier les planètes suivnt ses critères... 
            def __lt__(self, other):
                            return self.nb_def < other.nb_def

            def __gt__(self, other):
                            return self.nb_def > other.nb_def

            def __eq__(self, other):
                            return self.nb_def == other.nb_def

            def entouree_amis(self, couleur):

                    for voisin in self.liste_voisins:
                            if voisin.getProprietaire!=couleur:
                                    return False
                    return True

            def unique_ennemi_voisin(self, couleur):
                    compteur=0
                    ennemi=None
                    for voisin in self.getListe_voisins:
                            if voisin.getProprietaire!=couleur:
                                    ennemi=voisin
                                    compteur+=1
                            if compteur>1 or compteur==0:
                                    return False
                    return ennemi

            

            def defense_actuelle_planete(self):
                            return (self.getNb_off+self.getNb_def)

            def defense_possible_planetes(self):
                            return (self.getUnit_max_off+self.getUnit_max_def)

            def voisin_ennemi_moins_defendu(self, couleur):
                            nb=self.getListe_voisins[0].defense_actuelle()
                            planete=self.getListe_voisins[0]
                            for i in self.getListe_voisins:
                                            nbr=self.getListe_voisins[i].defense_actuelle()
                                            if i.proprietaire!=couleur and nb>nbr:
                                                            nb=nbr
                                                            planete=i
                            return planete
            def pourcentage_a_expedier(self,but):
                            '''La moitié de ce qu'il a en plus'''
                            if self.defense_actuelle_planete()<but.defense_actuelle_planete():
                                            return 0
                            else:
                                            return(self.defense_actuelle_planete()-but.defense_actuelle_planete())/2                                    

       
                                                                                                                                     
                                                                       
class Arete:
            """docstring for Arete"""
            def __init__(self, distance, ide = None):
                            self.ide = ide
                            self.flotte_traverse = []
                            self.distance = distance
                            self.extremites = []

                            #données pour les déplacements sur l'interface graphique
                            self.flottes = []

            def getFlotte_traverse(self,carte):
                carte.mutex.acquire()
                x = self.flotte_traverse
                carte.mutex.release()
                return x


class Flotte:
            """docstring for Flotte"""
            def __init__(self, nb_unite, couleur, direction):       
                            self.nb_unite = nb_unite
                            self.couleur = couleur
                            self.destination = direction
                            self.distance = 0

                            self.position_courante = 0
                            
                            
