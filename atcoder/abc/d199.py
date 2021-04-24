N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
dist = [[0 for i in range(N)] for j in range(N)]
for a, b in AB:
    dist[a - 1][b - 1] = 1
    dist[b - 1][a - 1] = 1
visited = [0 for i in range(N)]


def bfs(cur, color, num_colored=0):
    if num_colored == N:
        # print(color)
        return 1
    if color[cur] != 0:
        return 0

    # curに濡れる色を探す
    set_ = set([1, 2, 3])
    for i, e in enumerate(dist[cur]):
        if e == 0:
            continue
        set_ -= set([color[i]])
    if len(set_) == 0:
        print(0)
        exit(0)
    ans = 0
    for posible in set_:
        # 塗る
        color_copy = [posible if i == cur else c for i, c in enumerate(color)]
        # 塗り終わり
        if num_colored == N - 1:
            ans += 1
            continue
        # 塗ってない点に移る
        for i in range(N):
            if color_copy[i] != 0:
                continue
            ans += bfs(i, color_copy, num_colored + 1)
            # print(color_copy)
            break
    return ans


print(bfs(0, visited))
