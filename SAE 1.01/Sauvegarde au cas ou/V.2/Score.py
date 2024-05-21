from typing import TextIO
import csv 
from Devinette import *
class Joueur :
    Pseudo : str
    ScoreDevine : int
    ScoreChoisi : int
    ScoreAllumettes : int
    ScoreMorpion : int
    ScorePuissance4 : int

ListeScore : list[Joueur]
ListeScore = []
f : TextIO

#Dans devinette : from score import (procédure de choix du nom)
#Tableau.ScoreDevine = Tableau.ScoreDevine + Score1
#Save dans un fichier ?
def Ajouter(Tableau : list[Joueur],Pseudo : str) :
    j = Joueur()
    j.Pseudo = Pseudo
    j.ScoreDevine = 0
    j.ScoreChoisi = 0
    j.ScoreAllumettes = 0
    j.ScoreMorpion = 0
    j.ScorePuissance4 = 0
    Tableau.append(j)

    
def Recherche(Tableau: list[Joueur],nom : str) -> int:
    i : int
    indice : int

    indice = 0

    for i in range(0, len(Tableau)) :
        if Tableau[i].Pseudo == nom  :
            indice = i
    return indice

def AffDev (Tableau: list[Joueur]) :
    for i in range(0, len(Tableau)) :
        print(Tableau[i].Pseudo)
        print(Tableau[i].ScoreDevine)
        print(Tableau[i].ScoreChoisi)

def AffAll (Tableau : list[Joueur]) :
    for i in range(0, len(Tableau)) :
        print(Tableau[i].Pseudo)
        print(Tableau[i].ScoreAllumettes)

def AffMor (Tableau : list[Joueur]) :
    for i in range(0, len(Tableau)) :
        print(Tableau[i].Pseudo)
        print(Tableau[i].ScoreMorpion)

def AffPui (Tableau : list[Joueur]):
    for i in range(0, len(Tableau)):
        print(Tableau[i].Pseudo)
        print(Tableau[i].ScorePuissance4)


def ScoreDev(Tableau : list[Joueur],Nom1 : str,Nom2: str, score1 : int, score2 : int) :
    indice : int

    indice =Recherche(Tableau, Nom1)
    Tableau[indice].ScoreChoisi = Tableau[indice].ScoreChoisi + score1

    indice = Recherche(Tableau, Nom2)
    Tableau[indice].ScoreDevine = Tableau[indice].ScoreDevine + score2


    f = open("DonnéeJoueur.txt","a")
    ligne= f.readlines()
    lecteur = csv.reader(f)
    for ligne in lecteur :
        print (ligne)


    f.close()

    #importation circulaire