from math import fabs
from typing import NamedTuple


class pair(NamedTuple):
    x: int
    y: int


def main():
    N = int(input())
    xy_list = []
    for i in range(N):
        x, y = list(map(int, input().split()))
        xy_list.append(pair(x, y))

    ans = 0
    for i in range(len(xy_list)):
        for j in range(i + 1, len(xy_list)):
            if fabs((xy_list[i].y - xy_list[j].y) / (xy_list[i].x - xy_list[j].x)) <= 1:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
