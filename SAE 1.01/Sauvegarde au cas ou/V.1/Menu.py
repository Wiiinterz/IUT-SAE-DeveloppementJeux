from Devinette import *
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
    print("------Jeux------\n1.Devinette\n2.Alumette\n3.Morpion\n4.Retour Menu\n----------------")
    choix = int(input("Que voulez vous faire ? "))
    return(choix)

def MenuScore() -> int :
    """Procédure qui affiche le menu des scores des différents jeux, permet de séléctionner un affichage de score

    Returns:
        int: Renvoie le choix de l'utilisateur 
    """
    choix : int 
    print("------Score------\n1.Score Devinette\n2.Score Alumette\n3.Score Morpion\n4.Retour Menu\n----------------")
    choix = int(input("Que voulez vous faire ? "))
    return(choix)

if __name__ == "__main__" :
    repMenu : int
    repMenuJ : int
    repMenuS : int

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
                DebutDevi()
            else:
                if repMenuJ == 2 :
                    pass
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
                    pass
                else :
                    if repMenuS == 2 :
                        pass
                    else :
                        if repMenuS == 3 :
                            pass
                        else :
                            pass
                print("Retour au menu principal")
                rep =Menu()
        print("Vous quittez l'application. Au revoir !")
        print(Separation(2))





