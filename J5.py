import re

def etoile1(fichier): 
    retour = 0
    
    with open(fichier,"r") as f:
        lignes = f.readlines()

    for ligne in lignes :
        nbvoyelle = 0
        double = False
        paireinterdite = False

        for i in range(len(ligne)) :
            if ligne[i] in ['a','e','u','i','o'] :
                nbvoyelle += 1
            if  i+1<len(ligne) and ligne[i] == ligne[i+1] :
                double = True
            if i+1<len(ligne) and ligne[i] + ligne[i+1] in ['ab', 'cd','pq','xy'] :
                paireinterdite = True
        if nbvoyelle >= 3 and double and not paireinterdite :
            retour += 1
    return retour

def etoile2(fichier): 
    retour = 0
    
    with open(fichier,"r") as f:
        lignes = f.readlines()

    for ligne in lignes :
        listerepetition = []
        repetition = False
        sandwich = False

        for i in range(len(ligne)) :
            if  i+1<len(ligne) and ligne[i] + ligne[i+1] in listerepetition:
                repetition = True
            
            if  i-1>=0 :
                listerepetition.append(ligne[i-1] + ligne[i])

            if  i+2<len(ligne) and ligne[i] == ligne[i+2] :
                sandwich = True

        if repetition and sandwich :
            retour += 1
    return retour


print("etoile1",etoile1("J5.txt"))
print("etoile2",etoile2("J5.txt"))
