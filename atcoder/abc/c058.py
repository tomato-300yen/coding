from collections import Counter
N = int(input())
S = [Counter(input()) for _ in range(N)]
ans_counter = S[0]
for s in S:
    ans_counter &= s
print("".join(sorted(ans_counter.elements())))
