import re
import hashlib

def etoile1(fichier): 
    with open(fichier,"r") as f:
        lignes = f.readlines()
    ligne = lignes[0]
    i = 0
    while True :
        texte = ligne + str(i)
        md5 = hashlib.md5(texte.encode('utf-8')).hexdigest()
        if md5[0] == '0' and md5[1] == '0' and md5[2] == '0' and md5[3] == '0' and md5[4] == '0':
            return i
        i+=1

def etoile2(fichier): 
    with open(fichier,"r") as f:
        lignes = f.readlines()
    ligne = lignes[0]
    i = 0
    while True :
        texte = ligne + str(i)
        md5 = hashlib.md5(texte.encode('utf-8')).hexdigest()
        if md5[0] == '0' and md5[1] == '0' and md5[2] == '0' and md5[3] == '0' and md5[4] == '0' and md5[5] == '0':
            return i
        i+=1

print("etoile1",etoile1("J4.txt"))
print("etoile2",etoile2("J4.txt"))
