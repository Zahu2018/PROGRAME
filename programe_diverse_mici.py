# PROGRAMS, SNIPETS

# ['cel mai mare divizor comum', 'cmmdc', 'gcd']
from functools import reduce
import math
def cmmdc(num):
   return reduce(math.gcd, num)
# print(cmmdc([25, 100, 50]))
# -----------------------------------------------

# ['lambda']
x = lambda a, b, c : a + b + c
# print(x(5,10,20))
# -----------------------------------------------

# ['size of var in bites', 'size', 'bites']
import sys
# print(sys.getsizeof(""))  # size in bites
# -----------------------------------------------

# ['palindrom']
#print('caiac' == 'caiac'[::-1])
# -----------------------------------------------

# ['list to string', 'list', 'string', 'str']
# print('-'.join(['1', '2', '3', '4']))
# -----------------------------------------------

# ['media unor numere', 'average', 'media']
args = (1, 2, 3, 4)
# print(sum(args) / len(args))
# -----------------------------------------------

# ['collocation table', 'clasament', 'top']
from collections import Counter
# print(Counter([1, 2, 3, 2, 5, 3, 2]))  # => un dict {name: how many time}
# -----------------------------------------------

# ['time to execute code', 'time', 'code', 'seconds']
import time
#start = time.time()  # best in linux: time.time()
start = time.perf_counter()  # best on windows: time.perf_counter()
# print("Code goes here")
# print(time.perf_counter() - start)  # time is in seconds
# -----------------------------------------------



