N = int(input())
A = list(map(int, input().split()))
ans = 0
while True:
    if sum([a % 2 == 0 for a in A]) == N:
        ans += 1
        A = list(map(lambda x: x // 2, A))
    else:
        break
print(ans)
