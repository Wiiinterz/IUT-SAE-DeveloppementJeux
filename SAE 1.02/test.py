import random
if __name__=="__main__" :
    scoreb = 0
    scorea = 0

    scorec = 0
    scored = 0

    scoree = 0
    scoref = 0

    scoreg = 0
    scoreh = 0

    scorei = 0
    scorej = 0

    for k in range(0,100) :
        res = 20
        while res > 0 :
            a = random.randint(1,3)
            if res-a <1 :
                scoreb =scoreb +1
            res = res - a
            b = random.randint(1,3)
            if res-b <1 and res >0:
                scorea = scorea +1
            res = res - b
    print("Diff 1- Victoire Gus: ",scorea, "Victoire Bobby: ",scoreb)

    for k in range(0,100) :
        res = 20
        while res > 0 :
            if res ==3 :
                a =2
            elif res == 2 :
                a = 1
            else :
                a = random.randint(1,3)
            if res-a <1 :
                scored =scored +1
            res = res - a
            if res ==3 :
                b =2
            elif res == 2 :
                b = 1
            else :
                b = random.randint(1,3)
            if res-b <1 and res >0:
                scorec = scorec +1
            res = res - b
    print("Diff 2- Victoire Gus: ",scorec, "Victoire Bobby: ",scored)
            
    for k in range(0,100) :
        res = 20
        while res > 0 :
            if res == 20 or res == 16 or res ==12 or res == 8 or res == 4:
                a = 3
            elif res == 19 or res ==15 or res == 11 or res == 7 or res == 3 :
                a = 2
            else :
                a = 1
            if res-a <1 :
                scoref =scoref +1
            res = res - a
            if res == 20 or res == 16 or res ==12 or res == 8 or res == 4:
                b = 3
            elif res == 19 or res ==15 or res == 11 or res == 7 or res == 3 :
                b = 2
            else :
                b = 1
            if res-b <1 and res >0:
                scoree = scoree +1
            res = res - b
    print("Diff 3- Victoire Gus: ",scoree, "Victoire Bobby: ",scoref)

    for k in range(0,100) :
        res = 20
        while res > 0 :
            a = random.randint(1,3)
            if res-a <1 :
                scoreh =scoreh +1
            res = res - a
            if res ==3 :
                b =2
            elif res == 2 :
                b = 1
            else :
                b = random.randint(1,3)
            if res-b <1 and res >0:
                scoreg = scoreg +1
            res = res - b
    print("Diff 1-Diff 2- Victoire Gus: ",scoreg, "Victoire Bobby: ",scoreh)

    for k in range(0,100) :
        res = 20
        while res > 0 :
            if res ==3 :
                a =2
            elif res == 2 :
                a = 1
            else :
                a = random.randint(1,3)
            if res-a <1 :
                scorej =scorej +1
            res = res - a
            if res == 20 or res == 16 or res ==12 or res == 8 or res == 4:
                b = 3
            elif res == 19 or res ==15 or res == 11 or res == 7 or res == 3 :
                b = 2
            else :
                b = 1
            if res-b <1 and res >0:
                scorei = scorei +1
            res = res - b
    print("Diff 2-Diff 3- Victoire Gus: ",scorei, "Victoire Bobby: ",scorej)