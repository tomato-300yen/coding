N = int(input())
ans = 1
for i in range(N):
    if i ** 2 > N:
        break
    ans = max(ans, i ** 2)
print(ans)
