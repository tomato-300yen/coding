A, B = map(int, input().split())
for price in range(1, 1251):
    if int(price * 0.08) == A and int(price * 0.1) == B:
        print(price)
        break
else:
    print(-1)
