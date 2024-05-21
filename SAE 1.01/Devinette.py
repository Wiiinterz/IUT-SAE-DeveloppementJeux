import getpass #Module pour cacher l'écriture
from Utile import * #Module avec des fonctions souvent réécrite
from Score import *
def Fchoix (essai : int, nbre: int, choix : int, Nom2 : str )-> str :
    """
    ------------------------------------------------------------------------------------------
    La fonction permet au Joueur 1 de dire si le nombre saisie par le joueur 2
    est bon, trop petit ou trop grand. Le programme regarde donc si le joueur dit
    la vérité

    Entrée: essai : entier <- nombre saisie par le Joueur 2
            nbre : entier <- le nombre saisie par Joueur 1 et rechercher par le joueur 2
            choix : choix de réponse de joueur 1

    Sortie: réponse : une chaine de caractère donnant à joueur 2 la réponse de joueur 1
    ------------------------------------------------------------------------------------------
    """
    reponse : str

    reponse = ""
    
    if choix == 1 :                         #Joueur 1 dit que l'essai est trop petit
        if essai < nbre :
            reponse = Nom2+", Trop petit !"      #Joueur 1 dit la vérité, réponse donné
        else:
            reponse = "Erreur"                  #Erreur le joueur a menti, soit essai> nbre, soit essai == nombre
    elif choix == 2 :                     #Joueur 1 dit que l'essai est trop grand
        if essai > nbre :
            reponse = Nom2+", Trop grand !"      #Joueur 1 dit la vérité, réponse donnée
        else:
            reponse = "Erreur"                  # Erreur le joueur a menti, soit essai< nbre soit essai == nombre
    else :                            #Joueur 1 dit que Joueur 2 à trouvé le bon nombre
        if essai == nbre :
            reponse = Nom2+", c'est gagné !!"        #Joueur 1 dit la vérité, réponse donné
        else :
            reponse ="Erreur"               #Joueur 1 à menti, soit essai< nbre soit essai > nombre
    return (reponse)



def Demande(Nom1 : str, Nom2: str ,essai : int, ) -> int  :
    """Cette Fonction affiche les différents choix que joueur 1 peut répondre (Car on le demande souvent )

    Args:
        Nom1 (str): Le pseudo de joueur 1
        Nom2 (str): Le pseudo de joueur 2
        essai (int): Nombre saisie par Joueur 2

    Returns:
        int: Renvoie le choix de Joueur 1
    """
    choix :int

    print(Separation(4))
    print(Nom1+", "+ Nom2 +" a saisi",essai,"quelle est votre réponse ?")
    print("1. Trop petit  2. Trop grand  3. C'est gagné")
    choix = int(input("Réponse: "))
    while  choix < 0 or choix >3 :
        print("Erreur, 1. Trop petit  2. Trop grand  3. C'est gagné")
        choix = int(input("Réponse: "))
    print(Separation(4))
    return (choix)



