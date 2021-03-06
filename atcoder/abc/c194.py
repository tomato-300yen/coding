N = int(input())
A = list(map(int, input().split()))
tmp = sum([a ** 2 for a in A])
print(tmp * N - sum(A) ** 2)
