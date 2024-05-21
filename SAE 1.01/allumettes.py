from Utile import *
from Score import *

def allumettes(Nom1 : str, Nom2 : str, ListeScore : list[Joueur]) :
    """ Procédure qui permet de jouer au jeu Allumettes, et de modifier les scores des joueurs 
        Affiche également le gagnant du jeu

    Args:
        Nom1 (str): Nom du joueur 1
        Nom2 (str): Nom du joueur 2
        ListeScore (list[Joueur]): Liste contenant tous les scores de tous les joueurs
    """
    res:int
    allu:str
    a:int
    b:int
    score1 : int
    score2 : int
    indice : int

    score1 = 0
    score2 = 0
    
    
    print (Separation(1))
    print ("But: Il y a un tas de 20 allumettes, chaque joueur peut en prendre 1,2 ou 3 , le joueur qui prend la dernière allumette à perdu")
    print (Separation(1))
    res = 20
    while res > 0:
        a = int(input(Nom1 +", choisissez le nombre d'allumettes que vous voulez prendre: \n"))
        print (Separation(2))
        while a < 1 or a > 3:
            a = int(input(Nom1+", Veuillez choisir un nombre entre 1 et 3: \n"))
            print (Separation(2))
        res = res - a
        if res < 0 :
            score2 = score2 + 10        #Joueur 1 à perdu, +10 points pour l'adversaire
        else :
            print ("Il reste ",res, " allumettes ")

        if res > 0 :       
            print (Separation(2))
            b = int(input(Nom2+", choisissez le nombre d'allumettes que vous voulez prendre: \n"))
            print (Separation(2))
            while b<1 or b>3:
                b = int(input(Nom2+", Veuillez choisir un nombre entre 1 et 3: \n"))
                print (Separation(2))
            res = res - b
            if res < 0 :
                score1 = score1 + 10        #Joueur 2 à perdu, +10 points pour l'adversaire
            else : 
                print ("Il reste ",res, " allumettes ")
                print (Separation(2))
    if res <1:
        allu = "Tu as perdu, il n'y a plus d'allumettes !"
        print (allu)
        print (Separation(2))
        print("Score:\n",Nom1+":",score1,"\n",Nom2 +":",score2)
        print(Separation(2))

        indice =Recherche(ListeScore, Nom1)                                                #Enregistrement du nouveaux score
        ListeScore[indice].ScoreAllumettes = ListeScore[indice].ScoreAllumettes + score1
    
        indice = Recherche(ListeScore, Nom2)
        ListeScore[indice].ScoreAllumettes = ListeScore[indice].ScoreAllumettes + score2