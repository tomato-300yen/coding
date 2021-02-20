# from math import ceil, floor


def base_n2ten(X: str, n: int, M: int) -> int:
    ans = 0
    for i, x in enumerate(X):
        ans += int(x) * (n ** (len(X) - i - 1))
        if ans > M:
            return M + 1
    return ans


X = input()
M = int(input())
n = int(sorted(X)[-1]) + 1
ans_set = set()
left = n
right = M
while True:
    mid = (left + right) // 2
    # print(left, mid, right)
    tmp = base_n2ten(X, mid, M)
    if tmp > M:  # midより左
        if left == right:
            ans = mid - 1
            break
        elif right - left == 1:
            ans = left - 1
            break
        right = mid
    elif tmp < M:  # midより右
        if left == right:
            ans = mid
            break
        elif right - left == 1:
            left = left + 1
            continue
        left = mid
    else:  # midが最大
        ans = mid  # last
        break

print(int(ans - n + 1))
