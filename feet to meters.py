"""FEET TO METERS."""

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
 'Tags': ['feet', 'meter', 'converter', 'metru', 'bind', 'enter'],
 'Title': 'FEET TO METERS',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""


#  functia care calculeaza
def calculeaza(*args):
    """."""
    try:
        value = float(feet.get())
        meters.set((0.308 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title('Feet to meters')

cadru = Frame(root, )
cadru.grid(column=0, row=0, sticky=(N, W, S, E))
cadru.columnconfigure(0, weight=1)
cadru.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = Entry(cadru, width=15, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

Label(cadru, textvariable=meters).grid(column=2, row=2, sticky=(W, E))  # aici se va scrie rezultatul
Button(cadru, text='Calculeaza', command=calculeaza).grid(column=3, row=3, sticky = (W))

Label(cadru, text='feet').grid(column=3, row=1, sticky=(W))
Label(cadru, text='echivalent cu').grid(column=1, row=2, sticky=(E))
Label(cadru, text='meters').grid(column=3, row=2, sticky=(W))

for child in cadru.winfo_children():  # pune un padding de 5 la widgeturi,
    child.grid_configure(padx=5, pady=5)  # se putea si separat la fiecare cand a fost construit

feet_entry.focus()  # cursorul apare in widgetul feet_entry
root.bind('<Return>', calculeaza)  # daca apesi Enter atunci calculeaza

root.mainloop()
