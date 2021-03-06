N, M = map(int, input().split())
A = list(map(int, input().split()))


def mex(B):
    B = set(B)
    for i in range(N):
        if i not in B:
            return i


ans = N
for i in range(N - M + 1):
    ans = min(ans, mex(A[i: i + M]))
print(ans)
