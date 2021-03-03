from itertools import combinations

ll = combinations(map(int, input().split()), 3)
ll = sorted(map(lambda x: sum(x), ll))
print(ll[-3])
