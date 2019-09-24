"""DOWNLOAD."""

import requests
import urllib
import wget  # pip install wget
import shutil

# !/usr/bin/env python
#  -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
'Contact': '',
'Copyright': '',
'Credits': '',
'Date': '07.08.2019',
'Description': 'Function for download file',
'Last Modification': '24.09.2019',
'Licence': '',
'Maintainer': '',
'Status': 'NOT TESTED ENTIRELY',
'Tags': ['download', 'descarca', 'web page', 'youtube', 'pdf', 'jpg', 'image'],
'Title': 'DOWNLOAD',
'Version': '1.0.0'}.

Content:
 1. Download_image
 2. Download_image_1
 3. Download_image_2
 4. Download_large_1
 5. Download_video
 6. Download_file_that_redirect
 7. Download_multiple_file
 8. Download_web_page
 9. Download_web_page_1
10. Download_web_page_2 - BEST
11. Download_via_proxy
12. Download_from_youtube
"""


def incarca_pagina_web_pt_lucru(url):
    """MERGE."""
    #  proxy = {'http':'http://ipaddress:port'}
    #  response = requests.get("http://")
    #  print(response.text)  # output the html of the page
    #  links = re.findall('"((http|ftp)s?://.*?)"', html)  # retrieve all links
    import urllib3
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    print(response.data)  # output the html of the page
    print('Terminat!')


#  incarca_pagina_web_pt_lucru('http://www.')


def download_image(url):
    """Download small files like: pictures."""
    r = requests.get(url)  # create HTTP response object
    with open("poza.png", 'wb') as f:
        f.write(r.content)
    print("Terminat!")


#  download_image(url_of_image.jpg)

def download_image_1(url):
    """Download small files like: pictures."""
    myfile = requests.get(url)
    open('image.png', 'wb').write(myfile.content)
    print("Terminat!")

#  download_image_1('https://www.python.org/static/img/python-logo@2x.png')


def download_image_2(url):
    """."""
    wget.download(url, 'img.png')
    print("Terminat!")

#  download_image_2('https://www.python.org/static/img/python-logo@2x.png')

def download_image_3(url, imagine):
    """."""
    urllib.request.urlretrieve(url, imagine)


download_image_3("http://atkgalleria.ero.today/lingerie/342632/m07.jpg", "img.jpg")


def download_large_1(url):
    """Big files like: pdf."""
    """Bun si pentru download html file."""
    r = requests.get(url, stream=True)
    with open("downloaded.pdf", "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            # writing one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)
    print("Terminat!")

# download_large_1(url_of_pdf_file.pdf)


def download_video(url):
    """NOTE TESTED! Download videos from an archive."""
    from bs4 import BeautifulSoup

    def get_video_links():
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        links = soup.findAll('a')  # find all links on web-page
        # filter the link sending with .mp4
        video_links = [url + link['href'] for link in links if
                       link['href'].endswith('mp4')]
        download_video_series(video_links)

    def download_video_series(video_links):
        for link in video_links:
            file_name = link.split('/')[-1]  # obtain filename
            print("Downloading file:%s" % file_name)
            r = requests.get(link, stream=True)
            # download started
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            print("%s downloaded!\n" % file_name)
        print("All videos downloaded!")


# download_video("http://www-personal.umich.edu/~csev/books/py4inf/media/")

def download_file_that_redirect(url):
    """Download file that redirect: pdf, ."""
    """url example: https://readthedocs.org/projects.../latest/"""
    myfile = requests.get(url, allow_redirects=True)
    open('file.pdf', 'wb').write(myfile.content)
    print("Terminat!")

#  fdownload_file_that_redirect('https://readthedocs.org/projects/python-guide/downloads/pdf/latest/')


def download_multiple_file(*url):
    """Download multiple file. Like html, ..."""
    #  from multiprocessing.pool import ThreadPool
    #  NU MERGE
    path, url = url
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for ch in r:
            f.write(ch)

# download_multiple_file([("Event1", "https://www.python.org/events/.../805/"),
# ("Event2", "https://www.python.org/events/python-events/801/"),
# ("Event3", "https://www.python.org/events/python-events/790/")])


def download_web_page(url, fisier):
    """Descarca si salveaza in calculator o pagina web."""
    urllib.request.urlretrieve(url, fisier)  # target = pagina.html salvata
    print("Terminat!")


#  download_web_page('http://www./', 'web.html')

def download_web_page_1(url, fisier):
    """FOLOSIT MAI NOU."""
    import urllib3  # pip install urllib3
    c = urllib3.PoolManager()
    with c.request('GET', url, preload_content=False) as res:
        out_file = open(fisier, 'wb')
        shutil.copyfileobj(res, out_file)
        print(res.data)
    print("Terminat!")


#  download_web_page_1('http://www.', 'test.txt')


def descarca_web_page_2(url):
    """CEL MAI FOLOSIT."""
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read()
    #  htmltext_final = htmltext.decode('utf-8')  # decode binary to utf-8
    print(htmltext)


#  descarca_web_page_2('https://www.python.org/')


def download_via_proxy(url):
    """???Se conecteaza via proxy??? Si ce face???."""
    my_proxy = {'http': 'http://127.0.0.2:3001'}
    web = requests.get(url, proxies=my_proxy)
    print(web)


# download_via_proxy('https://www.python.org/')


def download_from_youtube():
    """Download youtube movie."""
    import pytube
    yt = pytube.YouTube("https://www.youtube.com/watch?v=himEMfYQJ1w")
    streams = yt.streams.all()
    for x in streams:
        print(x)


# download_from_youtube()
