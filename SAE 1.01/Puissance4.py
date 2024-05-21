from Utile import *
from Score import *


def plateau(plat:list[list[str]]):
    """Création du plateau de jeu
    
    On crée 6 listes de 7 indices dans le plateau qu'on fait afficher à la suite
    
    Args:
        plat (list[list[str]]): plateau du jeu
    """
    a=5
    for i in plat:
        print("+---+---+---+---+---+---+---+")
        for x in i:
            print("| ",x, end='')
        print("|", a)
        a=a-1
    print("+---+---+---+---+---+---+---+")
    print("  0   1   2   3   4   5   6")




def joueur(plat:list[list[str]],Nom : str, signe:str): 
    """Procédure qui demande au joueur de jouer
    
    Un message s'affiche pour demander au joueur de choisir une colonne
    Si la case est vide, on affiche le pion dans cette case, sinon on demande de changer de case.

    Args:
        plat (list[list[str]]): plateau du jeu
        Nom (str): Nom du joueur
        signe (str): Signe du joueur (jaune ou rouge)
    """
    col:int
    li:int
    li = 5
    print("A "+Nom+" de jouer")
    plateau(plat)
    col=int(input("Numéro de la colonne ( Entre 0 et 6 ): "))
        
    while (col < 0 or col >6):
        col=int(input("Numéro de la colonne ( Entre 0 et 6 ): ")) 
    for i in plat:
        while plat[int(li)][int(col)]!=" " and li>=0:
            li = li-1
        if li == -1:
            col=int(input("Colonne complète, choisissez une autre colonne (entre 0 et 6) : "))
            li = 5
            
    plat[int(li)][int(col)]= signe
    plateau(plat)




def verif(plat:list[list[str]])-> int:
    """Fonction qui vérifie si le joueur a gagné
    
    Vérifie toutes les combinaisons possibles si les joueurs ont gagné ou non
    et renvoie 1 si les conditions sont vérifiées et validées, sinon 0 et le jeu continue

    Args:
        plat (list[list[str]]): plateau du jeu

    Returns:
        int: 0 ou 1
    """
    i : int
    j : int
    gagne : int 
    gagne = 0
    #pour les lignes
    for i in range(0,7):
        for j in range(0,3):
            if plat[j][i]==plat[j+1][i] and plat[j+1][i]==plat[j+2][i] and plat[j+2][i] == plat[j+3][i] and plat[j][i]!= " ":
                gagne = 1
                return gagne
    #Pour les colonnes
    for j in range(0,6):
        for i in range(0,4):
            if plat[j][i]==plat[j][i+1] and plat[j][i+1]==plat[j][i+2] and plat[j][i+2]==plat[j][i+3] and plat[j][i]!= " ":
                gagne = 1
                return gagne
    #Pour les diagonales
    for i in range(0,3):
        for j in range(0,4):
                if plat[i][j]==plat[i+1][j+1] and plat[i+1][j+1]==plat[i+2][j+2] and plat[i+2][j+2]== plat[i+3][j+3] and plat[i][j]!= " ":
                    gagne = 1
                    return gagne
    for i in range(0,3):
        for j in range(0,4):
            if plat[i+3][j]==plat[i+2][j+1] and plat[i+2][j+1]==plat[i+1][j+2] and plat[i+1][j+2]== plat[i][j+3] and plat[i+3][j]!= " ":
                gagne = 1
                return gagne
    return gagne





def egal(plat:list[list[str]])-> int:
    """Fonction qui vérifie s'il y a égalité, toutes les cases sont remplies
    
    Vérifie si toutes les cases sont complètes ou non
    si c'est le cas, on renvoie un message égalité et on arrète le jeu
    sinon on renvoie 0 et le jeu continue

    Args:
        plat (list[list[str]]): plateau du jeu

    Returns:
        int: 0 ou 1
    """
    egalite :int
    
    egalite = 0
    for j in range(6):
        for i in plat[j]:
            if i == " ":
                egalite = 0
            else:
                egalite = egalite + 1
    if egalite == 42 :
        print("Egalité ! Aucun joueur n'a gagné.")  
        return 1
    else :
        return 0



def Puissance4 (Nom1 : str, Nom2:str, ListeScore : list[Joueur],plat : list[list[str]]) :
    """ Procédure qui permet de faire jouer les joueurs et qui vérifie s'il y a un gagnant
    
    Procédure principal qui va utiliser toutes les procédures et qui va permettre le fonctionnement
    du jeu

    Args:
        Nom1 (str): Nom du joueur 1
        Nom2 (str): Nom du joueur 2
        ListeScore (list[Joueur]): Liste contenant tous les scores de tous les joueurs
        plat : list[list[str]]: Le plateau vide qu'on rempliera durant la partie
    """
    v : bool        #Initialisation des variables
    score1 : int
    score2 : int
    indice : int
    score1 = 0
    score2 = 0
    v = True
    jaune="\033[0;93mO\033[0m"
    rouge= "\033[0;31mO\033[0m"
    print(Nom1 +" joue avec les jaunes et "+Nom2+" joue avec les rouges")
    
    while v ==True :                            #Tant que le booléen reste True
        joueur(plat,Nom1,jaune)                           #On lance la procédure pour faire jouer le joueur 1
        if verif(plat) == 1:             #Si la vérification du score du joueur 1 renvoie 1 (uniquement quand le joueur gagne)
            v = False 
            print(Nom1+", tu as gagné !")

            score1 = score1 +10
            indice =Recherche(ListeScore, Nom1)
            ListeScore[indice].ScorePuissance4 = ListeScore[indice].ScorePuissance4 + score1
            print("Score:\n",Nom1+":",score1,"\n",Nom2 +":",score2)
        elif egal(plat) == 1:                   #Sinon on vérifie si il y a égalité ou non
            v =False
        else:
            if verif(plat) == 0:         #On fait la même chose avec le joueur 2
                joueur(plat,Nom2,rouge)
                if verif(plat) == 1:
                    v =False
                    print(Nom2+", tu as gagné !")

                    score2 = score2 +10
                    indice = Recherche(ListeScore, Nom2)
                    ListeScore[indice].ScorePuissance4 = ListeScore[indice].ScorePuissance4 + score2
                    print("Score:\n",Nom1+":",score1,"\n",Nom2 +":",score2)
                    
                elif egal(plat) == 1:
                    v = False