def allumettes(jouer:bool) -> int:
    res:int
    allu:str
    a:int
    b:int
    nom1: str
    nom2: str
    
    allu = " Il reste des allumettes !"
    while jouer:
        nom1= input("Choisissez le nom du joueur 1: ")
        nom2= input("Choisissez le nom du joueur 2: ")
        res = 20
        while res > 0:
            
            a = int(input(nom1 +", choisissez le nombre d'allumettes que vous voulez prendre: \n"))
            while a < 1 or a > 3:
                a = int(input(nom1+", Veuillez choisir un nombre entre 1 et 3: \n"))
            res -= a
            if res <1:
                allu = "Tu as perdu, il n'y a plus d'allumettes !\n"
                return allu
                
            b = int(input(nom2+", choisissez le nombre d'allumettes que vous voulez prendre: \n"))
            while b<1 or b>3:
                b = int(input(nom2+", Veuillez choisir un nombre entre 1 et 3: \n"))
            res -=b
            if res > 0:
                print(allu)
        if res <1:
            allu = "Tu as perdu, il n'y a plus d'allumettes !"
            return allu
print(allumettes(True))