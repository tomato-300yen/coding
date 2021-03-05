from math import factorial

N = factorial(int(input()))
i = 2
ans = 1
while i * i <= N:
    count = 1
    while N % i == 0:
        count += 1
        N //= i
    ans *= count
    i += 1
if N != 1:
    ans *= 2
print(int(ans % (10**9 + 7)))
