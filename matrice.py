"""MATRICE."""

import string

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': 'dd.mm.yyyy',
 'Description': 'creaza o matrice din cele doua siruri(1a, 1,b, .../ 2a, 2b,)',
 'Last Modification': '24.09.2019y',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Prototype/Production/Abandoned',
 'Tags': ['matrice', 'matrix', 'list of lists'],
 'Title': 'MATRICE',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""


def randuri(ra):
    """Creaza randuri pt o matrice de la 1 - ..."""
    ls_nr = []
    for i in range(1, ra + 1):  # pana la ce numar vrem
        ls_nr.append(i)
    return ls_nr


def coloane(col):
    """Creaza coloane pt o matrice de la a - ..."""
    ls = list(string.ascii_lowercase)  # de la a-z
    ls1 = []
    for i1 in ls:
        for i2 in ls:
            nl = str(i1 + i2)
            ls1.append(nl)  # de la aa-zz
    ls.extend(ls1)  # ls=lista de la a-zz
    ls_col = ls[:col]
    return ls_col


def main():
    """Main function."""
    ran = int(input("Introduceti nr de randuri: "))
    col = int(input("Introduceti nr de coloane: "))
    ls_nr = randuri(ran)
    ls_col = coloane(col)
    # print(ls_nr)
    # print(ls_col)
    with open("re.csv", 'w') as m:  # deschidem fisier pt scriere
        for nr in ls_nr:
            for let in ls_col:
                if let != ls_col[-1]:
                    m.write(str(nr) + let + ', ')  # scrie in fisier
                else:
                    m.write(str(nr) + let + "\n")  # scrie in fisier


main()
