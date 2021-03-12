N, M = map(int, input().split())
A = set([int(input()) for _ in range(M)])
b, a = 1, 1 if 1 not in A else 0
for i in range(2, N + 1):
    b, a = a, 0 if i in A else b + a
print(a % 1000000007)
