N, M = map(int, input().split())
match_list = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
A = sorted(map(int, input().split()), key=lambda x: (match_list[x], -x))
match_min = min([match_list[a] for a in A])
dp = [0]
candinate = [-1]
for i in range(1, N + 1):
    if i < match_min:
        dp.append(-1e10)
        candinate.append(-1)
        continue
    max_ = -1
    max_int = -1
    for a in A:
        if i < match_list[a]:
            break
        if dp[-match_list[a]] + 1 > max_:
            max_ = dp[-match_list[a]] + 1
            max_int = a
    dp.append(max_)
    candinate.append(max_int)
# print(dp)
# print(candinate)

i = 0
ans_list = []
candinate = candinate[::-1]
for _ in range(dp[-1]):
    ans_list.append(candinate[i])
    i += match_list[candinate[i]]
print("".join(map(str, sorted(ans_list)[::-1])))
