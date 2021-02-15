X = int(input())
ans = X
while True:
    for i in range(2, int(X ** 0.5) + 1):
        if ans % i == 0:
            ans += 1
            break
    else:
        break
print(ans)
