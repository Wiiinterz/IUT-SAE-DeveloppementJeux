from Utile import *
from Score import *



def plateau(plat:list[list[str]]):
    """Création du plateau de jeu
    
    On crée 3 listes de 3 indices dans le plateau qu'on fait afficher à la suite
    
    Args:
        plat (list[list[str]]): plateau du jeu
    """
    a=0
    for i in plat:
        print("|---|---|---|")
        for x in i:
            print("|",x, end=' ')
        print("|",a)
        a= a+1
    print("|---|---|---|")
    print("  0   1   2")

    


def joueur(plat:list[list[str]],Nom : str, signe: str ): 
    """Procédure qui demande au joueur de jouer
    
    Un message s'affiche pour demander au joueur de choisir une ligne et une colonne
    Si la case est vide, on affiche le signe dans cette case, sinon on demande de changer de case.

    Args:
        plat (list[list[str]]): plateau du jeu
        Nom (str): Nom du joueur
        signe (str): Signe du joueur (croix ou rond)
    """
    col:int
    li:int

    print("A "+Nom+" de jouer")
    plateau(plat)
    li=int(input("Numero de la ligne ( Entre 0 et 2 ): "))
    col=int(input("Numéro de la colonne ( Entre 0 et 2 ): "))

    while (col < 0 or col >2) or (li<0 or li>2):
        li=int(input("Numero de la ligne ( Entre 0 et 2 ): "))
        col=int(input("Numéro de la colonne ( Entre 0 et 2 ): "))

    while plat[int(li)][int(col)]!=" ":
        print("Saisissez une autre case !")
        li=int(input("Numéro de la ligne ( Entre 0 et 2 ): "))
        col=int(input("Numéro de la colonne ( Entre 0 et 2 ): "))
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
    gagne : int
    i : int
    gagne = 0

    for i in range(0,3):
        if plat[0][i]==plat[1][i] and plat[2][i] == plat[0][i] and plat[0][i]!= " ":
            gagne = 1
            return gagne
        elif plat[i][0]==plat[i][1] and plat[i][2] == plat[i][0] and plat[i][0]!= " ":
            gagne = 1
            return gagne
    if plat[0][0]==plat[1][1] and plat[2][2] == plat[0][0] and plat[0][0]!= " ":
        gagne = 1
        return gagne
    elif plat[0][2]==plat[1][1] and plat[2][0] == plat[0][2] and plat[0][2]!= " ":
        gagne = 1
        return gagne
    return gagne




def egal(plat:list[list[str]]) -> int:
    """Fonction qui vérifie s'il y a égalité, toutes les cases sont remplies
    
    Vérifie si toutes les cases sont complètes ou non
    si c'est le cas, on renvoie un message égalité et on arrète le jeu
    sinon on renvoie 0 et le jeu continue

    Args:
        plat (list[list[str]]): plateau du jeu

    Returns:
        int: 0 ou 1
    """
    
    i:str
    j : int
    egalite :int
    
    egalite = 0
    for j in range(3):
        for i in plat[j]:
            if i == " ":
                egalite = 0
            else:
                egalite = egalite + 1
    if egalite == 9 :
        print("Egalité ! Aucun joueur n'a gagné.")  
        return 1
    else: 
        return 0

def Morpion(Nom1 : str, Nom2:str, ListeScore : list[Joueur],plat : list[list[str]]):
    """ Procédure qui permet de faire jouer les joueurs et qui vérifie si il y a un gagnant
    
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
    croix ="X"
    rond="O"
    print(Nom1 +" joue avec O et "+Nom2+" joue avec X")     #Attributions des symboles
    
    while v ==True :                            #Tant que le booléen reste True
        joueur(plat,Nom1,rond)                          #On lance la procédure pour faire jouer le joueur 1
        if verif(plat) == 1:             #Si la vérification du score du joueur 1 renvoie 1 (uniquement quand le joueur gagne)
            v = False 
            print(Nom1+", tu as gagné !")
            score1 = score1 +10
            indice =Recherche(ListeScore, Nom1)                                         #On fait arrêter le programme + enregistrement du score de joueur 1
            ListeScore[indice].ScoreMorpion = ListeScore[indice].ScoreMorpion + score1 
            print("Score:\n",Nom1+":",score1,"\n",Nom2 +":",score2)                     
        elif egal(plat) == 1:                   #Sinon on vérifie si il y a égalité ou non
            v =False
        else:
            if verif(plat) == 0:         #On fait la même chose avec le joueur 2
                joueur(plat,Nom2,croix)
                if verif(plat)==1:
                    v= False
                    print(Nom2+", tu as gagné !")
                    score2 = score2 +10
                    
                    indice = Recherche(ListeScore, Nom2)                                        #Enregistrement du nouveaux score de joueur 2
                    ListeScore[indice].ScoreMorpion = ListeScore[indice].ScoreMorpion + score2
                    print("Score:\n",Nom1+":",score1,"\n",Nom2 +":",score2)
                elif egal(plat) == 1:
                    v = False