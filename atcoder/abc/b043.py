ans = []
for s in input():
    if s == "B":
        if ans:
            ans.pop()
    else:
        ans.append(s)
print("".join(ans))
