N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
X = list(map(int, input().split()))
Q = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]

WV = sorted(WV, key=lambda ll: (-ll[1], -ll[0]))
# print(*WV, sep="\n")
for L, R in Q:
    tmp_X = sorted(X[:L] + X[R + 1 :])
    tmp_WV = [ll for ll in WV]
    tmp_ans = 0
    for x in tmp_X:
        for i, (w, v) in enumerate(tmp_WV):
            if w <= x:
                tmp_ans += v
                tmp_WV.pop(i)
                break
    print(tmp_ans)
