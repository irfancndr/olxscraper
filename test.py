import requests
from bs4 import BeautifulSoup
from lxml import html
import string
import csv
import sys
import re
global j
links = []
old_links = []
for j in range(1,3):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    r = requests.get("http://olx.co.id/properti/rumah//?page="+str(j), headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    container = soup.findAll("table", {"id": "offers_table"})[1]
    for link in container.find_all("a"):
        links = link.get("href")
        try:
            if "https://www.olx.co.id/iklan/" in links:
                if links not in old_links:
                    old_links.append(links)
                    print(links)
        except:
            pass