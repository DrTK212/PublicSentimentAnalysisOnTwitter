#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:58:11 2017

@author: RyutaroTakanami
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import sys
import csv
import re




joyFile = '/Users/RyutaroTakanami/Desktop/gdata/dictionary/joy.csv'
likeFile = '/Users/RyutaroTakanami/Desktop/gdata/dictionary/like.csv'
acceptanceFile = '/Users/RyutaroTakanami/Desktop/gdata/dictionary/acceptance.csv'
sadFile = '/Users/RyutaroTakanami/Desktop/gdata/dictionary/sad.csv'


"""
excitingFile = '/Users/RyutaroTakanami/Desktop/gdata/dictionary/exciting.csv'
surpriseFile = '/Users/RyutaroTakanami/Desktop/gdata/dictionary/surprise.csv'
shameFile = '/Users/RyutaroTakanami/Desktop/gdata/dictionary/shame.csv'
"""


"""
angerFile = '/Users/RyutaroTakanami/Desktop/gdata/dictionary/anger.csv'
disgustFile = '/Users/RyutaroTakanami/Desktop/gdata/dictionary/disgust.csv'
fearFile = '/Users/RyutaroTakanami/Desktop/gdata/dictionary/fear.csv'
"""


s007File = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/007_wakati.csv'
ansatu_kyosituFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/ansatu_kyositu_wakati.csv'
ariceFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/arice_wakati.csv'
civil_warFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/civil_war_wakati.csv'
conanFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/conan_wakati.csv'
doraemonFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/doraemon_wakati.csv'
doryFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/dory_wakati.csv'
girls_and_panzerFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/girls_and_panzer_wakati.csv'
independentFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/independent_wakati.csv'
jungle_bookFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/jungle_book_wakati.csv'
nobunaga_concertFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/nobunaga_concert_wakati.csv'
odesseiFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/odessei_wakati.csv'
one_pieceFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/one_piece_wakati.csv'
orangeFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/orange_wakati.csv'
petFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/pet_wakati.csv'
sin_godzillaFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/sin_godzilla_wakati.csv'
star_warsFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/star_wars_wakati.csv'
yokai_watchFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/yokai_watch_wakati.csv'
your_nameFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/your_name_wakati.csv'
zootopiaFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/zootopia_wakati.csv'

koenokatatiFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/koenokatati_wakati.csv'
shokubutuFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/shokubutu_wakati.csv'
death_noteFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/death_note_wakati.csv'
pokemonFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/pokemon_wakati.csv'
kureyonFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/kureyon_wakati.csv'
high_movieFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/high_movie_wakati.csv'
hahatokurasebaFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/hahatokuraseba_wakati.csv'
s64_zenpenFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/64_zenpen_wakati.csv'
s64_kouhenFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/64_kouhen_wakati.csv'
chihayahuru_kaminokuFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/chihayahuru_kaminoku_wakati.csv'
I_am_heroFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/I_am_hero_wakati.csv'
saraba_keijiFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/saraba_keiji_wakati.csv'
ikariFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/ikari_wakati.csv'
konosekaiFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/konosekai_wakati.csv'
gosaigyoFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/gosaigyo_wakati.csv'
too_youngFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/too_young_wakati.csv'
museumFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/museum_wakati.csv'
rudoruhuFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/rudoruhu_wakati.csv'
sigatuFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/sigatu_wakati.csv'
bokudakeFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/bokudake_wakati.csv'
kazokuhaturaiyoFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/kazokuhaturaiyo_wakati.csv'
tono_risokuFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/tono_risoku_wakati.csv'
everestFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/everest_wakati.csv'
aozora_yellFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/aozora_yell_wakati.csv'
kurosakikunFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/kurosakikun_wakati.csv'
sekaikaranekoFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/sekaikaraneko_wakati.csv'
chihayahuru_shimonokuFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/chihayahuru_shimonoku_wakati.csv'
sugiharachiuneFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/sugiharachiune_wakati.csv'
okami_syojyoFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/okami_syojyo_wakati.csv'
high_redFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/high_red_wakati.csv'
sankinkotaiFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/sankinkotai_wakati.csv'
nanimonoFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/nanimono_wakati.csv'
sadakoFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/sadako_wakati.csv'
deadpoolFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/deadpool_wakati.csv'
batmanFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/batman_wakati.csv'
suicide_squadFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/suicide_squad_wakati.csv'
aroFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/aro_wakati.csv'
infernoFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/inferno_wakati.csv'
jason_bourneFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/jason_bourne_wakati.csv'
hudsonFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/hudson_wakati.csv'
ghost_bustersFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/ghost_busters_wakati.csv'
revenantFile = '/Users/RyutaroTakanami/Desktop/gdata/movie_wakati/revenant_wakati.csv'


left_source = '/Users/RyutaroTakanami/Desktop/gdata/word_source2/joy_source.csv'
right_source = '/Users/RyutaroTakanami/Desktop/gdata/word_source2/sad_source.csv'

wakati_list = []
left_list = []
right_list = []


