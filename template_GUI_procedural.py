"""TEMPLATE GUI PROCEDURAL."""

from tkinter import *
from phones import *

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
 'Tags': ['template', 'gui', 'procedural'],
 'Title': 'TEMPLATE GUI PROCEDURAL',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""


def unu():
    pass


def doi():
    pass


def makeWindow():
    global nameVar, phoneVar, select
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    return win


def setSelect():
    phonelist.sort()
    select.delete(0, END)
    for name, phone in phonelist:
        select.insert(END, name)


win = makeWindow()
setSelect()
win.mainloop()
