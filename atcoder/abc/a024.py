A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
print(A * S + B * T - ((S + T) * C if (S + T) >= K else 0))
