N, D, H = map(int, input().split())
DH = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for d, h in DH:
    ans = max(ans, (D * h - H * d) / (D - d))
print(ans)
