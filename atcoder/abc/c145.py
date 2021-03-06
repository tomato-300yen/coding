from itertools import permutations
import numpy as np
N = int(input())
XY = np.array([list(map(int, input().split())) for _ in range(N)])
arr_dist = [[0 for _ in range(N)] for _ in range(N)]
for i in range(len(XY)):
    for j in range(i + 1, len(XY)):
        arr_dist[i][j] = sum((XY[i, :] - XY[j, :]) ** 2) ** 0.5
        arr_dist[j][i] = arr_dist[i][j]
ans = 0
for i, p in enumerate(permutations(list(range(N)))):
    ans += sum([arr_dist[p[i]][p[i + 1]] for i in range(len(p) - 1)])
print(ans / (i + 1))
