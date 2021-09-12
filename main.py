import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib import cm
from tqdm import tqdm
import numpy as np
import random

import image_generator as img_gene
import perlin_noise as pnoise

#scale = 1 meter/pixel----------

def seed(delta):
    return np.random.randint(0, delta)

map = np.zeros((2002, 2002))

#algorithm for seaside
def seaside():
    global map
    map = pnoise.perlin_array((2002, 2002), 2500, 1, 0, 0, seed(1000)) * 200
    map -= 100

    map += pnoise.perlin_array((2002, 2002), 300, 1, 0, 0, seed(1001)) * 30

    map += (pnoise.perlin_array((2002, 2002), 10, 1, 0, 0, seed(1002)) - 0.5) * 5

#algorithm for plain
def plain():
    global map

    map += 100

    map += pnoise.perlin_array((2002, 2002), 2000, 1, 0, 0, seed(1000)) * 30

    map += pnoise.perlin_array((2002, 2002), 400, 1, 0, 0, seed(1001)) * 10


plain()


#point of view
map[-1][-1] = np.max(map) + 300



"""
img_gene.gene(map)

image = img.imread("image.png")
plt.imshow(image)
plt.show()
"""



X = np.indices((2002, 2002))[0]
Y = np.indices((2002, 2002))[1]
Z = map

# Tracé du résultat en 3D
fig = plt.figure()
ax = fig.gca(projection='3d')  # Affichage en 3D
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0)  # Tracé d'une surface
plt.title("3D map viewer")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.show()
