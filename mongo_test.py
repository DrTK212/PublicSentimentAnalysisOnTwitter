#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 17:05:01 2017

@author: RyutaroTakanami
"""


import sys
sys.path.append('/anaconda/lib/python3.5/site-packages')
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client['TweetDB']


for data in db.tweets1231.find():
    print(data)
print(db.tweets1231.count())

