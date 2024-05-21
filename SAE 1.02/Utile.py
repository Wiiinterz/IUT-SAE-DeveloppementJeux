def Separation(sep : int) -> str :
    """Fonction uniquement esthétique permetant de placer des séparation pour facilité la lecture

    Args:
        sep (int): Choix de la séparation (saisie par le programmeur)

    Returns:
        str: Renvoie la séparation
    """
    res : str

    if sep == 1 :
        res = "-------------------------------------------------------------------------------------------------------------------------------"
    else :
        if sep == 2 :
            res = "------------------------------"                          #Pour l'esthétique du programme
        else :
            if sep == 3 :
                res = "********************************"
            else :
                res ="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    return(res)


class Joueur :
    Pseudo : str
    ScoreDevine : int                   #On a mis la classe joueur dans Utile pour éviter aux maximun les import circulaire 
    ScoreChoisi : int                   #vu que l'on doit mettre le tableau en paramètre dans plusieurs module qui sont déjà relier entre eux
    ScoreAllumettes : int
    ScoreMorpion : int
    ScorePuissance4 : int
