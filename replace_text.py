"""REPLACE A TEXT IN A FILE."""

import os

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': '17.09.2019',
 'Description': 'Replace a text in a file',
 'Last Modification': 'dd.mm.yyyy',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Production',
 'Tags': ['replace', 'text', 'file'],
 'Title': 'REPLACE TEXT IN A FILE',
 'Usage': .'
 'Version': '1.0.0'}
"""

fisiere = os.listdir()
print("Wait ...")
for fila in fisiere:
    if "." not in fila:
        continue
    else:
        with open(fila, 'r+', encoding='utf-8') as f:
            original = f.read()
            final = original.replace("/Deprecated", "/Abandoned")
            f.seek(0, 0)  # where to inject code (here at the beginning)
            f.write(final)
print("Finalizare OK")
