import cv2
import os


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
augment() 

    
#loop through pictures directory
    #augment images in directory
    #save new images in /augmented
    #empty standalones directory
    

#def generateCanva():
    # random selection of pollen in /augmented
    # create gray image 961x626 
    # add noise to image
    # random positioning of pollens on the image