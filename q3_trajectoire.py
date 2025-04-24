import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Par Maya Déry et Mia Croft-Pelletier

#QUESTION 3A ET B

# Constantes utilisées pour les calculs
q_e = -1.602e-19  # Charge d'un électron (C)
m_e = 9.109e-31    # Masse d'un électron (kg)

def calcul_trajectoire(Ex, Ey, dynodes, grid_res=0.1e-3, dt=1e-12, steps=10000,
                                x0=0, y0=3e-3, vx0=0, vy0=0):
    """
    Simulation de la trajectoire d'un électron à l'aide de la méthode d'Euler avec une vérification des limites du tube.
    S'arrête lorsque l'électron quitte le tube.

    Arguments: 
    Les composantes en x et en y du champ électrique (Ex, Ey)
    La résolution de la grille (grid_res)
    Le pas de temps de la simulation (dt), permet de contrôler la précision de la trajectoire et le temps réel que dure la trajectoire
    Le nombre de "pas" que fera l'électron, donc le nombre de fois qu'on calculera sa nouvelle position (steps)
    Les position et vitesse intiales (x0, y0, vx0, vy0)

    Retourne un array numpy de listes contenant chaque position x, y calculée, donc la trajectoire de l'électron
    """
    # Constantes
    q = -1.602e-19  # Charge d'un électron (C)
    m = 9.11e-31    # Masse d'un électron (kg)

    # Mettre l'état à sa valeur initiale
    x, y = x0, y0
    vx, vy = vx0, vy0
    trajectoire = [(x, y)]

    # Frontières du tube (en metres)
    tube_width = Ey.shape[0] * grid_res
    tube_length = Ex.shape[1] * grid_res

    for _ in range(steps):
        # Vérifier si l'électron a quitté le tube
        if x < 0 or x > tube_length or y < 0 or y > tube_width:
            print("L'électron a quitté le tube.")
            break
        
        # # Vérifier les limites du tableau
        # if i < 0 or i >= Ey.shape[0] or j < 0 or j >= Ex.shape[1]:
        #     print("Electron left the simulation grid.")
        #     break

        # Convertir la position en indices de grille
        i = int(y / grid_res)
        j = int(x / grid_res)

        # Obtenir le champ électrique de cette position
        Ex_local = Ex[i, j]
        Ey_local = Ey[i, j]

        # Calcul de l'accélération avec F = ma
        ax = (q * Ex_local / m)
        ay = (q * Ey_local / m)

        # Mettre à jour la vitesse et la position (selon la méthode d'Euler)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        for (x1, y1, x2, y2) in dynodes:
        # Convertir la position (en m) en indice de grille
            if x1 * grid_res <= x <= x2 * grid_res and y1 * grid_res <= y <= y2 * grid_res:
                # Rebondi verticallement de 2mm
                #On met un déplacement contraire à la vitesse
                if vy > 0:
                    y -= 0.002  # en m
                if vy < 0:
                    y += 0.002  # en m
                break

        # Mémoriser la nouvelle position en l'ajoutant à la liste des positions de la trajectoire
        trajectoire.append((x, y))

    return np.array(trajectoire)

def afficher_trajectoire(trajectoire, potentiel, dynodes, Ex, Ey, grid_res=0.1e-3):
    plt.figure(figsize=(10, 6))
    extent = [0, potentiel.shape[1] * grid_res,
              0, potentiel.shape[0] * grid_res]

    plt.imshow(potentiel, cmap='viridis', origin='lower', extent=extent)
    plt.colorbar(label='Potentiel (V)')

    x = trajectoire[:, 0]
    y = trajectoire[:, 1]
    plt.plot(x, y, 'r-', label="Trajectoire de l'électron")
    plt.xlabel('Position en x (m)')
    plt.ylabel('Position en y (m)')
    plt.legend()

    # 3. Tracer les flèches représentant le champ électrique
    ds = 6  # Facteur de sous-échantillonnage afin d'éviter la surcharge de flèches (on prends seulement un point tous les 6 points)
    x = np.arange(0, potentiel.shape[1], ds) * grid_res
    y = np.arange(0, potentiel.shape[0], ds) * grid_res
    X, Y = np.meshgrid(x, y)

    # Normaliser la longueur des flèches (1 mm = 1e5 V/m)
    échelle = 100000  # V/m par mm de longueur de flèche
    Ex_norme = Ex[::ds, ::ds] / échelle
    Ey_norme = Ey[::ds, ::ds] / échelle

    plt.quiver(X, Y, Ex_norme, Ey_norme,
              color='white',
              scale=25,  # plus bas = flèches plus larges
              width=0.003,
              pivot='middle',
              headwidth=3)

    # 4. Identifier les dynodes sur le graphique
    for i, (x1, y1, x2, y2) in enumerate(dynodes):
        plt.gca().add_patch(Rectangle(
            (x1*grid_res, y1*grid_res),
            (x2-x1)*grid_res, (y2-y1)*grid_res,
            linewidth=1, edgecolor='red', facecolor='none'
        ))
        plt.text((x1+x2)/2*grid_res, (y1+y2)/2*grid_res,
                f'{100*(i+1)}V', ha='center', va='center', color='white')

    plt.title('Champ électrique dans le tube photomultiplicateur\n(1 mm de flèche = 10000 V/m)')
    plt.grid(alpha=0.3)
    plt.show()