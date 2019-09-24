"""SEARCH IN LIST."""


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
 'Tags': ['cautare', 'search', 'find', 'list'],
 'Title': 'SEARCH IN LIST',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""


Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
# 1. transformare lista in lowercase
# 2. transformare cuvantul introdus in lowercase
ColorSelect = ""
while str.upper(ColorSelect) != "QUIT":
    ColorSelect = input("Please type a color name: ")
    if (Colors.count(ColorSelect) >= 1):
        print("The color exists in the list!")
    elif (str.upper(ColorSelect) != "QUIT"):
        print("The list doesn't contain the color.")
