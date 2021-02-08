N, M, C = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
A = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for each_A in A:
    sum_ = C
    for a, b in zip(each_A, B):
        sum_ += a * b
    ans = ans + 1 if sum_ > 0 else ans
print(ans)
