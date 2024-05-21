from Utile import *
from Score import *
plat=[[" "," "," "],[" "," "," "],[" "," "," "]]

def plateau(plat:list[list[str]]):
    """Création du plateau de jeu

    Args:
        plat (list[list[str]]): On crée 3 listes de 3 indices dans le plateau qu'on fait afficher à la suite
    """
    for i in plat:
        print("|---||---||---|")
        for x in i:
            print("|",x, end=' |')
        print()
    print("|---||---||---|")
    

def joueur1(plat:list[list[str]],Nom1 : str): 
    """Procédure pour faire jouer le joueur 1

    Args:
        plat (list[list[str]]): _description_
    """
    col:int
    li:int

    print("A "+Nom1+" de jouer")
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
    plat[int(li)][int(col)]="O"
    plateau(plat)
        
def joueur2(plat:list[list[str]],Nom2 : str):
    """Procédure pour faire jouer le joueur 2

    Args:
        plat (list[list[str]]): _description_
    """
    li:int
    col:int
    
    print("A "+Nom2+" de jouer")
    plateau(plat)
    li=int(input("Numéro de la ligne ( Entre 0 et 2 ): "))
    col=int(input("Numéro de la colonne ( Entre 0 et 2 ): "))
            
    while (col < 0 or col >2) or (li<0 or li>2):
        li=int(input("Numero de la ligne ( Entre 0 et 2 ): "))
        col=int(input("Numéro de la colonne ( Entre 0 et 2 ): "))
                
    while plat[int(li)][int(col)]!=" ":
        plateau(plat)
        print("Saisissez une autre case !")
        li=int(input("Numéro de la ligne ( Entre 0 et 2 ): "))
        col=int(input("Numéro de la colonne ( Entre 0 et 2 ): "))
    plat[int(li)][int(col)]="X"
    plateau(plat)
        
def verif1(plat:list[list[str]],gagne:int,Nom1 : str):
    """Fonction qui vérifie si le joueur 1 à gagné

    Args:
        plat (list[list[str]]): _description_
        gagne (int): _description_

    Returns:
        _type_: _description_
    """
    gagne = 0
    
    if plat[0][0]=="O" and plat[1][0] == "O" and plat[2][0] == "O":
        gagne = 1
        print(Nom1+", tu as gagné !")
        return gagne
    elif plat[0][1]=="O" and plat[1][1] == "O" and plat[2][1] == "O":
        gagne = 1
        print(Nom1+", tu as gagné !")
        return gagne
    elif plat[0][2]=="O" and plat[1][2] == "O" and plat[2][2] == "O":
        gagne = 1
        print(Nom1+", tu as gagné !")
        return gagne
    elif plat[0][0]=="O" and plat[0][1] == "O" and plat[0][2] == "O":
        gagne = 1
        print(Nom1+", tu as gagné !")
        return gagne
    elif plat[1][0]=="O" and plat[1][1] == "O" and plat[1][2] == "O":
        gagne = 1
        print(Nom1+", tu as gagné !")
        return gagne
    elif plat[2][0]=="O" and plat[2][1] == "O" and plat[2][2] == "O":
        gagne = 1
        print(Nom1+", tu as gagné !")
        return gagne
    elif plat[0][0]=="O" and plat[1][1] == "O" and plat[2][2] == "O":
        gagne = 1
        print(Nom1+", tu as gagné !")
        return gagne
    elif plat[0][2]=="O" and plat[1][1] == "O" and plat[2][0] == "O":
        gagne = 1
        print(Nom1+", tu as gagné !")
        return gagne
    return gagne
        
def verif2(plat:list[list[str]],gagne:int,Nom2 : str):
    """Fonction qui vérifie si le joueur 2 à gagné

    Args:
        plat (list[list[str]]): _description_
        gagne (int): _description_

    Returns:
        _type_: _description_
    """
    gagne = 0
    
    if plat[0][0]=="X" and plat[1][0] == "X" and plat[2][0] == "X":
        gagne = 1
        print(Nom2+", tu as gagné !")
        return gagne
    elif plat[0][1]=="X" and plat[1][1] == "X" and plat[2][1] == "X":
        gagne = 1
        print(Nom2+", tu as gagné !")
        return gagne
    elif plat[0][2]=="X" and plat[1][2] == "X" and plat[2][2] == "X":
        gagne = 1
        print(Nom2+", tu as gagné !")
        return gagne
    elif plat[0][0]=="X" and plat[0][1] == "X" and plat[0][2] == "X":
        gagne = 1
        print(Nom2+", tu as gagné !")
        return gagne
    elif plat[1][0]=="X" and plat[1][1] == "X" and plat[1][2] == "X":
        print(Nom2+", tu as gagné !")
        return gagne
    elif plat[2][0]=="X" and plat[2][1] == "X" and plat[2][2] == "X":
        gagne = 1
        print(Nom2+", tu as gagné !")
        return gagne
    elif plat[0][0]=="X" and plat[1][1] == "X" and plat[2][2] == "X":
        gagne = 1
        print(Nom2+", tu as gagné !")
        return gagne
    elif plat[0][2]=="X" and plat[1][1] == "X" and plat[2][0] == "X":
        gagne = 1
        print(Nom2+", tu as gagné !")
        return gagne
    return gagne
            
def egal(plat:list[list[str]]):
    """Fonction qui vérifie si il y a égalité, toutes les cases sont remplies

    Args:
        plat (list[list[str]]): _description_

    Returns:
        _type_: _description_
    """
    
    i:int
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

#Initialisation Programme morpion
def Morpion(Nom1 : str, Nom2:str, Tableau : list[Joueur]):
    v : bool        #Initialisation des variables
    gagne : int
    score1 : int
    score2 : int

    score1 = 0
    score2 = 0
    v = True
    gagne = 0
    
    print(Nom1 +" joue avec O et "+Nom2+" joue avec X")     #Attributions des symboles
    
    while v ==True :                            #Tant que le booléen reste True
        joueur1(plat,Nom1)                           #On lance la procédure pour faire jouer le joueur 1
        if verif1(plat,gagne,Nom1) == 1:             #Si la vérification du score du joueur 1 renvoie 1 (uniquement quand le joueur gagne)
            v = False 
            score1 = score1 +10
            ScoreMor(Tableau,Nom1,Nom2,score1,score2)                       #On fait arrêter le programme
        elif egal(plat) == 1:                   #Sinon on vérifie si il y a égalité ou non
            v =False
        else:
            if verif1(plat,gagne,Nom1) == 0:         #On fait la même chose avec le joueur 2
                joueur2(plat,Nom2)
                if verif2(plat,gagne,Nom2) == 1:
                    v =False
                    score2 = score2 +10
                    ScoreMor(Tableau,Nom1,Nom2,score1,score2)
                elif egal(plat) == 1:
                    v = False
    
    