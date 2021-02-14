S = input()
count = 0
ans = 0
for s in S:
    if s == "A" or s == "T" or s == "G" or s == "C":
        count += 1
    else:
        count = 0
    ans = max(ans, count)
print(ans)
