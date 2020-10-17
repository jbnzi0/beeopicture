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

def get_correct_url(driver):
    with open("oreme.txt", "r") as file:
        images = json.load(file)
        j=1
        for i in images:
            print("URL n°" +str(j))
            driver.get(images[i])
            images[i] = driver.current_url
            j+=1
            
    save(images, "oreme_with_correct_url.txt")
            
def download_and_store(images):
    for img in images:
        urllib.request.urlretrieve(images[img], img + ".jpg")

def main():
    driver = webdriver.Chrome('chromedriver')
    get_correct_url(driver)
    #url = "https://data.oreme.org/palyno/palyno_gallery#photo_taxon_list"
    #driver.get(url)
    #scrap(driver)
    time.sleep(5)
    driver.quit()



if __name__ == "__main__":
    main()