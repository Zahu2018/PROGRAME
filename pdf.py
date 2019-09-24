"""PDF FILE WORKING WITH."""

import os
import subprocess

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
'Contact': '',
'Copyright': 'Florian Zah',
'Credits': [],
'Date': '18.09.2019',
'Description': 'Various operation with pdf file',
'Last Modification': 'dd.mm.yyyy',
'Licence': '',
'Maintainer': 'Florian Zah',
'Status': 'Prototype/Production/Abandoned',
'Tags': ['pdf', 'extract', 'img', 'foto', 'text'],
'Title': 'PDF FILE',
'Usage': '.',
'Version': '1.0.0'}
"""


def extrage_poze(pdf_path, output_dir):
    """Quick and dirt. Work with pdf 1.6."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cmd = ['pdfimages', '-all', pdf_path,
           '{}/prefix'.format(output_dir)]
    subprocess.call(cmd)
    print('Images extracted:')
    print(os.listdir(output_dir))


extrage_poze('israel.pdf', output_dir='extracted_images')


def extrage_poze_2(file):
    """Nu merge la toate pdf-urile."""
    with open(file, "rb") as file:
        file.seek(0)
        pdf = file.read()

    startmark = b"\xff\xd8"
    startfix = 0
    endmark = b"\xff\xd9"
    endfix = 2
    i = 0
    print("Asteapta!")
    njpg = 0
    while True:
        istream = pdf.find(b"stream", i)
        if istream < 0:
            break
        istart = pdf.find(startmark, istream, istream + 20)
        if istart < 0:
            i = istream + 20
            continue
        iend = pdf.find(b"endstream", istart)
        if iend < 0:
            raise Exception("Didn't find end of stream!")
        iend = pdf.find(endmark, iend - 20)
        if iend < 0:
            raise Exception("Didn't find end of JPG!")

        istart += startfix
        iend += endfix
        print("JPG %d from %d to %d" % (njpg, istart, iend))
        jpg = pdf[istart:iend]
        with open("jpg%d.jpg" % njpg, "wb") as jpgfile:
            jpgfile.write(jpg)

        njpg += 1
        i = iend
    print("Final!")

#  extrage_poze_2('love yoga.pdf')
