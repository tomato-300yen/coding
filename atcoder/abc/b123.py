from math import ceil

cost = sorted([int(input()) for _ in range(5)], key=lambda x: -((x - 1) % 10))
ans = sum(map(lambda x: (ceil(x / 10)) * 10, cost[:-1])) + cost[-1]
print(ans)
