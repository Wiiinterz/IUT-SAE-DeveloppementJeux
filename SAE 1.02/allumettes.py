from Utile import *
from Score import *
import random 

def allumettes(Nom1 : str, Nom2 : str, ListeScore : list[Joueur]) :
    """ Procédure qui permet de jouer au jeu Allumettes contre un joueur ou un robot, de choisir la difficulté
        et de modifier les scores des joueurs, Affiche également le gagnant du jeu

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
    diff : int

    score1 = 0
    score2 = 0
    
    
    print (Separation(1))
    print ("But: Il y a un tas de 20 allumettes, chaque joueur peut en prendre 1,2 ou 3 , le joueur qui prend la dernière allumette à perdu")
    print (Separation(1))

    print("1.Joueur contre Joueur\n2.Joueur contre ordi\n3.Ordi contre ordi")
    choix = int(input("Quel choix ? "))
    while choix < 0 or choix>3 :
        choix =int(input("Quel est votre choix ? "))


    if choix == 1:
        res = 20
        while res > 0:
            a = int(input(Nom1 +", choisissez le nombre d'allumettes que vous voulez prendre: \n"))
            print (Separation(2))
            while a < 1 or a > 3:
                a = int(input(Nom1+", Veuillez choisir un nombre entre 1 et 3: \n"))
                print (Separation(2))
            res = res - a
            if res < 1 :
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
                if res < 1 :
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
    elif choix ==2:
        choix2 = int(input("Quel joueur veut jouer ? Joueur: "))
        while choix2 <1 or choix2 >2:
            choix2= int(input("Erreur, quel joueur veut jouer ? Joueur: "))

        diff= int(input("Quel difficulté ?(1,2,3) "))
        while diff < 0 or diff>3 :
            diff= int(input("Quel difficulté ?(1,2,3) "))

        if choix2 == 1:
            Nom2 = Nom1                 #Le joueur (anciennement 1) Devine
            Nom1 = 'Bobby'              #L'ordi choisis un nombre
        else:
            Nom1 = 'Bobby'

        res = 20
        while res > 0:
            a = int(input(Nom2 +", choisissez le nombre d'allumettes que vous voulez prendre: \n"))
            print (Separation(2))
            while a < 1 or a > 3:
                a = int(input(Nom2+", Veuillez choisir un nombre entre 1 et 3: \n"))
                print (Separation(2))
            res = res - a
            if res > 0 :
                print ("Il reste ",res, " allumettes ")

            if res > 0 :       
                print (Separation(2))
                if diff == 1:
                    b = random.randint(1,3)
                elif diff ==2 :
                    if res ==3 :
                        b =2
                    elif res == 2 :
                        b = 1
                    else :
                        b = random.randint(1,3)
                else :
                    if res == 20 or res == 16 or res ==12 or res == 8 or res == 4:
                        b = 3
                    elif res == 19 or res ==15 or res == 11 or res == 7 or res == 3 :
                        b = 2
                    elif res == 18 or res ==14 or res == 10 or res == 6 or res == 2 :
                        b = 1
                    else :
                        b = random.randint(1,3)
                print(Nom1+" dit,",b)
                print (Separation(2))
                res = res - b
                if res < 1 :
                    score2 = score2 + 10        #Joueur 2 à perdu, +10 points pour l'adversaire
                else : 
                    print ("Il reste ",res, " allumettes ")
                    print (Separation(2))
        if res <1:
            allu = "Tu as perdu, il n'y a plus d'allumettes !"
            print (allu)
            print (Separation(2))
            print("Score:\n",Nom2+":",score2)
            print(Separation(2))

            indice =Recherche(ListeScore, Nom2)                                                #Enregistrement du nouveaux score
            ListeScore[indice].ScoreAllumettes = ListeScore[indice].ScoreAllumettes + score2
    else:
        Nom1='Bobby'
        Nom2='Gus'
        res = 20
        diff= int(input("Quel difficulté ?(1,2,3) "))
        while diff < 0 or diff>3 :
            diff= int(input("Quel difficulté ?(1,2,3) "))
        while res > 0:
            if diff == 1:
                a = random.randint(1,3)
            elif diff ==2 :
                if res ==3 :
                    a =2
                elif res == 2 :
                    a = 1
                else :
                    a = random.randint(1,3)
            else :
                if res == 20 or res == 16 or res ==12 or res == 8 or res == 4:
                    a = 3
                elif res == 19 or res ==15 or res == 11 or res == 7 or res == 3 :
                    a = 2
                else :
                    a = 1
            print(Nom2+" dit,",a)
            print (Separation(2))
            res = res - a
            if res > 0 :
                print ("Il reste ",res, " allumettes ")
            if res > 0 :       
                print (Separation(2))
                if diff == 1:
                    b = random.randint(1,3)
                elif diff ==2 :
                    if res ==3 :
                        b =2
                    elif res == 2 :
                        b = 1
                    else :
                        b = random.randint(1,3)
                else :
                    if res == 20 or res == 16 or res ==12 or res == 8 or res == 4:
                        b = 3
                    elif res == 19 or res ==15 or res == 11 or res == 7 or res == 3 :
                        b = 2
                    else :
                        b = 1
                print(Nom1+" dit,",b)
                print (Separation(2))
                res = res - b
                if res > 0 :
                    print ("Il reste ",res, " allumettes ")
                    print (Separation(2))
        if res <1:
            allu = "Tu as perdu, il n'y a plus d'allumettes !"
            print (allu)
