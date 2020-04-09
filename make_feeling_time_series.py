#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:03:52 2017

@author: RyutaroTakanami
"""


import csv
import sys
sys.path.append('/anaconda/lib/python3.5/site-packages')
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client['TweetDB']



"""
joyFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_0'+ str(a)+'/joy_word.csv'
sadFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_0'+ str(a)+'/sad_word.csv'
excitingFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_0'+ str(a)+'/exciting_word.csv'
surpriseFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_0'+ str(a)+'/surprise_word.csv'
angerFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_0'+ str(a)+'/anger_word.csv'
fearFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_0'+ str(a)+'/fear_word.csv'
"""

joyFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_04/joy_word.csv'
sadFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_04/sad_word.csv'
excitingFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_04/exciting_word.csv'
surpriseFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_04/surprise_word.csv'
angerFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_04/anger_word.csv'
fearFile = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_04/fear_word.csv'

janFile = '/Users/RyutaroTakanami/Desktop/gdata/January.csv'
febFile = '/Users/RyutaroTakanami/Desktop/gdata/February.csv'
marFile = '/Users/RyutaroTakanami/Desktop/gdata/March.csv'
aprFile = '/Users/RyutaroTakanami/Desktop/gdata/April.csv'
mayFile = '/Users/RyutaroTakanami/Desktop/gdata/May.csv'
junFile = '/Users/RyutaroTakanami/Desktop/gdata/June.csv'
julFile = '/Users/RyutaroTakanami/Desktop/gdata/July.csv'
augFile = '/Users/RyutaroTakanami/Desktop/gdata/August.csv'
sepFile = '/Users/RyutaroTakanami/Desktop/gdata/September.csv'
octFile = '/Users/RyutaroTakanami/Desktop/gdata/October.csv'
novFile = '/Users/RyutaroTakanami/Desktop/gdata/November.csv'
decFile = '/Users/RyutaroTakanami/Desktop/gdata/December.csv'


out_joyFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_04/all_joy.csv'
out_sadFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_04/all_sad.csv'
out_excitingFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_04/all_exciting.csv'
out_surpriseFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_04/all_surprise.csv'
out_angerFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_04/all_anger.csv'
out_fearFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_04/all_fear.csv'

"""
out_joyFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(a)+'/all_joy.csv'
out_sadFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(a)+'/all_sad.csv'
out_excitingFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(a)+'/all_exciting.csv'
out_surpriseFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(a)+'/all_surprise.csv'
out_angerFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(a)+'/all_anger.csv'
out_fearFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(a)+'/all_fear.csv'
"""

joy = open(joyFile,'r')
sad = open(sadFile,'r')
exciting = open(excitingFile,'r')
surprise = open(surpriseFile,'r')
anger = open(angerFile,'r')
fear = open(fearFile,'r')

jan = open(janFile,'r')
feb = open(febFile,'r')
mar = open(marFile,'r')
apr = open(aprFile,'r')
may = open(mayFile,'r')
jun = open(junFile,'r')
jul = open(julFile,'r')
aug = open(augFile,'r')
sep = open(sepFile,'r')
octo = open(octFile,'r')
nov = open(novFile,'r')
dec = open(decFile,'r')

out_joy = open(out_joyFile,'w')
out_sad = open(out_sadFile,'w')
out_exciting = open(out_excitingFile,'w')
out_surprise = open(out_surpriseFile,'w')
out_anger = open(out_angerFile,'w')
out_fear = open(out_fearFile,'w')


joy_word_list = []
sad_word_list = []
exciting_word_list = []
surprise_word_list = []
anger_word_list = []
fear_word_list = []

joy_value_list = []
sad_value_list = []
exciting_value_list = []
surprise_value_list = []
anger_value_list = []
fear_value_list = []

date_list = []

reader = csv.reader(joy)
for row in reader:
    a = str(row[0])
    b = str(row[1])
    joy_word_list.append(a.strip())
    joy_value_list.append(b.strip())
joy.close()


reader = csv.reader(sad)
for row in reader:
    a = str(row[0])
    b = str(row[1])
    sad_word_list.append(a.strip())
    sad_value_list.append(b.strip())
sad.close()

reader = csv.reader(exciting)
for row in reader:
    a = str(row[0])
    b = str(row[1])
    exciting_word_list.append(a.strip())
    exciting_value_list.append(b.strip())
exciting.close()

reader = csv.reader(surprise)
for row in reader:
    a = str(row[0])
    b = str(row[1])
    surprise_word_list.append(a.strip())
    surprise_value_list.append(b.strip())
surprise.close()

reader = csv.reader(anger)
for row in reader:
    a = str(row[0])
    b = str(row[1])
    anger_word_list.append(a.strip())
    anger_value_list.append(b.strip())
anger.close()

reader = csv.reader(fear)
for row in reader:
    a = str(row[0])
    b = str(row[1])
    fear_word_list.append(a.strip())
    fear_value_list.append(b.strip())
fear.close()





reader = csv.reader(jan)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
jan.close()

reader = csv.reader(feb)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
feb.close()

reader = csv.reader(mar)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
mar.close()

reader = csv.reader(apr)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
apr.close()

reader = csv.reader(may)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
may.close()

reader = csv.reader(jun)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
jun.close()

reader = csv.reader(jul)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
jul.close()

reader = csv.reader(aug)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
aug.close()

reader = csv.reader(sep)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
sep.close()

reader = csv.reader(octo)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
octo.close()

reader = csv.reader(nov)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
nov.close()

reader = csv.reader(dec)
for row in reader:
    a = str(row[0])
    date_list.append(a.strip())
dec.close()

  





joy_length = len(joy_word_list)
sad_length = len(sad_word_list)
exciting_length = len(exciting_word_list)
surprise_length = len(surprise_word_list)
anger_length = len(anger_word_list)
fear_length = len(fear_word_list)



joy_point_list = []
sad_point_list = []
exciting_point_list = []
surprise_point_list = []
anger_point_list = []
fear_point_list = []


day_count = 0
joy_point = 0
sad_point = 0
exciting_point = 0
surprise_point = 0
anger_point = 0
fear_point = 0


joy_point = 0
sad_point = 0
exciting_point = 0
surprise_point = 0
anger_point = 0
fear_point = 0



for text in date_list:
    
    
    day_count += 1
    
    
        
    for feel in range(joy_length):
        if text.count(joy_word_list[feel]) != 0:
            joy_point += text.count(joy_word_list[feel]) * float(joy_value_list[feel] )
                    
    for feel in range(sad_length):
        if text.count(sad_word_list[feel]) != 0:
            sad_point += text.count(sad_word_list[feel]) * float(sad_value_list[feel] )
        
    for feel in range(exciting_length):
        if text.count(exciting_word_list[feel]) != 0:
            exciting_point += text.count(exciting_word_list[feel]) * float(exciting_value_list[feel] )
        
    for feel in range(surprise_length):
        if text.count(surprise_word_list[feel]) != 0:
            surprise_point += text.count(surprise_word_list[feel]) * float(surprise_value_list[feel] )
        
    for feel in range(anger_length):
        if text.count(anger_word_list[feel]) != 0:
            anger_point += text.count(anger_word_list[feel]) * float(anger_value_list[feel] )
        
    for feel in range(fear_length):
        if text.count(fear_word_list[feel]) != 0:
            fear_point += text.count(fear_word_list[feel]) * float(fear_value_list[feel] )
    

    if day_count == 1000:
        day_count = 0
        
        print(joy_point)
        print(sad_point)
        print(exciting_point)
        print(surprise_point)
        print(anger_point)
        print(fear_point)
    
        joy_point_list.append(joy_point)
        sad_point_list.append(sad_point)
        exciting_point_list.append(exciting_point)
        surprise_point_list.append(surprise_point)
        anger_point_list.append(anger_point)
        fear_point_list.append(fear_point)
        
        joy_point = 0
        sad_point = 0
        exciting_point = 0
        surprise_point = 0
        anger_point = 0
        fear_point = 0
        
print(joy_point)
print(sad_point)
print(exciting_point)
print(surprise_point)
print(anger_point)
print(fear_point)

if(joy_point > 0):
    joy_point_list.append(joy_point)
    sad_point_list.append(sad_point)
    exciting_point_list.append(exciting_point)
    surprise_point_list.append(surprise_point)
    anger_point_list.append(anger_point)
    fear_point_list.append(fear_point)
    
    joy_point = 0
    sad_point = 0
    exciting_point = 0
    surprise_point = 0
    anger_point = 0
    fear_point = 0
    
for value in joy_point_list:
    out_joy.write(str(value) + '\n')
for value in sad_point_list:
    out_sad.write(str(value) + '\n')
for value in exciting_point_list:
    out_exciting.write(str(value) + '\n')
for value in surprise_point_list:
    out_surprise.write(str(value) + '\n')
for value in anger_point_list:
    out_anger.write(str(value) + '\n')
for value in fear_point_list:
    out_fear.write(str(value) + '\n')


out_joy.close()
out_sad.close()
out_exciting.close()
out_surprise.close()
out_anger.close()
out_fear.close()

