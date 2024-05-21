from typing import BinaryIO
import os
import pickle
from Utile import *

def Ajouter(ListeScore : list[Joueur],Pseudo : str) :
    """Cette procédure permet d'ajouter un nouveau joueur dans la liste de joueur déjà présente

    Args:
        ListeScore (list[Joueur]): La liste dans laquelle on doit ajouter le joueur
        Pseudo (str): Le pseudo du joueur à ajouter
    """
    j : Joueur
    
    j = Joueur()                        #Ajoute le nouveaux joueur au fichier (si il existe pas)
    j.Pseudo = Pseudo
    j.ScoreDevine = 0
    j.ScoreChoisi = 0
    j.ScoreAllumettes = 0
    j.ScoreMorpion = 0
    j.ScorePuissance4 = 0
    ListeScore.append(j)
    




def Recherche(ListeScore: list[Joueur],nom : str) -> int:
    """Cette procédure permet de rechercher dans le tableau un joueur à l'aide de son nom, et renvoie son indice

    Args:
        ListeScore (list[Joueur]): Liste dans laquelle on fait la recherche
        nom (str): Pseudo du joueur à chercher

    Returns:
        int: indice du joueur trouvé dans le tableau
    """
    i : int
    indice : int
    indice = -1

    for i in range(0,len(ListeScore)) :
        if ListeScore[i].Pseudo == nom  :                   #Vérifie si le pseudo est dans la base de donnée
            indice = i
    return indice





def AffDev (ListeScore: list[Joueur]) :
    """Procédure qui affiche la liste des scores du jeu Devinette du meilleur au moins bon

    Args:
        ListeScore (list[Joueur]): Liste de tout les scores 
    """
    choix : int
    i : int
    ListeTri : list[Joueur]
    ListeTri = []

    print("Vous voulez ? 1. Top Score du joueur qui devine 2.Top Score du joueur qui fait deviner ")
    choix = int(input("Quel choix ? "))
    if choix < 1 or choix > 2 :
        print("Erreur \nVous voulez ? 1. Top Score du joueur qui devine 2.Top Score du joueur qui fait deviner ")
        choix = int(input("Quel choix ? "))
    if choix == 1 :
        for i in range(len(ListeScore)) :
            max = i 
            for j in range(i+1, len(ListeScore)):
                if ListeScore[max].ScoreDevine < ListeScore[j].ScoreDevine :            #Fait le trie du meilleur au moins bon joueur pour le joueur qui devine de devinette
                    max = j
            tmp = ListeScore[i]
            ListeScore[i] = ListeScore[max]
            ListeScore[max] = tmp
            ListeTri.append(ListeScore[max])

        for u in range(0, len(ListeTri)) :                                              #Affiche tous les joueur de la liste triée
            print("Nom:",ListeTri[u].Pseudo,"Score:",ListeTri[u].ScoreDevine)
    else :
        for i in range(len(ListeScore)) :
            max = i 
            for j in range(i+1, len(ListeScore)):                                       #Fait le trie du meilleur au moins bon joueur pour le joueur qui choisis de devinette
                if ListeScore[max].ScoreChoisi < ListeScore[j].ScoreChoisi :
                    max = j
            tmp = ListeScore[i]
            ListeScore[i] = ListeScore[max]
            ListeScore[max] = tmp
            ListeTri.append(ListeScore[max])

        for u in range(0, len(ListeTri)) :                                              #Affiche tous les joueurs de la liste triée
            print("Nom:",ListeTri[u].Pseudo,"Score:",ListeTri[u].ScoreChoisi)





def AffAll (ListeScore : list[Joueur]) :
    """Procédure qui affiche la liste des scores du jeu Allumettes

    Args:
        ListeScore (list[Joueur]): Liste de tout les scores 
    """
    i : int
    ListeTri : list[Joueur]
    ListeTri = []
    for i in range(len(ListeScore)) :                                   #Fait le trie du meilleur au moins bon joueur pour le jeu allumette
            mini = i 
            for j in range(i+1, len(ListeScore)):
                if ListeScore[mini].ScoreAllumettes < ListeScore[j].ScoreAllumettes :
                    mini = j
            tmp = ListeScore[i]
            ListeScore[i] = ListeScore[mini]
            ListeScore[mini] = tmp
            ListeTri.append(ListeScore[mini])

    for u in range(0, len(ListeTri)) :                                          #Affiche tous les joueurs de la liste triée
        print("Nom:",ListeTri[u].Pseudo,"Score:",ListeTri[u].ScoreAllumettes)




def AffMor (ListeScore : list[Joueur]) :
    """Procédure qui affiche la liste des scores du jeu Morpion

    Args:
        ListeScore (list[Joueur]): Liste de tous les scores 
    """
    i : int
    ListeTri : list[Joueur]
    ListeTri = []
    for i in range(len(ListeScore)) :                           #Fait le trie du meilleur au moins bon joueur pour le jeu morpion
            min = i 
            for j in range(i+1, len(ListeScore)):
                if ListeScore[min].ScoreMorpion < ListeScore[j].ScoreMorpion :
                    min = j
            tmp = ListeScore[i]
            ListeScore[i] = ListeScore[min]
            ListeScore[min] = tmp
            ListeTri.append(ListeScore[min])

    for u in range(0, len(ListeTri)) :                                  #affiche tous les joueurs de la liste triée
        print("Nom:",ListeTri[u].Pseudo,"Score:",ListeTri[u].ScoreMorpion)




def AffPui (ListeScore : list[Joueur]):
    """Procédure qui affiche la liste des scores du jeu Puissance 4

    Args:
        ListeScore (list[Joueur]): Liste de tout les scores 
    """
    i : int
    ListeTri : list[Joueur]
    ListeTri = []
    for i in range(len(ListeScore)) :                               #Fait le trie du meilleur au moins bon joueur pour le jeu puissance 4
            max = i 
            for j in range(i+1, len(ListeScore)):
                if ListeScore[max].ScorePuissance4 < ListeScore[j].ScorePuissance4 :
                    max = j
            tmp = ListeScore[i]
            ListeScore[i] = ListeScore[max]
            ListeScore[max] = tmp
                
            ListeTri.append(ListeScore[max])    #probleme là
    for u in range(0, len(ListeTri)) :                                  #Affiche tous les joueurs de la liste triée
        print("Nom:",ListeTri[u].Pseudo,"Score:",ListeTri[u].ScorePuissance4)
        





def lectureScore() -> list[Joueur] :
    """Procédure qui permet de lire le fichier binaire du score ou d'en créer un si il n'existe pas

    Returns:
        list[Joueur]: Liste de tout les joueurs présent sur le fichier binaire
    """

    f : BinaryIO
    j : Joueur
    tab :list[Joueur]
    tab = []
    if os.path.exists("score.dat") :            #Vérifie si le fichier binaire existe
        f = open("score.dat","rb")
        tab = pickle.load(f)
    else :
        j = Joueur()
        j.Pseudo = 'Zero'                   #Crée le fichier binaire si il existe pas
        j.ScoreChoisi = 0
        j.ScoreDevine = 0
        j.ScoreMorpion = 0
        j.ScoreAllumettes = 0
        j.ScorePuissance4 = 0
        tab.append(j)
    return tab





def sauvegardeScore(tab : list[Joueur]) :
    """Procédure permettant de sauvegarder les changements dans le fichier binaire (écrase les information d'avant)

    Args:
        tab (list[Joueur]): Liste de joueur à écrire dans le fichier
    """
    f : BinaryIO
    f = open("score.dat","wb")              #Remplace le fichier par le fichier modifié
    pickle.dump(tab,f)
    f.close()
