import getpass #Module pour cacher l'écriture
from Utile import * #Module avec des fonctions souvent réécrite

def Fchoix (essai : int, nbre: int, choix : int )-> str :
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
    if  choix < 0 or choix >3 :
        reponse = "Erreur ce choix n'existe pas"
    else :
        if choix == 1 :                         #Joueur 1 dit que l'essai est trop petit
            if essai < nbre :
                reponse = "\nJoueur 2, Trop petit !"      #Joueur 1 dit la vérité, réponse donné
            else:
                reponse = "Erreur"                  #Erreur le joueur a menti, soit essai> nbre, soit essai == nombre
        if choix == 2 :                     #Joueur 1 dit que l'essai est trop grand
            if essai > nbre :
                reponse = "\nJoueur 2, Trop grand !"      #Joueur 1 dit la vérité, réponse donnée
            else:
                reponse = "Erreur"                  # Erreur le joueur a menti, soit essai< nbre soit essai == nombre
        if choix == 3 :                             #Joueur 1 dit que Joueur 2 à trouvé le bon nombre
            if essai == nbre :
                reponse = "\nJoueur 2, c'est gagné !!"        #Joueur 1 dit la vérité, réponse donné
            else :
                reponse ="Erreur"               #Joueur 1 à menti, soit essai< nbre soit essai > nombre
    return (reponse)



def Demande(Nom1 : str, Nom2: str ,essai : int, ) -> int  :
    """Cette Fonction affiche les différent choix que joueur 1 peut répondre (Car on le demande souvent )

    Args:
        essai (int): Nombre saisie par Joueur 2

    Returns:
        int: Renvoie le choix de Joueur 1
    """
    choix :int

    print(Separation(4))
    print(Nom1,",", Nom2 ,"à saisi",essai,"quelle est votre réponse ?")
    print("1. Trop petit  2. Trop grand  3. C'est gagné")
    choix = int(input("Réponse: "))
    print(Separation(4))
    return (choix)



def Devinette(nbre : int, Nom1 : str, Nom2 :str )-> str:
    """Cette fonction gére le jeu en demandant choix de Joueur 2, en gérant le score ect...

    Args:
        nbre (int): Le nombre choisis par Joueur 1

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

    score1 = 0                               #Pour joueur 1: On part de 0 et on ajoute 1 point à chaque essai raté du joueur 2
    score2 = 50                         #Pour Joueur 2: On part de n point et on en retire un à chaque essai raté pour 
    essai = 0
    retirer = 0
    fin = ""
    resultat = ''

    
    while essai != nbre or (essai == nbre and resultat== "Erreur") :
        print(Nom2,",devinez le nombre de",Nom1,": ")
        essai = int(input())
        while essai > nbre+1 :
            print("Essai superieur à la limite, réessayer")
            print(Separation(2))
            print("\n",Nom2,"devinez le nombre de",Nom1,",: \n")
            essai = int(input())
        choix = Demande(Nom1,Nom2,essai)
        resultat = Fchoix(essai,nbre,choix)

        if resultat == "Erreur ce choix n'existe pas" :
            while resultat == "Erreur ce choix n'existe pas" :
                print("Ce choix n'est pas disponible")
                choix = Demande(Nom1,Nom2,essai)
                resultat = Fchoix(essai,nbre,choix)

        if resultat == "Erreur" :                   # On a Erreur si le joueur a menti ou s'est trompé 
            print(Nom1," à menti, moins un point ! ")
            score1 = score1-1
            retirer = retirer +1
        else :
            if resultat == "\nJoueur 2, c'est gagné !!" :
                pass
            else :
                score1 = score1 +1                   #Joueur 1: On ajoute un point à chaque essai raté de joueur 2
                score2 = score2 -1                   #Joueur 2: On enlève un point à chaque essai raté
        if retirer > 10 :
            print(Separation(2))
            print(Nom1," à menti trop de fois et à perdu")
            essai = nbre    #On force la sortie de la boucle car le joueur 1 à perdu
            resultat = "Joueur 2 à gagné !"
            print(Separation(2))
        if resultat != "Erreur" :
            print(resultat)
    print("Le nombre était: ",nbre)
    print(Nom1,": ", score1,"\n")
    print(Nom2,": ", score2)
    if retirer > 0 :
        print(Nom1," à menti",retirer,"fois et il a perdu ",retirer, "point(s)")
    fin ="\nLa partie est fini !!"              #On arrête la partie quand le nombre est trouvé
    return (fin)


def Nom()-> str :
    pseudo : str

    pseudo = ''
    pseudo = input("Quel est votre pseudo ? ")
        #Si nom dans la base de donner on modifiera le score si il est meilleur
        #Sinon, on redemande le nom
    return(pseudo)
    
    


def DebutDevi() :
    """Procédure qui explique le but et demande la limite 
    """
    limite : int 
    saisir : str
    fin : str
    DemandeNom : str
    Nom1 : str
    Nom2 : str

    Nom1 = ''
    Nom2 = ''

    print("-----Bienvenue dans Devinette !-----")
    print(Separation(2))
    DemandeNom = (input("Joueur 1 va choisir un nombre\nAvez vous déjà jouer ? o/n "))
    print(Separation(2))
    if DemandeNom == 'o' :
        Nom1 = Nom()
    else :
        if DemandeNom == 'n' :
            Nom1 = Nom()
        else :
            print("Je n'ai pas compris" )
            DebutDevi() 
            
    print(Separation(2))
    DemandeNom = (input("Joueur 2 va choisir un nombre\nAvez vous déjà jouer ? o/n "))
    print(Separation(2))
    if DemandeNom == 'o' :
        Nom2 = Nom()
        while Nom1 == Nom2 :
            print("Erreur Joueur 1 à déjà ce pseudo")
            Nom2 = Nom()
    else:
        if DemandeNom == 'n' :
            Nom2 = Nom()
            while Nom1 == Nom2 :
                print("Erreur Joueur 1 à déjà ce pseudo")
                Nom2 = Nom()
        else:
            print("Je n'ai pas compris")
            DebutDevi()
    

            
        

    
    print(Separation(1)) 
    print("But: Le Joueur 1 doit choisir une limite et un nombre. Le Joueur 2 doit deviner ce nombre\nLe Joueur 1 choisi ensuite si le nombre est 'plus petit', 'plus grand', ou si il est bon. Il peut mentir mais sera pénalisé.")
    print(Separation(1)) 

    limite = int(input("Saisir la limite: "))
    print(Separation(2)) 
    saisir = getpass.getpass(prompt= "Joueur 1, entrer votre nombre: " )  #Le joueur écrit son nombre de manière caché
    nbre = int(saisir)                                                      #Conversion de la chaine de caractère en entier
    while nbre > limite or nbre< 1 :
        print("Erreur le nombre est supérieur à la limite ou négatif")      #On vérifie que le nombre est bien entre 1 et la limite fixé
        saisir = getpass.getpass(prompt= "Joueur 1 , entrer votre nombre: ")
        print(Separation(2)) 
        nbre = int(saisir)

    fin = Devinette(nbre, Nom1, Nom2)
    print(fin)
    print(Separation(2))
    

