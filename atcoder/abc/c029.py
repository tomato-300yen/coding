from itertools import product

ll = ["abc" for _ in range(int(input()))]
for p in product(*ll):
    print("".join(p))
