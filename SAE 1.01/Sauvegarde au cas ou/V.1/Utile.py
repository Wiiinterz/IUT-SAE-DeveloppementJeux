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
            res = "----------------------------"
        else :
            if sep == 3 :
                res = "********************************"
            else :
                res ="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    return(res)

