N, M = tuple(map(int, input().split()))
KA = [tuple(map(int, input().split())) for _ in range(N)]
ans_set = set(range(M + 1))
for k, *a in KA:
    ans_set = ans_set & set(a)
print(len(ans_set))
