n = int(input())
d = [input().split() for _ in range(n)]
ans = 0
for x, u in d:
    x = float(x)
    if u == "JPY":
        ans += x
    else:
        ans += x * 380000
print(ans)
