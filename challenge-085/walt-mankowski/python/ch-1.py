#!/usr/bin/env python

from itertools import combinations
from sys import argv

data = [float(x) for x in argv[1:]]
comb = combinations(data, 3)
res = 0
for c in comb:
    total = sum(c)
    if 1 < total < 2:
        res = 1
        break

print(res)

