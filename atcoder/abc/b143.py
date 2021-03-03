from itertools import combinations

N = int(input())
D = map(int, input().split())
print(sum(a * b for a, b in combinations(D, 2)))