def Devinette(nbre : int,limite :int, Nom1 : str, Nom2 :str, ListeScore : list[Joueur] )-> str:
    """Cette fonction gére le jeu en demandant choix de Joueur 2, en gérant le score ect...

    Args:
        nbre (int): Le nombre choisi par Joueur 1
        limite (int): le nombre limite choisi pour le jeu dans le quel Joueur 1 choisi un nombre
        Nom1 (str): Pseudo de joueur 1
        Nom2 (str): Pseudo de joueur 2
        ListeScore liste[Joueur]: La liste dans laquelle se trouve les score des deux joueurs

    Returns:
        str: Renvoie la phrase de fin
    """
    essai: int
    score1 : int
    score2 : int
    choix: int
    resultat : str
    retirer : int                       #Point retirer à Joueur 1 si il a menti
    fin : str
    indice : int
    
    score1 = 0                               #Pour joueur 1: On part de 0 et on ajoute 1 point à chaque essai raté du joueur 2
    score2 = limite                         #Pour Joueur 2: On part de la limite en point et on en retire un à chaque essai raté pour 
    essai = 0
    retirer = 0
    fin = ""
    resultat = ""

    
    while essai != nbre or (essai == nbre and resultat== "Erreur") :
        print(Nom2+", devinez le nombre de "+Nom1+": ")
        essai = int(input())
        while essai > limite+1 or essai < 0:
            print("Essai superieur ou inférieur à la limite, réessayer")
            print(Separation(2))
            print(Nom2+", devinez le nombre de "+Nom1+",: ")
            essai = int(input())
        choix = Demande(Nom1,Nom2,essai)
        resultat = Fchoix(essai,nbre,choix, Nom2)

        if resultat == "Erreur" :                   # On a Erreur si le joueur a menti ou s'est trompé 
            print(Nom1," a menti, moins un point ! ")
            score1 = score1-1
            retirer = retirer +1
        elif resultat != "\nJoueur 2, c'est gagné !!" : 
            score1 = score1 +1                   #Joueur 1: On ajoute un point à chaque essai raté de joueur 2
            score2 = score2 -2 
                             #Joueur 2: On enlève deux point à chaque essai raté
        if retirer > 9 :
            print(Separation(2))
            print(Nom1+" a menti trop de fois et à perdu")
            essai = nbre    #On force la sortie de la boucle car le joueur 1 à perdu
            resultat = "Joueur 2 a gagné !"
            print(Separation(2))
        if resultat != "Erreur" :
            print(resultat)
    print("Le nombre était: ",nbre)
    print("Score:\n",Nom1+":",score1,"\n",Nom2 +":",score2)
    if retirer > 0 :
        print(Nom1+" a menti",retirer,"fois et il a perdu ",retirer, "point(s)")
    fin ="\nLa partie est fini !!"              #On arrête la partie quand le nombre est trouvé
    
    indice =Recherche(ListeScore, Nom1)                                             #Enregistrement des nouveaux score
    ListeScore[indice].ScoreChoisi = ListeScore[indice].ScoreChoisi + score1
    
    indice = Recherche(ListeScore, Nom2)
    ListeScore[indice].ScoreDevine = ListeScore[indice].ScoreDevine + score2

    return (fin)





def DebutDevi(Nom1 : str, Nom2 : str, ListeScore : list[Joueur]) :
    """ Procédure qui permet de joueur de choisir la limite et le nombre à deviner

    Args:
        Nom1 (str): Nom du joueur 1
        Nom2 (str): Nom du joueur 2
        ListeScore (list[Joueur]): Liste contenant tous les scores de tous les joueurs
    """
    limite : int 
    saisir : str
    fin : str  
    choix : int
    tempo : str     #Variable temporaire

    
    print(Separation(1)) 
    print("But: Le Joueur 1 doit choisir une limite et un nombre (entre 1 et la limite). Le Joueur 2 doit deviner ce nombre\nLe Joueur 1 choisi ensuite si le nombre est 'plus petit', 'plus grand', ou si il est bon. Il peut mentir mais sera pénalisé.")
    print(Separation(1)) 

    choix= int(input("Quel joueur veut deviner ? Joueur: "))
    while choix <1 or choix >2:
        print("Erreur choix impossible")
        choix= int(input("Quel joueur veut deviner ? Joueur: "))
    if choix == 1 :
        tempo = Nom2            #Si le joueur 1 veut deviner, joueur 1 devient joueur 2
        Nom2 = Nom1
        Nom1 = tempo

    limite = int(input("Saisir la limite: "))
    while limite < 1 :
        print ("Erreur limite plus petite que 1")
        limite = int(input("Saisir la limite: "))
    print(Separation(2)) 
    saisir = getpass.getpass(prompt= Nom1+", entrer votre nombre: " )  #Le joueur écrit son nombre de manière caché
    nbre = int(saisir)                                                      #Conversion de la chaine de caractère en entier
    while nbre > limite or nbre< 1 :
        print("Erreur le nombre est supérieur à la limite ou négatif")      #On vérifie que le nombre est bien entre 1 et la limite fixé
        saisir = getpass.getpass(prompt= Nom1+", entrez votre nombre: ")
        print(Separation(2)) 
        nbre = int(saisir)

    fin = Devinette(nbre,limite, Nom1, Nom2, ListeScore)
    print(fin)
    print(Separation(2))
    