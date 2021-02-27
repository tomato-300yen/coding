N = int(input())
P = map(int, input().split())
min_ = 2e6
ans = 0
for p in P:
    if p <= min_:
        ans += 1
    min_ = min(min_, p)
print(ans)
