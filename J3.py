import re

def etoile1(fichier): 
    x = 0
    y = 0
    l = [(x,y)] 
    
    with open(fichier,"r") as f:
        lignes = f.readlines()
    ligne = lignes[0]
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
    xsc = 0 # sc -> santa clauss
    ysc = 0
    xr = 0 # r -> robot
    yr = 0
    l = [(xr,yr)] 
    
    with open(fichier,"r") as f:
        lignes = f.readlines()

    i  = 0
    ligne = lignes[0]
    for c in ligne :
        if i % 2 == 0 :
            if c == '^' :
                xsc+=1
            if c == 'v' :
                xsc-=1
            if c == '>' :
                ysc+=1
            if c == '<' :
                ysc-=1
            if not (xsc,ysc) in l:
                l.append((xsc,ysc))
        else :
            if c == '^' :
                xr+=1
            if c == 'v' :
                xr-=1
            if c == '>' :
                yr+=1
            if c == '<' :
                yr-=1
        if not (xr,yr) in l:
            l.append((xr,yr))
    
        i+=1
    return len(l)

print("etoile1",etoile1("J3.txt"))
print("etoile2",etoile2("J3.txt"))
