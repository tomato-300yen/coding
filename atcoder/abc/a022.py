N, S, T = map(int, input().split())
A = [int(input()) for _ in range(N)]
W = ans = 0
for a in A:
    W += a
    ans += S <= W <= T
print(ans)
