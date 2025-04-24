import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Par Maya Déry et Mia Croft-Pelletier

#QUESTION 2: CHAMP ÉLECTRIQUE

def calcul_champE(potential, grid_res=0.1e-3):
    """
    Fonction permettant de calculer le champ électrique à l'aide de la formule E = -del(V)
    Arguments: potentiel (tableau 2D numpy de potentiel (V)), grid_res (résolution de la grille en m)
    Retourne Ex et Ey (Composants du champ électrique en V/m)
    """
    # Calculer le gradient avec la fonction numpy
    Ey, Ex = np.gradient(-potential, grid_res, grid_res)

    return Ex, Ey

def afficher_champE(potential, Ex, Ey, dynodes, grid_res=0.1e-3):
    """Fonction permettant de visualiser le champ électrique avec le potentiel en fond"""
    plt.figure(figsize=(12, 6))

    # 1. Afficher le potentiel (background avec échelle de couleur)
    plt.imshow(potential, cmap='viridis',
              extent=[0, potential.shape[1]*grid_res,
                      0, potential.shape[0]*grid_res],
              origin='lower', alpha=0.7)
    plt.colorbar(label='Potentiel (V)')

    # 2. Tracer les vecteurs du champ électrique
    ds = 6  # Facteur de sous-échantillonnage (on prends 1 point tous les 6 points, pour réduire le nombre de flèches)
    x = np.arange(0, potential.shape[1], ds) * grid_res
    y = np.arange(0, potential.shape[0], ds) * grid_res
    X, Y = np.meshgrid(x, y)

    # Normaliser la longueur des flèches (1 mm = 1e5 V/m)
    scale = 100000  #V/m par mm de longueur de flèche
    Ex_norm = Ex[::ds, ::ds] / scale
    Ey_norm = Ey[::ds, ::ds] / scale

    plt.quiver(X, Y, Ex_norm, Ey_norm,
              color='white',
              scale=25,
              width=0.003,
              pivot='middle',
              headwidth=3)

    # 3. Identifier les dynodes avec des rectangles
    for i, (x1, y1, x2, y2) in enumerate(dynodes):
        plt.gca().add_patch(Rectangle(
            (x1*grid_res, y1*grid_res),
            (x2-x1)*grid_res, (y2-y1)*grid_res,
            linewidth=1, edgecolor='red', facecolor='none'
        ))
        plt.text((x1+x2)/2*grid_res, (y1+y2)/2*grid_res,
                f'{100*(i+1)}V', ha='center', va='center', color='white')

    plt.title('Champ électrique dans le tube photomultiplicateur\n(1 mm de flèche = 10000 V/m)')
    plt.xlabel('Position en x (m)')
    plt.ylabel('Position en y (m)')
    plt.grid(alpha=0.3)
    plt.show()