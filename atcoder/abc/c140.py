N = int(input())
B = list(map(int, input().split()))
A = [0 for _ in range(N)]
A[0] = B[0]
for i in range(1, N):
    A[i] = min(B[i - 1:i + 1])
print(sum(A))
