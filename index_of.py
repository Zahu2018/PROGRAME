"""IDEX OF."""

import urllib.request
import os.path
import subprocess
from time import sleep

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': 'dd.mm.yyyy',
 'Description': 'Transforma o lista INDEX OF in imagini una dupa cealalta',
 'Last Modification': '24.09.219',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Production',
 'Tags': ['index of', 'indexof', 'pics', 'picture', 'poze', 'foto'],
 'Title': 'INDEX OF',
 'Usage': '.'
 'Version': '1.0.0'}
"""

if os.path.exists('html.html'):  # sterge fisierul html.html daca exista
    os.remove('html.html')

"""Open a html file content."""
input_url = input("Introduceti url: \n")
htmlfile = urllib.request.urlopen(input_url).read().decode('utf-8')
sir = htmlfile.replace('HREF', 'href')
num = sir.count('href')
# print(a, num)

final = 0
for i in range(num):
    start = sir.find('href', final)
    final = sir.find('>', start)
    url_ok = sir[start + 6:final + 1]
    mesaj = ('<img src="' + input_url + url_ok + '<br>')
    print(mesaj)
    n = open('html.html', 'a')
    we = n.write(mesaj)
    n.close()
    # print(n.name)

# subprocess.call(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "-incognito", "C:\\Users\\User\\Desktop\\PYTHON\\html.html"])  # fisier sau url
# sau
subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "-incognito", "C:\\Users\\User\\Desktop\\PYTHON\\html.html"])  # fisier sau url
sleep(10)  # trebuie lasat putin sa incarce, si dupa aceea: os.remove
os.remove("html.html")


# ===========================================================
# NU MERGE CU FUNCTII - TREBUIE RETESTAT

# if os.path.exists('html.html'):  # sterge fisierul html.html daca exista
#     os.remove('html.html')
#
#
# def descarca_pagina_web():
#     """Open a html file content."""
#     input_url = input("Introduceti url: \n")
#     htmlfile = urllib.request.urlopen(input_url).read().decode('utf-8')
#     sir = htmlfile.replace('HREF', 'href')
#     num = sir.count('href')
#     # print(sir, num, input_url)
#     return sir, num, input_url
#
#
# def aranjeaza(sir, num, input_url):
#     """."""
#     final = 0
#     for i in range(num):
#         start = sir.find('href', final)
#         final = sir.find('>', start)
#         url_ok = sir[start + 6:final + 1]
#         mesaj = ('<img src="' + input_url + url_ok + '<br>')
#         print(mesaj)
#         n = open('html.html', 'a')
#         we = n.write(mesaj)
#         n.close()
#         # print(n.name)
#         return n.name
#
#
# def deschide_in_browser(pagina):
#     """."""
#     # subprocess.call(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "-incognito", "C:\\Users\\User\\Desktop\\PYTHON\\html.html"])  # fisier sau url
#     # sau
#     subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "-incognito", "C:\\Users\\User\\Desktop\\PYTHON\\html.html"])  # fisier sau url
#     sleep(10)  # trebuie lasat putin sa incarce, si dupa aceea: os.remove
#     os.remove("html.html")
#
#
# def main():
#     a, b, c = descarca_pagina_web()  # a = textul htmlfile; b = numarul de href-uri; c = url-ul
#     d = aranjeaza(a, b, c)
#     deschide_in_browser(d)
#
#
# if __name__ == '__main__':
#     main()
