from Utile import *
from Score import *
import random


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
            print("|",x, end=" ")
        print("|",a)
        a= a+1
    print("|---|---|---|")
    print("  0   1   2")

def robotdur(plat:list[list[str]],Jouer:bool,signe_rechercher:str, signe_jouer : str):
    """Fonction pour faire jouer le robot difficile

    Args:
        plat (list[list[str]]): plateau du jeu
        Jouer (bool): condition pour savoir où le robot doit mettre son signe selon les conditions
        signe_rechercher (str): le signe change en fonction de s'il attaque ou il défend
        signe_jouer (str): le signe du robot

    Returns:
        bool: savoir si le robot à jouer ou non
    """
    
    print("C'est au tour du robot difficile.")
    
    # Vérifier les lignes pour gagner ou défendre, selon signe_rechercher
    for i in range(3):
        if plat[i][0] == plat[i][1] == signe_rechercher and plat[i][2] == " " and not Jouer:
            plat[i][2] = signe_jouer
            Jouer = True
        elif plat[i][1] == plat[i][2] == signe_rechercher and plat[i][0] == " " and not Jouer:
            plat[i][0] = signe_jouer
            Jouer = True
        elif plat[i][0] == plat[i][2] == signe_rechercher and plat[i][1] == " " and not Jouer:
            plat[i][1] = signe_jouer
            Jouer = True

    # Vérifier les colonnes pour gagner ou défendre, selon signe_rechercher
    for j in range(3):
        if plat[0][j] == plat[1][j] == signe_rechercher and plat[2][j] == " " and not Jouer:
            plat[2][j] = signe_jouer
            Jouer = True
        elif plat[1][j] == plat[2][j] == signe_rechercher and plat[0][j] == " " and not Jouer:
            plat[0][j] = signe_jouer
            Jouer = True
        elif plat[0][j] == plat[2][j] == signe_rechercher and plat[1][j] == " " and not Jouer:
            plat[1][j] = signe_jouer
            Jouer = True

    # Vérifier les diagonales pour gagner ou défendre, selon signe_rechercher
    if plat[0][0] == plat[1][1] == signe_rechercher and plat[2][2] == " " and not Jouer:
        plat[2][2] = signe_jouer
        Jouer = True
    elif plat[1][1] == plat[2][2] == signe_rechercher and plat[0][0] == " " and not Jouer:
        plat[0][0] = signe_jouer
        Jouer = True
    elif plat[0][0] == plat[2][2] == signe_rechercher and plat[1][1] == " " and not Jouer:
        plat[1][1] = signe_jouer
        Jouer = True
    elif plat[0][2] == plat[1][1] == signe_rechercher and plat[2][0] == " " and not Jouer:
        plat[2][0] = signe_jouer
        Jouer = True
    elif plat[1][1] == plat[2][0] == signe_rechercher and plat[0][2] == " " and not Jouer:
        plat[0][2] = signe_jouer
        Jouer = True
    elif plat[0][2] == plat[2][0] == signe_rechercher and plat[1][1] == " " and not Jouer:
        plat[1][1] = signe_jouer
        Jouer = True
        
    return Jouer

def robotfacile(plat:list[list[str]], signe: str ): 
    """Procédure qui fait jouer le robot facile

    Args:
        plat (list[list[str]]): plateau du jeu
        signe (str): signe du robot
    """
    col:int
    li:int
    
    print("Au robot Facile de jouer")
    
    #La case est choisie aléatoirement
    li=random.randint(0,2)
    col=random.randint(0,2)

    #Si la case est déjà prise, il en choisi une autre aléatoirement
    while plat[int(li)][int(col)]!=" ":
        li= random.randint(0,2)
        col=random.randint(0,2)
    plat[int(li)][int(col)]= signe
    

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
    

def verif(plat:list[list[str]],gagne:int):
    """Fonction qui vérifie si le joueur a gagné
    
    Vérifie toutes les combinaisons possibles si les joueurs ont gagné ou non
    et renvoie 1 si les conditions sont vérifiées et validées, sinon 0 et le jeu continue

    Args:
        plat (list[list[str]]): plateau du jeu
        gagne (int): si le joueur a gagné

    Returns:
        int: 0 ou 1
    """
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


