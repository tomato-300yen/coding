from math import gcd
from functools import reduce

N = int(input())
T = [int(input()) for _ in range(N)]
print(reduce(lambda x, y: x * y // gcd(x, y), T))
