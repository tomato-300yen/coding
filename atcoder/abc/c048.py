N, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(len(A) - 1):
    tmp_sum = A[i] + A[i + 1]
    if tmp_sum > x:
        if A[i + 1] > tmp_sum - x:
            A[i + 1] -= tmp_sum - x
            ans += tmp_sum - x
        else:
            tmp = A[i + 1]
            A[i + 1] = 0
            ans += tmp
            A[i] -= tmp_sum - x - tmp
            ans += tmp_sum - x - tmp
            assert A[i] >= 0
print(ans)
