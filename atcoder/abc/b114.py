S = input()
ans = 999
for i in range(2, len(S)):
    ans = min(ans, abs(753 - int(S[i - 2 : i + 1])))
print(ans)
