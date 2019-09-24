"""EXCEL TO DICT."""

import openpyxl
import pprint

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': 'dd.mm.yyyy',
 'Description': '# Citeste dintr-un fisier xlsx randurile si le exporta
  intr-un fisier .py sub forma de dictionar ce poate fi accesat',
 'Last Modification': '24.09.2019',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Prototype/Production/Abandoned',
 'Tags': ['excel', 'xls', 'xlsx', 'dict', 'dictionar'],
 'Title': 'EXCEL TO DICT',
 'Usage': '.'
 'Version': '1.0.0'}
"""


print('Opening workbook ...')
wb = openpyxl.load_workbook(r'mat\censuspopdata.xlsx')
sheet = wb.get_sheet_by_name("Population by Census Tract")
countyData = {}  # cream un dictionar gol
print("Reading rows ...")
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value  # preia valoarea o celula B2 prima
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    #  CREAZA DICTIONARUL
    countyData.setdefault(state, {})  # setdefault
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    #  UPDATE-AZA DICTIONARUL CU NOILE VALORI
    countyData[state][county]['tracts'] += 1  # mai adauga unu
    countyData[state][county]['pop'] += int(pop)  # mai adauga pop la pop
print('Writing results ...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
#  resultFile.write('allData = ' + str(countyData))  # merge si asa da arata mai rau ca e pe o singura linie
resultFile.close()
print('Done.')

'''
accesarea se poate face in felul urmator din consola python:
import census2010 (numele fisierului)
census2010.allData['AK']['Haines'] # => {'pop':2508, 'tracts':1}
census2010.allData['AK']['Haines']['pop'] # => 2508
'''
