N = int(input())
ans = -1
for i in range(N):
    if 2 ** i > N:
        break
    ans = 2 ** i
print(ans)
