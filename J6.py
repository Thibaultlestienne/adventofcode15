import re

def comptervrai(lumieres):
    retour = 0
    for i in range(1000) :
        retour += sum(lumieres[i])
    return retour

def turnon(matrice, x1, y1 , x2, y2) :
    for i in range (x1, x2+1) :
        for j in range (y1, y2+1) :
            matrice[i][j]  = True

def turnoff(matrice, x1, y1 , x2, y2) :
    for i in range (x1, x2+1) :
        for j in range (y1, y2+1) :
            matrice[i][j]  = False

def switch(matrice, x1, y1 , x2, y2) :
    for i in range (x1, x2+1) :
        for j in range (y1, y2+1) :
            matrice[i][j]  = not matrice[i][j] 
        

def etoile1(fichier): 
    lumieres = [[False] * 1000 for _ in range (1000)]
    
    with open(fichier,"r") as f:
        lignes = f.readlines()

    for ligne in lignes :
        correspond = re.search(r"turn on (\d+),(\d+) through (\d+),(\d+)", ligne)
        if correspond :
            turnon(lumieres, int(correspond.group(1)) , int(correspond.group(2)), int(correspond.group(3)), int(correspond.group(4)))

        correspond = re.search(r"turn off (\d+),(\d+) through (\d+),(\d+)", ligne)
        if correspond :
            turnoff(lumieres, int(correspond.group(1)) , int(correspond.group(2)), int(correspond.group(3)), int(correspond.group(4)))

        correspond = re.search(r"toggle (\d+),(\d+) through (\d+),(\d+)", ligne)
        if correspond :
            switch(lumieres, int(correspond.group(1)) , int(correspond.group(2)), int(correspond.group(3)), int(correspond.group(4)))


    return comptervrai(lumieres)


def sommematrice(lumieres):
    retour = 0
    for i in range(1000) :
        retour += sum(lumieres[i])
    return retour

def turnon2(matrice, x1, y1 , x2, y2) :
    for i in range (x1, x2+1) :
        for j in range (y1, y2+1) :
            matrice[i][j]  += 1

def turnoff2(matrice, x1, y1 , x2, y2) :
    for i in range (x1, x2+1) :
        for j in range (y1, y2+1) :
            matrice[i][j]  = max([0, matrice[i][j]-1])

def switch2(matrice, x1, y1 , x2, y2) :
    for i in range (x1, x2+1) :
        for j in range (y1, y2+1) :
            matrice[i][j]  += 2
        

def etoile2(fichier): 
    lumieres = [[0] * 1000 for _ in range (1000)]
    
    with open(fichier,"r") as f:
        lignes = f.readlines()

    for ligne in lignes :
        correspond = re.search(r"turn on (\d+),(\d+) through (\d+),(\d+)", ligne)
        if correspond :
            turnon2(lumieres, int(correspond.group(1)) , int(correspond.group(2)), int(correspond.group(3)), int(correspond.group(4)))

        correspond = re.search(r"turn off (\d+),(\d+) through (\d+),(\d+)", ligne)
        if correspond :
            turnoff2(lumieres, int(correspond.group(1)) , int(correspond.group(2)), int(correspond.group(3)), int(correspond.group(4)))

        correspond = re.search(r"toggle (\d+),(\d+) through (\d+),(\d+)", ligne)
        if correspond :
            switch2(lumieres, int(correspond.group(1)) , int(correspond.group(2)), int(correspond.group(3)), int(correspond.group(4)))


    return sommematrice(lumieres)

print("etoile1",etoile1("J6.txt"))
print("etoile2",etoile2("J6.txt"))
