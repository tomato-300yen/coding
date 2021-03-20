def copy_list(ll):
    ll_c = [[el for el in line] for line in ll]
    return ll_c


def dfs(map_, i, j, a):
    """
    map_ : タイルをおいたかどうかを記録する
    i, j : 次におくところ
    a : Aの残りの枚数
    """
    if a == 0:  # 全てをおいた
        # print(*map_, sep="\n")
        # print()
        return 1
    if j == W:  # 折り返す
        i, j = i + 1, 0
    if i == H:  # これ以上おけない
        return 0
    if map_[i][j] >= 1:
        return dfs(map_, i, j + 1, a)

    if i < H - 1 and map_[i + 1][j] == 0:
        map_h = copy_list(map_)
        map_h[i][j] = a
        map_h[i + 1][j] = a
        if j < W - 1 and map_[i][j + 1] == 0:
            map_w = copy_list(map_)
            map_w[i][j] = a
            map_w[i][j + 1] = a
            return (
                dfs(map_, i, j + 1, a)
                + dfs(map_h, i, j + 1, a - 1)
                + dfs(map_w, i, j + 1, a - 1)
            )
        else:
            return dfs(map_, i, j + 1, a) + dfs(map_h, i, j + 1, a - 1)
    else:
        if j < W - 1 and map_[i][j + 1] == 0:
            map_w = copy_list(map_)
            map_w[i][j] = a
            map_w[i][j + 1] = a
            return dfs(map_, i, j + 1, a) + dfs(map_w, i, j + 1, a - 1)
        else:
            return dfs(map_, i, j + 1, a)


H, W, A, B = map(int, input().split())
map_master = [[0 for _ in range(W)] for _ in range(H)]
print(dfs(map_master, 0, 0, A))
