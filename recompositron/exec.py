import cv2
import os, random, string
from PIL import Image, ImageDraw, ImageFilter
#loop through pictures directory
#augment images in directory
#save new images in /augmented
#empty standalones directory

def augment():
    augmented = {}
    for filename in os.listdir("test/"):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = cv2.imread(os.path.join('test/',filename))
            name = filename.replace(".png", "") or filename.replace(".jpg", "")
            augmented[name + '_vertical.png'] = cv2.flip(img, 0)
            augmented[name + '_horizontal.png'] = cv2.flip(img, 1)
            augmented[name + '_both.png'] = cv2.flip(img, -1)
            
            cv2.imwrite(os.path.join('augmented/', filename), img)
            for key, val in augmented.items():
                cv2.imwrite(os.path.join('augmented/', key), val)
            os.remove('test/' +filename)
            augmented = {}
        else:
            print("Empty folder")
#augment() 

#n, zoomLevel
def generateCanva(n):
    background = Image.open('background.png')
    pollens = []
    for i in range(n):
        rand = random.choice([x for x in os.listdir("standalones/") if os.path.isfile(os.path.join("standalones/", x))])
        x = int(random.uniform(0, 963))
        y = int(random.uniform(0, 624))
        img = Image.open('standalones/' + rand)
        background.paste(img, (x,y))
    z = int(random.uniform(3,15))
    name = get_random_string(z) + '.png'
    background.save('canvas/' +name, quality=95)
        #pollens.append(rand)
    #loop through augmented/ and select n images
        



def get_random_string(length):
    letters = string.ascii_lowercase
    rand = ''.join(random.choice(letters) for i in range(length))
    return rand

augment()

#generateCanva(7)
    # random selection of pollen in /augmented
    # create gray image 961x626 
    # add noise to image
    # random positioning of pollens on the image