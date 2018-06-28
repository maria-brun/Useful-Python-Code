# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:16:00 2018

@author: mcboe72
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def login_and_search():
    
    driver = webdriver.Chrome(executable_path=r'C:\Users\mcboe72\Anaconda\chromedriver.exe' )
    
    driver.get('https://www.PUTYOURWEBSITEHERE.com/')
    
    driver.maximize_window()
    
   #update this using copy xpath
    email = driver.find_element_by_xpath('//*[@id="login-email"]')
    email.send_keys('youremail@domain.com')
    
    time.sleep(1)
    
   #update this using copy xpath
    password = driver.find_element_by_xpath('//*[@id="login-password"]')
    password.send_keys('your_password')
    
    time.sleep(1)
    
   #update this using copy xpath
    login = driver.find_element_by_xpath('//*[@id="login-submit"]')
    login.click()
    
    time.sleep(1)
    
   #update this using copy xpath
    search = driver.find_element_by_xpath('//*[@id="ember1232"]/input')
    search.send_keys('electricity markets')
    
    time.sleep(1)
   
   #update this using copy xpath
    search_buttom = driver.find_element_by_xpath('//*[@id="nav-search-controls-wormhole"]/button')
    search_buttom.click()
    
    time.sleep(1)
    
     
    return driver
    
    #driver.quit()

def get_detail_information(driver):
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    #update this using copy xpath
    for p in soup.find_all('p', class_ = 'subline-level-1 Sans-15px-black-85% search-result__truncate'):
        print(p.text)
    
    #update this using copy xpath
    for a in soup.find_all('a', class_= 'search-result__info pt3 pb4 ph0'):
        print(a['href'])
        
get_detail_information(login_and_search())
    