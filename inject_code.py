"""INJECT CODE IN A FILE."""

import os

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': '17.09.2019',
 'Description': 'Inject code at beginning/(or elsewere) of file.',
 'Last Modification': '29.09.2019',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Production',
 'Tags': ['inject', 'code', 'file', 'fisier'],
 'Title': 'INJECT CODE IN A FILE',
 'Usage': '.',
 'Version': '1.0.0'}
"""
# =========================================
# Code to inject begin here
# =========================================
code_to_inject = '''"""TITLE OF FILE."""

import os

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
 'Tags': [],
 'Title': 'CAPITAL LETTER',
 'Usage': '.',
 'Version': 'major.minor.patch'}
"""'''
# =========================================
# Code to inject end here
# =========================================
fisiere = os.listdir()
for fila in fisiere:
    if fila == "inject_code.py" or "." not in fila:
        continue
    else:
        with open(fila, 'r+', encoding='utf-8') as f:
            original = f.read()
            final = code_to_inject + '\n' + original
            f.seek(0, 0)  # where to inject code (here at the beginning)
            f.write(final)
print("Finalizare OK")
