N = int(input())
S = [input() for _ in range(N)] + ["_"]
M = int(input())
T = [input() for _ in range(M)] + ["_"]
ans = -1
for querry in S + T:
    tmp = 0
    for s in S:
        if querry == s:
            tmp += 1
    for t in T:
        if querry == t:
            tmp -= 1
    ans = max(tmp, ans)
print(ans)
