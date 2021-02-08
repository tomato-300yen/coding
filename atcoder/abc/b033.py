N = int(input())
SP = [tuple(input().split()) for _ in range(N)]
max_p = -1
sum_p = 0
max_p_name = "initi"
for s, p in SP:
    p = int(p)
    sum_p += p
    if p > max_p:
        max_p = p
        max_p_name = s
print(max_p_name if max_p > (sum_p / 2) else "atcoder")
