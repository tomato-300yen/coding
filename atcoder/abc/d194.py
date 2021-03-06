from math import factorial
N = int(input())
M = N
ans = 0
while True:
    tmp = factorial(M) * (N - 1) * (M - N + 1) / (factorial(M - N + 1) * pow(N, M))
    print(tmp)
    if tmp < 0.0000000001:
        break
    ans += tmp
    M += 1
print(ans)
