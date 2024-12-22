J1:
	python3 J1.py

J2:
	python3 J2.py

J3:
	python3 J3.py


# Règle pour nettoyer le programme
nettoyer:
	rm -f ex

# Permet de add commit et push avec un message par default
partager : nettoyer
	sh partager.sh