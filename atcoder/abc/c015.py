N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]


def dfs(i, j, tmp_rslt, debug=[]):
    assert 0 <= i < N
    assert 0 <= j < K

    tmp_rslt ^= T[i][j]
    debug = debug + [(i, j)]
    if i == N - 1:
        if not debug:
            print()
            print(*debug, sep="\n")
        return tmp_rslt != 0

    ret = True
    for k in range(K):
        ret = ret and dfs(i + 1, k, tmp_rslt, debug)
    return ret


for j in range(K):
    if not dfs(0, j, 0, []):
        print("Found")
        break
else:
    print("Nothing")
