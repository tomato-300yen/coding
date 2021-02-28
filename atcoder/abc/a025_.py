D, J = [map(int, input().split()) for _ in range(2)]
ans = 0
for d, j in zip(D, J):
    ans += max(d, j)
print(ans)
