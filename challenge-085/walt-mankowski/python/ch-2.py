#!/usr/bin/env python
from math import log, sqrt
from sys import argv

def round(n):
    return int(f'{n:.0f}')

def is_whole(n, eps):
    return abs(n - round(n)) < eps

EPS = 1e-6
n = int(argv[1])
logn = log(n)
res = 0

for i in range(2, round(sqrt(n))+1):
    power = logn / log(i)
    if is_whole(power, EPS):
        res = 1
        break

print(res)
