L = [int(input()) for _ in range(3)]
L_sorted = sorted(L)[::-1]
for ll in L:
    print(L_sorted.index(ll) + 1)
