# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 08:47:09 2018

@author: mcboe72
"""

#Get the working directory

import os
os.getcwd()

#Change the working directory and confirm it changed to where you want it to be!

os.chdir('C:\\Users\\mcboe72\\Desktop\\')
os.getcwd()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from inscriptis import get_text
import pandas as pd
from pandas import DataFrame
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from datetime import datetime 

class Job():
    def _init_(self):
        self.title = ""
        self.company = ""
        self.location = ""
        self.link = ""
        
job_list = []
link_list = []

def login_and_search(keyword, location):
    
    driver = webdriver.Chrome(executable_path=r'C:\Users\mcboe72\Anaconda\chromedriver.exe' )
    
    driver.get('https://www.monster.com/')
        
    driver.maximize_window()
        
    search = driver.find_element_by_xpath('//*[@id="q2"]')
    search.send_keys(keyword)
    time.sleep(1)
        
    place = driver.find_element_by_xpath('//*[@id="where2"]')
    place.send_keys(Keys.CONTROL + "a");
    place.send_keys(Keys.DELETE)
    place.send_keys(location)    
    time.sleep(1)
        
    search_buttom = driver.find_element_by_xpath('//*[@id="doQuickSearch2"]')
    search_buttom.click()
    time.sleep(1)
    
    try:
        more_button = driver.find_element_by_xpath('//*[@id="ResultsScrollable"]/div/a')
        more_button.click()
        time.sleep(1)
        more_button.click()
    except NoSuchElementException:
        time.sleep(1)
        

    return driver

def get_detail_information(driver):
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    results = soup.find('div', {'id':'SearchResults'})    #job_list = []
    
    
   
    for result in results.find_all('section', class_ = 'card-content'): #{"class":["card-content", "card-content is-active"]}):
        
        info_find = result.find('div', class_='summary')
        title = info_find.find('h2', class_ = 'title')
        job_title = title.text 
        link = info_find.find('a')
        job_link = link.attrs['href'].strip().replace('\r', '').replace('\n', '')
        company = result.find('div', class_='company')
        company_name = company.text.replace('\r', '').replace('\n', '')
        location = result.find('div', class_='location')
        job_location = location.text.replace('\r', '').replace('\n', '')
        
        new_job = Job()
        new_job.title = job_title
        new_job.company = company_name
        new_job.location = job_location
        new_job.link = job_link
        job_list.append(new_job)
        
    for one_job in job_list:
        
        print(one_job.title, one_job.company, "\n", one_job.location, "\n", one_job.link, "\n")

    driver.quit()
    
    for one_job in job_list:
        
        link_list.append(one_job.link) 
 

get_detail_information(login_and_search('data scientist','Minneapolis, MN'))

get_detail_information(login_and_search('data scientist','Vermont'))

len(link_list)

good_job_list = []

key_words = ['python','SAS','sas','PhD', 'economics', 'machine', 'predictive', 'economist','data','SQL', 'phd','dashboard','dashboards','vizualizations', 'visualization']

def click_link(link):
    
    link_driver = webdriver.Chrome(executable_path=r'C:\Users\mcboe72\Anaconda\chromedriver.exe' )
    
    link_driver.get(link)
    
    link_soup = BeautifulSoup(link_driver.page_source, 'lxml')
        
    link_soup_text = str(BeautifulSoup(link_driver.page_source, 'lxml'))

    text = str(get_text(link_soup_text).lower())
    
    text_list = text.split()

    try:
        heading = link_soup.find('div', class_ = 'heading').text.replace('\r', '').replace('\n', '')
        heading_obj = link_soup.find('div', class_ = 'heading')
        location = heading_obj.find('h2').text
    except AttributeError:
        return None

          
    link_driver.quit()
  
    #print(heading)


    keyword_count = 0
    
    for word in text_list:
        if word in key_words:
            keyword_count = keyword_count +1
    
    if keyword_count>0:
        good_job = (keyword_count, heading, location, link)
        good_job_list.append(good_job)


for link in link_list:
    click_link(link)

GOOD_JOBS = DataFrame.from_records(good_job_list)
GOOD_JOBS.columns = ['Relevance', 'Job', 'Location', 'Link',]
GOOD_JOBS.head()



GOOD_JOBS.to_csv('GOOD_JOBS.csv')
