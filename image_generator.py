from PIL import Image
from tqdm import tqdm
import numpy as np

def gene(arr):
    size = np.shape(arr)

    im = Image.new("RGB", size)
    pix = im.load()

    seaRGB = (49, 96, 114)
    sandRGB = (213, 195, 163)
    grassRGB = (75, 115, 69)
    dirtRGB = (103, 83, 67)
    stoneRGB = (134, 134, 134)
    snowRGB = (255, 255, 255)

    color = (0,0,0)
    for y in tqdm(range(size[1])):
        for x in range(size[0]):

            if arr[y][x] <= 0.35:
                color = seaRGB

            if arr[y][x] > 0.35 and arr[y][x] <= 0.4:
                color = sandRGB

            if arr[y][x] > 0.4 and arr[y][x] <= 0.65:
                color = grassRGB 

            if arr[y][x] > 0.65 and arr[y][x] <= 0.75:
                color = dirtRGB

            if arr[y][x] > 0.75 and arr[y][x] <= 0.9:
                color = stoneRGB

            if arr[y][x] > 0.9 and arr[y][x] <= 1:
                color = snowRGB

            pix[x, y] = color

    im.save('image.png')
