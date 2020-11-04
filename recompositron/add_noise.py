import sys 
import os
from skimage import io, util
import matplotlib.pyplot as plt

def noise(path, noise, rows, cols, i):
    img = io.imread(path)/255.0
    plt.subplot(rows, cols, i)
    if noise is not None:
        n_img = util.random_noise(img, mode=noise)
        plt.imshow(n_img)
    else:
        plt.imshow(img)
    plt.title(noise)
    plt.axis("off")
    

def main(argv):
    plt.figure(figsize=(18,24))
    r=4
    c=2
    #for filename in os.listdir("canvas/"):
    path = os.path.join('canvas/', "pollen_colorized.jpg")
    print(path)
    noise(path, "gaussian", r, c, 1)
    noise(path, "localvar", r, c, 2)
    noise(path, "poisson", r, c, 3)
    noise(path, "salt", r, c, 4)
    noise(path, "pepper", r, c, 5)
    noise(path, "speckle", r, c, 1)
    noise(path, None, r, c, 8)
    plt.show() 

if __name__ == "__main__":
    argv = sys.argv[1:]
    main(argv)