s007 = open(s007File,'r')
ansatu_kyositu = open(ansatu_kyosituFile,'r')
arice = open(ariceFile,'r')
civil_war = open(civil_warFile,'r')
conan = open(conanFile,'r')
doraemon = open(doraemonFile,'r')
girls_and_panzer = open(girls_and_panzerFile,'r')
dory = open(doryFile,'r')
independent = open(independentFile,'r')
jungle_book = open(jungle_bookFile,'r')
nobunaga_concert = open(nobunaga_concertFile,'r')
odessei = open(odesseiFile,'r')
one_piece = open(one_pieceFile,'r')
orange = open(orangeFile,'r')
pet = open(petFile,'r')
sin_godzilla = open(sin_godzillaFile,'r')
star_wars = open(star_warsFile,'r')
yokai_watch = open(yokai_watchFile,'r')
your_name = open(your_nameFile,'r')
zootopia = open(zootopiaFile,'r')

##################################################################
koenokatati = open(koenokatatiFile,'r')
shokubutu = open(shokubutuFile,'r')
death_note = open(death_noteFile,'r')
pokemon = open(pokemonFile,'r')
kureyon = open(kureyonFile,'r')
high_movie = open(high_movieFile,'r')
hahatokuraseba = open(hahatokurasebaFile,'r')
s64_zenpen = open(s64_zenpenFile,'r')
s64_kouhen = open(s64_kouhenFile,'r')
chihayahuru_kaminoku = open(chihayahuru_kaminokuFile,'r')
I_am_hero = open(I_am_heroFile,'r')
saraba_keiji = open(saraba_keijiFile,'r')
ikari = open(ikariFile,'r')
konosekai = open(konosekaiFile,'r')
gosaigyo = open(gosaigyoFile,'r')
too_young = open(too_youngFile,'r')
museum = open(museumFile,'r')
rudoruhu = open(rudoruhuFile,'r')
sigatu = open(sigatuFile,'r')
bokudake = open(bokudakeFile,'r')
kazokuhaturaiyo = open(kazokuhaturaiyoFile,'r')
tono_risoku = open(tono_risokuFile,'r')
everest = open(everestFile,'r')
aozora_yell = open(aozora_yellFile,'r')
kurosakikun = open(kurosakikunFile,'r')
sekaikaraneko = open(sekaikaranekoFile,'r')
chihayahuru_shimonoku = open(chihayahuru_shimonokuFile,'r')
sugiharachiune = open(sugiharachiuneFile,'r')
okami_syojyo = open(okami_syojyoFile,'r')
high_red = open(high_redFile,'r')
sankinkotai = open(sankinkotaiFile,'r')
nanimono = open(nanimonoFile,'r')
sadako = open(sadakoFile,'r')
deadpool = open(deadpoolFile,'r')
batman = open(batmanFile,'r')
suicide_squad = open(suicide_squadFile,'r')
aro = open(aroFile,'r')
inferno = open(infernoFile,'r')
jason_bourne = open(jason_bourneFile,'r')
hudson = open(hudsonFile,'r')
ghost_busters = open(ghost_bustersFile,'r')
revenant = open(revenantFile,'r')


joy = open(joyFile,'r')
like = open(likeFile,'r')
acceptance = open(acceptanceFile,'r')

sad = open(sadFile,'r')


"""
exciting = open(excitingFile,'r')
surprise = open(surpriseFile,'r')
shame = open(shameFile,'r')
"""

"""
anger = open(angerFile,'r')
disgust = open(disgustFile,'r')
fear = open(fearFile,'r')
"""

leftout = open(left_source,'w')
rightout = open(right_source,'w')

reader = csv.reader(s007)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
s007.close()


reader = csv.reader(ansatu_kyositu)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
ansatu_kyositu.close()

reader = csv.reader(arice)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
arice.close()

reader = csv.reader(civil_war)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
civil_war.close()

reader = csv.reader(conan)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
conan.close()


reader = csv.reader(doraemon)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
doraemon.close()


reader = csv.reader(dory)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
dory.close()

reader = csv.reader(girls_and_panzer)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
girls_and_panzer.close()

reader = csv.reader(independent)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
    
independent.close()

reader = csv.reader(jungle_book)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
jungle_book.close()


reader = csv.reader(nobunaga_concert)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
nobunaga_concert.close()


reader = csv.reader(odessei)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
odessei.close()

reader = csv.reader(one_piece)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
one_piece.close()

reader = csv.reader(orange)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
orange.close()

reader = csv.reader(pet)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
pet.close()


reader = csv.reader(sin_godzilla)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
sin_godzilla.close()


reader = csv.reader(star_wars)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
star_wars.close()

reader = csv.reader(yokai_watch)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
yokai_watch.close()

reader = csv.reader(your_name)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
your_name.close()

reader = csv.reader(zootopia)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
zootopia.close()

######################################################################################


reader = csv.reader(koenokatati)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
koenokatati.close()

reader = csv.reader(shokubutu)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
shokubutu.close()

