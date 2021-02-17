S = input()
ans = ""
for s in S:
    if s == "0":
        ans = ans + "0"
    elif s == "1":
        ans = ans + "1"
    elif s == "B":
        ans = ans[:-1]
    else:
        assert False
print(ans)
