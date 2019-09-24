"""DYNAMIC BUTTON TKINTER."""

from tkinter import *

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': 'dd.mm.yyyy',
 'Description': 'creaza butoane le da un nume si pot fi activate',
 'Last Modification': 'dd.mm.yyyy',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Prototype/Production/Abandoned',
 'Tags': ['button', 'dinamic', 'tkinter'],
 'Title': 'DYNAMIC BUTTON TKINTER',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""


root = Tk()

button = []
for i in range(3):
    button.append(Button(root, text='Game ' + str(i + 1), command=lambda i=i + 1: open_this(i)))
    button[i].grid(column=4, row=i + 1, sticky=W)


def open_this(myNum):
    print(myNum)


root.mainloop()
