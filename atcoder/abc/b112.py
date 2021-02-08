N, T = tuple(map(int, input().split()))
CT = [tuple(map(int, input().split())) for _ in range(N)]
ans = 1001
for c, t in CT:
    if t > T:
        continue
    ans = min(ans, c)
print(ans if ans < 1001 else "TLE")
