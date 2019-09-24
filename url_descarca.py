
import urllib.request
def descarca_url(web):
    htmlfile = urllib.request.urlopen(web)
    htmltext = htmlfile.read()
    return (htmltext)

import os.path
def scrie_fisier(rez):
    n = open('html.html', 'a')  # incepe sa creeze fisierul mare
    we = n.write(mm)
    n.close()
# si1=si.decode('utf-8') #decode binary to utf-8
