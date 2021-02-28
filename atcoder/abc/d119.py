import bisect

A, B, Q = map(int, input().split())
S, T, X = [[int(input()) for _ in range(i)] for i in [A, B, Q]]
for x in X:
    idx_s = bisect.bisect_left(S, x)
    idx_t = bisect.bisect_left(T, x)
    S_near = S[max(idx_s - 1, 0) : idx_s + 1]
    T_near = T[max(idx_t - 1, 0) : idx_t + 1]
    # print(S_near, T_near)
    ans = 1e100
    for s in S_near:
        for t in T_near:
            ans = min(ans, abs(s - x) + abs(t - s))
            ans = min(ans, abs(t - x) + abs(s - t))
    print(ans)
