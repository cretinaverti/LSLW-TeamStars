class Carte:
	"""docstring for Carte"""
	def __init__(self, nb_joueur, id_joueur):
                self.liste_planetes = []
                self.liste_aretes = []
                self.liste_joueurs = []
                self.id_joueur = id_joueur
                self.nb_joueur = nb_joueur
		# Liste d'aretes:
		# 	matrice d'Aretes


	def extremites(self):
		extremites = []

		for planete in liste_planetes:
			if len(planete.liste_voisins) == 1:
				extremites.append(planete)
		return extremites


		

class Planete:
	"""docstring for Cellule"""
	def __init__(self, ide, unit_max_off, unit_max_def, offs, defs, proprio, cadence_prod):
		self.identifiant = ide
		self.proprietaire = proprio
		self.unit_max_off = unit_max_off
		self.unit_max_def = unit_max_def
		self.liste_voisins = []
		# [(Arete, Planete), ...]

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


	# Sert à la méthode sort(); pour comparer les planetes entre eux, 
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
		
		
