from tkinter import *
 
Fenetre=Tk()	#La fonction Tk() du module Tkinter permet de créer une fenêtre qui se nomme Fenetre
Fenetre.title("Mon programme avec Tkinter") # Donne un titre à la fenêtre (par défaut c'est Tk)
 
# Dans Fenetre nous allons créer un objet type Canvas qui se nomme zone_dessin
# Nous donnons des valeurs aux propriétés "width", "height", "bg", "bd", "relief"
zone_dessin = Canvas(Fenetre,width=500,height=500,
			            bg='yellow',bd=8,relief="ridge")
zone_dessin.pack() #Affiche le Canvas
 
#Nous allons maintenant utiliser quelques méthodes du widget "zone_dessin"
zone_dessin.create_line(0,0,400,500,fill='red',width=4) # Dessine une ligne
zone_dessin.create_line(0,500,500,0,fill='red',width=4) # Dessine une ligne
zone_dessin.create_rectangle(150,150,350,350,fill='red') # Dessine un rectangle
zone_dessin.create_oval(150,150,350,350,fill='white',width=4) # Dessine un cercle
 
# boutons_sortir est un widget de type "Button"
# dont nous définissons les propriétés "text" et "command")
bouton_sortir= Button(Fenetre,text="Sortir",command=Fenetre.destroy)
# la commande "destroy" appliquée à la fenêtre détruit l'objet "Fenetre" et clôture le programme
bouton_sortir.pack()
 
Fenetre.mainloop() # Lancement de la boucle du programme, en attente d'événements (clavier, souris,...) 
