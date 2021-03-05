from itertools import product

N = int(input())
ans = 0
for i in range(3, len(str(N)) + 1):
    ll = ["753" for _ in range(i)]
    for p in product(*ll):
        num = int("".join(p))
        if 1 <= num <= N and set(str(num)) == set("573"):
            ans += 1
print(ans)
