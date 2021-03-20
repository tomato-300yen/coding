N = int(input())
A = list(map(int, input().split()))
a, b = 0, abs(A[0] - A[1])
for i in range(2, N):
    a, b = b, min(a + abs(A[i] - A[i - 2]), b + abs(A[i] - A[i - 1]))
print(b)
