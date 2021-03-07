from math import gcd

A, B, C, D = map(int, input().split())
lcm = C * D // gcd(C, D)
num_c = B // C - (A - 1) // C
num_d = B // D - (A - 1) // D
num_lcm = B // lcm - (A - 1) // lcm
print(B - A + 1 - (num_c + num_d - num_lcm))
