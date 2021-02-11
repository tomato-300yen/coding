from math import ceil

N, D = tuple(map(int, input().split()))
print(ceil(N / (2 * D + 1)))
