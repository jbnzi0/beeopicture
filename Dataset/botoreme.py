#!/usr/bin/env python
# coding: utf-8
import os
import time
import urllib.request
import json
from selenium import webdriver

def scrap(driver):
    print('Oreme Database')
    print('Launched at ' + time.strftime('%X %x %Z'))
    images = {}
    divs = driver.find_elements_by_class_name("col-md-3")
    for div in divs:
        try:
            link = div.find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute('data-src')
            pollen = div.find_element_by_tag_name('a').find_element_by_tag_name('p').get_attribute('innerHTML').strip()
            pollen = pollen.replace(" ", "_").lower()
            images[pollen] = link
            print(images)
        except:
            print("No desc")
    print('Ended at ' + time.strftime('%X %x %Z'))
    save(images, "oreme.txt")
    #download_and_store(images)

def save(images, filename):
    with open(filename, "w") as file:
        json.dump(images, file)

def get(filename):
    with open(filename, "r") as file:
        images = json.load(file)
    return images

def get_correct_url(driver):
    images = get("oreme.txt")
    j=1
    for i in images:
        print("URL n°" +str(j))
        driver.get(images[i])
        images[i] = driver.current_url
        j+=1  
    save(images, "oreme_with_correct_url.txt")
            
def download_and_store():
    images = get("oreme_with_correct_url.txt")
    errors = {}
    i=0
    for img in images:
        try:
            filepath = os.path.join('/Users/golfdivine/Desktop/Computer Science/Engineering School/2020-2021/Cap Projet/BeeOImage/Dataset/Oreme2', img + ".jpg")
            urllib.request.urlretrieve(images[img], filepath)
            print(img + " downloaded")
        except urllib.error.HTTPError:
            print("Error on file " + img)
            errors[i]=img
            i+=1
            continue
    save(errors, "http_errors.txt")
    
def main():
    download_and_store()
    #driver = webdriver.Chrome('chromedriver')
    #url = "https://data.oreme.org/palyno/palyno_gallery#photo_taxon_list"
    #driver.get(url)
    #scrap(driver)
    
    #time.sleep(5)
    #driver.quit()



if __name__ == "__main__":
    main()