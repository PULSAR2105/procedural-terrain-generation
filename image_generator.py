from PIL import Image
from tqdm import tqdm
import numpy as np
from numba import jit
import math

def gene(arr):
    size = np.shape(arr)

    im = Image.new("RGB", size)
    pix = im.load()

    sea = [(1, 40, 63),
           (11, 56, 81),
           (16, 74, 107),
           (22, 79, 106),
           (29, 85, 109),
           (39, 90, 111),
           (49, 96, 114)]

    sand = (212, 195, 163)

    grass = [(75, 115, 69), 
             (66, 104, 62), 
             (62, 98, 60),
             (59, 95, 57),
             (56, 92, 54),
             (49, 85, 46)]
    
    dirt = [(103, 83, 67), 
            (110, 90, 75),
            (120, 100, 85)]

    stone = [(109, 109, 109),
             (118, 118, 118)]

    snow = [(216, 216, 216),
            (229, 229, 229)]
     
    #grass = (75, 115, 69)
    #dirt = (103, 83, 67)
    #stone = (109, 109, 109)
    #snow = (229, 229, 229)    

    """
    angles = np.zeros(size)
    for y in tqdm(range(1, size[1] - 1)):
        for x in range(1, size[0] - 1):
                pix_angles = np.array([arr[y][x] - arr[y-1][x],
                                       arr[y][x] - arr[y-1][x+1], 
                                       arr[y][x] - arr[y][x+1], 
                                       arr[y][x] - arr[y+1][x+1], 
                                       arr[y][x] - arr[y+1][x], 
                                       arr[y][x] - arr[y+1][x-1], 
                                       arr[y][x] - arr[y][x-1], 
                                       arr[y][x] - arr[y-1][x-1]])

                pix_angles = abs(pix_angles)

                for r in range(len(pix_angles)):
                    pix_angles[r] = math.atan(abs(pix_angles[r])) * (180 / math.pi)
                
                angles[y][x] = np.max(pix_angles)
    """

    #Couleur altitude
    color = (0,0,0)
    for y in tqdm(range(1, size[1] - 1)):
        for x in range(1, size[0] - 1):
            
            if arr[y][x] <= 350:
                c = round(arr[y][x] / (350 / len(sea)))
                if c != 0: c-=1
                color = sea[c]
            
            if arr[y][x] > 350 and arr[y][x] <= 420:
                color = sand

            if arr[y][x] > 420 and arr[y][x] <= 650:
                c = round((arr[y][x] - 420) / ((650 - 420) / len(grass)))
                if c != 0: c-=1
                color = grass[c]

            if arr[y][x] > 650 and arr[y][x] <= 750:
                c = round((arr[y][x] - 650) / ((750 - 650) / len(dirt)))
                if c != 0: c-=1
                color = dirt[c]

            if arr[y][x] > 750 and arr[y][x] <= 900:
                c = round((arr[y][x] - 750) / ((900 - 750) / len(stone)))
                if c != 0: c-=1
                color = stone[c]

            if arr[y][x] > 900 and arr[y][x] <= 1000:
                c = round((arr[y][x] - 900) / ((1000 - 900) / len(snow)))
                if c != 0: c-=1
                color = snow[c]

            pix[x, y] = color






    """
    color = (142, 142, 142)
    for y in tqdm(range(1, size[1] - 1)):
        for x in range(1, size[0] - 1):

            if (arr[y][x]%10 == 0 or arr[y][x]%10 == 1) and arr[y][x] > 351:

                n = 0
                if pix[x, y + 1] == color:
                    n += 1
                if pix[x, y - 1] == color:
                    n += 1
                if pix[x - 1, y] == color:
                    n += 1
                if pix[x + 1, y] == color:
                    n += 1

                if pix[x - 1, y - 1] == color:
                    n += 1
                if pix[x - 1, y + 1] == color:
                    n += 1
                if pix[x + 1, y + 1] == color:
                    n += 1
                if pix[x + 1, y - 1] == color:
                    n += 1
                
                if n < 6:
                    pix[x, y] = color
    """
    
    im.save('image.png')

