"""DINAMIC TKINTER 2."""

from os import listdir
from tkinter import *

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
 'Tags': ['dinamic', 'tkinter', 'button'],
 'Title': 'DINAMIC TKINTER 2',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""


main = Tk()

lista = listdir()  # creaza o lista din fisierele din DIR curent
txt = StringVar()


# daca alegem prima varianta bu_var_1 = Button... atunci functia b
def b():
    global i
    c = bu.cget("text")
    print(c)


# daca alegem a doua varianta bu_var_2 = Button... atunci functia c
def c(file):
    print(file)


for file in lista:
    """Bu_var_1 = Button(main, text=file, command=b, background="white", borderwidth=0, activeforeground='red')."""
    bu_var_2 = Button(main, text=file, command=lambda file=file: c(file), background="white", borderwidth=0, activeforeground='red')
    bu_var_2.grid(sticky='W')


main.mainloop()
