import re

def etoile1(fichier): 
    x = 0
    y = 0
    l = [(x,y)] 
    
    with open(fichier,"r") as f:
        lignes = f.readlines()
    for ligne in lignes:
        for c in ligne :
            if c == '^' :
                x+=1
            if c == 'v' :
                x-=1
            if c == '>' :
                y+=1
            if c == '<' :
                y-=1
            if not (x,y) in l:
                l.append((x,y))
    return len(l)
    
def etoile2(fichier): 
    xsc = 0
    ysc = 0
    xr = 0 
    yr = 0
    l = [(x,y)] 
    
    with open(fichier,"r") as f:
        lignes = f.readlines()
    for ligne in lignes:
        for c in ligne :
            if c == '^' :
                x+=1
            if c == 'v' :
                x-=1
            if c == '>' :
                y+=1
            if c == '<' :
                y-=1
            if not (x,y) in l:
                l.append((x,y))
    return len(l)

print("etoile1",etoile1("J3.txt"))
#print("etoile2",etoile2("J3.txt"))
