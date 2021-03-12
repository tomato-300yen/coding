L = list(map(int, input().split()))
K = int(input())
ans = 0
for _ in range(K):
    max_ = 0
    max_idx = -1
    for i in range(len(L)):
        tmp = L[i] * 2 + sum(L[:i] + L[i + 1 :])
        if tmp > max_:
            max_idx = i
            max_ = tmp
    L[max_idx] *= 2
    ans = max_
print(ans)
