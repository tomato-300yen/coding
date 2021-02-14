S, T = [input() for _ in range(2)]
ans = False
for _ in range(len(S)):
    S = S[-1] + S[:-1]
    if S == T:
        ans = True
print("Yes" if ans else "No")
