N = int(input())
LR = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for left, right in LR:
    ans += right - left + 1
print(ans)
