# Matrix bot that will ideally post random images of frogs to a Matrix server.
import shutil
from math import floor
from random import random

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://calphotos.berkeley.edu"
FROG_URL = "https://calphotos.berkeley.edu/cgi/img_query?where-lifeform=Animal--Amphibian+%2844335%29&rel-taxon=contains&where-taxon=&rel-namesoup=matchphrase&where-namesoup=frog&rel-location=matchphrase&where-location=&rel-county=eq&where-county=any&rel-state=eq&where-state=any&rel-country=eq&where-country=any&where-collectn=any&rel-photographer=contains&where-photographer=&rel-kwid=equals&where-kwid=&max_rows=24"
#Temp variable, scrape it girl
TOTAL_FROGS = 10845

def get_frog():
    # it's actually ceil don't @ me I want full pages of frogs
    total_pages = floor(TOTAL_FROGS / 24)
    page_start = floor(random() * (total_pages - 1)) * 24
    data = {'query_src':'', 'tmpfile': '462539', 'num-matches':'10845', 'max':'24', 'prevwhere':'', 'button_flag': '',
            'prevselect':'*', 'table':'img', 'special':'', 'OK2SHOWPRIVATE':'', 'display2':'', 'display3': '',
            'display4': '', 'display5': '', 'display6': '', 'display7': '', 'display8': '', 'display9': '',
            'display10':'', 'display11': '', 'display12': '', 'display13': '', 'title_tag': '', 'next': 'next+24',
            'row-to-start' : '{row_start}'.format(row_start=page_start)}
    htmldata = requests.get(FROG_URL)
    htmldata = requests.post(FROG_URL, headers = {'Content-Type': 'application/x-www-form-urlencoded'}, data=data)
    soup = BeautifulSoup(htmldata.text, 'html.parser')
    frogs = soup.find_all('img')

    print(htmldata.text)

    frog = floor(random() * frogs.__len__())
    url_split = frogs[frog]['src'].split('.')
    file_extension = url_split[url_split.__len__() - 1]
    frog_img = requests.get(BASE_URL + frogs[frog]['src'], stream=True)
    if frog_img.status_code == 200:
        with open('frog.' + file_extension, 'wb') as f:
            shutil.copyfileobj(frog_img.raw, f)
        print('image downloaded: frog.' + file_extension)
    print('frog.' + file_extension)
    return 'frog.' + file_extension