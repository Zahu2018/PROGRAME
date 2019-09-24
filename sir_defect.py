"""SIR DEFECT."""


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
 'Tags': ['sir', 'str', 'string', 'defect', 'repara'],
 'Title': 'SIR DEFECT',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""

sir = 'Aces t a   est e   un   si r   def ec t'
inceput = 0
sirFinal = ''
for i in range(0, 11):  # de gasit RANGE care sa se potriveasca la orice sir
    a = sir.find(' ', inceput)
    if (sir[a + 1]) != ' ':
        sirFinal += sir[inceput:a]
        inceput = a + 1
    else:
        sirFinal += sir[inceput:a + 2]
        inceput = a + 3
print(sirFinal + 't')
