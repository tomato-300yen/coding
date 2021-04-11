from math import ceil

R, X, Y = map(int, input().split())
dist = (X ** 2 + Y ** 2) ** (1 / 2)
if dist < R:
    print(2)
else:
    print(ceil(dist / R))
