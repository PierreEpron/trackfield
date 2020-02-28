import os, json
from pathlib import Path
from settings import *
from scrap import *
import pandas as pd

with open('%ssports_bck.json'%JSON_DIR, 'r', encoding='utf-8') as f:
    sports_bck = json.loads(f.read())
with open('%ssports.json'%JSON_DIR, 'r', encoding='utf-8') as f:
    sports = json.loads(f.read())
table = []

def get_date(date):
    if type(date) == str:
        date = ' '.join(date.split())
        if len(date.split(' ')) == 1:
            return '%s 01'%(date)
        return date
    return ''

def get_sport_id(path):
    return sports_bck[path.parts[2]][path.parts[3]].split('=')[1].split('&')[0]

def html_to_table(path):
    soup = read_html(path)
    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')
        if len(tds) == 8:
            table.append([path.parts[2], get_sport_id(path), sports[get_sport_id(path)], path.stem])
            for td in tds[:-1]:
                table[-1].append(td.text.strip())
            table[-1].append(get_date(tds[-1].text.strip()))
            # print(table[-1][-1])  

for dp, dns, fns in os.walk('%s/sports'%HTML_DIR):
    for fn in fns:
        print('%s/%s'%(dp, fn))
        html_to_table(Path('%s/%s'%(dp, fn)))

df = pd.DataFrame(table, columns=COLS)
df.to_csv('%sperfs.csv'%CSV_DIR, index=False)






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