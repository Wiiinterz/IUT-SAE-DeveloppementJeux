from Devinette import *
from allumettes import *
from Utile import *
from Score import *
from Morpion import *
from Puissance4 import *


def Nom(ListeScore : list[Joueur])-> str :
    """Procédure permettant de choisir son pseudo et qui vérifie si le joueur à un compte
        ou un pseudo qui existe déjà

    Args:
        ListeScore liste[Joueur]: La liste dans laquelle se trouve les score des deux joueurs

    Returns:
        str: Renvoie le pseudo du joueur
    """
    pseudo : str
    valide : int
    DemandeCompte : str
    pseudo = ''
    valide = -1
    while valide == -1 :
        DemandeCompte = (input("Avez vous un compte ? o/n "))
        while DemandeCompte != 'o' and DemandeCompte != 'n' :
            print("Erreur je n'ai pas compris")
            DemandeCompte = (input("Avez vous un compte ? o/n "))
    
        pseudo = input("Quel est votre pseudo ? ")
        valide = Recherche(ListeScore,pseudo)               #On regarde si le pseudo est dans la liste
        if DemandeCompte == 'o' :
            if valide == -1 :
                print("Ce pseudo n'est pas dans la base de données")        #Le pseudo n'est pas dans la liste donc Erreur

        if DemandeCompte == 'n':
            if valide >= 0 :
                print("Erreur ce pseudo est déjà pris")     #Le pseudo existe déjà on demande à ce qu'il le change de nom
                valide = -1
                Nom (ListeScore)
            else :
                Ajouter(ListeScore,pseudo)                  #Le pseudo est ajouter car il n'est pas dans la liste
        valide = Recherche(ListeScore,pseudo)
    return(pseudo)





def Menu() -> int :
    """Procédure qui affiche le menu principal, permet de sélectionner une action

    Returns:
        int: Renvoie le choix de l'utilisateur
    """
    choix : int
    print("------Bienvenue------\n1.Jeux\n2.Score\n3.Quitter\n----------------------")
    choix = int(input("Que voulez vous faire ? "))
    while choix <0 or choix >3 :
        "Erreur choix non disponible"
        print("------Bienvenue------\n1.Jeux\n2.Score\n3.Quitter\n----------------------")
        choix = int(input("Que voulez vous faire ? "))
    return(choix)



def MenuJeux() -> int :
    """Procédure qui affiche le menu de Jeux, permet de sélectionner un jeu

    Returns:
        int: Renvoie le choix de l'utilisateur
    """
    choix : int 
    print("------Jeux------\n1.Devinette\n2.Allumettes\n3.Morpion\n4.Puissance 4\n5.Retour Menu\n----------------")
    choix = int(input("Que voulez vous faire ? "))
    while choix <0 or choix >5 :
        "Erreur choix non disponible"
        print("------Jeux------\n1.Devinette\n2.Allumettes\n3.Morpion\n4.Puissance 4\n5.Retour Menu\n----------------")
        choix = int(input("Que voulez vous faire ? "))
    return(choix)



def MenuScore() -> int :
    """Procédure qui affiche le menu des scores des différents jeux, permet de séléctionner un affichage de score

    Returns:
        int: Renvoie le choix de l'utilisateur 
    """
    choix : int 
    print("------Score------\n1.Score Devinette\n2.Score Allumettes\n3.Score Morpion\n4.Score Puissance 4\n5.Retour Menu\n----------------")
    choix = int(input("Que voulez vous faire ? "))
    while choix <0 or choix >5 :
        "Erreur choix non disponible"
        print("------Score------\n1.Score Devinette\n2.Score Allumettes\n3.Score Morpion\n4.Score Puissance 4\n5.Retour Menu\n----------------")
        choix = int(input("Que voulez vous faire ? "))
    return(choix)




if __name__ == "__main__" :
    rep : int
    repMenuJ : int
    repMenuS : int
    Nom1 : str
    Nom2 : str
    plat:list[list[str]]
    ListeScore : list[Joueur]
    
    rep = 0
    Nom1 = ''
    Nom2 = ''
    ListeScore = lectureScore()

    print("-----Bienvenue !-----")
    print("Joueur 1: ")
    Nom1 = Nom(ListeScore)          #Joueur 1 choisi son nom
    print(Separation(2))

    print("Joueur 2:")
    Nom2 = Nom(ListeScore)          #Joueur 2 choisi son nom
    while Nom1 == Nom2 :
        print("Erreur Joueur 1 a déjà ce pseudo")
        Nom2 = Nom(ListeScore)
    
    
    while rep != 3 :
        rep =Menu()
        if rep == 1 :
            repMenuJ = MenuJeux()                       #Menu des jeux
            if repMenuJ == 1 :
                DebutDevi(Nom1,Nom2, ListeScore)            #Jeu de devinette
            elif repMenuJ == 2 :
                allumettes(Nom1,Nom2,ListeScore)            #Jeu de allumette
            elif repMenuJ == 3 :
                plat=[[" "," "," "],[" "," "," "],[" "," "," "]]
                Morpion(Nom1,Nom2,ListeScore,plat)              #Jeu du morpion
            elif repMenuJ == 4 :
                plat=[[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
                Puissance4(Nom1,Nom2,ListeScore,plat)                 #Jeu du puissance 4
            print("Retour au menu principal")
        elif rep == 2:
            repMenuS = MenuScore()                      #Menu des scores
            if repMenuS == 1 :
                AffDev(ListeScore)                  #Score de devinette
            elif repMenuS == 2 :
                AffAll(ListeScore)                  #Score de allumette
            elif repMenuS == 3 :
                AffMor(ListeScore)                  #Score du morpion
            elif repMenuS == 4 :
                AffPui(ListeScore)                              #Score du puisance 4
            print("Retour au menu principal")
    print(Separation(2))
    print("Vous quittez l'application. Au revoir !")
    print(Separation(2))
    sauvegardeScore(ListeScore)