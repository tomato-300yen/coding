N = int(input())
D = sorted([int(input()) for _ in range(N)])
ans = 0
last = 0
for d in D:
    if d == last:
        continue
    ans += 1
    last = d
print(ans)
