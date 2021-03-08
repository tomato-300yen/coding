N, K = map(int, input().split())
X = list(map(int, input().split()))
ans = 1e10
for i in range(N - K + 1):
    left = X[i]
    right = X[i + K - 1]
    ans = min(ans, min(abs(left), abs(right)) + abs(left - right))
print(ans)
