N = int(input())
NN = 2 * N
S = input()
Q = int(input())
TAB = [map(int, input().split()) for _ in range(Q)]


def trans(a):
    return (a - N) % NN


# init
list_ = [i for i in range(NN)]

num_flip = 0
for t, a, b in TAB:
    a, b = a - 1, b - 1
    if t == 1:
        if num_flip % 2 == 1:
            a = trans(a)
            b = trans(b)
        list_[a], list_[b] = list_[b], list_[a]
    else:
        num_flip += 1

ans = "".join(map(lambda idx: S[idx], list_))
if num_flip % 2 == 1:
    ans = ans[N:] + ans[:N]
print(ans)
