from Devinette import *
from allumettes import *
from Score import *

def Nom(DemandeNom : str)-> str :
    pseudo : str
    valide : int

    pseudo = ''
    pseudo = input("Quel est votre pseudo ? ")
    
    if DemandeNom == 'o' :
        valide = Recherche(ListeScore,pseudo)
        while valide == False and DemandeNom == 'o' :
            print("Ce pseudo n'est pas dans la base de données")
            DemandeNom = ("Vous êtes sûr d'avoir un compte ? o/n")
            Nom(DemandeNom)

    else :
        if DemandeNom == 'n' :
            valide = Recherche(ListeScore,pseudo)
            while valide != 0 :  
                print("Erreur ce pseudo est déjà pris")     #Le pseudo existe déjà on demande à ce qu'il le change
                pseudo = input("Quel est votre pseudo ? ")
                valide = Recherche(ListeScore,pseudo)
            Ajouter(ListeScore,pseudo)
    return(pseudo)

def Menu() -> int :
    """Procédure qui affiche le menu principal, permet de sélectionner une action

    Returns:
        int: Renvoie le choix de l'utilisateur
    """
    choix : int
    print("------Bienvenue------\n1.Jeux\n2.Score\n3.Quitter\n----------------------")
    choix = int(input("Que voulez vous faire ? "))
    return(choix)

def MenuJeux() -> int :
    """Procédure qui affiche le menu de Jeux, permet de sélectionner un jeu

    Returns:
        int: Renvoie le choix de l'utilisateur
    """
    choix : int 
    print("------Jeux------\n1.Devinette\n2.Allumettes\n3.Morpion\n4.Retour Menu\n----------------")
    choix = int(input("Que voulez vous faire ? "))
    return(choix)

def MenuScore() -> int :
    """Procédure qui affiche le menu des scores des différents jeux, permet de séléctionner un affichage de score

    Returns:
        int: Renvoie le choix de l'utilisateur 
    """
    choix : int 
    print("------Score------\n1.Score Devinette\n2.Score Allumettes\n3.Score Morpion\n4.Retour Menu\n----------------")
    choix = int(input("Que voulez vous faire ? "))
    return(choix)

if __name__ == "__main__" :
    repMenu : int
    repMenuJ : int
    repMenuS : int
    DemandeNom : str
    Nom1 : str
    Nom2 : str
    
    Nom1 = ''
    Nom2 = ''

    print("-----Bienvenue !-----")
    DemandeNom = (input("Joueur1, avez vous un compte ? o/n "))
    print(Separation(2))
    while DemandeNom != 'o' and DemandeNom != 'n' :
        print("Erreur je n'ai pas compris")
        DemandeNom = (input("Joueur1, avez vous un compte ? o/n "))
    if DemandeNom == 'o' :
        Nom1 = Nom(DemandeNom)
    else :
        Nom1 = Nom(DemandeNom)

    print(Separation(2))
    DemandeNom = (input("Joueur2, avez vous un compte ? o/n "))
    print(Separation(2))
    while DemandeNom !='o' and DemandeNom != 'n' :
        print("Erreur je n'ai pas compris")
        DemandeNom = (input("Joueur2, avez vous un compte ? o/n "))

    if DemandeNom == 'o' :
        Nom2 = Nom(DemandeNom)
        while Nom1 == Nom2 :
            print("Erreur Joueur 1 a déjà ce pseudo")
            Nom2 = Nom(DemandeNom)
    else:
        Nom2 = Nom(DemandeNom)
        while Nom1 == Nom2 :
            print("Erreur Joueur 1 a déjà ce pseudo")
            Nom2 = Nom(DemandeNom)

    rep =Menu()
    
    while rep <0 or rep >3 :
        "Erreur choix non disponible"
        rep =Menu()
    while rep != 3 :
        if rep == 1 :
            repMenuJ = MenuJeux()
            while repMenuJ <0 or repMenuJ >4 :
                "Erreur choix non disponible"
                repMenuJ = MenuJeux()
            if repMenuJ == 1 :
                DebutDevi(Nom1,Nom2)
            else:
                if repMenuJ == 2 :
                    allumettes(Nom1,Nom2)
                else :
                    if repMenuJ == 3 :
                        pass
                    else :
                        pass
                print("Retour au menu principal")
                rep =Menu()
        else:
            if rep == 2 :
                repMenuS = MenuScore()
                while repMenuS <0 or repMenuS >4 :
                    "Erreur choix non disponible"
                    repMenuS = MenuScore()
                if repMenuS == 1 :
                    AffDev(ListeScore)
                else :
                    if repMenuS == 2 :
                        AffAll(ListeScore)
                    else :
                        if repMenuS == 3 :
                            AffMor(ListeScore)
                        else :
                            pass
                print("Retour au menu principal")
                rep =Menu()
    print(Separation(2))
    print("Vous quittez l'application. Au revoir !")
    print(Separation(2))
