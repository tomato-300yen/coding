N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]
if S.count(0):
    print(N)
    exit(0)
mul, left = 1, 0
ans = 0
for right in range(N):
    mul *= S[right]
    if mul <= K:
        ans = max(ans, right - left + 1)
    else:
        mul /= S[left]
        left += 1
print(ans)
