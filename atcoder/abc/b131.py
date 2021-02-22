N, L = map(int, input().split())
sum_ = N * (L - 1) + N * (N + 1) // 2
taste_min = 999
sign = 1
for i in range(1, N + 1):
    if taste_min > abs(L + i - 1):
        taste_min = abs(L + i - 1)
        sign = -1 * ((L + i - 1) < 0) + 1 * ((L + i - 1) >= 0)
print(sum_ - taste_min * sign)
