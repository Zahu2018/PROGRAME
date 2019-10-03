"""PDF FILE WORKING WITH."""

import os
import subprocess
import PyPDF2
# sau
import PyPDF3


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
'Tags': ['pdf', 'extract', 'img', 'foto', 'text', 'merge pdf', 'text', 'rotate'],
'Title': 'WORKING WITH PDF FILE',
'Usage': '.',
'Version': '1.1.0'}
"""


def extrage_poze(pdf_path, output_dir):  # MERGE!!!
    """Quick and dirt. Work with pdf 1.6."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cmd = ['pdfimages', '-all', pdf_path,
           '{}/prefix'.format(output_dir)]
    subprocess.call(cmd)
    print('Images extracted:')
    print(os.listdir(output_dir))


# extrage_poze('israel.pdf', output_dir='extracted_images')


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

# ===============================================
# WORKING WITH TEXT
# ===============================================

# 1. EXTRACT TEXT FROM PDF - IT WORKED!!!
def extrage_text(pdf_file):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
    pdfReader.numPages
    pageObj = pdfReader.getPage(0)
    pageObj.extractText()
    print(pdfReader.numPages)
    print(pageObj.extractText())
# extrage_text('ebp.pdf')

# 2. DECRYPTING PDF - NU MERGE
def decripteaza():
    pdfReader = PyPDF3.PdfFileReader(open('encrypted.pdf', 'rb'))
    print(pdfReader.isEncrypted)
    # print(pdfReader.getPage(0))
    # print(pdfReader.getPage())
    print(pdfReader.decrypt('rosebud'))
    print(pageObj=pdfReader.getPage(0))
# decripteaza()

