import bisect

N = int(input())
A, B, C = [sorted(map(int, input().split())) for _ in range(3)]
ans, idx_b, idx_c = 0, 0, 0
for b in B:
    idx_a = bisect.bisect_left(A, b)
    idx_c = bisect.bisect_right(C, b)
    ans += idx_a * (N - idx_c)

print(ans)
