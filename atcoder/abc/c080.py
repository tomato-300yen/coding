N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
ans = -1e10
for i in range(1, 2 ** 10):
    tmp = 0
    for j in range(N):
        num_open = 0
        for k in range(10):
            if i & (1 << k):
                num_open += F[j][k]
        tmp += P[j][num_open]
    ans = max(ans, tmp)
print(ans)
