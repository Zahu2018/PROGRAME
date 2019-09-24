"""TEMPLATE GUI."""

from tkinter import *
from tkinter import ttk
from os import listdir

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': 'dd.mm.yyyy',
 'Description': '.',
 'Last Modification': '24.09.2019',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Prototype/Production/Abandoned',
 'Tags': ['template', 'gui'],
 'Title': 'TEMPLATE GUI',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""


class Ate:
    def __init__(self, master):
        self.master = master

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Contacte(self.newWindow)


class Contacte:  # nu are nici o treaba cu programul. E asa ... in plus
    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Contacte(self.newWindow)

    def close_windows(self):
        self.master.destroy()


def main():
    root = Tk()
    root.title("Fise de magazie (pt. Serafil)")
    app = Ate(root)
    root.mainloop()


if __name__ == '__main__':
    main()
