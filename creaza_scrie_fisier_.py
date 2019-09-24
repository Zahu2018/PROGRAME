"""TITLE OF FILE."""


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': 'dd.mm.yyyy',
 'Description': '.',
 'Last Modification': 'dd.mm.yyyy',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Prototype/Production/Abandoned',
 'Tags': ['create file', 'append file'],
 'Title': 'CAPITAL LETTER',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""


def scrie_fisier(rez):
    n = open('html.html', 'a')  # incepe sa creeze fisierul mare
    we = n.write(rez)
    n.close()
#  si1=si.decode('utf-8') #decode binary to utf-8  to utf-8


scrie_fisier("Text")
