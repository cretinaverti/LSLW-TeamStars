import re
from classes import *

#m = re.match(r"(\w+)","ma maman est chez moi")
#print(m.group(1))


#id du match
def getMatchId(state):
    m = re.match("STATE([0-9a-zA-Z-]+)IS[0-9];",state)
    return m.group(1)

#nombre de joueurs
def getNbJoueurs(state):
    m = re.match(".*IS(\d);",state)
    return m.group(1)

#nombre de planètes
def getNbPlanetes(state):
    m = re.match(".*;(\d)CELLS",state)
    return m.group(1)

#tableau des planetes
def getTabPlanetes(state):
    m = re.match(".*:(.*);",state).group(1)
    sPlanete = re.split(",",m)
    tab = []
    for chaine in sPlanete:
        ide = int(re.match("^\d+",chaine).group(0))
        proprio = int(re.match("^\d+\[(\d)\]",chaine).group(1))
        offs = int(re.match(".*\](\d+)",chaine).group(1))
        defs = int(re.match(".*(\d)$",chaine).group(1))
        tab.append(Planete(ide,0,0,offs,defs,proprio))
    return tab

#retourne un tableau d'aretes sur lesquelles il y a du mouvement
def getMoves(state):
    tab = [] #contiendra les aretes à la fin
    m = re.match(".*MOVES:(.*)",state).group(1)
    tabAretes = re.split(",",m)
    print(tabAretes)
    for areteS in tabAretes:#la on a une chaine contenant les mouvements sur une arete
        arete = Arete(0)
        arete.extremites = (int(re.match("\d+",areteS).group(0)),int(re.match(".*'(\d)+",areteS).group(1)))
        movesS = re.match("\d+(.*)'\d+",areteS).group(1)
        tabMoveS = re.split("'",movesS)
        for flotteS in tabMoveS:#la on a un tableau de flottes à décoder sur une arete
            f = Flotte(0,0,0)
            if(flotteS[0] == '>'):
                f.direction = arete.extremites[1]
            else:
                f.direction = arete.extremites[0]
            f.nb_unite = re.match(".(\d+)\[",flotteS).group(1)
            f.couleur = re.match(".*\[(\d+)\]",flotteS).group(1)
            f.distance = re.match(".*@(\d+)$",flotteS).group(1)
            arete.flotte_traverse.append(f)
        tab.append(arete)
    return tab


state = "STATE20ac18ab-6d18-450e-94af-bee53fdc8fcaIS2;3CELLS:1[2]12'4,2[2]15'2,3[1]33'6;4MOVES:1<5[2]@232'>6[2]@488'>3[1]@4330'2,1<10[1]@2241'3"

print(getMoves(state))
