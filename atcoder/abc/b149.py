A, B, K = map(int, input().split())
a, b = (A - K, B) if A >= K else (0, max(0, B - (K - A)))
print(a, b)
