from tkinter import *



def creerPlanete(z,x,y,rayon):
    z.create_oval(x-(50*rayon),y-(50*rayon),x+(50*rayon),y+(50*rayon),outline='white',fill='black',width=4)



 
Fenetre=Tk()	#La fonction Tk() du module Tkinter permet de créer une fenêtre qui se nomme Fenetre
Fenetre.title("Mon programme avec Tkinter") # Donne un titre à la fenêtre (par défaut c'est Tk)
 
# Dans Fenetre nous allons créer un objet type Canvas qui se nomme zone_dessin
# Nous donnons des valeurs aux propriétés "width", "height", "bg", "bd", "relief"
z = Canvas(Fenetre,width=500,height=500,
			            bg='black',bd=8,relief="ridge")
z.pack() #Affiche le Canvas

z.create_line(50,300,200,450,fill='white',width=4)
z.create_line(50,300,250,250,fill='white',width=4)
z.create_line(250,250,250,50,fill='white',width=4)
z.create_line(250,250,350,150,fill='white',width=4)
z.create_line(250,250,400,250,fill='white',width=4)
z.create_line(350,150,400,250,fill='white',width=4)
z.create_line(350,150,450,50,fill='white',width=4)
z.create_line(250,50,450,50,fill='white',width=4)


creerPlanete(z,450,50,2)
creerPlanete(z,350,150,1)
creerPlanete(z,250,250,1)
creerPlanete(z,400,250,1)
creerPlanete(z,50,300,2)
creerPlanete(z,200,450,1)
creerPlanete(z,250,50,1)

z.create_text(50,300-15,fill="white",width=100,text="5")
i = z.create_text(50,300,fill="white",width=100,text="0")
z.create_text(50,300+15,fill="white",width=100,text="II")



z.delete(i)



# boutons_sortir est un widget de type "Button"
# dont nous définissons les propriétés "text" et "command")
bouton_sortir= Button(Fenetre,text="Sortir",command=Fenetre.destroy)
# la commande "destroy" appliquée à la fenêtre détruit l'objet "Fenetre" et clôture le programme
bouton_sortir.pack()
 
Fenetre.mainloop() # Lancement de la boucle du programme, en attente d'événements (clavier, souris,...) 