def egal(plat:list[list[str]]):
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
    gagne : int
    score1 : int
    score2 : int
    indice : int

    score1 = 0
    score2 = 0
    v = True
    gagne = 0
    Jouer = False
    
    #Les joueurs choisissent le mode de jeu
    choix = int(input("A quel mode voulez-vous jouer ?\n1) Joueur contre joueur\n2) Joueur contre robot\n3) Robot contre robot\n"))
    while choix<1 or choix>3:
        choix = int(input("Choisisez un nombre en 1 et 3.\nA quel mode voulez-vous jouer ?\n1) Joueur contre joueur\n2) Joueur contre robot\n3) Robot contre robot\n"))
    #Si on joue joueur contre joueur
    if choix == 1:
            print(Nom1 +" joue avec O et "+Nom2+" joue avec X")     #Attributions des symboles
    #Si on joue joueur contre robot, on demande la difficulté du robot
    if choix == 2:
        difficulte = int(input("Quelle difficulté pour le robot ?\n1) Facile\n2) Difficile\n"))
        while difficulte<1 or difficulte>2:
            difficulte = int(input("Quelle difficulté pour le robot ?\n1) Facile\n2) Difficile\n"))

        joue=int(input("Quel joueur joue contre le robot ?\n1) "+Nom1+"\n2) "+Nom2+"\n"))
        while joue<1 or joue>2:
            joue=int(input("Choisissez un nombre entre 1 et 2.\nQuel joueur joue contre le robot ?\n1) "+Nom1+"\n2) "+Nom2+"\n"))
            
        if joue==1:
            print(Nom1 +" joue avec O et le robot joue avec X")
        elif joue==2:
            print(Nom2 +" joue avec O et le robot joue avec X")
    #Si on joue robot contre robot, on demande la difficulté des deux robots
    elif choix == 3:
        difficulte1 = int(input("Quelle difficulté pour le robot 1?\n1) Facile\n2) Difficile\n"))
        difficulte2 = int(input("Quelle difficulté pour le robot 2?\n1) Facile\n2) Difficile\n"))
        while difficulte1<1 or difficulte1>2:
            difficulte1 = int(input("Choississez un nombre entre 1 et 2.\nQuelle difficulté pour le robot 1?\n1) Facile\n2) Difficile\n"))
        while difficulte2<1 or difficulte2>2:
            difficulte2 = int(input("Choississez un nombre entre 1 et 2.\nQuelle difficulté pour le robot 2?\n1) Facile\n2) Difficile\n"))
        
            
    while v ==True :    #Tant que le booléen reste True
        #Selon les choix faits précédemment
        if choix == 1:
            plateau(plat)
            joueur(plat,Nom1,"O")
            
        elif choix == 2:
            plateau(plat)
            if joue==1:
                joueur(plat,Nom1,"O")
            elif joue==2:
                joueur(plat,Nom2,"O")
            
        elif choix == 3:
            plateau(plat)
            if difficulte1 == 2:
                
                if robotdur(plat,Jouer, "O", "O") == False:         #On lance la fonction pour faire jouer le robot
                    if robotdur(plat,Jouer, "X", "O") == False:     #Si le robot ne peut pas gagner, il essaye de défendre
                        # Si aucune opportunité de gagner ou de défendre, le robot joue aléatoirement
                        li= random.randint(0, 2)
                        col= random.randint(0, 2)
                        while plat[li][col] != " ":
                            li= random.randint(0, 2)
                            col= random.randint(0, 2)
                        plat[li][col] = "O"
            elif difficulte1 == 1:
                plateau(plat)
                robotfacile(plat,"O")
        
            
        if verif(plat,gagne) == 1:             #Si la vérification du score du joueur 1 renvoie 1 (uniquement quand le joueur gagne)
            v = False
            #On ajoute les scores pour les joueurs 1 ou 2
            if choix == 1 or (choix==2 and joue==1):
                plateau(plat)
                print(Nom1+", tu as gagné !")
                score1 = score1 +10
                indice =Recherche(ListeScore, Nom1)                                         #On fait arrêter le programme + enregistrement du score de joueur 1
                ListeScore[indice].ScorePuissance4 = ListeScore[indice].ScorePuissance4 + score1 
                print("Score:\n",Nom1+" :",score1,"\nRobot : 0")
            elif choix== 2 and joue==2:
                plateau(plat)
                print(Nom2+", tu as gagné !")
                score2 = score2 +10
                indice =Recherche(ListeScore, Nom2)                                         #On fait arrêter le programme + enregistrement du score de joueur 2
                ListeScore[indice].ScorePuissance4 = ListeScore[indice].ScorePuissance4 + score2 
                print("Score:\n",Nom2+" :",score2,"\nRobot : 0")
            elif choix==3:
                plateau(plat)
                print("Le robot 1 a gagné !")
        elif egal(plat) == 1:                   #Sinon on vérifie si il y a égalité ou non
            v =False
        else:
            if verif(plat,gagne) == 0:         #On fait la même chose avec le deuxième joueur
                plateau(plat)
                if choix == 1:
                    joueur(plat,Nom1,"X")
                elif choix == 2:
                    if difficulte==1:
                        robotfacile(plat,"X")
                    elif difficulte==2:
                        if robotdur(plat,Jouer, "X", "X") == False:
                            if robotdur(plat,Jouer, "O", "X") == False:
                            # Si aucune opportunité de gagner ou de défendre, jouer aléatoirement
                                li= random.randint(0, 2)
                                col= random.randint(0, 2)
                                while plat[li][col] != " ":
                                    li= random.randint(0, 2)
                                    col= random.randint(0, 2)
                                plat[li][col] = "X"
                elif choix == 3:
                    if difficulte2 == 2:
                        if robotdur(plat,Jouer, "X", "X") == False:         #On lance la procédure pour faire jouer le joueur 1
                            if robotdur(plat,Jouer, "O", "X") == False:
                            # Si aucune opportunité de gagner ou de défendre, jouer aléatoirement
                                li= random.randint(0, 2)
                                col= random.randint(0, 2)
                                while plat[li][col] != " ":
                                    li= random.randint(0, 2)
                                    col= random.randint(0, 2)
                                plat[li][col] = "X"
                    elif difficulte2 == 1:
                        robotfacile(plat,"X")
                        
                if verif(plat,gagne) == 1:
                    v= False
                    if choix == 1:
                        plateau(plat)
                        print(Nom2+", tu as gagné !")
                        score2 = score2 +10
                        indice = Recherche(ListeScore, Nom2)                 #Enregistrement du nouveaux score de joueur 2
                        ListeScore[indice].ScorePuissance4 = ListeScore[indice].ScorePuissance4 + score2
                        print("Score:\nRobot : 0\n",Nom2 +":",score2)
                    elif choix == 2:
                        plateau(plat)
                        print("Le robot a gagné !")
                    elif choix == 3:
                        plateau(plat)
                        print("Le robot 2 a gagné !")
                elif egal(plat) == 1:
                    v = False
