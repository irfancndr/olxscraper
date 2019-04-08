import requests
from bs4 import BeautifulSoup
from lxml import html
import string
import csv
import sys
import re
import os
from _colorized import banner

print(banner)
while True:
    folder = input('Nama CSV : ').lower()
    if not os.path.exists((folder) + ".csv"):
        namafile = folder + ".csv"
        break
    else :
        print("Nama Sudah Ada, Script Error")

f = open(namafile, "w")
writer = csv.writer(f)
header = "Nama ; Harga ; Info \n"

old =''
def getKonten(link):
    data = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    html = requests.get(link, headers=headers)
    soup = BeautifulSoup(html.content, "lxml")
    nama = soup.findAll("h1")[1].string.strip()
    print(nama)
    harga = soup.findAll("span", {"itemprop": "price"})[0].string
    print(harga)
    inf = []
    items = soup.findAll("ul", {"class": "spesifikasi"})
    for x in items:
        try:
            info = x.findAll("li")
            for m in info:
                inf.append(m.text.replace("\t", "").replace("\n", ""))
        except:
            pass
    infomobil = (";".join(inf))
    print(infomobil)
    f.write(nama + ";" + harga + ";" + infomobil + "\n")


links = []
old_links = []  # menyimpan data link agar tidak duplikat
global j
def spider(num):
    for j in range(1, num):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        r = requests.get("http://olx.co.id/" + apa + "/?page=" + str(j), headers=headers)
        soup = BeautifulSoup(r.content, "lxml")
        container = soup.findAll("table", {"class": "fixed offers breakword"})[0]
        for link in container.find_all("a"):
            links = link.get("href")
            try:
                if "https://www.olx.co.id/iklan/" in links:
                    if links not in old_links:
                        old_links.append(links)
                        print(links)
                        getKonten(links)
            except KeyboardInterrupt:
                break
                f.close()
            except:
                pass
                # import time
                #
                # print("\n \n \n")
                # print("Tunggu 20 detik")
                # time.sleep(20)
apa = input("Kategori : ").lower()
brp = int(input("Berapa Halaman : "))
spider(brp)