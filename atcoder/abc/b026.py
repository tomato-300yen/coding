from math import pi

N = int(input())
R = sorted([int(input()) for _ in range(N)])[::-1]
ans = 0
for i, r in enumerate(R):
    ans += r * r * pi * (1 if i % 2 == 0 else -1)
print(ans)
