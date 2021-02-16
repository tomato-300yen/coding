S, T = [input() for _ in range(2)]
ans = 0
for s, t in zip(S, T):
    ans += int(s == t)
print(ans)
