import numpy as np

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
