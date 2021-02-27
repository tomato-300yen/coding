from math import ceil
N = int(input())
APX = [list(map(int, input().split())) for _ in range(N)]
APX = sorted(APX, key=lambda ll: ll[0])
ans = 1e10
for a, p, x in APX:
    rest = x - ceil(a)
    if rest > 0:
        ans = min(ans, p)
print(ans if ans < 1e10 else -1)
