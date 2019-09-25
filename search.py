"""SEARCH."""

import os
import ast
#  import json

"""{'Author': 'Florian Zah',
'Contact': '',
'Copyright': '',
'Credits': '',
'Date': '07.08.2019',
'Deprecated': '',
'Description': 'Search in py, txt, zah file for tags, etc...',
'Last Modification': '25.09.2019',
'Licence': '',
'Maintainer': '',
'Status': 'Production',
'Tags': ['search', 'find', 'cauta', 'gaseste'],
'Title': 'SEARCH',
'Version': '1.0.0'}.
"""


fisiere1 = os.listdir()
#  Cautare doar in fisierele python: .py
fisiere = []
for fi in fisiere1:
    if fi[-3:] == '.py':
        fisiere.append(fi)
#  print(fisiere)


class SearchHeaderDictionary:
    """Type of header: Dictionary."""

    def __init__(self, word):
        self.a_word = word

    def fa_dictionar(self, fila):
        """."""
        with open(fila, 'r', encoding='utf-8') as f:
            t = f.read()
            #  print(t)
            initial = t.find('"""{')
            final = t.find('}', initial + 4)
            d = t[initial + 3:final + 1].lstrip('"""')
            #  print(d, '\n')
            di = ast.literal_eval(d)  # dictionarul OK
            #  di = json.loads(d) # name enclosed in double quotes "
            #  print(di)
            return di

    def rezolva(self):
        for filename in fisiere:
            if "." in filename:
                #  print(filename)
                dw = SearchHeaderDictionary.fa_dictionar(self, filename)  # dw = dictinar cuvinte header
                if word in str(dw.values()).lower():
                    SearchHeaderDictionary.afiseaza(self, filename, dw)
            else:
                continue


    def afiseaza(self, filename, dw):
        print('{}: {}\n'.format(filename.upper(), dw["Tags"]))


class SearchHeaderDunders:
    """For header with double underscore."""
    def __init__():
        pass


class SearchHeaderSermon:
    """For header of sermon."""
    def __init__():
        pass


word = input("Cauta\n:").lower()
search = SearchHeaderDictionary
search.rezolva(word)
