"""ANO-TEST."""


import urllib.request
import re

d = {}
HREF = 'http://www.a...'


def descarca_url(web):
    htmlfile = urllib.request.urlopen(web)
    htmltext = htmlfile.read().decode(encoding='utf-8', errors='ignore')
    # print(htmltext)
    return (htmltext)


def litere(text):  # nivel 1
    """[('/href...', 'B', '120')]."""
    pat = re.compile(r'<a href="(/\w+/\w).+>(\w)\sindex\s-\s(\d+)')
    lista_litere = re.findall(pat, text)
    # print(lista_litere)
    return lista_litere


def nume(text):  # nivel 2
    """[('/href...', 'Ion', '3')]."""
    pat = re.compile(r'<a href="(/\w+/\w+-?\w+?-?\w+?).+>(\w+\s?\w+?)\s\((\d+)')
    lista_nume = re.findall(pat, text)
    # print(lista_nume)
    # print(len(lista_nume))
    return lista_nume


def galerii(text):  # nivel 3
    """Ex: [('2019-12-12', 'www...', 'Summer')]."""
    pat = re.compile(r"<p class='desc'>.+(\d\d\d\d-\d\d-\d\d).+\n<p class='desc'><a href='(http://www.+)\'\starget='_self'>(\w+)")
    lista_galerii = re.findall(pat, text)
    # print(lista_galerii)
    # print(len(lista_galerii))
    return lista_galerii


def tags(text):  # nivel 4
    """['tag1', 'tag2']."""
    pat = re.compile(r"<a\sclass='interstitial'\shref='/tag/.+?'>([\w+\s?]+)")
    lista_tags = re.findall(pat, text)
    # print(lista_tags)
    # print(len(lista_tags))
    sir_lista_tag = ""
    for item in lista_tags:
        sir_lista_tag += item + ','

    return sir_lista_tag


def main():
    zero = descarca_url('http://www.a.../p.../')
    unu = litere(zero)
    with open('rezultat.csv', 'a') as fila:
        for i in unu:
            if i[1] == 'V':
                url_doi = descarca_url(HREF + i[0])
                doi = nume(url_doi)
                for j in doi:
                    if j[1] == 'V... B':
                        url_trei = descarca_url(HREF + j[0])
                        trei = galerii(url_trei)
                        for k in trei:
                            an = k[0][0:4]
                            luna = k[0][5:7]
                            zi = k[0][8:10]
                            url_patru = descarca_url(k[1])
                            patru = tags(url_patru)
                            rand = ("{},{},{},{},{},{},{},{}\n".format(i[1], j[1], k[2], an, luna, zi, k[1], patru))
                            # print("{},{},{},{},{},{},{},{}".format(i[1], j[1], k[2], an, luna, zi, k[1], patru))
                            fila.write(rand)
                    else:
                        continue
            else:
                continue



if __name__ == '__main__':
    main()
