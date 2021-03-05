from itertools import groupby
s = input()
ans = ""
for k, g in groupby(s):
    ans = ans + k + str(len(list(g)))
print(ans)
