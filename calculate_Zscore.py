#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:03:52 2017

@author: RyutaroTakanami
"""


import csv
import sys
import matplotlib.pyplot as plt
from statistics import mean,stdev
import datetime
#import pandas_datareader.data as web

start = datetime.datetime(2016,1,1)
end = datetime.datetime(2016,3,31)

"""
stock_value = web.DataReader("NIKKEI225","fred",start,end)
stock_value.plot()
"""

sys.path.append('/anaconda/lib/python3.5/site-packages')
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client['TweetDB']

for num in 4,5,6,7,8:
    
    
    joyFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(num)+'/all_joy.csv'
    sadFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(num)+'/all_sad.csv'
    excitingFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(num)+'/all_exciting.csv'
    surpriseFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(num)+'/all_surprise.csv'
    angerFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(num)+'/all_anger.csv'
    fearFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood2_0'+ str(num)+'/all_fear.csv'
    
    """
    Feb_joyFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Feb_joy.csv'
    Feb_sadFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Feb_sad.csv'
    Feb_excitingFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Feb_exciting.csv'
    Feb_surpriseFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Feb_surprise.csv'
    Feb_angerFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Feb_anger.csv'
    Feb_fearFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Feb_fear.csv'
    
    Mar_joyFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Mar_joy.csv'
    Mar_sadFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Mar_sad.csv'
    Mar_excitingFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Mar_exciting.csv'
    Mar_surpriseFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Mar_surprise.csv'
    Mar_angerFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Mar_anger.csv'
    Mar_fearFile = '/Users/RyutaroTakanami/Desktop/gdata/public_mood0'+ str(num)+'/Mar_fear.csv'
    """
    
    
    
    joy1 = open(joyFile,'r')
    sad1 = open(sadFile,'r')
    exciting1 = open(excitingFile,'r')
    surprise1 = open(surpriseFile,'r')
    anger1 = open(angerFile,'r')
    fear1 = open(fearFile,'r')
    
    """
    joy2 = open(Feb_joyFile,'r')
    sad2 = open(Feb_sadFile,'r')
    exciting2 = open(Feb_excitingFile,'r')
    surprise2 = open(Feb_surpriseFile,'r')
    anger2 = open(Feb_angerFile,'r')
    fear2 = open(Feb_fearFile,'r')
    
    joy3 = open(Mar_joyFile,'r')
    sad3 = open(Mar_sadFile,'r')
    exciting3 = open(Mar_excitingFile,'r')
    surprise3 = open(Mar_surpriseFile,'r')
    anger3 = open(Mar_angerFile,'r')
    fear3 = open(Mar_fearFile,'r')
    """
    
    joy_value_list = []
    sad_value_list = []
    exciting_value_list = []
    surprise_value_list = []
    anger_value_list = []
    fear_value_list = []
    
    
    
    
    reader = csv.reader(joy1)
    for row in reader:
        a = float(row[0])
        joy_value_list.append(a)
    joy1.close()
    
    
    reader = csv.reader(sad1)
    for row in reader:
        a = float(row[0])
        sad_value_list.append(a)
    sad1.close()
    
    reader = csv.reader(exciting1)
    for row in reader:
        a = float(row[0])
        exciting_value_list.append(a)
    exciting1.close()
    
    reader = csv.reader(surprise1)
    for row in reader:
        a = float(row[0])
        surprise_value_list.append(a)
    surprise1.close()
    
    reader = csv.reader(anger1)
    for row in reader:
        a = float(row[0])
        anger_value_list.append(a)
    anger1.close()
    
    reader = csv.reader(fear1)
    for row in reader:
        a = float(row[0])
        fear_value_list.append(a)
    fear1.close()
    
    
    """
    reader = csv.reader(joy2)
    for row in reader:
        a = float(row[0])
        joy_value_list.append(a)
    joy2.close()
    
    reader = csv.reader(sad2)
    for row in reader:
        a = float(row[0])
        sad_value_list.append(a)
    sad2.close()
    
    reader = csv.reader(exciting2)
    for row in reader:
        a = float(row[0])
        exciting_value_list.append(a)
    exciting2.close()
    
    reader = csv.reader(surprise2)
    for row in reader:
        a = float(row[0])
        surprise_value_list.append(a)
    surprise2.close()
    
    reader = csv.reader(anger2)
    for row in reader:
        a = float(row[0])
        anger_value_list.append(a)
    anger2.close()
    
    reader = csv.reader(fear2)
    for row in reader:
        a = float(row[0])
        fear_value_list.append(a)
    fear2.close()
    
    
    
    
    reader = csv.reader(joy3)
    for row in reader:
        a = float(row[0])
        joy_value_list.append(a)
    joy3.close()
    
    reader = csv.reader(sad3)
    for row in reader:
        a = float(row[0])
        sad_value_list.append(a)
    sad3.close()
    
    reader = csv.reader(exciting3)
    for row in reader:
        a = float(row[0])
        exciting_value_list.append(a)
    exciting3.close()
    
    reader = csv.reader(surprise3)
    for row in reader:
        a = float(row[0])
        surprise_value_list.append(a)
    surprise3.close()
    
    reader = csv.reader(anger3)
    for row in reader:
        a = float(row[0])
        anger_value_list.append(a)
    anger3.close()
    
    reader = csv.reader(fear3)
    for row in reader:
        a = float(row[0])
        fear_value_list.append(a)
    fear3.close()
    """
    
    
    
    joy_length = len(joy_value_list)
    sad_length = len(sad_value_list)
    exciting_length = len(exciting_value_list)
    surprise_length = len(surprise_value_list)
    anger_length = len(anger_value_list)
    fear_length = len(fear_value_list)
    
    
    
    
    
    
    """
    plt.plot(range(joy_length),joy_value_list,color = "yellow")
    plt.plot(range(joy_length),sad_value_list,color = "blue")
    plt.plot(range(joy_length),exciting_value_list,color = "orange")
    plt.plot(range(joy_length),surprise_value_list,color = "lime")
    plt.plot(range(joy_length),anger_value_list,color = "red")
    plt.plot(range(joy_length),fear_value_list,color = "green")
    """
    
    
    joy_mean = mean(joy_value_list)
    sad_mean = mean(sad_value_list)
    exciting_mean = mean(exciting_value_list)
    surprise_mean = mean(surprise_value_list)
    anger_mean = mean(anger_value_list)
    fear_mean = mean(fear_value_list)
    
    joy_std = stdev(joy_value_list)
    sad_std = stdev(sad_value_list)
    exciting_std = stdev(exciting_value_list)
    surprise_std = stdev(surprise_value_list)
    anger_std = stdev(anger_value_list)
    fear_std = stdev(fear_value_list)
    
    
    
    joyz_list = []
    sadz_list = []
    excitingz_list = []
    surprisez_list = []
    angerz_list = []
    fearz_list = []
    z_value = 0
    
    for value in joy_value_list:
        z_value = (value - joy_mean) / joy_std
        joyz_list.append(z_value)
    
    for value in sad_value_list:
        z_value = (value - sad_mean) / sad_std
        sadz_list.append(z_value)
        
    for value in exciting_value_list:
        z_value = (value - exciting_mean) / exciting_std
        excitingz_list.append(z_value)
    
    for value in surprise_value_list:
        z_value = (value - surprise_mean) / surprise_std
        surprisez_list.append(z_value)
    
    for value in anger_value_list:
        z_value = (value - anger_mean) / anger_std
        angerz_list.append(z_value)
        
    for value in fear_value_list:
        z_value = (value - fear_mean) / fear_std
        fearz_list.append(z_value)
    
 
    plt.plot(range(joy_length),joyz_list,color = "yellow")
    plt.plot(range(joy_length),sadz_list,color = "blue")
    
    """
    plt.plot(range(joy_length),excitingz_list,color = "orange")
    plt.plot(range(joy_length),surprisez_list,color = "lime")
    plt.plot(range(joy_length),angerz_list,color = "red")
    plt.plot(range(joy_length),fearz_list,color = "green")
    """
    
    
    plt.show()
  