N = int(input())
A = map(int, input().split())
A = sorted([a - i - 1 for i, a in enumerate(A)])
print(sum([abs(a - A[N // 2]) for a in A]))
