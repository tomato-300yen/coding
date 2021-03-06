N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
ans = 10 ** 5
for i in range(N):
    for j in range(N):
        if i == j:
            tmp = AB[i][0] + AB[j][1]
        else:
            tmp = max(AB[i][0], AB[j][1])
        ans = min(ans, tmp)
print(ans)
