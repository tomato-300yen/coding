H, W, X, Y = map(int, input().split())
X, Y = X - 1, Y - 1
S = [input() for _ in range(H)]
ans = 0
tmp = 0
passed = False
for i in range(H):  # (i, Y)を見る
    # print(i, Y, S[i][Y])
    if S[i][Y] == "#":
        if passed:
            break
        tmp = 0
    else:
        if i == X:
            passed = True
        tmp += 1
ans += tmp
tmp = 0
passed = False
for j in range(W):  # (X, j)を見る
    # print(X, j, S[X][j])
    if S[X][j] == "#":
        if passed:
            break
        tmp = 0
    else:
        if j == Y:
            passed = True
        tmp += 1
ans += tmp
print(ans - 1)
