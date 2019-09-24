"""HTML APPEND."""

import urllib.request

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': 'dd.mm.yyyy',
 'Description': '.',
 'Last Modification': '24.09.2019',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Production',
 'Tags': ['html', 'htm', 'append', 'url'],
 'Title': 'HTML APPEND',
 'Usage': '.'
 'Version': '1.1.0'}
"""


def descarca_url(web):
    """."""
    htmlfile = urllib.request.urlopen(web)
    htmltext = htmlfile.read()
    return (htmltext)


def scrie_fisier(rez):
    """."""
    n = open('x.html', 'a')  # incepe sa creeze fisierul mare
    we = n.write(rez)
    n.close()


input_url = input("Introduceti URL:\n")
sir = descarca_url(input_url)
#  parsing file
sir1 = sir.decode('utf-8')  # decode from binary to unicode utf-8
index_1 = sir1.find('<h1>')  # indexi intermediari
index_2 = sir1.find('</style>', index_1)
index_table = sir1.find('<table ', index_2)
nr = sir1.count("<p class=\'desc\'><a href=", index_2, index_table)
'''if os.path.exists('html.html'):
    os.remove('html.html')
print(sir1)'''
final = index_2
lista_url = []
for i in range(nr):
    start = sir1.find("<p class=\'desc\'><a href=", final)
    final = sir1.find('target', start)
    urluri = sir1[start + 25:final - 2]
    lista_url.append(urluri)
    #  print(urluri)
#  print(lista_url)
rezult = ''
for i in lista_url:
    pagina = descarca_url(i)
    pagina_decodata = pagina.decode('utf-8')
    #  parse fiecare fisier inainte de a-l scrie
    i_1 = pagina_decodata.find('<div class="picture_block">')
    i_2 = pagina_decodata.find('<font size=', i_1)
    rezult += pagina_decodata[i_1 + 25:i_2 - 10]
#  print(rezult)
scrie_fisier(rezult)
