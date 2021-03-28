K, N = map(int, input().split())
A = list(map(int, input().split()))

# 区間内の和がK以下の区間の個数を数える
# ans = 0
le, ri, sum_ = 0, 0, 0
while le < N:
    while ri < N and sum_ + A[ri] <= K:
        sum_ += A[ri]
        ri += 1
    # ans += 1

    sum_ -= A[le]
    le += 1
# print(ans)
