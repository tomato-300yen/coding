N, Q = tuple(map(int, input().split()))
LRT = [tuple(map(int, input().split())) for _ in range(Q)]
A = [0 for _ in range(N)]
for left, right, t in LRT:
    for i in range(left - 1, right):
        A[i] = t
print(*A, sep="\n")
