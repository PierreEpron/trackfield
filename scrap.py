import requests, json, os, time
from bs4 import BeautifulSoup
from pathlib import Path

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