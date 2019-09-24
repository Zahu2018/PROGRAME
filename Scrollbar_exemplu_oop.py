"""SCROLLBAR TKINTER."""

import tkinter as tk

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
 'Tags': ['scroll', 'scrollbar', 'tkinter'],
 'Title': 'SCROLL BAR TKINTER',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""


class Example(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        """Put in some fake data."""
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1",
                     relief="solid").grid(row=row, column=0)
            t = "this is the second column for row %s" % row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        """Reset the scroll region to encompass the inner frame."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
