N = int(input())
T = [int(input()) for _ in range(N)]
total = sum(T)
ans = 1e10
for i in range(2 ** N):
    tmp = 0
    for j in range(N):
        if i & (1 << j):
            tmp += T[j]
    ans = min(ans, max(tmp, total - tmp))
print(ans)
