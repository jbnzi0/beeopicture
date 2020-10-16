#!/usr/bin/env python
# coding: utf-8
import os
import time
import urllib.request
import json
from selenium import webdriver

def scrap(driver):
    images = {}
    divs = driver.find_elements_by_class_name("col-md-3")
    i=0
    for div in divs:
        try:
            if i<=2:
                link = div.find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute('data-src')
                pollen = div.find_element_by_tag_name('a').find_element_by_tag_name('p').get_attribute('innerHTML').strip()
                pollen = pollen.replace(" ", "_").lower()
                images[pollen] = link
                print(images)
                i+=1
            else:
                break
        except:
            print("No desc")
    save(images)
    #download_and_store(images)

def save(images):
    with open("oreme.txt", "w") as file:
        json.dump(images, file)
def download_and_store(images):
    for img in images:
        urllib.request.urlretrieve(images[img], img + ".jpg")

def main():
    driver = webdriver.Chrome('chromedriver')
    url = "https://data.oreme.org/palyno/palyno_gallery#photo_taxon_list"
    driver.get(url)
    scrap(driver)
    time.sleep(5)
    driver.quit()
    
    
    
if __name__ == "__main__":
    main()