from tkinter import *
from classes import *


def creerPlanete(z,x,y,rayon,color):
    return z.create_oval(x-(rayon/4),y-(rayon/4),x+(rayon/4),y+(rayon/4),outline=color,fill='black',width=4)


def make_init(carte):

    leY = 15
    #création des lignes
    for arete in carte.liste_aretes:
        carte.map.create_line(carte.liste_planetes[arete.extremites[0]].x/25+100,
                      carte.liste_planetes[arete.extremites[0]].y/25+100,
                      carte.liste_planetes[arete.extremites[1]].x/25+100,
                      carte.liste_planetes[arete.extremites[1]].y/25+100,fill='white',width=4)

        #création des déplacements
        # début = (700,20)

        leY += 10
        for i in range(0,5):
            if i==0:
                tt = "arete "+str(arete.ide)+" de "+str(arete.extremites[0])+" vers "+str(arete.extremites[1])
                arete.flottes.append(carte.map.create_text(700,leY,fill="white",width=400,anchor="nw",text=tt))
            else:
                arete.flottes.append(carte.map.create_text(700,leY,fill="white",width=400,anchor="nw",text=""))
            leY += 20
        

    #création des planetes
    for planete in carte.liste_planetes:
        planete.contour = creerPlanete(carte.map,planete.x/25+100,planete.y/25+100,planete.rad,"white")

        cad = ""
        for i in range(0,planete.cadence_prod):
            cad += "I"
        carte.map.create_text(planete.x/25+100,planete.y/25+100+15,fill="white",width=100,text=cad)
        planete.deff = carte.map.create_text(planete.x/25+100,planete.y/25+100,fill="white",width=100,text="0")
        planete.off  = carte.map.create_text(planete.x/25+100,planete.y/25+100-15,fill="white",width=100,text="0")

        #identifiant des planetes
        carte.map.create_text(planete.x/25+100+40,planete.y/25+100+15,fill="white",width=100,text=planete.identifiant)

    
    



def boucle_principale(carte):
    Fenetre=Tk()
    Fenetre.title("LSLW")
    carte.map = Canvas(Fenetre,width=1200,height=700,bg='black',bd=8,relief="ridge")
    carte.map.pack()

    make_init(carte)
   
    # boutons_sortir est un widget de type "Button"
    # dont nous définissons les propriétés "text" et "command")
    bouton_sortir= Button(Fenetre,text="Sortir",command=Fenetre.destroy)
    # la commande "destroy" appliquée à la fenêtre détruit l'objet "Fenetre" et clôture le programme
    bouton_sortir.pack()
 
    Fenetre.mainloop() # Lancement de la boucle du programme, en attente d'événements (clavier, souris,...) 



'''
#création d'un faux init
debut = "INIT20ac18ab-6d18-450e-94af-bee53fdc8fcaTO2[1];1;7CELLS:"
p1 = "1(150,500)'2'50'10'II,"
p2 = "2(300,600)'1'50'10'I,"
p3 = "3(600,450)'1'50'10'I,"
p4 = "4(600,150)'1'50'10'I,"
p5 = "5(800,300)'1'50'10'I,"
p6 = "6(900,450)'1'50'10'I,"
p7 = "7(1000,150)'2'50'10'II;8LINES:"
debut += p1 + p2 + p3 + p4 + p5 + p6 + p7
l1 = "1@5426OF2,"
l2 = "1@7238OF3,"
l3 = "3@6530OF4,"
l4 = "3@5211OF5,"
l5 = "3@12382OF6,"
l6 = "6@5211OF5,"
l7 = "5@7188OF7,"
l8 = "4@13800OF7"
init = debut + l1+l2+l3+l4+l5+l6+l7+l8

init_pooo(init)

Fenetre=Tk()
Fenetre.title("LSLW")
z = Canvas(Fenetre,width=1200,height=700,bg='black',bd=8,relief="ridge")
z.pack()
'''

'''



z.create_text(50,300-15,fill="white",width=100,text="5")
i = z.create_text(50,300,fill="white",width=100,text="0")
z.create_text(50,300+15,fill="white",width=100,text="II")


'''




