def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


s = int(input())
num_set = set()
value, ans = s, 1
while True:
    if value in num_set:
        print(ans)
        break
    ans += 1
    num_set.add(value)
    value = f(value)