reader = csv.reader(death_note)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
death_note.close()

reader = csv.reader(pokemon)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
pokemon.close()

reader = csv.reader(kureyon)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
kureyon.close()

reader = csv.reader(high_movie)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
high_movie.close()

reader = csv.reader(hahatokuraseba)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
hahatokuraseba.close()


reader = csv.reader(s64_zenpen)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
s64_zenpen.close()

reader = csv.reader(s64_kouhen)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
s64_kouhen.close()

reader = csv.reader(chihayahuru_kaminoku)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
chihayahuru_kaminoku.close()

reader = csv.reader(I_am_hero)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
I_am_hero.close()

reader = csv.reader(saraba_keiji)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
saraba_keiji.close()

reader = csv.reader(ikari)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
ikari.close()

reader = csv.reader(konosekai)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
konosekai.close()

reader = csv.reader(gosaigyo)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
gosaigyo.close()

reader = csv.reader(too_young)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
too_young.close()

reader = csv.reader(museum)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
museum.close()

reader = csv.reader(rudoruhu)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
rudoruhu.close()

reader = csv.reader(sigatu)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
sigatu.close()

reader = csv.reader(bokudake)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
bokudake.close()

reader = csv.reader(kazokuhaturaiyo)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
kazokuhaturaiyo.close()

reader = csv.reader(tono_risoku)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
tono_risoku.close()

reader = csv.reader(everest)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
everest.close()

reader = csv.reader(aozora_yell)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
aozora_yell.close()

reader = csv.reader(kurosakikun)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
kurosakikun.close()

reader = csv.reader(sekaikaraneko)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
sekaikaraneko.close()

reader = csv.reader(chihayahuru_shimonoku)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
chihayahuru_shimonoku.close()

reader = csv.reader(sugiharachiune)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
sugiharachiune.close()

reader = csv.reader(okami_syojyo)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
okami_syojyo.close()

reader = csv.reader(high_red)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
high_red.close()

reader = csv.reader(sankinkotai)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
sankinkotai.close()

reader = csv.reader(nanimono)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
nanimono.close()

reader = csv.reader(sadako)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
sadako.close()

reader = csv.reader(deadpool)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
deadpool.close()

reader = csv.reader(batman)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
batman.close()

reader = csv.reader(suicide_squad)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
suicide_squad.close()

reader = csv.reader(aro)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
aro.close()

reader = csv.reader(inferno)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
inferno.close()

reader = csv.reader(jason_bourne)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
jason_bourne.close()

reader = csv.reader(hudson)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
hudson.close()

reader = csv.reader(ghost_busters)
for row in reader:
    a = str(row[0])
    a = re.sub(r"[0-9]","",a)
    a = re.sub(r"[０-９]","",a)
    wakati_list.append(a.strip())
ghost_busters.close()

reader = csv.reader(revenant)
for row in reader:
    try:
        a = str(row[0])
        a = re.sub(r"[0-9]","",a)
        a = re.sub(r"[０-９]","",a)
        wakati_list.append(a.strip())
    except:
        print('error')
        continue
revenant.close()



reader = csv.reader(joy)
for row in reader:
    a = str(row[0])
    left_list.append(a.strip())
joy.close()

reader = csv.reader(like)
for row in reader:
    a = str(row[0])
    left_list.append(a.strip())
like.close()

reader = csv.reader(acceptance)
for row in reader:
    a = str(row[0])
    left_list.append(a.strip())
acceptance.close()

reader = csv.reader(sad)
for row in reader:
    a = str(row[0])
    right_list.append(a.strip())
sad.close()




"""
reader = csv.reader(exciting)
for row in reader:
    a = str(row[0])
    left_list.append(a.strip())
exciting.close()

reader = csv.reader(surprise)
for row in reader:
    a = str(row[0])
    right_list.append(a.strip())
surprise.close()

reader = csv.reader(shame)
for row in reader:
    a = str(row[0])
    right_list.append(a.strip())
shame.close()
"""

"""
reader = csv.reader(anger)
for row in reader:
    a = str(row[0])
    left_list.append(a.strip())
anger.close()

reader = csv.reader(disgust)
for row in reader:
    a = str(row[0])
    left_list.append(a.strip())
disgust.close()

reader = csv.reader(fear)
for row in reader:
    a = str(row[0])
    right_list.append(a.strip())
fear.close()
"""

left_length = len(left_list)
right_length = len(right_list)


count = 0
for text in wakati_list:
    
    left_point = 0
    right_point = 0
    
    for left in range(left_length):
        left_point += text.count(left_list[left])
        if text.count(left_list[left]) > 0:
            print(left_list[left])
            
    for right in range(right_length):
        right_point += text.count(right_list[right])
        if text.count(right_list[right]) > 0:
            print(right_list[right])
    
    print(left_point)
    print(right_point)
    
    if left_point > right_point:
        leftout.write(str(text) + '\n')
    
    if left_point < right_point:
        rightout.write(str(text) + '\n')
    
    count += 1
    
    
leftout.close()
rightout.close()













