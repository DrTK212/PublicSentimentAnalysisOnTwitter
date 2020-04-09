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

filename = '/Users/RyutaroTakanami/Desktop/tweets.csv'
client = MongoClient('localhost',27017)
db = client['TweetDB']
TWEET_NUM = 1000

#音夢
#'https://twitter.com/search?l=ja&q=%E7%94%B1%E5%A4%A2%20since%3A2017-09-01%20until%3A2017-09-02&src=typd'
#2016/1/1
#'https://twitter.com/search?l=ja&q=since%3A2016-01-01%20until%3A2016-01-02&src=typd'
#2016/1/3
#https://twitter.com/search?l=ja&q=since%3A2016-01-03%20until%3A2016-01-04&src=typd&lang=ja
path_to_chromedriver = '/usr/local/bin/chromedriver'            # change path as needed
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


    
#function to handle/parse HTML and extract data - using BeautifulSoup    
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
     
    #set to global in case you want to play around with the HTML later   
    global soup    
    
    #call dynamic page scroll function here
    soup = BeautifulSoup(twt_scroller(url), "html.parser")
    tweet_num = TWEET_NUM
    """
    phour = '15'
    """
    
    
    print('aaaaaaaaaaaaaaaaa')
    
        
    for i in soup.find_all('li', {"data-item-type":"tweet"}):
        try:
            tweet_num -= 1
            
            date = (i.small.a['title'] if i.small is not None else "")
            """
            nhour = date[0]+date[1]
            nhour = re.sub(':','',nhour)
            
            
            
            
            if nhour == str(phour):
            """
                
                    
                
            
                
                
            user = (i.div['data-name'] if i.div is not None else "")
            text = (i.p.get_text() if i.p is not None else "")


            
            
            """
            #build dictionary
            blog_dict = {
                    "number": 1000-tweet_num, 
                    "user": user,
                    "date": date,
                    "blog_text": problemchars.sub('', url_finder.sub('', text)),
                    }
        
          
            blog_list.append(blog_dict)
            """
            db.tweets1231.insert_one({
                    "number": 1000-tweet_num, 
                    "user": user,
                    "date": date,
                    "blog_text": problemchars.sub('', url_finder.sub('', text))
                    })
            
            
            
            if tweet_num <= 0:
                break
                
            """
                tweet_num -= 1
                print(tweet_num)
                if tweet_num <= 0:
                    phour = int(phour)-1
                    tweet_num = TWEET_NUM
                    print(phour)
            
 
                if phour < 0:
                        print('ccccccc')
                        phour = 23
                
                
            else:
                print('aaaaaa')
                continue
            """
    #error handling  
        except (AttributeError, TypeError, KeyError, ValueError):
            print("missing_value")
            tweet_num += 1
            continue
    
    
    """
    #call csv writer function and output file
    writer_csv_3(blog_list)
    """
    
    
    
    return 


"""
#pp.pprint(blog_list[0:2])
    
#function to write CSV file
def writer_csv_3(blog_list):
    
    #uses group name from URL to construct output file name
    file_out = filename.format(page = url.rsplit('/',2)[1])
    
    with open(file_out, 'w') as csvfile:

        writer = csv.writer(csvfile, lineterminator='\n', delimiter=',', quotechar='"')
    
        for i in blog_list:
            if len(i['blog_text']) > 0:
                newrow = i['number'],i['user'], i['date'], i['blog_text']

                writer.writerow(newrow)                     
            else:
                pass
                
"""
    
#tip the domino
if __name__ == "__main__":
    blogxtract(url)
    print("\007")

