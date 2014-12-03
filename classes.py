class Carte(object):
	"""docstring for Carte"""
	def __init__(self, nb_joueur, planetes = []):
		self.planetes = planetes

		self.nb_joueur = nb_joueur

		

class Planete(Carte):
	"""docstring for Cellule"""
	def __init__(self, unit_max_off, unit_max_def, propietaire = None, liste_adj = []):
		self.proprietaire = proprietaire
		self.unit_max_off = unit_max_off
		self.unit_max_def = unit_max_def
		self.liste_adj = liste_adj

		self.cadence_prod = cadence_prod
		self.nb_off = 0
		self.nb_def = 0

class Arete():
	"""docstring for Arete"""
	def __init__(self, distance):
		self.flotte_traverse = []
		self.distance = distance


class Flotte():
	"""docstring for Flotte"""
	def __init__(self, nb_unite, couleur, direction):	
		self.nb_unite = nb_unite
		self.couleur = couleur
		self.direction = direction

		self.position_courante = 0
		
		