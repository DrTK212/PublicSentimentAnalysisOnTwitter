# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:06:03 2017

@author: RyutaroTakanami
"""
import csv
import sys
sys.path.append('/anaconda/lib/python3.5/site-packages')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re
import time
import pprint as pp
from collections import OrderedDict


file_out = '/Users/RyutaroTakanami/Desktop/movie.csv'
path_to_chromedriver = '/usr/local/bin/chromedriver'            # change path as needed
url = 'https://movies.yahoo.co.jp/movie/%E3%83%AC%E3%83%B4%E3%82%A7%E3%83%8A%E3%83%B3%E3%83%88%EF%BC%9A%E8%98%87%E3%81%88%E3%82%8A%E3%81%97%E8%80%85/354289/review/%E7%94%9F%E3%81%8D%E3%81%A6%E3%81%84%E3%81%8F%E3%81%AB%E3%81%AF%E7%BE%8E%E3%81%97%E3%81%84%E3%81%93%E3%81%A8%E3%81%A0%E3%81%91%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84/700/?c=601&sort=lrf'

browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.get(url);

count = 228
blog_list = []
miss_count = 0


for n in range(count):

    
    try:

        soup = BeautifulSoup(browser.page_source, "html.parser")
        
        text = soup.find("p",{"class":"text-small text-break text-readable p1em"})
        content = text.get_text()
        
        
        blog_dict = {
                "number": n+1, 
                "text": content.strip(),
                }
        
        blog_list.append(blog_dict)
        
        
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        tags = browser.find_elements_by_class_name('listview__element--right-icon')
        if len(tags)>1:
            tags[1].click()
        else:
            tags[0].click()
        
        time.sleep(1)
        
        
        
       
        
        
    except(AttributeError, TypeError, KeyError, ValueError):
        print("missing_value")
        miss_count += 1
        
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        tags = browser.find_elements_by_class_name('listview__element--right-icon')
        if len(tags)>1:
            tags[1].click()
        else:
            tags[0].click()
    
    
with open(file_out, 'w') as csvfile:

        writer = csv.writer(csvfile, lineterminator='\n', delimiter=',')
    
        for i in blog_list:
            if len(i['text']) > 0:
                newrow = i['number'],i['text']

                writer.writerow(newrow)                     
            else:
                pass
print(miss_count)
print("\007")

