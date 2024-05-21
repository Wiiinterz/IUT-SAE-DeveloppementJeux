from typing import BinaryIO
import os
import pickle
from Utile import *

def Ajouter(ListeScore : list[Joueur],Pseudo : str) :
    """Cette procédure permet d'ajouter un nouveau joueur dans la liste de joueur déjà présente

    Args:
        Tableau (list[Joueur]): La liste dans laquelle on doit ajouter le joueur
        Pseudo (str): Le pseudo du joueur à ajouter
    """


    j = Joueur()
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
        Tableau (list[Joueur]): Liste dans laquelle on fait la recherche
        nom (str): Pseudo du joueur à chercher

    Returns:
        int: indice du joueur trouvé dans le tableau
    """
    i : int
    indice : int
    indice = 0

    for i in range(len(ListeScore)) :
        if ListeScore[i].Pseudo == nom  :
            indice = i
    return indice

def AffDev (ListeScore: list[Joueur]) :
    """Procédure qui affiche la liste des scores du jeu Devinette

    Args:
        Tableau (list[Joueur]): Liste de tout les scores 
    """
    for i in range(0, len(ListeScore)) :
        print("Nom:",ListeScore[i].Pseudo,", Score Devine:",ListeScore[i].ScoreDevine,", Score Choisi:",ListeScore[i].ScoreChoisi)

def AffAll (ListeScore : list[Joueur]) :
    """Procédure qui affiche la liste des scores du jeu Allumettes

    Args:
        Tableau (list[Joueur]): Liste de tout les scores 
    """
    j : int
    i : int

    j = 0
    while j > len(ListeScore) :
        for i in range (1 , len(ListeScore)) :
            k = ListeScore[i].ScoreAllumettes
            j = i-1
            while j >=0 and k < ListeScore[j].ScoreAllumettes:
                ListeScore[j+1].ScoreAllumettes = ListeScore[j].ScoreAllumettes
                j=j+1
            ListeScore[j+1].ScoreAllumettes=k
    for i in range(0, len(ListeScore)) :
        print("Nom:",ListeScore[i].Pseudo,"Score:",ListeScore[i].ScoreAllumettes)

def AffMor (ListeScore : list[Joueur]) :
    """Procédure qui affiche la liste des scores du jeu Morpion

    Args:
        Tableau (list[Joueur]): Liste de tout les scores 
    """
    for i in range(0, len(ListeScore)) :
        print("Nom:",ListeScore[i].Pseudo,"Score:",ListeScore[i].ScoreMorpion)

def AffPui (ListeScore : list[Joueur]):
    """Procédure qui affiche la liste des scores du jeu Puissance 4

    Args:
        Tableau (list[Joueur]): Liste de tout les scores 
    """
    for i in range(0, len(ListeScore)):
        print("Nom: ",ListeScore[i].Pseudo,"Score: ",ListeScore[i].ScorePuissance4)


def tri (ListeScore : list[Joueur]) :
    for i in range (1 , len(ListeScore)) :
        k = ListeScore[i].ScoreAllumettes
        j = i-1
        while j >=0 and k < ListeScore[j].ScoreAllumettes:
            ListeScore[j+1].ScoreAllumettes = ListeScore[j].ScoreAllumettes
            j=j+1
        ListeScore[j+1].ScoreAllumettes=k


def ScoreDev(ListeScore : list[Joueur],Nom1 : str,Nom2: str, score1 : int, score2 : int) :
    """Procédure qui ajoute aux joueurs le score qu'il viennent d'avoir dans le jeu devinette à celui qu'ils ont déjà

    Args:
        Tableau (list[Joueur]): Liste avec leurs scores déjà existant
        Nom1 (str): Nom du joueur 1
        Nom2 (str): Nom du joueur 2
        score1 (int): Score du joueur 1
        score2 (int): Score du joueur 2
    """
    indice : int
    indice =Recherche(ListeScore, Nom1)
    ListeScore[indice].ScoreChoisi = ListeScore[indice].ScoreChoisi + score1
    
    indice = Recherche(ListeScore, Nom2)
    ListeScore[indice].ScoreDevine = ListeScore[indice].ScoreDevine + score2

def ScoreAll(ListeScore : list[Joueur],Nom1 : str,Nom2: str, score1 : int, score2 : int) :
    """Procédure qui ajoute aux joueurs le score qu'il viennent d'avoir dans le jeu allumettes à celui qu'ils ont déjà

    Args:
        Tableau (list[Joueur]): Liste avec leurs scores déjà existant
        Nom1 (str): Nom du joueur 1
        Nom2 (str): Nom du joueur 2
        score1 (int): Score du joueur 1
        score2 (int): Score du joueur 2
    """
    indice : int
    indice =Recherche(ListeScore, Nom1)
    ListeScore[indice].ScoreAllumettes = ListeScore[indice].ScoreAllumettes + score1
    
    indice = Recherche(ListeScore, Nom2)
    ListeScore[indice].ScoreAllumettes = ListeScore[indice].ScoreAllumettes + score2

def ScoreMor(ListeScore : list[Joueur],Nom1 : str,Nom2: str, score1 : int, score2 : int) :
    """Procédure qui ajoute aux joueurs le score qu'il viennent d'avoir dans le jeu Morpion à celui qu'ils ont déjà

    Args:
        Tableau (list[Joueur]): Liste avec leurs scores déjà existant
        Nom1 (str): Nom du joueur 1
        Nom2 (str): Nom du joueur 2
        score1 (int): Score du joueur 1
        score2 (int): Score du joueur 2
    """
    indice : int
    indice =Recherche(ListeScore, Nom1)
    ListeScore[indice].ScoreMorpion = ListeScore[indice].ScoreMorpion + score1
    
    indice = Recherche(ListeScore, Nom2)
    ListeScore[indice].ScoreMorpion = ListeScore[indice].ScoreMorpion + score2

def ScorePuiss(ListeScore : list[Joueur],Nom1 : str,Nom2: str, score1 : int, score2 : int) :
    """Procédure qui ajoute aux joueurs le score qu'il viennent d'avoir dans le jeu Puissance 4 à celui qu'ils ont déjà

    Args:
        Tableau (list[Joueur]): Liste avec leurs scores déjà existant
        Nom1 (str): Nom du joueur 1
        Nom2 (str): Nom du joueur 2
        score1 (int): Score du joueur 1
        score2 (int): Score du joueur 2
    """
    indice : int
    indice =Recherche(ListeScore, Nom1)
    ListeScore[indice].ScorePuissance4 = ListeScore[indice].ScorePuissance4 + score1
    
    indice = Recherche(ListeScore, Nom2)
    ListeScore[indice].ScorePuissance4 = ListeScore[indice].ScorePuissance4 + score2

def lectureScore() -> list[Joueur] :
    f : BinaryIO
    j : Joueur
    tab :list[Joueur]
    tab = []
    if os.path.exists("score.dat") :
        f = open("score.dat","rb")
        tab = pickle.load(f)
        print("type du tableau", type(tab))
    else :
        j = Joueur()
        j.Pseudo = ''
        j.ScoreChoisi = 0
        j.ScoreDevine = 0
        j.ScoreMorpion = 0
        j.ScoreAllumettes = 0
        j.ScorePuissance4 = 0
        tab.append(j)
    return tab

def sauvegardeScore(tab : list[Joueur]) :
    f : BinaryIO
    f = open("score.dat","wb")
    pickle.dump(tab,f)
    f.close()
