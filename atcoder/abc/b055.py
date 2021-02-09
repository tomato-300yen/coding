from math import factorial

N = int(input())
print(factorial(N) % (10 ** 9 + 7))
