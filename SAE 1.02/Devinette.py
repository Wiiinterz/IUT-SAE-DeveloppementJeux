import getpass #Module pour cacher l'écriture
from Utile import * #Module avec des fonctions souvent réécrite
from Score import *
import random

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





def JoueurBot (nbre : int,limite :int, Nom1 : str,Nom2 : str, ListeScore : list[Joueur], diff : int ):
    """Cette procèdure permet au joueur choisi de jouer contre le robot avec la difficulté qu'il a choisi

    Args:
        nbre (int): Nombre choisi par le robot
        limite (int): Limite choisi par le joueur
        Nom1 (str): Le robot
        Nom2 (str): Le joueur
        ListeScore (list[Joueur]): Liste des scores dans laquelle on changera le score du joueur en cas de victoire
        diff (int): La difficulté du robot choisis
    """
    essai: int
    score2 : int
    indice : int
    resultat : str
    retirer : int

    retirer =0
    resultat = ''
    score2 = limite                         #Pour Joueur 2: On part de la limite en point et on en retire deux à chaque essai raté pour 
    essai = 0
    
    while essai != nbre or (essai == nbre and resultat== "Erreur") :
        print(Nom2+", devinez le nombre de "+Nom1+": ")
        essai = int(input())
        while essai > limite+1 or essai < 0:
            print("Essai superieur ou inférieur à la limite, réessayer")
            print(Separation(2))
            print(Nom2+", devinez le nombre de "+Nom1+",: ")
            essai = int(input())
        if diff == 1 :
            if essai < nbre :
                print(Nom2+", Trop petit !") 
                score2 =score2 - 2                   
            elif essai > nbre :
                print(Nom2+", Trop grand !")
                score2 =score2 -2      
        elif diff == 2 :
            if essai == nbre:
                choix = 3
            else :
                choix = random.randint(1,2)
            
            resultat =Fchoix(essai,nbre,choix,Nom2)
            if resultat == "Erreur" :                   # On a Erreur si le joueur a menti ou s'est trompé 
                if choix == 1 :
                    print(Nom2+", Trop petit !")
                else :
                    print (Nom2+",Trop grand !")
                print(Nom1," a menti")
                score2 = score2 -2
                retirer = retirer +1
            else:
                print (resultat)
                score2 = score2 -2
            if retirer > 9 :
                print(Separation(2))
                print(Nom1+" a menti trop de fois et à perdu")
                essai = nbre    #On force la sortie de la boucle car le joueur 1 à perdu
                resultat =''
                score2 = limite
                print(Separation(2))
        elif diff == 3 :
            if retirer < 9 :
                if essai == nbre:
                    choix = 3
                else :
                    choix = random.randint(1,2)
                resultat =Fchoix(essai,nbre,choix,Nom2)
                if resultat == "Erreur" :                   # On a Erreur si le joueur a menti ou s'est trompé 
                    if choix == 1 :
                        print(Nom2+", Trop petit !")
                    else :
                        print (Nom2+",Trop grand !")
                    print(Nom1," a menti")
                    score2 = score2 -2
                    retirer = retirer +1
                else:
                    print (resultat)
                    score2 = score2 -2
            else :
                if essai < nbre :
                    print(Nom2+", Trop petit !") 
                    score2 =score2 - 2                   
                elif essai > nbre :
                    print(Nom2+", Trop grand !")
                    score2 =score2 -2 
                else :
                    print(Nom2+", C'est gagné !!")
                    resultat =''
    print("Le nombre était: ",nbre)
    print(Nom2,": ", score2)
    indice = Recherche(ListeScore, Nom2)
    ListeScore[indice].ScoreDevine = ListeScore[indice].ScoreDevine + score2
            


