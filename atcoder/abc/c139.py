N = int(input())
H = list(map(int, input().split()))
ans = 0
current = 0
for i in range(N - 1):
    current = current + 1 if H[i] >= H[i + 1] else 0
    ans = max(current, ans)
print(ans)
