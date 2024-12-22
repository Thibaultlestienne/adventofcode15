def etoile1(fichier): 
    s = 0;
    with open(fichier,"r") as f:
        lignes = f.readlines()
    for ligne in lignes:
        for c in ligne : 
            if c == "(" :
                s+=1
            else :
                s-=1
    return s
    
def etoile2(fichier): 
    s = 0;
    i = 0
    with open(fichier,"r") as f:
        lignes = f.readlines()
    for ligne in lignes:
        for c in ligne : 
            i+=1
            if c == "(" :
                s+=1
            else :
                s-=1
            if s == -1 :
                return i
    return "ERREUR"

print("etoile1",etoile1("J1.txt"))
print("etoile2",etoile2("J1.txt"))
