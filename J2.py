import re

def etoile1(fichier): 
    s = 0;
    with open(fichier,"r") as f:
        lignes = f.readlines()
    for ligne in lignes:
        resultat = re.search(r"(\d+)x(\d+)x(\d+)\s+", ligne)
        if resultat:
            x = int(resultat.group(1)) 
            y = int(resultat.group(2)) 
            z = int(resultat.group(3)) 
            s+=2*(x*y+x*z+y*z) + min(x*y,x*z,y*z)
    return s
    
def etoile2(fichier): 
    s = 0;
    with open(fichier,"r") as f:
        lignes = f.readlines()
    for ligne in lignes:
        resultat = re.search(r"(\d+)x(\d+)x(\d+)\s+", ligne)
        if resultat:
            x = int(resultat.group(1)) 
            y = int(resultat.group(2)) 
            z = int(resultat.group(3)) 
            s+=x*y*z + 2*( min(x, y) + min (x, z) + min (y, z) - min (x, y, z) )
    return s

print("etoile1",etoile1("J2.txt"))
print("etoile2",etoile2("J2.txt"))
