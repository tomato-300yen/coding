N = int(input())
ans = 1e12
# 約数を求める。N**.5までで十分
for n in range(1, int(N ** 0.5) + 1):
    if N % n == 0:
        ans = min(ans, n + N // n - 2)
print(ans)
