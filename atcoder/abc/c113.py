N, M = map(int, input().split())
PYI = [list(map(int, input().split())) + [i] for i in range(M)]
PYI = sorted(PYI, key=lambda ll: (ll[0], ll[1]))
ans_list = []
x = 1
last_p = -1
for p, y, i in PYI:
    if last_p != p:
        x = 1
    ans_list.append([str(p).zfill(6) + str(x).zfill(6), i])
    x += 1
    last_p = p
ans_list = sorted(ans_list, key=lambda ll: ll[1])
for id_, _ in ans_list:
    print(id_)
