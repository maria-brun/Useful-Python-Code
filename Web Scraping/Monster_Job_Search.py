# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 08:47:09 2018

@author: mcboe72
"""






# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 09:01:27 2018

@author: mcboe72
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

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
    place.send_keys(Keys.DELETE);
    place.send_keys(location)    
    time.sleep(1)
        
    search_buttom = driver.find_element_by_xpath('//*[@id="doQuickSearch2"]')
    search_buttom.click()
    time.sleep(1)
    
    return driver

def get_detail_information(driver):
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    results = soup.find('div', {'id':'SearchResults'})    #job_list = []
    
    for result in results.find_all('section', class_='card-content'):
        
        title = result.find('h2', class_ = 'title')
        job_title = title.text
        link_find = result.find('div', class_='summary')
        link = link_find.find('a')
        job_link = link.attrs['href'].strip()
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

link_list[2]

jobs_and_quals_list = []

def click_link(link):
    
    quals_list = []
    
    link_driver = webdriver.Chrome(executable_path=r'C:\Users\mcboe72\Anaconda\chromedriver.exe' )
    
    link_driver.get(link)
        
    link_soup = BeautifulSoup(link_driver.page_source, 'lxml')
    
    job = link_soup.find('div', {'JobBody'}).text
    
    description = link_soup.find('div', {'id':'JobDesription'})
    
    for qual in description.find_all('li'):
        qualification = qual.text
        quals_list.append(qualification)

    job_quals = quals_list.append(job)
    
    jobs_and_quals_list.append(job_quals)
    

for item in link_list:
    click_link(item)