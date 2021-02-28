N, A, B = map(int, input().split())
ans = 0
for n in range(1, N + 1):
    if A <= sum(map(int, str(n))) <= B:
        ans += n
print(ans)
