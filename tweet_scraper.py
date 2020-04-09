#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:55:06 2017

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
from pymongo import MongoClient
import pprint as pp
from collections import OrderedDict

filename = '/Users/パス/tweets.csv'
client = MongoClient('localhost',27017)
db = client['TweetDB']
TWEET_NUM = 1000


path_to_chromedriver = '/usr/local/bin/chromedriver'          
url = 'https://twitter.com/search?l=ja&q=since%3A2016-12-31%20until%3A2017-01-01&src=typd'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

browser.get(url);



#function to handle dynamic page content loading - using Selenium
def twt_scroller(url):

    browser.get(url)
    
    #define initial page height for 'while' loop
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    
    for a in range(100):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #define how many seconds to wait while dynamic page content loads
        time.sleep(2)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        
        if newHeight == lastHeight:
            break
        else:
            lastHeight = newHeight
            
    html = browser.page_source

    return html


    
  
def blogxtract(url):
    
    #regex patterns
    problemchars = re.compile(r'[\[=\+/&<>;:!\\|*^\'"\?%$@)(_\,\.\t\r\n0-9-—\]]')
    #prochar = '[(=\-\+\:/&<>;|\'"\?%#$@\,\._)]'
    crp = re.compile(r'MoreCopy link to TweetEmbed Tweet|Reply')
    wrd = re.compile(r'[A-Z]+[a-z]*')
    dgt = re.compile(r'\d+')
    url_finder = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    retweet = re.compile(r"(?<=Retweet:)(.*)(?=', u'R)")
    fave = re.compile(r"(?<=Like:)(.*)(?=', u'Liked)")

    blog_list = []
     
  
    global soup    
    

    soup = BeautifulSoup(twt_scroller(url), "html.parser")
    tweet_num = TWEET_NUM

    
        
    for i in soup.find_all('li', {"data-item-type":"tweet"}):
        try:
            tweet_num -= 1
            
            date = (i.small.a['title'] if i.small is not None else "")
                 
 
                
            user = (i.div['data-name'] if i.div is not None else "")
            text = (i.p.get_text() if i.p is not None else "")


            
            

            db.tweets1231.insert_one({
                    "number": 1000-tweet_num, #一日につき1000件のツイートを取得
                    "user": user,
                    "date": date,
                    "blog_text": problemchars.sub('', url_finder.sub('', text))
                    })
            
            
            
            if tweet_num <= 0:
                break
                

    #error handling  
        except (AttributeError, TypeError, KeyError, ValueError):
            print("missing_value")
            tweet_num += 1
            continue
    
    

    
    
    
    return 


if __name__ == "__main__":
    blogxtract(url)


