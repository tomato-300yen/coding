N = int(input())
S = ["".join(sorted(input())) for _ in range(N)]
dict_count = dict()
for s in S:
    if s in dict_count.keys():
        dict_count[s] += 1
    else:
        dict_count[s] = 1
ans = 0
for _, item in dict_count.items():
    ans += (item * (item - 1)) // 2
print(ans)
