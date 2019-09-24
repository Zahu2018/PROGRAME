"""FILE RENAMER BIBLIOTECA."""

import os
import shutil

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
 'Tags': ['file', 'rename', 'biblioteca', 'renamer'],
 'Title': 'FILE RENAMER BIBLIOTECA',
 'Usage': '.'
 'Version': 'major.minor.patch'}
"""

"""
TO DO:
- de reverificat return a,b,c si revizuit functiile
- de cautat daca nu cumva exista deja cartea si de rescris sau nu si in BD
"""


class AdaugaCarti:
    def citesteCarti():
        path = "/media/z/Biblioteca/BIBLIOTECA_ZAH"
        lista_nume_vechi = os.listdir(path)
        #  print(lista_nume_vechi) # afiseaza fisierele din director
        return lista_nume_vechi

    def renameCarti(x):  # si Coperta
        lista_nume_noi = []
        for nume_vechi in x:
            nv, extensia_fisierului = os.path.splitext(nume_vechi)
            if extensia_fisierului == ".py" or extensia_fisierului == ".csv" or extensia_fisierului == ".jpg" or extensia_fisierului == ".py" or os.path.isdir(nume_vechi) == True:
                continue

            else:
                print(nume_vechi)
                titlu = input("TITLU = ")
                autor = input("AUTOR = ")
                serie = input("SERIE = ")
                keywords = input("KEYWORDS = ")
                nume_nou = titlu+","+autor+","+serie+","+keywords+","+extensia_fisierului
                nume_nou_fila = titlu+"_"+autor+extensia_fisierului
                cop = input("Are coperta? da/nu")  # redenumim coperta (daca este)
                if cop == "da" or cop == "d" or cop == "D":
                    poza_coperta = nv+".jpg"
                    nume_nou_coperta = titlu+"_"+autor+".jpg"
                    try:
                        os.rename(poza_coperta, nume_nou_coperta)
                    except FileNotFoundError:
                        print("Eroare redenumire coperta!")
                else:
                    pass
                try:
                    os.rename(nume_vechi, nume_nou_fila)
                except FileNotFoundError:
                    print("Eroare redenumire carte!")

                print(nume_nou)
                print("="*20)
                lista_nume_noi.append(nume_nou)
                print(serie)
                AdaugaCarti.mutaFile(serie, nume_nou_fila)  # creaza dosar carte si muta cartea
                AdaugaCarti.mutaCoperti(serie, nume_nou_coperta)  # creaza dosar coperta si muta poza

        return lista_nume_noi

    def mutaFile(a, f):  # a este directorul, f este fila
        director = a.replace("-", "/")
        if os.path.exists(director) is False:
            os.makedirs(director)  # creaza director daca nu exista
            shutil.move(f, director)  # muta cartea in director
        else:
            shutil.move(f, director)

    def mutaCoperti(a, f):
        director = a.replace("-", "/")
        director1 = director+"/coperti"
        if os.path.exists(director1) is False:
            os.makedirs(director1)  # creaza director daca nu exista
            shutil.move(f, director1)  # muta poza in director
        else:
            shutil.move(f, director1)

    def scrieBD(x):
        with open("BD.csv", "a") as fila:
            try:
                fila.write(str(x))
                fila.write("\n")
                fila.close
            except IOError:
                print("Eroare! Nu a putut scrie in BD")


def main():
    lista_nume_vechi = AdaugaCarti.citesteCarti()  # citeste filele vechi
    lista_nume_noi = AdaugaCarti.renameCarti(lista_nume_vechi)  # redenumire carti

    for i in lista_nume_noi:
        AdaugaCarti.scrieBD(i)  # adauga in BD.csv o linie
    print(lista_nume_vechi)
    print(lista_nume_noi)


if __name__ == "__main__":  # sau main()
    main()










