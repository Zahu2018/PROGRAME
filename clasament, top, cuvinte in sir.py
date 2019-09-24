"""CLASAMENT CUVINTE IN SIR."""


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
 'Contact': '',
 'Copyright': 'Florian Zah',
 'Credits': [],
 'Date': 'dd.mm.yyyy',
 'Description': 'face un clasament cu cuvintele care apar cel mai des intr-o lista',
 'Last Modification': '24.09.2019',
 'Licence': '',
 'Maintainer': 'Florian Zah',
 'Status': 'Prototype/Production/Abandoned',
 'Tags': ['clasament', 'cuvinte', 'collocation table'],
 'Title': 'CLASAMENT CUVINTE IN SIR',
 'Usage': '.'
 'Version': '1.0.0'}
"""


from collections import Counter
MyList = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 5]
ListCount = Counter(MyList)
print(ListCount)
for ThisItem in ListCount.items():
    print("Item: ", ThisItem[0], " Appears: ", ThisItem[1])

print("The value 1 appears {0} times.".format(ListCount.get(1)))
