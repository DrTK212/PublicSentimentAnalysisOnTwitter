#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 09:56:02 2017

@author: RyutaroTakanami
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import csv
"""
from collection import Counter
"""

leftSource = '/Users/RyutaroTakanami/Desktop/gdata/word_source2/anger_source.csv'
rightSource = '/Users/RyutaroTakanami/Desktop/gdata/word_source2/fear_source.csv'

leftFile1 = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_04/anger_word.csv'
rightFile1 = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_04/fear_word.csv'
leftFile2 = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_05/anger_word.csv'
rightFile2 = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_05/fear_word.csv'
leftFile3 = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_06/anger_word.csv'
rightFile3 = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_06/fear_word.csv'
leftFile4 = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_07/anger_word.csv'
rightFile4 = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_07/fear_word.csv'
leftFile5 = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_08/anger_word.csv'
rightFile5 = '/Users/RyutaroTakanami/Desktop/gdata/feeling_word2_08/fear_word.csv'



left_source_list = []
right_source_list = []
left_result_list = []
right_result_list = []
left_count_list = []
right_count_list = []
word = ''

left_source = open(leftSource,'r')
right_source = open(rightSource,'r')
left_out1 = open(leftFile1,'w')
right_out1 = open(rightFile1,'w')
left_out2 = open(leftFile2,'w')
right_out2 = open(rightFile2,'w')
left_out3 = open(leftFile3,'w')
right_out3 = open(rightFile3,'w')
left_out4 = open(leftFile4,'w')
right_out4 = open(rightFile4,'w')
left_out5 = open(leftFile5,'w')
right_out5 = open(rightFile5,'w')

reader = csv.reader(left_source)
for row in reader:
    a = str(row[0])
    left_source_list.append(a.strip())
left_source.close()

reader = csv.reader(right_source)
for row in reader:
    a = str(row[0])
    right_source_list.append(a.strip())
right_source.close()

left_num = len(left_source_list)
right_num = len(right_source_list)

v1 = CountVectorizer()
left_trans = v1.fit_transform(left_source_list)
left_names = v1.get_feature_names()
left_array = left_trans.toarray()
left_names_len = len(left_names)

for word in range(left_names_len):
    counter = 0
    for n in range(left_num):
        if left_array[n,word] > 0:
            counter += 1
    left_count_list.append(counter)


v2 = CountVectorizer()
right_trans = v2.fit_transform(right_source_list)
right_names = v2.get_feature_names()
right_array = right_trans.toarray()
right_names_len = len(right_names)

for word in range(right_names_len):
    counter = 0
    for n in range(right_num):
        if right_array[n,word] > 0:
            counter += 1
    right_count_list.append(counter)



for word in range(left_names_len):
    PL = left_count_list[word] / left_num
    try:
        PR = right_count_list[right_names.index(left_names[word])] / right_num
    except:
        PR = 0
    numer = PL * np.log10(left_num)
    denom = numer + PR * np.log10(right_num)
    word_value = numer / denom
    
    if (word_value.astype(float) != 1 and word_value.astype(float) >= 0.4):
        left_out1.write(str(left_names[word]) + ' , ' + word_value.astype(str) + ' , ' + str(left_count_list[word]) + '\n')
    if (word_value.astype(float) != 1 and word_value.astype(float) >= 0.5):
        left_out2.write(str(left_names[word]) + ' , ' + word_value.astype(str) + ' , ' + str(left_count_list[word]) + '\n')
    if (word_value.astype(float) != 1 and word_value.astype(float) >= 0.6):
        left_out3.write(str(left_names[word]) + ' , ' + word_value.astype(str) + ' , ' + str(left_count_list[word]) + '\n')
    if (word_value.astype(float) != 1 and word_value.astype(float) >= 0.7):
        left_out4.write(str(left_names[word]) + ' , ' + word_value.astype(str) + ' , ' + str(left_count_list[word]) + '\n')
    if (word_value.astype(float) != 1 and word_value.astype(float) >= 0.8):
        left_out5.write(str(left_names[word]) + ' , ' + word_value.astype(str) + ' , ' + str(left_count_list[word]) + '\n')
        

for word in range(right_names_len):
    PR = right_count_list[word] / right_num
    try:
        PL = left_count_list[left_names.index(right_names[word])] / left_num
    except:
        PL = 0
    numer = PR * np.log10(right_num)
    denom = numer + PL * np.log10(left_num)
    word_value = numer / denom
    if(word_value.astype(float) != 1 and word_value.astype(float) >= 0.4):
        right_out1.write(str(right_names[word]) + ' , ' + word_value.astype(str) + ' , ' + str(right_count_list[word]) + '\n')
    if(word_value.astype(float) != 1 and word_value.astype(float) >= 0.5):
        right_out2.write(str(right_names[word]) + ' , ' + word_value.astype(str) + ' , ' + str(right_count_list[word]) + '\n')
    if(word_value.astype(float) != 1 and word_value.astype(float) >= 0.6):
        right_out3.write(str(right_names[word]) + ' , ' + word_value.astype(str) + ' , ' + str(right_count_list[word]) + '\n')
    if(word_value.astype(float) != 1 and word_value.astype(float) >= 0.7):
        right_out4.write(str(right_names[word]) + ' , ' + word_value.astype(str) + ' , ' + str(right_count_list[word]) + '\n')
    if(word_value.astype(float) != 1 and word_value.astype(float) >= 0.8):
        right_out5.write(str(right_names[word]) + ' , ' + word_value.astype(str) + ' , ' + str(right_count_list[word]) + '\n')
        
        
left_out1.close()
right_out1.close()
left_out2.close()
right_out2.close()
left_out3.close()
right_out3.close()
left_out4.close()
right_out4.close()
left_out5.close()
right_out5.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



























