S = input()
ans = ""
for s in S:
    if not s.isalpha():
        ans = ans + s
print(ans)
