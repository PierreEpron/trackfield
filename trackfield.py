import requests
from bs4 import BeautifulSoup


HTML_DIR = 'html/'

''' Get all sports for mens and womens '''

req = requests.get('http://trackfield.brinkster.net/Main.asp')
soup = BeautifulSoup(req.text, 'html.parser')

with open('%shome.html'%HTML_DIR, 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# print(soup.find_all('table')[].find_all('tr')[0])
