from typing import NamedTuple
from math import sqrt


class v(NamedTuple):
    x: int
    y: int


def main():
    N = int(input())
    v_list = []
    for _ in range(N):
        x, y = list(map(int, input().split()))
        v_list.append(v(x, y))

    dis_list = []
    for i in range(N):
        for j in range(i + 1, N):
            dis = sqrt((v_list[i].x - v_list[j].x) ** 2 + (v_list[i].y - v_list[j].y) ** 2)
            dis_list.append(dis)

    print(max(dis_list))


if __name__ == "__main__":
    main()