# 3. CREATE PDF = MERGE 2 PDF FILE IN A SINGLE ONE  - WORKED!
# Steps for editing pdf
# 1. Open one or more existing PDFs (the source PDFs) into PdfFileReader objects.
# 2. Create a new PdfFileWriter object.
# 3. Copy pages from the PdfFileReader objects into the PdfFileWriter object.
# 4. Finally, use the PdfFileWriter object to write the output PDF.
def append_pdf():  # append a pdf to another pdf (merge 2 pdf-uri)
    pdf1File = open('meetingminutes.pdf', 'rb')
    pdf2File = open('meetingminutes2.pdf', 'rb')
    pdf1Reader = PyPDF3.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF3.PdfFileReader(pdf2File)
    pdfWriter = PyPDF3.PdfFileWriter()
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfOutputFile = open('combinedminutes1.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
# append_pdf()

# 4. ROTATE PAGE - MERGE!
def roteste_pagina(pdf_file):  # roteste prima pagina si face din ea un nou pdf
    minutesFile = open(pdf_file, 'rb')
    pdfReader = PyPDF3.PdfFileReader(minutesFile)
    page = pdfReader.getPage(0)
    page.rotateClockwise(90)
    pdfWriter = PyPDF3.PdfFileWriter()
    pdfWriter.addPage(page)
    resultPdfFile = open('rezultat_rotire.pdf', 'wb')
    pdfWriter.write(resultPdfFile)
    resultPdfFile.close()
    minutesFile.close()
# roteste_pagina('3340063.pdf')

# 5. OVERLAY (pune o stampila, imagine peste pagina) - MERGE!
def overlay(pdf_file):
    minutesFile = open(pdf_file, 'rb')
    pdfReader = PyPDF3.PdfFileReader(minutesFile)
    minutesFirstPage = pdfReader.getPage(0)
    pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
    minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
    pdfWriter = PyPDF3.PdfFileWriter()
    pdfWriter.addPage(minutesFirstPage)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    resultPdfFile = open('rezultat_overlay.pdf', 'wb')
    pdfWriter.write(resultPdfFile)
    minutesFile.close()
    resultPdfFile.close()
# overlay('3340063.pdf')  # fisierul in care pune pe prima pagina

# 6. ENCRYPT PDF - MERGE!
def encripteaza(pdf_file):
    pdfFile = open(pdf_file, 'rb')
    pdfReader = PyPDF3.PdfFileReader(pdfFile)
    pdfWriter = PyPDF3.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt('swordfish')  # parola cu care encripteaza
    resultPdf = open('rezultat_encriptare.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
# encripteaza('3340063.pdf')

# 7. COMBINE SELECTED PAGES FROM VARIOUS PDF - nu merge!!!
# Combina mai multe pdf-uri (merge) dar fara prima pagina
def combina_foi_din_diferite_pdf():
    """1. Find all pdf in a folder."""
    pdfFiles = []
    pdfWriter = PyPDF3.PdfFileWriter()
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)
    pdfFiles.sort(key=str.lower)
    #print(pdfFiles)
    pdfFiles = ['3340063.pdf', 'bus.pdf']  # pentru test
    print(pdfFiles)  # pentru test
    # pdfWriter = PyPDF3.PdfFileWriter()
    # """2. Open each pdf."""
    # pdfFiles = []
    for filename in pdfFiles:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
        print(pdfReader)
    # """3. Add each page."""
    for filename in pdfFiles:
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        print(pdfWriter)
    # """4. Save the result."""
    for filename in pdfFiles:
        for pageNum in range(1, pdfReader.numPages):
            pdfOutput = open('rezultat_merging.pdf', 'wb')
            pdfWriter.write(pdfOutput)
            pdfOutput.close()
# combina_foi_din_diferite_pdf()

# =======================================================
# ASTEA SUNT NETESTATE
# =======================================================
"""
mypdf = 'bus.pdf'
pdf_document = PyPDF2.PdfFileReader(mypdf)  # read a file
pdf_document.numPages  # numar pagini
print(pdf_document)
print(pdf_document.numPages)
first_page = pdf_document.getPage(0)  # get first page
print(first_page.extractText())
page_one = pdf_document.getPage(0)

pdf_document_writer = PyPDF2.PdfFileWriter()  # for write a pdf
pdf_document_writer.addPage(page_one)
pdf_output_file = open('new_pdf_file.pdf', 'wb')
pdf_document_writer.write(pdf_output_file)
"""
# =============================================================================
"""
# Let's try to read the contents of our newly created PDF document:
mypdf = open(r'bus.pdf', mode='rb')
pdf_document = PyPDF2.PdfFileReader(mypdf)
pdf_document.numPages
page_one = pdf_document.getPage(0)
print(page_one.extractText())
"""
# =============================================================================
"""
# print pages from pdf
mypdf = open(r'D:\\lipsum.pdf', mode='rb')
pdf_document = PyPDF2.PdfFileReader(mypdf)

for i in range(pdf_document.numPages):
    page_to_print = pdf_document.getPage(i)
    print(page_to_print.extractText())
"""
# =============================================================================
"""
# read the contents of all pages
text = ''
mypdf = PyPDF2.PdfFileReader(mypdf)
i = 1
for page in range(mypdf.getNumPages()):
    pdf_page = mypdf.getPage(page)
    text += pdf_page.extractText()
    print(i)
    i += 1
"""
# =============================================================================
"""
# get_doc_info.py # extrage informatii din pdf
from PyPDF2 import PdfFileReader
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    print(info)
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title
if __name__ == '__main__':
    path = 'bus.pdf'
    get_info(path)
"""
# =============================================================================
"""
# extracting_text.py
# EXTRAGE DIN ANUMITE PDF-uri
from PyPDF2 import PdfFileReader
def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        # get the first page
        page = pdf.getPage(0)
        print(page)
        print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        print(text)
if __name__ == '__main__':
    path = 'bus.pdf'
    text_extractor(path)
"""
# =============================================================================
"""
pdfFileObj = open('bus.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()
"""
# =============================================================================
"""
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('3340063.pdf', 'rb'))
print(pdfReader.isEncrypted)
print(pdfReader.getPage(0))
print(pdfReader.decrypt('rosebud'))  # asta e parola daca pdf e encriptat
print(pageObj=pdfReader.getPage(0))
"""
# =============================================================================
"""
from tika import parser
raw = parser.from_file('3340063.pdf')
print(raw['content'])
"""
# =============================================================================
"""
import textract
text = textract.process("bus.pdf")
"""
# =============================================================================
"""
from py4j.java_gateway import JavaGateway
gw = JavaGateway()
result = gw.entry_point.strip('bus.pdf')
# result is a dict of {
#   'success': 'true' or 'false',
#   'payload': pdf file content if 'success' is 'true'
#   'error': error message if 'success' is 'false'}
print (result['payload'])
"""
# =============================================================================

