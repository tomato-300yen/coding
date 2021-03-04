from math import factorial

(N, D), (X, Y) = [map(int, input().split()) for _ in range(2)]
if X % D != 0 or Y % D != 0:
    print(0)
    exit(0)
fac_x = X // D
fac_y = Y // D
surplus = N - fac_x - fac_y
ans = factorial(N) // factorial(fac_x) // factorial(fac_y) // factorial(surplus)
print(ans / 4 ** N)
