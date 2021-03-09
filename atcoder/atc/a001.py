import sys

sys.setrecursionlimit(500000)
H, W = map(int, input().split())
C = []
for i in range(H):
    line = list(input())
    try:
        start_idx = (i, line.index("s"))
    except Exception:
        pass
    try:
        goal_idx = (i, line.index("g"))
    except Exception:
        pass
    C.append(line)
D = [[0 for _ in range(W)] for _ in range(H)]


def dfs(C, i, j, last_move="init"):
    """
    last_move: left, right, up, down, init
    """
    if not (0 <= i < H):
        return False
    if not (0 <= j < W):
        return False
    if D[i][j]:
        return False
    if C[i][j] == "g":
        return True
    elif C[i][j] == "#":
        return False
    else:
        # print(i, j)
        D[i][j] = 1
        return (
            (dfs(C, i + 1, j, "down") if last_move != "up" else False)
            or (dfs(C, i, j + 1, "right") if last_move != "left" else False)
            or (dfs(C, i, j - 1, "left") if last_move != "right" else False)
            or (dfs(C, i - 1, j, "up") if last_move != "down" else False)
        )


print("Yes" if dfs(C, start_idx[0], start_idx[1]) else "No")
