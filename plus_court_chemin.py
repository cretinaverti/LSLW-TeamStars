def plus_court_chemin(p,a,s): #on passe en paramètre la liste des planetes, la liste des aretes et le sommet duquel on part
    dist = [len(p) * [100000]]
    dist[0][s] = 0
    pred = [len(p) * ['-']]
    som = [s]
    etp = 0

    while etp <= len(p):
        s1 = []
        for i in som:
            s1.append(i)
        etp += 1
        dist.append([])
        pred.append([])
        for i in range(len(dist[etp-1])):
            dist[etp].append(dist[etp-1][i])
            pred[etp].append(pred[etp-1][i])
        for i in p: #parcours des distances (application de l'algo)
            if i != s:
                for j in s1: #on ne passe que par les sommets djà connu à cette étape
                    for k in len(a): 
                        if a[k] == (j,i) or a[k] == (i,j): #on vérifie qu'il exites un chemin entre le sommet connu et les autres inconnu
                            if (dist[etp][j] + a[k].distance < dist[etp][i]): #on recherche la plus petite distance
                                dist[etp][i] = dist[etp][j] + a[k].distance
                                pred[etp][i] = j
                                if i not in som: #on rajoute le sommet s'il n'exite pas déjà
                                    som.append(i)
        cpt = 0
        for i in p: #comparaison des 2 dernières lignes pour l'arrêt de l'algo
            if dist[etp][i] == dist[etp-1][i]:
                cpt += 1
        if cpt == len(p): #arrêt si les 2 dernières lignes sont identiques
            etp = len(p)+1
    return (dist[len(dist)-1],pred[len(dist)-1]) #on retourne la dernière ligne de la distance et la dernière des prédécesseur

def plus_court_chemin(d,x): #d est le résultat de la fonction précédente pour un sommet précis
    #x est l'autre extrémité piur laquelle on recherche le plus chemin.
    #là on retourne une chaine successive des sommets à parcourir
    chaine = str(x)
    if d[1][x] == '-':
        chaine = ""
    else:
        chaine = plus_court_chemin(d,d[1][x]) + "\t" + chaine
    return chaine
