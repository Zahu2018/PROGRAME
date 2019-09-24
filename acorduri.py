"""ACORDURI MUZICALE."""

#  import module

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': 'dd.mm.yyyy',
 'Description': '.',
 'Last Modification': '17.09.2019',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Production',
 'Tags': ['muzica', 'music', 'chord', 'acorduri'],
 'Title': 'ACORDURI MUZICALE',
 'Usage': '.',
 'Version': '1.0.0'}
"""
dictionar = {"DO# Major - 7#": "DO#-FA-SOL#",
             "FA# Major - 6#": "FA#-LA#-DO#",
             "SI Major - 5#": "SI-RE#-FA",
             "MI Major - 4#": "MI-SOL#-SI",
             "LA Major - 3#": "LA-DO#-MI",
             "RE Major - 2#": "RE-FA#-LA",
             "SOL Major - 1#": "SOL-SI-RE",
             "DO Major": "DO-MI-SOL",
             "FA Major - 1b": "FA-LA-DO",
             "Sib Major - 2b": "SIb-RE-FA",
             "Mib Major - 3b": "MIb-SOL-SIb",
             "Lab Major - 4b": "LAb-DO-MIb",
             "Reb Major - 5b": "REb-FA-LAb",
             "SOLb Major - 6b": "SOLb-SIb-REb",
             "Dob Major - 7b": "DOb-MIb-SOLb",
             "LA# minor - 7#": "LA#-DO#-FA",
             "RE# minor - 6#": "RE#-FA#-LA#",
             "SOL# minor - 5#": "SOL#-SI–RE#",
             "DO# minor - 4#": "DO#-MI–SOL#",
             "FA# minor - 3#": "FA#-LA-DO#",
             "SI minor - 2#": "SI-RE-FA#",
             "MI minor - 1#": "MI-SOL-SI",
             "LA minor": "LA-DO-MI",
             "RE minor - 1b": "RE-FA-LA",
             "SOL minor - 2b": "SOL-SIb-RE",
             "DO minor - 3b": "DO-MIb-SOL",
             "FA minor - 4b": "FA-LAb-DO",
             "Sib minor - 5b": "SIb-REb-FA",
             "Mib minor - 6b": "MIb-SOLb-SIb",
             "Lab minor - 7b": "LAb-SI-MIb"}

nota1 = input().lower()
nota2 = input().lower()
nota3 = input().lower()
var1 = nota1 + "-" + nota2 + "-" + nota3
var2 = nota1 + "-" + nota3 + "-" + nota2
var3 = nota2 + "-" + nota1 + "-" + nota3
var4 = nota2 + "-" + nota3 + "-" + nota1
var5 = nota3 + "-" + nota1 + "-" + nota2
var6 = nota3 + "-" + nota2 + "-" + nota1

b = dictionar.items()

for ix in b:
    i = str(ix).lower()
    if var1 in i:
        print(i)
    if var2 in i:
        print(i)
    if var3 in i:
        print(i)
    if var4 in i:
        print(i)
    if var5 in i:
        print(i)
    if var6 in i:
        print(i)
