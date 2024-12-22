J1:
	python3 J1.py

J2:
	python3 J2.py

J3:
	python3 J3.py

J4:
	python3 J4.py

J5:
	python3 J5.py

J6:
	python3 J6.py

All : J1 J2 J3 J4 J5 J6

# Règle pour nettoyer le programme
nettoyer:
	rm -f ex

# Permet de add commit et push avec un message par default
partager : nettoyer
	sh partager.sh