N, K, M = map(int, input().split())
A = map(int, input().split())
ans = max(M * N - sum(A), 0)
print(ans if ans <= K else -1)
