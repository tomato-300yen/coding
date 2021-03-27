import numpy as np
from math import sin, cos, pi


def rotate(arr, theta):
    """
    arrを原点を中心にthetaだけ半時計周りに回転させる
    """
    rot_mat = np.array([
        [cos(theta), sin(theta)],
        [-sin(theta), cos(theta)]
    ])
    return arr @ rot_mat


N = int(input())
x, y = map(int, input().split())
x_, y_ = map(int, input().split())
c_x, c_y = (x + x_) / 2, (y + y_) / 2

X = np.array([x, y]).T
C = np.array([c_x, c_y]).T
theta = 2 * pi / N
X_1 = rotate(X - C, theta)
X_1 = X_1 + C
print(X_1[0], X_1[1])
