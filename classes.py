class Carte:
	"""docstring for Carte"""
	def __init__(self, nb_joueur, id_joueur):
                self.liste_planetes = []
                self.liste_aretes = []
                self.liste_joueurs = []
                self.id_joueur = id_joueur
                self.nb_joueur = nb_joueur

                self.dict = {}
		# Liste d'aretes:
		# 	matrice d'Aretes



	def graphe_dictionnaire_generator(self):
		'''
		Renvoie un dictionnaire de la forme suivantes:
			{id_planete_A: {id_voisin_de_A_1: poids_de_l'arete, id_voisin_de_A_2: poids_de_l'arete, ...}, id_planete_B: {...}

		'''
		liste_ide_planetes = []
		liste_ide_voisins = []
		liste_poids = []

		for planete in self.liste_planetes:
			liste_ide_planetes.append(planete.identifiant)
			
			_liste_ide_voisins = []
			for voisin in planete.liste_voisins:
				_liste_ide_voisins.append(voisin[1])
				
			liste_ide_voisins.append(_liste_ide_voisins)

			_liste_poids = []
			for voisin in planete.liste_voisins:
				_liste_poids.append(voisin[0])

			liste_poids.append(_liste_poids)
		

		l_dic_p = []
		for i in range(len(liste_poids)):
			l_dic_p.append( dict( zip(liste_ide_voisins[i], liste_poids[i]) ) )
			

		return dict( zip(liste_ide_planetes, l_dic_p) ) # Mettre "yield" si l'on veut un générateur (~ itérateur).



	def extremites(self):
		extremites = []

		for planete in liste_planetes:
			if len(planete.liste_voisins) == 1:
				extremites.append(planete)
		return extremites

	def planetes_ennemi(self):
	# Retourne la liste des planètes ennemies.
		planetes_ennemi = []

		for planete in self.liste_planetes:
			if planete.proprio != self.id_joueur or planete.proprio != 0:
				planetes_ennemi.append(planete)

		return planetes_ennemi

	def mes_planetes(self):
	# Retourne la liste de nos planètes
		mes_planetes = []

		for planete in self.liste_planetes:
			if planete.proprio == self.id_joueur or planete.proprio != 0:
				mes_planetes.append(planete)

		return mes_planetes



	# Fonctions servant à implémenter l'agorithme de Dijskra.
	def affiche_peres(self, pere, id_planete_A, extremite, trajet):
	    
	    if extremite == id_planete_A:
	        return [id_planete_A] + trajet
	    else:
	        return self.affiche_peres(pere, id_planete_A, pere[extremite], [extremite] + trajet)

	def dijskra(self, etape, id_planete_B, visites, distances, pere, id_planete_A):
		
		'''
		On va utiliser l'algorithme de Dijskra: on calcule la distance minimale entre la planète en argument et une autre planète.
		etape			: entier correpondant à l'id de la planète en cours d'étude.
		id_planete_B	: entier.
		visites			: listes des planetes déjà examinées.
		distances		: dictionnaire.
		pere			: dictionnaire.
		id_planete_A	: entier.

 		'''

		# Si on est à l'étape finale, on renvoit la distance et la liste 
		# des planètes qu'il faut parcourir pour atteindre la planete B.
		if etape == id_planete_B:
			return distances[id_planete_B], self.affiche_peres(pere, id_planete_A, id_planete_B, [])

		# Si la liste des visites est nulle, 
		# on commence l'algorithme en initialisant la distance à 0.
		if len(visites) == 0:
			distances[etape] = 0

		# On regarde les voisins de notre planète (étape).
		for voisin in self.dict[etape]:

			# Si on ne l'a pas visitée...
			if voisin not in visites:
				dist_voisin = distances.get(voisin, float('inf'))
				candidat_dist = distances[etape] + self.dict[etape][voisin]

				if candidat_dist < dist_voisin:
					distances[voisin] = candidat_dist
					pere[voisin] = etape

		visites.append(etape)
		
		non_visites = dict((s, distances.get(s, float('inf'))) for s in self.dict if s not in visites)
		noeud_plus_proche = min(non_visites, key = non_visites.get)

		return self.dijskra(noeud_plus_proche, id_planete_B, visites, distances, pere, id_planete_A)

	def plus_court_chemin(self, id_planete_A, id_planete_B):
		return self.dijskra(id_planete_A, id_planete_B, [], {}, {}, id_planete_A)


	def planete_moins_defendue(self):
		''' 1 condition en plus= si planete entourée uniquement d'amies, ignorer la planete'''
		mini = self.mes_planetes()[0].nb_def + self.mes_planetes()[0].nb_off

		for planete in self.mes_planetes():
			if planete.nb_def + planete.nb_off < mini:
				ret_pla = planete
				mini = planete.nb_def + planete.nb_off

		return ret_pla



			


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




class Arete:
	"""docstring for Arete"""
	def __init__(self, distance, ide = None):
		self.ide = ide
		self.flotte_traverse = []
		self.distance = distance
		self.extremites = None


class Flotte:
	"""docstring for Flotte"""
	def __init__(self, nb_unite, couleur, direction):	
		self.nb_unite = nb_unite
		self.couleur = couleur
		self.destination = direction
		self.distance = 0

		self.position_courante = 0
		
		
