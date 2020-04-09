#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 21:31:14 2017

@author: RyutaroTakanami
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import sys
import csv
import re

sys.path.append(“/root/pyknp-0.3”)
from pyknp import Jumanpp
jumanpp = Jumanpp()


joyFile = ‘/root/Documents/dictionary/joy.csv’
sadFile = ‘root/Documents/dictionary/sad.csv’
movieFile = ‘/root/Documents/movie_source/dory.csv’
outFile = ‘/root/Documents/movie_wakati/dory.csv’




problemchars
crp
wrd
dgt
url_finder



text_list = []
add_list = []


f = open(movieFile,'r')
outF = open(outFile,'w')

reader = csv.reader(f)

"""
for row in reader:
    a = str(row[1])
    problemchars.sub('',a)
    crp.sub('',a)
    wrd.sub('',a)
    dgt.sub('',a)
    url_finder.sub('',a)
    
    add_list = [a,0]
    text_list.append(add_list)
    
f.close
"""

load_miss_count = 0
analyze_miss_count = 0

for row in reader:
    try:
        a = str(row[1])
        text_list.append(a)
    except:
        print('read_fail')
        load_miss_count += 1
f.close()

num = 0

for line in text_list:
    text = ''
    num += 1
    
    try:
        result = jumanpp.analysis(line)
        print(num)
        for mrph in result.mrph_list():
            hinsi = mrph.hinsi
            if(hinsi == "" or hinsi == "" or hinsi == "" or hinsi == ""):
                text += str(mrhp.midasi) + ' '
        outF.write(str(text) + '\n')
        
    except (AttributeError, TypeError, KeyError, ValueError):
            print("missing_value")
            analyze_miss_count += 1
            continue    

outF.close()
print(load_miss_count)
print(analyze_miss_count)




