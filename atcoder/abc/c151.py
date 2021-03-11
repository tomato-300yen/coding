N, M = map(int, input().split())
PS = [input().split() for _ in range(M)]
result_list = [0 for _ in range(N)]
penalty = 0
num_ac = 0
for p, s in PS:
    p = int(p)
    if s == "WA":
        if result_list[p - 1] != -1:
            result_list[p - 1] += 1
    elif s == "AC":
        if result_list[p - 1] != -1:
            penalty += result_list[p - 1]
            num_ac += 1
            result_list[p - 1] = -1
print(num_ac, penalty)
