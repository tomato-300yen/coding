import math

N = int(input())
cost = [int(input()) for _ in range(5)]
print(math.ceil(N / min(cost)) + 4)
