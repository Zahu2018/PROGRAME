# SEARCH WORD(S) IN (SPECIFIC WEBSITE) WITH GOOGLE
# Date:        21.08.2020
# Last update: 22.08.2020
# Author:      Zah

""" DOCUMENTATION

search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)
    query  : query string that we want to search for.
    tld    : tld = top level domain which means we want to search our
             result on google.com or google.in or some other domain.
    lang   : lang stands for language.
    num    : Number of results we want.
    start  : First result to retrieve.
    stop   : Last result to retrieve. Use None to keep searching forever.
    pause  : Lapse to wait between HTTP requests. Lapse too short may cause
             Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
    Return : Generator (iterator) that yields found URLs. If the stop
             parameter is None the iterator will loop forever.
"""
from googlesearch import search


def meniu():
    print("1. Search Google general")
    print("2. Search with Google in specific site")
    optiune = input("\nIntroduceti optiunea: \n>>> ")
    if optiune == "1":
        google_general()
    elif optiune == "2":
        google_specific()
    else:
        print("Introduceti optiunea 1 sau 2")
        meniu()


def google_general():
    cuvant_cautat = input("Introduceti cuvantul cautat: \n>>> ")
    cauta(cuvant_cautat)


def google_specific():
    cuvant_cautat = input("Introduceti cuvantul cautat: \n>>> ")
    lista_siteuri = input("Introduceti site-urile, cu virgula:\n>>> ").replace(" ", "").split(",")
    for site in lista_siteuri:
        query = f'site:{site} {cuvant_cautat}'
        print(f"\n=====  {site}  =====")
        cauta(query)
        
        
def cauta(query):
    for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
        print(j)
    
meniu()
