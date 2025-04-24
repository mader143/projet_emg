import numpy as np
from fonctions_communes import tube
from q1_potentiel import calcul_potentiel, afficher_potentiel
from q2_champE import calcul_champE, afficher_champE
from q3_trajectoire import calcul_trajectoire, afficher_trajectoire

# Par Maya Déry et Mia Croft-Pelletier

# # Appel pour calculer et visualiser le potentiel
potentiel = calcul_potentiel()
afficher_potentiel(potentiel)

# # Calculer le champ électrique
Ex, Ey = calcul_champE(potentiel)

# # Visualiser le champ électrique
grid, dynodes = tube()
afficher_champE(potentiel, Ex, Ey, dynodes)

# Exécution permettant le calcul et l'affichage de la trajectoire de l'électron
trajectoire = calcul_trajectoire(Ex, Ey, dynodes)
afficher_trajectoire(trajectoire, potentiel, dynodes, Ex, Ey)

#QUESTION 3C
#Exécution permettant d'afficher la trajectoire d'un électron, avec les paramètres du tube ajustés afin que l'électron percute chacune des dynodes
potentiel = calcul_potentiel(a=2e-3, b=2e-3, c=3.7e-3, d=1.8e-3, e=0.2e-3, f=6e-3, grid_res=0.1e-3)
grid, dynodes = tube(a=2e-3, b=2e-3, c=3.7e-3, d=1.8e-3, e=0.2e-3, f=6e-3, grid_res=0.1e-3)
Ex, Ey = calcul_champE(potentiel)
trajectoire = calcul_trajectoire(Ex, Ey, dynodes)
afficher_trajectoire(trajectoire, potentiel, dynodes, Ex, Ey)

# QUESTION 3D (BONUS)
#Exécution permettant d'afficher la trajectoire d'un électron, avec les paramètres du tube ajustés afin que l'électron percute chacune des dynodes
# Avec 12 dynodes
potentiel = calcul_potentiel(N=12, a=2e-3, b=2e-3, c=5e-3, d=1e-3, e=0.4e-3, f=6e-3)
grid, dynodes = tube(N=12, a=2e-3, b=2e-3, c=5e-3, d=1e-3, e=0.4e-3, f=6e-3)
Ex, Ey = calcul_champE(potentiel)
trajectoire = calcul_trajectoire(Ex, Ey, dynodes)
afficher_trajectoire(trajectoire, potentiel, dynodes, Ex, Ey)