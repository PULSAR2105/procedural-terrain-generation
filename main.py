import matplotlib.pyplot as plt
import matplotlib.image as img
from tqdm import tqdm
import numpy as np
import noise

import image_generator as img_gene
import perlin_noise as pnoise

map = pnoise.perlin_array((4002, 4002), 1000, 5, 0.3, 3, 0)

#map = np.round(map * 1000)

map *= 1000

img_gene.gene(map)

image = img.imread("image.png")
plt.imshow(image)
plt.show()



from mpl_toolkits.mplot3d import axes3d  # Fonction pour la 3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

X = np.indices((4002, 4002))[0]
Y = np.indices((4002, 4002))[1]
Z = map

# Tracé du résultat en 3D
fig = plt.figure()
ax = fig.gca(projection='3d')  # Affichage en 3D
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0)  # Tracé d'une surface
plt.title("Tracé d'une surface")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.show()
