N, K = map(int, input().split())


def f(x: int) -> int:
    if x == 0:
        return 0
    else:
        tmp = sorted(str(x))
        num_g1 = int("".join(tmp[::-1]))
        num_g2 = int("".join(tmp))
        return num_g1 - num_g2


a = N
for k in range(K):
    a = f(a)
    if a == 0:
        break
print(a)
