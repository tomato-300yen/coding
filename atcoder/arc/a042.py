N, M = map(int, input().split())
A = [int(input()) for _ in range(M)][::-1]
ans_list = []
set_apprd = set()
for a in A:
    if a in set_apprd:
        continue
    set_apprd.add(a)
    ans_list.append(a)

print(*ans_list, sep="\n")
print(*sorted(list(set(range(1, N + 1)) - set_apprd)), sep="\n")
