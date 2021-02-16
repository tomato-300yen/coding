S = input()
ans = 0
half_idx = len(S) // 2
for s, s_r in zip(S[:half_idx], S[::-1][:half_idx]):
    ans += s != s_r
print(ans)