def BotBot(Nom1 : str,Nom2 : str,limite : int,nbre : int,diff :int):
    """Procèdure permettant de faire s'affronter les deux robot

    Args:
        Nom1 (str): Nom du robot qui choisis le nombre
        Nom2 (str): Nom du robot qui devine le nombre
        limite (int): limite choisis dans laquelle se trouve le nombre
        nbre (int): le nombre a deviner choisis par le premier robot
        diff (int): la difficulté des robots
    """
    essai : int
    mini : int
    maxi : int
    tentative : int
    rep : str
    rep = ''
    essai = 0
    mini = 1
    maxi = limite
    tentative = 0
    while essai != nbre :
        if diff == 1 :
            if rep == '' :
                essai = essai +10
            elif rep == "Trop petit !" :
                if essai+10 < maxi and essai+10> mini :
                    essai = essai +10
                elif essai+5 < maxi and essai+5 > mini :
                    essai = essai +5 
                else :
                    essai = essai +1
            elif rep == "Trop grand !" :
                if essai-10 < maxi and essai-10> mini :
                    essai = essai -10
                elif essai-5 < maxi and essai-5 > mini :
                    essai = essai -5 
                else :
                    essai = essai -1
        elif diff == 2 :
            essai =random.randint(mini,maxi)
        else :
            essai = (mini + maxi)//2
        print(Nom2+" dit: ",essai)
        if essai < nbre :
            rep = ("Trop petit !")
            print(Nom1+" dit," + rep) 
            mini = essai  
            tentative = tentative +1                 
        elif essai > nbre :
            rep = ("Trop grand !")
            print(Nom1+" dit,"+ rep)  
            maxi = essai  
            tentative = tentative +1  
        else:
            rep = ("C'est gagné !!")
            print(Nom1+" dit," +rep)
            print("Le nombre était: ",nbre, "\n Il a été trouvé en ",tentative," essais")





def MenuDev(Nom1 : str, Nom2 : str, ListeScore : list[Joueur]):
    """ Procédure qui permet aux joueurs de choisir le mode et la difficulté des robots
      mais aussi la limite et le nombre à deviner

    Args:
        Nom1 (str): Nom du joueur 1
        Nom2 (str): Nom du joueur 2
        ListeScore (list[Joueur]): Liste contenant tous les scores de tous les joueurs
    """
    limite : int 
    saisir : str
    fin : str  
    choix : int
    choix2 : int
    tempo : str     #Variable temporaire

    print(Separation(1)) 
    print("But: Le Joueur 1 doit choisir une limite et un nombre (entre 1 et la limite). Le Joueur 2 doit deviner ce nombre\nLe Joueur 1 choisi ensuite si le nombre est 'plus petit', 'plus grand', ou si il est bon. Il peut mentir mais sera pénalisé.")
    print(Separation(1)) 

    print("1.Joueur contre Joueur\n2.Joueur contre ordi\n3.Ordi contre ordi")
    choix = int(input("Quel choix ? "))
    while choix < 0 or choix>3 :
        choix =int(input("Quel est votre choix ? "))

    if choix == 1:

        choix2= int(input("Quel joueur veut deviner ? Joueur: "))
        while choix2 <1 or choix2 >2:
            choix2= int(input("Erreur, quel joueur veut deviner ? Joueur: "))
        if choix2 == 1 :
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
    elif choix ==2 :

        choix2 = int(input("Quel joueur devine ? Joueur: "))
        while choix2 <1 or choix2 >2:
            choix2= int(input("Erreur, quel joueur veut jouer ? Joueur: "))     #Choix du joueur qui devine face au robot
        diff= int(input("Quel difficulté ?(1,2,3) "))               #Choix de la difficulté
        while diff < 0 or diff>3 :
            diff= int(input("Quel difficulté ?(1,2,3) "))
        limite = int(input("Saisir la limite: "))
        while limite < 1 :
            print ("Erreur limite plus petite que 1")
            limite = int(input("Saisir la limite: "))

        if choix2 == 1:
            Nom2 = Nom1                 #Le joueur (anciennement 1) Devine
            Nom1 = 'Bobby'              #L'ordi choisis un nombre
            nbre = (random.randint(1,limite))
            JoueurBot(nbre,limite,Nom1,Nom2,ListeScore,diff)

        else:
            Nom1 = 'Bobby'
            nbre = (random.randint(1,limite))
            JoueurBot(nbre,limite,Nom1,Nom2,ListeScore,diff)
    else :
        Nom1='Bobby'
        Nom2='Gus'
        diff= int(input("Quel difficulté ?(1,2,3) "))
        while diff < 0 or diff>3 :
            diff= int(input("Quel difficulté ?(1,2,3) "))
        limite = int(input("Saisir la limite: "))
        while limite < 1 :
            print ("Erreur limite plus petite que 1")
            limite = int(input("Saisir la limite: "))
        nbre = (random.randint(1,limite))
        BotBot(Nom1,Nom2,limite,nbre,diff)

