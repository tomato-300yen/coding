from math import gcd
from functools import reduce

N, S = map(int, input().split())
X = list(map(lambda x: abs(int(x) - S), input().split()))
print(reduce(gcd, X))
