# -*- coding: utf-8 -*-

import requests, json, os, time
from bs4 import BeautifulSoup
from pathlib import Path
from settings import *
from scrap import *

''' DDOS '''

with open('%ssports_bck.json'%JSON_DIR, 'r', encoding='utf-8') as f:
    sports = json.loads(f.read())

c = 0
for gender in sports.keys():
    for sport in sports[gender].keys():
        for year in range(1891, 2021):            
            c+=1

cc = 0
for gender in sports.keys():
    _dir = '%s%s'%(HTML_DIR, gender)
    if not os.path.isdir(_dir):
        os.mkdir(_dir)
    for sport in sports[gender].keys():
        _dir = '%s%s/%s'%(HTML_DIR, gender, sport.replace('/', '_'))
        if not os.path.isdir(_dir):
            os.mkdir(_dir)
        year = 1891
        while year <= 2020:
            _dir = '%s%s/%s/%s.html'%(HTML_DIR, gender, sport.replace('/', '_'), year)
            if os.path.isfile(_dir):
                print('(%s/%s) - %s - already exist' % (cc, c, _dir))
            else:
                time.sleep(SLEEP)
                try :
                    print('(%s/%s) - %s - try' % (cc, c, _dir))
                    get_html(
                        'http://trackfield.brinkster.net/More.asp?Year=%s&EventCode=%s&Gender=%s&P=T' %
                        (
                            year,
                            get_sport_id(sports[gender][sport]),
                            get_gender_char(gender)
                        ),
                        _dir)
                except Exception as e: 
                    print('(%s/%s) - %s - %s' % (cc, c, _dir, e))
                    year -= 1
                    cc -= 1
            year += 1
            cc += 1

''' Get all sports for men and women '''

# get_html('http://trackfield.brinkster.net/Main.asp?P=F', 'home')

# with open('%shome.html'%HTML_DIR, 'r', encoding='utf-8') as f:
#     soup = BeautifulSoup(f.read(), 'html.parser')

# sports = {'men' : {}, 'women' : {}}

# # Men
# for a in soup.find_all('table')[3].find_all('a'):
#     sports['men'][a.text.strip()]=a['href']

# # Women
# for a in soup.find_all('table')[4].find_all('a'):
#     sports['women'][a.text.strip()]=a['href']

# with open('%ssports.json'%JSON_DIR, 'w', encoding='utf-8') as f:
#     f.write(json.dumps(sports))

# # print('\n'.join(a['href'] for a in soup.find_all('table')[3].find_all('a')))
