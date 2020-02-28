# -*- coding: utf-8 -*-

import requests, json, os, time
from bs4 import BeautifulSoup
import csv
from pathlib import Path
import pandas as pd
import numpy as np

HTML_DIR = 'html/'
JSON_DIR = 'json/'
CSV_DIR = 'csv/'
SLEEP = 0
COLS = ['rank', 'name', 'nat', 'perf_0', 'perf_1', 'perf_2', 'city', 'date']

def get_html(url, name, parser='html.parser'):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, parser)
    with open(name, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

def read_html(path, parser='html.parser'):
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), parser)
    return soup

def get_date_file_path(gender, sport):
    return '%s/date/%s'%(gender, sport.replace('/', '_'))

def get_sport_id(url):
    return url.split('=')[1].split('&')[0]

def get_dates_from_interval(interval):
    return interval.split('-')

def get_gender_char(gender):
    return 'M' if gender == 'men' else 'W'


df = pd.read_csv('csv/sports/women/10000 m/1988.csv')
print(df.head())
print(df.tail())

# for dp, dns, fns in os.walk('%s/sports'%HTML_DIR):
#     for fn in fns:
#         print('%s/%s'%(dp, fn))
#         table = []
#         empty = []
#         i = 0
#         path = Path('%s/%s'%(dp, fn))
#         soup = read_html(path)
#         for tr in soup.find_all('table')[0].find_all('tr'):
#             tds = tr.find_all('td')
#             if len(tds) == 8:
#                 table.append([])
#                 for td in tds:
#                     table[i].append(td.text.strip())
#                 i += 1
#             else:
#                 empty.append(path)
#         path = path.with_suffix('.csv')
#         npath = CSV_DIR
#         for part in path.parts[1:-1]:
#             npath += part + '/'
#             if not os.path.isdir(npath):
#                 os.mkdir(npath)
#         try:
#             df = pd.DataFrame(table, columns=COLS)
#             df.to_csv('%s%s'%(npath, path.name), index=False)
#         except:
#             pass


''' List problems '''

# c = 0
# res = []
# probs = []
# # dirpath, dirnames, filenames
# for dp, dns, fns in os.walk('%s/sports'%HTML_DIR):
#     is_prob = True
#     for fn in fns:
#         c += 1
#         td_count = []
#         soup = read_html('%s/%s'%(dp, fn))
#         trs = soup.find_all('table')[0].find_all('tr')
#         for tr in trs:
#             td_count.append(len(tr.find_all('td')))
#         res.append('%s/%s - %s - %s'% (dp, fn, len(trs), td_count))
#         if len(td_count) != 2:
#             is_prob = False
#         print('%s/%s'%(c, 6890))
#     if is_prob:
#         probs.append(dp.split('\\')[-1])

# with open('%ssports.json'%JSON_DIR, 'r', encoding='utf-8') as f:
#     sports = json.loads(f.read())

# _probs = {}
# for prob in probs:
#     if prob in sports['men'].keys():
#         _probs.update({prob : sports['men'][prob]})
#     elif prob in sports['women'].keys():
#         _probs.update({prob : sports['women'][prob]})
#     else:
#         print(prob)

# with open('%sprobs.json'%JSON_DIR, 'w', encoding='utf-8') as f:
#     f.write(json.dumps(_probs))

''' Scrap on first file '''

# soup = read_html('html/men/100 m/1891.html')
# trs = soup.find_all('table')[0].find_all('tr')[2:]

# res = []
# i = 1
# for tr in soup.find_all('table')[0].find_all('tr')[2:]:
#     res.append([])
#     print('*' * 10)
#     for td in trs[0].find_all('td'):
#         res[i].append(td.text.strip())
#         print(td.text.strip())
#     i += 1

# print(res)
# print(len(res[0]))



''' DDOS '''

# with open('%ssports.json'%JSON_DIR, 'r', encoding='utf-8') as f:
#     sports = json.loads(f.read())

# c = 0
# for gender in sports.keys():
#     for sport in sports[gender].keys():
#         for year in range(1891, 2021):            
#             c+=1

# cc = 0
# for gender in sports.keys():
#     _dir = '%s%s'%(HTML_DIR, gender)
#     if not os.path.isdir(_dir):
#         os.mkdir(_dir)
#     for sport in sports[gender].keys():
#         _dir = '%s%s/%s'%(HTML_DIR, gender, sport.replace('/', '_'))
#         if not os.path.isdir(_dir):
#             os.mkdir(_dir)
#         year = 1891
#         while year <= 2020:
#             _dir = '%s%s/%s/%s.html'%(HTML_DIR, gender, sport.replace('/', '_'), year)
#             if os.path.isfile(_dir):
#                 print('(%s/%s) - %s - already exist' % (cc, c, _dir))
#             else:
#                 time.sleep(SLEEP)
#                 try :
#                     print('(%s/%s) - %s - try' % (cc, c, _dir))
#                     get_html(
#                         'http://trackfield.brinkster.net/More.asp?Year=%s&EventCode=%s&Gender=%s&P=T' %
#                         (
#                             year,
#                             get_sport_id(sports[gender][sport]),
#                             get_gender_char(gender)
#                         ),
#                         _dir)
#                 except Exception as e: 
#                     print('(%s/%s) - %s - %s' % (cc, c, _dir, e))
#                     year -= 1
#                     cc -= 1
#             year += 1
#             cc += 1









''' Scrap date '''

# with open('%ssports_1.json'%JSON_DIR, 'r', encoding='utf-8') as f:
#     sports = json.loads(f.read())

# for gender in sports.keys():
#     for sport in sports[gender].keys():
#         soup = read_html('%s%s.html'%(HTML_DIR, get_date_file_path(gender, sport)))
#         sports[gender][sport] = {'url':sports[gender][sport], 'date':soup.find('script').text.split('\'')[1].split(';')}

# with open('%ssports_1.json'%JSON_DIR, 'w', encoding='utf-8') as f:
#     f.write(json.dumps(sports))


''' DDOS SERVER '''

# with open('%ssports.json'%JSON_DIR, 'r', encoding='utf-8') as f:
#     sports = json.loads(f.read())

# for gender in sports.keys():
#     i = 0
#     while i < len(sports[gender].keys()):
#         sport = list(sports[gender].keys())[i]
#         if os.path.isfile('%s%s.html'%(HTML_DIR, get_date_file_path(gender, sport))):
#             print('already get : %s'%(sport))
#         else:
#             try :
#                 print('try get : %s' % (sport))
#                 get_html('http://trackfield.brinkster.net/%s'%(sports[gender][sport]), get_date_file_path(gender, sport))
#             except:
#                 print('error get : %s' % (sport))
#                 i -= 1
#         i += 1

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
