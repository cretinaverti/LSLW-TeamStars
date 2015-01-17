from tkinter import *
from classes import *
from initialisation import *

global carte
print(carte)

#création d'un faux init
debut = "INIT20ac18ab-6d18-450e-94af-bee53fdc8fcaTO2[1];1;7CELLS:"
p1 = "1(150,500)'1'50'10'II,"
p2 = "2(300,600)'1'50'10'I,"
p3 = "3(600,450)'1'50'10'I,"
p4 = "4(600,150)'1'50'10'I,"
p5 = "5(800,300)'1'50'10'I,"
p6 = "6(900,450)'1'50'10'I,"
p7 = "7(1000,150)'1'50'10'II;8LINES:"
debut += p1 + p2 + p3 + p4 + p5 + p6 + p7



def creerPlanete(z,x,y,rayon):
    z.create_oval(x-(50*rayon),y-(50*rayon),x+(50*rayon),y+(50*rayon),outline='white',fill='black',width=4)



 
Fenetre=Tk()	#La fonction Tk() du module Tkinter permet de créer une fenêtre qui se nomme Fenetre
Fenetre.title("Mon programme avec Tkinter") # Donne un titre à la fenêtre (par défaut c'est Tk)
 
# Dans Fenetre nous allons créer un objet type Canvas qui se nomme zone_dessin
# Nous donnons des valeurs aux propriétés "width", "height", "bg", "bd", "relief"
z = Canvas(Fenetre,width=1200,height=700,
			            bg='black',bd=8,relief="ridge")
z.pack() #Affiche le Canvas

z.create_line(150,500,300,600,fill='white',width=4)
z.create_line(150,500,600,450,fill='white',width=4)
z.create_line(600,450,600,150,fill='white',width=4)
z.create_line(600,450,800,300,fill='white',width=4)
z.create_line(600,450,900,450,fill='white',width=4)
z.create_line(800,300,900,450,fill='white',width=4)
z.create_line(800,300,1000,150,fill='white',width=4)
z.create_line(600,150,1000,150,fill='white',width=4)


creerPlanete(z,150,500,2)
creerPlanete(z,300,600,1)
creerPlanete(z,600,450,1)
creerPlanete(z,600,150,1)
creerPlanete(z,800,300,1)
creerPlanete(z,900,450,1)
creerPlanete(z,1000,150,2)

z.create_text(50,300-15,fill="white",width=100,text="5")
i = z.create_text(50,300,fill="white",width=100,text="0")
z.create_text(50,300+15,fill="white",width=100,text="II")







# boutons_sortir est un widget de type "Button"
# dont nous définissons les propriétés "text" et "command")
bouton_sortir= Button(Fenetre,text="Sortir",command=Fenetre.destroy)
# la commande "destroy" appliquée à la fenêtre détruit l'objet "Fenetre" et clôture le programme
bouton_sortir.pack()
 
Fenetre.mainloop() # Lancement de la boucle du programme, en attente d'événements (clavier, souris,...) 
