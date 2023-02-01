import random
import math

def listidelist(list):
    mitugruppi = 0
    listidelist = []
    for lihasgrupp in list:
        f = open(lihasgrupp + ".txt")
        harjutused = []
        for rida in f:
            rida = rida.strip()
            harjutused += [rida]
        mitugruppi+=1
        f.close()
        listidelist += [harjutused]
    return listidelist,mitugruppi

def harjutused(listidelist):
    harj = []
    for a in listidelist[0]:
        if listidelist[1]>8:
            for b in range(math.ceil(8/listidelist[1])):
                x = random.choice(a)
                if x not in harj:
                    harj.append(x)
                else:
                    continue
                
        else:
            for b in range(math.floor(8/listidelist[1])):
                x = random.choice(a)
                if x not in harj:
                    harj.append(x)
                else:
                    continue
    return harj


