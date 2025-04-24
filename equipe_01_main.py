import numpy as np
from q1_potentiel import calcul_potentiel, afficher_potentiel
from q2_champE import calcul_champE, afficher_champE
from q3_trajectoire import calcul_trajectoire, afficher_trajectoire

# Par Maya Déry et Mia Croft-Pelletier

#Définition de la fonction principale pour construire le tube
def tube(N=4, a=3e-3, b=2e-3, c=4e-3, d=2e-3, e=0.2e-3, f=6e-3, grid_res=0.1e-3):
    """
        Fonction permettant de modéliser la géométrie d'un tube photomultiplicateur
        Arguments : paramètres du tube (de l'énoncé), grid_res (résolution de la grille, taille des carrés)
        Retourne un array numpy représentant le tube (grid) ainsi qu'une liste de tuples
        contenant les positions des dynodes (x1, y1, x2, y2)
    """

    # Calcul de la longueur et largeur du tube
    tube_length = 2*a + d/2 + ((N/2)-1)*d + (N/2)*c + c/2  # Horizontal (axe des x)
    tube_width = f                      # Vertical (axe des y)

    # Dimension de la grille
    nx = int(tube_length / grid_res)    # points sur l'axe des x
    ny = int(tube_width / grid_res)     # points sur l'axe des y

    #Création de la grille (matrice de zéros en array numpy) de taille (ny, nx)
    grid = np.zeros((ny, nx))           # Note: 1ere dimension est en y, 2eme en x

    # Calcul de la position des dynodes (coin inférieur gauche et coin supérieur droit, en x et en y, en coordonnées de la grille)

    # Initialisation de la liste des dynodes
    # Chaque dynode représentera un rectangle dans la grille
    dynodes = []
    for i in range(N):
        if i % 2 == 0:  # dynodes du bas (indices pairs)
            y1 = int(b / grid_res)
            y2 = int((b + e) / grid_res)
            x1 = int((a + (i/2)*(d + c)) / grid_res)
            x2 = int((a + (i/2)*(d + c) + c) / grid_res)
        else:            # dynodes du haut (indices impairs)
            y1 = int((tube_width - b - e) / grid_res)
            y2 = int((tube_width - b) / grid_res)
            x1 = int((a + c/2 + d/2 + ((i-1)/2)*(d + c)) / grid_res)
            x2 = int((a + c/2 + d/2 + c + ((i-1)/2)*(d + c)) / grid_res)

        dynodes.append((x1, y1, x2, y2))

    return grid, dynodes

# # Appel pour calculer et visualiser le potentiel
potentiel = calcul_potentiel()
afficher_potentiel(potentiel)

# # Calculer le champ électrique
Ex, Ey = calcul_champE(potentiel)

# # Visualiser le champ électrique
grid, dynodes = tube()
afficher_champE(potentiel, Ex, Ey, dynodes)

# Exécution permettant le calcul et l'affichage de la trajectoire de l'électron
Ex, Ey = calcul_champE(potentiel)
trajectoire = calcul_trajectoire(Ex, Ey, dynodes)
afficher_trajectoire(trajectoire, potentiel, Ex, Ey, dynodes)

#QUESTION 3C
#Exécution permettant d'afficher la trajectoire d'un électron, avec les paramètres du tube ajustés afin que l'électron percute chacune des dynodes
potentiel = calcul_potentiel(a=2e-3, b=4e-3, c=8e-3, d=4e-3, e=0.4e-3, f=14e-3, grid_res=0.1e-3)
grid, dynodes = tube(a=2e-3, b=4e-3, c=8e-3, d=4e-3, e=0.4e-3, f=14e-3, grid_res=0.1e-3)
Ex, Ey = calcul_champE(potentiel)
Emag = np.sqrt(Ex**2 + Ey**2)
print(F'Max field : {np.max(Emag)}')
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