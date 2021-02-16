N = int(input())
A = [int(input()) for _ in range(N)]
next_ = 1
ans = 0
while True:
    next_ = A[next_ - 1]
    ans += 1
    if next_ == 2:
        print(ans)
        break
    if ans > N:
        print(-1)
        break
