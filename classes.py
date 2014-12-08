class Carte(object):
	"""docstring for Carte"""
	def __init__(self, nb_joueur, planetes = [], aretes = [], id_joueur):
		self.liste_planetes = planetes
		self.liste_aretes = aretes
		self.liste_joueurs = liste_joueurs
                self.id_joeur = id_joueur
		# Liste d'aretes:
		# 	matrice d'Aretes

		

class Planete():
	"""docstring for Cellule"""
	def __init__(self, ide, unit_max_off, unit_max_def, offs, defs, proprio):
		self.identifiant = ide
		self.proprietaire = proprio
		self.unit_max_off = unit_max_off
		self.unit_max_def = unit_max_def
		self.liste_voisins = []
		# [(Arete, Planete), ...]

		self.cadence_prod = 0
		self.nb_off = offs
		self.nb_def = defs
		

        #Permet d'afficher une planète
	def __repr__(self):
	  s = "Planete "+str(self.identifiant)+"\n"
	  s += "Proprio : "+str(self.proprietaire)+"\n"
	  s += "offs : "+str(self.nb_off)+"\n"
	  s += "defs : "+str(self.nb_def)+"\n"
	  return s

class Arete():
	"""docstring for Arete"""
	def __init__(self, distance):
		self.flotte_traverse = []
		self.distance = distance
		self.extremites = None


class Flotte():
	"""docstring for Flotte"""
	def __init__(self, nb_unite, couleur, direction):	
		self.nb_unite = nb_unite
		self.couleur = couleur
		self.destination = direction
		self.distance = 0

		self.position_courante = 0
		
		
