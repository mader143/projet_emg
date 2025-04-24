import numpy as np
import matplotlib.pyplot as plt
from equipe_01_main import tube

# Par Maya Déry et Mia Croft-Pelletier

#QUESTION 1: POTENTIEL

def calcul_potentiel(N=4, a=3e-3, b=2e-3, c=4e-3, d=2e-3, e=0.2e-3, f=6e-3, tolerance=1e-4, grid_res=0.1e-3):
    '''
        Fonction permettant de calculer le potentiel en implémentant la méthode de la relaxation
        Arguments: paramètres du tube, tolerance (différence maximale causant l'arrêt du calcul)
        Retourne le potentiel
    '''

    grid, dynodes = tube(N, a, b, c, d, e, f, grid_res)

    # Initialisation d'un tube à potentiel zéro sous la forme d'un array numpy
    potentiel = np.zeros_like(grid)

    # Conditions frontières (0V sur les parois du tube)
    potentiel[0,:] = 0
    potentiel[-1,:] = 0
    potentiel[:,0] = 0
    potentiel[:,-1] = 0

    # On met le potentiel de chaque dynode
    for i, (x1, y1, x2, y2) in enumerate(dynodes):
        potentiel[y1:y2, x1:x2] = 100 * (i + 1)

    # Implémentation de la méthode de la relaxation

    # On initialise la différence maximale avec un très grand nombre (infini)
    max_diff = float('inf')
    iteration = 0

    # Tant que la différence entre la nouvelle valeur et la valeur la plus proche des valeurs précédentes n'excède pas la tolérance choisie
    while max_diff > tolerance:
        # On remet la différence maximale à zéro pour chaque point
        max_diff = 0
        # Pour tous les points intérieurs du tube (Pas les parois)
        for i in range(1, potentiel.shape[0]-1):
            for j in range(1, potentiel.shape[1]-1):
                # Identifier les points sur les dynodes
                in_dynode = False
                for (x1, y1, x2, y2) in dynodes:
                    if y1 <= i < y2 and x1 <= j < x2:
                        in_dynode = True
                        break
                # Si le point est sur une dynode, on le passe
                if in_dynode:
                    continue

                # Calcul du nouveau potentiel (La nouvelle valeur de potentiel est la moyenne des 4 points environnants)
                new_val = 0.25 * (potentiel[i+1,j] + potentiel[i-1,j] + potentiel[i,j+1] + potentiel[i,j-1])

                # On calcule la différence entre cette nouvelle valeur et l'ancienne valeur de potentiel
                diff = abs(new_val - potentiel[i,j])

                # Si la différence est plus grande que la différence maximale, cette différence devient la nouvelle valeur maximale
                if diff > max_diff:
                    max_diff = diff
                
                # Le potentiel de ce point devient la nouvelle valeur calculée
                potentiel[i,j] = new_val

        # Suivi des itérations et de la différence maximale (Aide en cas de problème qui rend le calcul trop long)
        iteration += 1
        if iteration % 100 == 0:
            print(f"Itération {iteration}, max_diff: {max_diff}")

    print(f"A convergé après {iteration} itérations")
    return potentiel

def afficher_potentiel(potentiel, grid_res=0.1e-3):
    '''Fonction qui permet de visualiser le potentiel à l'aide de matplotlib, les axes sont en mètres'''

    plt.figure(figsize=(10, 6))
    plt.imshow(potentiel, cmap='viridis', origin='lower', extent=[0, potentiel.shape[1]*grid_res,
                      0, potentiel.shape[0]*grid_res])
    plt.colorbar(label='Potentiel [V]')
    plt.title('Distribution du potentiel dans le tube photomultiplicateur')
    plt.xlabel('Position en x [m]')
    plt.ylabel('Position en y [m]')
    plt.show()