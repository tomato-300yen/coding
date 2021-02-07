N = int(input())
P = sorted([int(input()) for _ in range(N)])
print(int(P[-1] / 2 + sum(P[:-1])))
