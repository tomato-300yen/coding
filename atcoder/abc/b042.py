N, L = tuple(map(int, input().split()))
S = [input() for _ in range(N)]
S.sort(key=lambda s: s)
print("".join(S))
