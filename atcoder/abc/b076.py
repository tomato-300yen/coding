N, K = [int(input()) for _ in range(2)]
ans = 1
for i in range(N):
    ans = min(ans + K, ans * 2)
print(ans)
