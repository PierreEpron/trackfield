import requests, json, os, time
from bs4 import BeautifulSoup


HTML_DIR = 'html/'
JSON_DIR = 'json/'
SLEEP = 0
COLS = ['rank', 'name', 'birth_country', 'perf_0', 'perf_1', 'perf_2', 'perf_country', 'date']

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
#         for year in range(1891, 2020):            
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
