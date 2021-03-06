from tqdm import tqdm
import numpy as np
import noise

def perlin_array(shape = (1000, 1000), scale = 250, octaves = 5, persistence = 0.5, lacunarity = 2.6, seed =  0):

    arr = np.zeros(shape)
    for i in tqdm(range(shape[0])):
        for j in range(shape[1]):
            arr[i][j] = noise.pnoise2(i / scale,
                                      j / scale,
                                      octaves=octaves,
                                      persistence=persistence,
                                      lacunarity=lacunarity,
                                      repeatx=1024,
                                      repeaty=1024,
                                      base=seed)
    
    max_arr = np.max(arr)
    min_arr = np.min(arr)
    norm_me = lambda x: (x - min_arr) / (max_arr - min_arr)
    norm_me = np.vectorize(norm_me)
    arr = norm_me(arr)

    return arr