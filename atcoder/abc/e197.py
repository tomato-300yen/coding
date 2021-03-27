from itertools import groupby

N = int(input())
XC = [list(map(int, input().split())) for _ in range(N)]
XC = sorted(XC, key=lambda ll: (ll[1]))
last_left = 0
last_right = 0
ans = 0
a, b = 0, 0
for k, g in groupby(XC, key=lambda ll: ll[1]):
    g = list(map(lambda ll: ll[0], g))
    left = min(g)
    right = max(g)
    length = right - left
    a, b = (
        length + min(abs(right - last_left) + a, abs(right - last_right) + b),
        length + min(abs(left - last_left) + a, abs(left - last_right) + b),
    )
    last_right = right
    last_left = left
a, b = a + abs(last_left), b + abs(last_right)
print(min(a, b))
