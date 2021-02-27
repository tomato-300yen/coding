S = input()
ans = -9e10
for ope in ["+", "-", "*"]:
    ans = max(ans, eval(S.replace(" ", ope)))
print(ans)
