import re
import os
import urllib.request
import json

def save(images, filename):
    with open(filename, "w") as file:
        json.dump(images, file)
        
def download_and_store():
    lines = open('files/urls.txt').readlines()
    names = open('files/inra_names.txt').readlines()
    i=0
    j=0
    for line in lines:
        for name in names:
            img = line.replace('\n', '')
            name = name.replace('\n', '')
            try: 
                filepath = os.path.join('/Users/golfdivine/Desktop/Computer Science/Engineering School/2020-2021/Cap Projet/beeopicture/Dataset/INRA/', name)
                urllib.request.urlretrieve(img, filepath)
                j+=1
                print(str(j) + '...')
            except urllib.error.HTTPError:
                print('Error on file ' + line)
                errors[i] = line
                i+=1
                continue



#save(errors, "http_errors.txt") 

def main():
    print("-----------------------")
    print("Starting crawling of INRA DB")
    download_and_store()
    print("Crawling done")
    
if __name__ == "__main__":
    main()
