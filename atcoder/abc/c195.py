from math import ceil

N = input()
ans = (int(str(int(N[0]) - 1) + N[1:]) + 1) * (ceil(len(N) / 3) - 1)
for i in range(1, len(N)):
    ans += (ceil(i / 3) - 1) * int("9" + "0" * (i - 1))
print(ans)
