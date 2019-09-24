"""IDEX OF."""

import urllib.request
import os.path

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': 'dd.mm.yyyy',
 'Description': 'transforma o lista INDEX OF in imagini una dupa cealalta',
 'Last Modification': '24.09.219',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Production',
 'Tags': ['index of'],
 'Title': 'INDEX OF',
 'Usage': '.'
 'Version': '1.0.0'}
"""


input_url = input("Introduceti url: \n")


#  sterge fisierul existent
if os.path.exists('html.html'):
    os.remove('html.html')


#  open a html content file
htmlfile = urllib.request.urlopen(input_url)
si = htmlfile.read()
#  parsing file
si1 = si.decode('utf-8')  # decode binary to utf-8
sir = si1.replace('HREF', 'href')
num = sir.count('href')

final = 0
for i in range(num):
    start = sir.find('href', final)
    final = sir.find('>', start)
    url_ok = sir[start+6:final+1]
    mesaj = ('<img src="'+input_url+url_ok+'<br>')
    print(mesaj)
    n = open('html.html', 'a')
    we = n.write(mesaj)
    n.close()
