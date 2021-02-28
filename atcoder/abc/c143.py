N = int(input())
S = input()
ans = S[0]
for s in S[1:]:
    if ans[-1] == s:
        continue
    ans = ans + s
print(len(ans))
