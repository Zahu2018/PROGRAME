"""H E L P - D I R ."""

import os
import ast

# !/usr/bin/env python
#  -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
'Contact': '',
'Copyright': '',
'Credits': '',
'Date': '',
'Description': 'Extract help from python help',
'Last Modification': '24.09.2019',
'Licence': '',
'Maintainer': '',
'Status': '',
'Tags': ['help', 'ajutor', 'dir', 'generator', 'genereaza'],
'Title': 'HELP DIR',
'Version': ''}

Content:
1.
"""

import markdown

def extrage_b():
    """__builtins__."""
    sim = 'text'
    s = ''
    for i in dir(list):
        #  print(i)
        s += i + '\n'
    html = markdown.markdown(s)
    print(html)

#  extrage_b()

def afiseaza_help():
    """..."""
    for i in dir(list):
        #  print(help(i))  # NU MERGE
        print(i)

afiseaza_help()


