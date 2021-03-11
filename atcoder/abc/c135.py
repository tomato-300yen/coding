N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = 0
ans = 0
for i, b in enumerate(B + [0]):
    if res > 0:
        ans += min(res, A[i])
        A[i] -= res
    if A[i] > 0:
        ans += min(b, A[i])
        res = b - A[i] if b > A[i] else 0
    else:
        res = b
print(ans)
