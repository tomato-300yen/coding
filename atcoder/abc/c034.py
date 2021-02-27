from math import factorial
W, H = map(int, input().split())
print((factorial(W + H - 2) // factorial(W - 1) // factorial(H - 1)) % 1000000007)
