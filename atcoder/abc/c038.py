from math import factorial
N = int(input())
A = list(map(int, input().split()))
left = 0
right_most = A[0]
ans = 0
for right in range(N):
    if left == right:
        right_most = A[right]
    elif right_most < A[right]:
        ans += 1
        pass
    else:  # gradually getting bigger array
        pass
    right_most = A[right]
print(ans + N)
