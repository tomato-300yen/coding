S = input()
stack = []
ans = 0
for s in S:
    if stack:
        if stack[-1] == s:
            stack.append(s)
        else:
            stack.pop()
            ans += 2
    else:
        stack.append(s)
print(ans)
