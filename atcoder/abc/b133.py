from math import sqrt

import numpy as np

N, _ = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(len(X)):
    for j in range(i + 1, len(X)):
        a, b = np.array(X[i][:]), np.array(X[j][:])
        if sqrt(sum((a - b) ** 2)).is_integer():
            ans += 1
print(ans)
